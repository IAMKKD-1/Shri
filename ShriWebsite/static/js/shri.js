// Bottom Scroll
function scrollToBottom() {
  const chatContainer = document.querySelector(".chat-container");
  chatContainer.scrollTop = chatContainer.scrollHeight;
}
window.addEventListener("load", function() {
  scrollToBottom();
});

// Copied Button
function copyToClipboard(buttonId, code) {
  const textArea = document.createElement("textarea");
  textArea.value = code;
  document.body.appendChild(textArea);
  textArea.select();
  document.execCommand("copy");
  document.body.removeChild(textArea);
  const copyButton = document.getElementById(buttonId);
  copyButton.textContent = "Copied";
}

// Enter to submit message
function handleTextareaKeyPress(event) {
  const messageForm = document.getElementById("message-form");
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    messageForm.submit();
  } 
  adjustTextarea(event.target);
}

// Adjust textarea height
function adjustTextarea(textarea) {
  const lineHeight = 24; 
  const minRows = 1;
  const maxRows = 4;
  textarea.style.height = 'auto';
  const computedHeight = textarea.scrollHeight;
  const rows = Math.min(
    maxRows,
    Math.max(minRows, Math.ceil(computedHeight / lineHeight))
  );
  textarea.style.height = lineHeight * rows + 'px';
}