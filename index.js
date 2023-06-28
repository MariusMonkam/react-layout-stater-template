const { exec } = require("child_process");

//Specify the path to your Python file
const pythonFilePath = "main.py";

//execute the Python file using the child_process module
exec(`python ${pythonFilePath}`, (error, stdout, stderr) => {
  if (error) {
    //if there was an error executing the python file, log the error message
    console.error(`Error executing Python file:${error.message}`);
    return;
  }
  if (stderr) {
    //If the Python script returned an error, log the error message
    console.error(`Python script returned an error: ${stderr}`);
    return;
  }
  // Process the output from the Python script
  console.log(`Python script output: ${stdout}`);
});
