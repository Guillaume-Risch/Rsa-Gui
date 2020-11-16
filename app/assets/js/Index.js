
document.getElementById('lockButton').addEventListener('click', function() {
    this.classList.add('big');

    setTimeout(function() {
        document.getElementById('popupStart').classList.add('noDisplay')
        document.getElementById('formContainer').classList.remove('noDisplay')
      }, 1100);
})


document.getElementById('switchRSA').addEventListener('click', function() {
  document.getElementById('chifContainer').classList.toggle('noDisplay');
  document.getElementById('dechifContainer').classList.toggle('noDisplay');
})