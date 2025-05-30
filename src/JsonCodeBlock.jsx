import React, { useState, useEffect } from "react";
import { invoke } from "@tauri-apps/api/core";
import { useAppStore } from "./store";
import Editor from "react-simple-code-editor";
import Prism from "prismjs";
import "prismjs/themes/prism.duotune-sea.css";
import "prismjs/components/prism-json";
const JsonCodeBlock = () => {
    const [code, setCode] = useState("");
    const [activeLine, setActiveLine] = useState(null);
    const [isFocused, setIsFocused] = useState(false);
    const [executionResult, setExecutionResult] = useState(null);
    const [isExecuting, setIsExecuting] = useState(false);
    const currentAlgo = useAppStore((state) => state.selectedAlgorithm);
    const Results = useAppStore((state) => state.results);
    const setResults = useAppStore((state) => state.setResults);
    const selectedAlgorithm = useAppStore((state) => state.selectedAlgorithm);

    // Simulate cursor animation
    useEffect(() => {
        fetch("/instructions.json")
            .then((res) => res.json())
            .then((data) => setStructure(data))
            .catch((err) => console.error("Error loading JSON:", err));
        const interval = setInterval(() => {
            setIsFocused((prev) => !prev);
        }, 800);
        return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        fetch("/instructions.json")
            .then((res) => res.json())
            .then((data) => {
                if (selectedAlgorithm !== null) {
                    if (data[selectedAlgorithm] != null) {
                        setCode(data[selectedAlgorithm]);
                    }
                }
            })
            .catch((err) => console.error("Error loading JSON:", err));
    }, [selectedAlgorithm]);

    const handleLineClick = (lineIndex) => {
        setActiveLine(lineIndex);
    };

    const handleCodeChange = (e) => {
        setCode(e.target.value);
    };

    const handleExecute = async () => {
        setIsExecuting(true);
        setExecutionResult(null);
        if (currentAlgo === null) {
            setExecutionResult({
                success: false,
                message: "No Algorithm is selected!",
            });
            setIsExecuting(false);
            return;
        }
        try {
            const parsedJson = JSON.parse(code);

            const result = await invoke("execute_json", {
                jsonData: parsedJson,
                selectedAlgo: currentAlgo,
            });

            setExecutionResult({
                success: true,
                message: "Success",
            });

            setResults([
                ...Results,
                { text: result, time: new Date().toLocaleTimeString() },
            ]);
        } catch (error) {
            setExecutionResult({
                success: false,
                message: error.toString(),
            });
        } finally {
            setIsExecuting(false);
        }
    };

    const handleImport = (e) => {
        const file = e.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = (event) => {
            try {
                const fileContent = event.target.result;
                JSON.parse(fileContent);
                setCode(fileContent);
                setExecutionResult({
                    success: true,
                    message: "File imported successfully!",
                });
            } catch (error) {
                setExecutionResult({
                    success: false,
                    message: "Invalid JSON file: " + error.message,
                });
            }
        };
        reader.readAsText(file);
    };

    return (
        <div className="relative">
            {/* Floating window effect */}
            <div className="absolute -inset-2 bg-blue-500/10 rounded-xl blur-lg opacity-30 -z-10"></div>

            {/* Main container */}
            <div className="code-block-container bg-[#0A0E15] rounded-lg border border-gray-700/80 overflow-hidden shadow-2xl shadow-blue-500/10 transition-all duration-300 hover:shadow-blue-500/20">
                {/* Window header */}
                <div className="window-header bg-[#0A0E12] px-4 py-2 flex items-center border-b border-gray-700/50">
                    <div className="window-controls flex space-x-2 mr-4">
                        <div className="w-3 h-3 rounded-full bg-[#ff5f56]"></div>
                        <div className="w-3 h-3 rounded-full bg-[#ffbd2e]"></div>
                        <div className="w-3 h-3 rounded-full bg-[#27c93f]"></div>
                    </div>
                    <div className="text-xs text-gray-400 font-medium">
                        settings.json
                    </div>
                    <div className="ml-auto flex space-x-1.5">
                        <div className="w-2 h-2 rounded-full bg-gray-600/80"></div>
                        <div className="w-2 h-2 rounded-full bg-gray-600/80"></div>
                        <div className="w-2 h-2 rounded-full bg-gray-600/80"></div>
                    </div>
                </div>

                {/* Code area - always editable */}
                {/* <textarea
          ref={codeRef}
          className="w-full h-96 bg-[#0A0E15] text-gray-300 p-4 font-mono text-[15px] leading-snug outline-none resize-none"
          value={code}
          onChange={handleCodeChange}
          spellCheck="false"
          onClick={(e) => {
            const textarea = e.target;
            const lineNumber = (textarea.value.substr(0, textarea.selectionStart).match(/\n/g) || []).length;
            setActiveLine(lineNumber);
          }}
        /> */}
                <Editor
                    value={code}
                    onValueChange={setCode}
                    highlight={(code) =>
                        Prism.highlight(code, Prism.languages.json, "json")
                    }
                    padding={10}
                    placeholder="Code Here"
                    onClick={(e) => {
                        const textarea = e.target;
                        const lineNumber = (
                            textarea.value
                                .substr(0, textarea.selectionStart)
                                .match(/\n/g) || []
                        ).length;
                        setActiveLine(lineNumber);
                    }}
                    className="w-full h-96 bg-[#0A0E15] text-gray-300 p-4 font-mono text-[17px] leading-snug outline-none resize-none"
                />

                {/* Status bar */}
                <div className="bg-gray-950 text-white px-3 py-1.5 flex items-center justify-between text-xs">
                    <div className="flex items-center space-x-4">
                        <span>JSON</span>
                        <span className="opacity-80">UTF-8</span>
                        {executionResult && (
                            <span
                                className={`${
                                    executionResult.success
                                        ? "text-green-400"
                                        : "text-red-400"
                                }`}
                            >
                                {executionResult.message}
                            </span>
                        )}
                    </div>
                    <div className="flex items-center space-x-2">
                        <span className="opacity-90">
                            Ln {activeLine !== null ? activeLine + 1 : "--"}
                        </span>
                        <span className="opacity-70">•</span>
                        <span className="opacity-90">
                            Col{" "}
                            {activeLine !== null
                                ? code.substring(
                                      0,
                                      code.indexOf("\n", activeLine)
                                  ).length + 1
                                : "--"}
                        </span>
                    </div>
                </div>

                {/* Floating action buttons */}
                <div className="absolute right-4 bottom-16 flex space-x-3">
                    <label className="px-3 py-1.5 bg-gray-700/90 hover:bg-gray-600/90 text-gray-300 rounded-md text-xs font-medium flex items-center shadow-md transition-all duration-200 hover:shadow-lg hover:translate-y-[-1px] cursor-pointer">
                        <input
                            type="file"
                            accept=".json"
                            onChange={handleImport}
                            className="hidden"
                        />
                        <svg
                            className="w-3.5 h-3.5 mr-1.5 opacity-80"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth={2}
                                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                            />
                        </svg>
                        Import
                    </label>
                    <button
                        onClick={handleExecute}
                        disabled={isExecuting}
                        className={`px-3 py-1.5 ${
                            isExecuting
                                ? "bg-[#005a8c]"
                                : "bg-[#007acc] hover:bg-[#006bb3]"
                        } text-white rounded-md text-xs font-medium flex items-center shadow-md transition-all duration-200 hover:shadow-lg hover:translate-y-[-1px]`}
                    >
                        {isExecuting ? (
                            <>
                                <svg
                                    className="animate-spin -ml-1 mr-1.5 h-3.5 w-3.5 text-white"
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                >
                                    <circle
                                        className="opacity-25"
                                        cx="12"
                                        cy="12"
                                        r="10"
                                        stroke="currentColor"
                                        strokeWidth="4"
                                    ></circle>
                                    <path
                                        className="opacity-75"
                                        fill="currentColor"
                                        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                                    ></path>
                                </svg>
                                Executing...
                            </>
                        ) : (
                            <>
                                <svg
                                    className="w-3.5 h-3.5 mr-1.5"
                                    fill="none"
                                    stroke="currentColor"
                                    viewBox="0 0 24 24"
                                >
                                    <path
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth={2}
                                        d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"
                                    />
                                    <path
                                        strokeLinecap="round"
                                        strokeLinejoin="round"
                                        strokeWidth={2}
                                        d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                                    />
                                </svg>
                                Execute
                            </>
                        )}
                    </button>
                </div>
            </div>

            {/* Execution result panel - only show errors */}
            {executionResult && !executionResult.success && (
                <div className="mt-4 p-4 rounded-lg bg-red-900/20 border border-red-800/50">
                    <div className="font-medium mb-2 text-sm text-red-400">
                        ❌ Execution Failed
                    </div>
                    <div className="text-xs text-red-200">
                        {executionResult.message}
                    </div>
                </div>
            )}
        </div>
    );
};

export default JsonCodeBlock;
