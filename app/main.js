// Modules to control application life and create native browser window
const {app, BrowserWindow, ipcMain, session} = require('electron')
const path = require('path')
const fs = require("fs");
const {PythonShell} = require('python-shell')


let mainWindow

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true
    }
  })

  // and load the index.html of the app.
  mainWindow.loadFile('index.html')

  // Open the DevTools.
  // mainWindow.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  createWindow()
  
  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})


ipcMain.on("toCrypt", (event, args)=> {
  var options = {
    scriptPath : path.join(__dirname, '/py'),
    args:[args],
    mode:'json'
  };

  PythonShell.run('crypt.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    mainWindow.webContents.send("fromCrypt", results);
  });
  
});


ipcMain.on("toDecrypt", (event, args)=> {
  var stringF = args[0].replace('\n', '').split(' ');
  for(let i = 0; i < stringF.length; ++i) {
    stringF[i] = parseInt(stringF[i]);
  }

  var options = {
    scriptPath : path.join(__dirname, '/py'),
    args:[stringF, args[1], args[2]],
    mode:'json'
  };

  PythonShell.run('decrypt.py', options, function (err, results) {
    console.log(results);
    
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    mainWindow.webContents.send("fromDecrypt", results);
  });
});



// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
