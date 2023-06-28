const { spawn } = require("child_process");

// Run the main.py script as a child process
const pythonProcess = spawn("python", ["main.py"], { stdio: "inherit" });

// Listen for the Python script to exit
pythonProcess.on("close", (code) => {
  console.log(`Python script exited with code ${code}`);
});
