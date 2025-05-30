import Header from "./titlebar.jsx";
import "./App.css";
import { NavLink } from "react-router-dom";

function App() {
    return (
        <main className="flex flex-col items-center h-screen text-center font-[Montserrat] ">
            {/* Application Header / Titlebar */}
            <Header />

            <div className="grid relative overflow-hidden">
                {/* SVG Background Grid */}
                <svg
                    className="grid-svg"
                    xmlns="http://www.w3.org/2000/svg"
                    width="982"
                    height="786"
                    viewBox="0 0 982 786"
                    fill="none"
                >
                    <path
                        fillRule="evenodd"
                        clipRule="evenodd"
                        d="M490 401V537H348.5V401H490ZM490 785.5V676H348.5V785.5H347.5V676H206V785.5H205V676H63.5V785.5H62.5V676H0V675H62.5V538H0V537H62.5V401H0V400H62.5V258H0V257H62.5V116H0V115H62.5V0H63.5V115L205 115V0H206V115L347.5 115V0H348.5V115H490V0H491V115L627.5 115V0H628.5V115H765V0H766V115L902.5 115V0H903.5V115H982V116H903.5V257H982V258H903.5V400H982V401H903.5V537H982V538H903.5V675H982V676H903.5V785.5H902.5V676H766V785.5H765V676H628.5V785.5H627.5V676H491V785.5H490ZM902.5 675V538H766V675H902.5ZM902.5 537V401H766V537H902.5ZM902.5 400V258H766V400H902.5ZM902.5 257V116L766 116V257H902.5ZM627.5 675H491V538H627.5V675ZM765 675H628.5V538H765V675ZM348.5 675H490V538H348.5V675ZM347.5 538V675H206V538H347.5ZM205 538V675H63.5V538H205ZM765 537V401H628.5V537H765ZM765 400V258H628.5V400H765ZM765 257V116H628.5V257H765ZM347.5 401V537H206V401H347.5ZM205 401V537H63.5V401H205ZM627.5 401V537H491V401H627.5ZM627.5 116L491 116V257H627.5V116ZM627.5 258H491V400H627.5V258ZM63.5 257V116L205 116V257H63.5ZM63.5 400V258H205V400H63.5ZM206 116V257H347.5V116L206 116ZM348.5 116V257H490V116H348.5ZM206 400V258H347.5V400H206ZM348.5 258V400H490V258H348.5Z"
                        fill="url(#paint0_radial_1_8)"
                    />
                    <defs>
                        <radialGradient
                            id="paint0_radial_1_8"
                            cx="0"
                            cy="0"
                            r="1"
                            gradientUnits="userSpaceOnUse"
                            gradientTransform="translate(491 392.75) rotate(90) scale(513.25 679.989)"
                        >
                            <stop stopColor="#10D1BE" stopOpacity="0.5" />
                            <stop
                                offset="1"
                                stopColor="#4E3987"
                                stopOpacity="0"
                            />
                        </radialGradient>
                    </defs>
                </svg>

                {/* Main Content */}
                <div className="absolute inset-0 flex items-center justify-center pointer-events-none overflow-hidden">
                    <div className="flex flex-col items-center mt-[150px]">
                        {/* Intro Text */}
                        <h3 className="py-2 px-6 rounded-full border border-gray-400 w-fit text-sm font-medium text-gray-400 tracking-wider">
                            Unlocking the power of advanced algorithms to solve
                            tomorrow’s challenges
                        </h3>

                        {/* Heading with Gradient Text */}
                        <h1 className="text-[70px] font-semibold my-10 leading-[1.15] bg-gradient-to-r from-emerald-400 via-cyan-200 to-[#4E3987] text-transparent bg-clip-text font-[Montserrat]">
                            Powering the Future Through Intelligent Algorithms
                        </h1>

                        {/* Subheading */}
                        <h3 className="text-white mb-8">
                            Explore the universe of algorithms — from Greedy to
                            Graphs, <br />
                            Dynamic Programming to Divide & Conquer — all in one
                            platform.
                        </h3>

                        {/* Buttons Block */}
                        <div className="flex gap-5 mt-2 pointer-events-auto">
                            {/* Primary Action Button */}
                            <NavLink
                                to="/algorithms"
                                className="flex items-center gap-4 py-2 rounded-full bg-emerald-300 shadow-lg hover:scale-105 transition-transform duration-300"
                            >
                                <span className="text-black text-lg font-semibold ml-6">
                                    Try Now
                                </span>
                                <span className="flex mr-4 items-center justify-center w-10 h-10 rounded-full bg-black shadow-inner">
                                    <svg
                                        className="w-4 h-4 text-white"
                                        fill="none"
                                        stroke="currentColor"
                                        strokeWidth="2"
                                        viewBox="0 0 24 24"
                                    >
                                        <path
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            d="M5 12h14M12 5l7 7-7 7"
                                        />
                                    </svg>
                                </span>
                            </NavLink>

                            {/* Secondary Action Button */}
                            <NavLink
                                to="/algorithms"
                                className="flex items-center px-10 py-2 rounded-full border border-white/30 backdrop-blur-sm bg-white/5 text-white hover:border-white hover:scale-105 transition-all duration-300"
                            >
                                <span className="text-white text-lg">
                                    Learn More
                                </span>
                            </NavLink>
                        </div>
                    </div>
                </div>

                {/* Optional Decorative Blur Element */}
                <div className="blur"></div>
            </div>
        </main>
    );
}

export default App;
