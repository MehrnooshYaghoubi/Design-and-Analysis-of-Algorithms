import { useState } from "react";
import Header from "./titlebar.jsx";
import "./algorithm.css";
import { invoke } from "@tauri-apps/api/core";
import JsonCodeBlock from "./JsonCodeBlock";
import { ChevronRight } from "lucide-react";
import { NavLink } from "react-router-dom";
import Panel from "./Panel.jsx";
import { useAppStore } from "./store";

const Dashboard = () => {
  const [inputValue, setInputValue] = useState("");
  const results = useAppStore((state) => state.results);
  const [algorithmsVisible, setAlgorithmsVisible] = useState(false);

  return (
    <main className="font-[Montserrat] h-screen overflow-hidden">
      <Header />

      {/* Glowing orb decor */}
      <div className="fixed -right-64 -top-64 w-[600px] h-[600px] rounded-full blur-[100px]"></div>
      <div className="fixed -left-64 -bottom-64 w-[600px] h-[600px] rounded-full blur-[100px]"></div>

      <div className="relative flex h-screen">
        {/* Left Panel */}
        <div className="w-64 backdrop-blur-md border-r border-gray-800 p-4 h-full overflow-y-auto pb-[5em]">
          <h2 className="text-xl font-bold mb-6 text-emerald-300 flex items-center">
            <span className="w-3 h-3 bg-emerald-300 rounded-full mr-2 animate-pulse"></span>
            NAVIGATION
          </h2>

          <ul className="space-y-3">
            <li className="group">
              <NavLink
                to="/"
                className="flex items-center p-2 text-gray-300 hover:text-[oklch(91%_0.096_180.426)] hover:bg-gray-700/50 rounded-lg transition-all duration-200 border-l-2 border-transparent group-hover:border-[oklch(91%_0.096_180.426)]"
              >
                <span className="w-2 h-2 bg-[oklch(91%_0.096_180.426)] rounded-full mr-3 opacity-0 group-hover:opacity-100 transition-opacity"></span>
                Home Page
              </NavLink>
            </li>

            <li
              className="group"
              onClick={() => setAlgorithmsVisible(!algorithmsVisible)}
            >
              <a className="flex items-center p-2 text-gray-300 hover:text-[oklch(91%_0.096_180.426)] hover:bg-gray-700/50 rounded-lg transition-all duration-200 border-l-2 border-transparent group-hover:border-[oklch(91%_0.096_180.426)]">
                <span className="w-2 h-2 bg-[oklch(91%_0.096_180.426)] rounded-full mr-3 opacity-0 group-hover:opacity-100 transition-opacity"></span>
                <ChevronRight
                  className={
                    algorithmsVisible
                      ? "rotate-90 w-4 h-4 mr-2"
                      : "rotate-0 w-4 h-4 mr-2"
                  }
                />
                Algorithms
              </a>
            </li>

            {algorithmsVisible && <Panel />}
          </ul>

          <div className="mt-8 pt-4 border-t border-gray-700">
            <div className="text-xs text-gray-500 mb-2">SYSTEM STATUS</div>
            <div className="h-2 bg-gray-700 rounded-full overflow-hidden">
              <div className="h-full bg-emerald-300 rounded-full w-3/4"></div>
            </div>
            <div className="text-xs text-emerald-300 mt-1">
              74% Algorithms are set
            </div>
          </div>
        </div>

        {/* Main Content Area */}
        <div className="flex-1 flex flex-col p-6 space-y-6">
          <div className="flex space-x-6">
            {/* Input Panel */}
            <div className="flex-1 backdrop-blur-md rounded-xl border border-gray-800 p-5 shadow-lg shadow-emerald-500/5">
              <JsonCodeBlock />
            </div>

            {/* Results and Graph */}
            <div className="flex-1 space-y-6">
              {/* Results Panel */}
              <div className="backdrop-blur-md rounded-xl border border-gray-800 p-5 shadow-lg shadow-emerald-500/5">
                <h3 className="font mb-4 text-emerald-300 flex items-center">
                  <span className="w-2 h-2 bg-emerald-300 rounded-full mr-2"></span>
                  PROCESSING RESULTS
                </h3>
                <div className="space-y-3 max-h-[40vh] overflow-y-auto">
                  {results.length > 0 ? (
                    results.map((result, index) => (
                      <div
                        key={index}
                        className="bg-gray-900/50 border border-gray-700 rounded-lg px-4 py-3 flex items-start"
                      >
                        <div className="flex-shrink-0 mt-1">
                          <div className="w-2 h-2 bg-cyan-100 rounded-full animate-pulse"></div>
                        </div>
                        <div className="ml-3">
                          <div className="text-sm font-mono text-cyan-100">
                            {result.text}
                          </div>
                          <div>{result.algo}</div>
                          <div className="text-xs text-gray-500 mt-1 flex justify-between w-full">
                            <h3>{result.time}</h3>
                            <h3>{result.duration}</h3>
                          </div>
                        </div>
                      </div>
                    ))
                  ) : (
                    <div className="flex flex-col items-center justify-center text-center py-8 text-gray-500">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="36"
                        height="36"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="1.3"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="lucide lucide-frown-icon"
                      >
                        <circle cx="12" cy="12" r="10" />
                        <path d="M16 16s-1.5-2-4-2-4 2-4 2" />
                        <line x1="9" y1="9" x2="9.01" y2="9" />
                        <line x1="15" y1="9" x2="15.01" y2="9" />
                      </svg>
                      <p className="mt-2">No results generated yet</p>
                      <p className="text-sm mt-1">
                        Run an algorithm to see results
                      </p>
                    </div>
                  )}
                </div>
              </div>

              {/* Graph Panel */}
              <div className="backdrop-blur-md rounded-xl border border-gray-800 p-5 shadow-lg shadow-emerald-500/5">
                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-lg text-emerald-300 flex items-center">
                    <span className="w-2 h-2 bg-emerald-300 rounded-full mr-2"></span>
                    DATA VISUALIZATION
                  </h3>
                  <div className="flex space-x-2">
                    <button className="text-xs px-3 py-1 bg-gray-700 hover:bg-gray-600 rounded-lg transition-colors">
                      3D
                    </button>
                    <button className="text-xs px-3 py-1 bg-gray-700 hover:bg-gray-600 rounded-lg transition-colors">
                      HEATMAP
                    </button>
                    <button className="text-xs px-3 py-1 bg-indigo-500 text-gray-900 rounded-lg">
                      GRAPH
                    </button>
                  </div>
                </div>
                <div className="h-64 bg-gray-900/50 rounded-lg border border-gray-700 flex items-center justify-center">
                  <div className="flex flex-col items-center justify-center text-center">
                    <div className="text-cyan-200 mb-2">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="36"
                        height="36"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="3"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="lucide lucide-chart-column-decreasing-icon"
                      >
                        <path d="M13 17V9" />
                        <path d="M18 17v-3" />
                        <path d="M3 3v16a2 2 0 0 0 2 2h16" />
                        <path d="M8 17V5" />
                      </svg>
                    </div>
                    <p className="text-gray-400">
                      Processing data visualization
                    </p>
                    <p className="text-xs text-gray-500 mt-1">
                      This section would be done in Future...
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default Dashboard;
