document.addEventListener("DOMContentLoaded", function () {
    const toolSelect = document.getElementById("toolSelect");
    const languageSelect = document.getElementById("languageSelect");
    const codeInput = document.getElementById("codeInput");
    const submitBtn = document.getElementById("submitBtn");
    const outputDiv = document.getElementById("outputDiv"); // The output <div>

    // Enable or disable the language dropdown based on the selected tool
    toolSelect.addEventListener("change", function () {
        if (toolSelect.value === "conversion") {
            languageSelect.removeAttribute("disabled");
        } else {
            languageSelect.setAttribute("disabled", "disabled");
        }
    });

    submitBtn.addEventListener("click", function () {
        const tool = toolSelect.value;
        const language = languageSelect.value;
        const code = codeInput.value;

        if (tool === "quality") {
            // Handle code quality check
            handleQualityCheck(code);
        } else if (tool === "conversion") {
            // Handle code conversion
            handleCodeConversion(code, language);
        } else if (tool === "debug") {
            // Handle code debugging
            handleCodeDebug(code);
        }
    });

async function handleQualityCheck(code) {
        const apiUrl = 'http://127.0.0.1:5000/codequality';
    
        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ code }), // Send the code to the server
            });
    
            if (response.ok) {
                const data = await response.json();
                const qualityResult = data.quality_of_code; // Assuming the API response structure
    
                // Split the quality result into lines
                const lines = qualityResult.split('\n');
    
                // Create an HTML string for the lines
                const linesHTML = lines.map(line => `<p>${line}</p>`).join('');
    
                // Update the outputDiv content with the HTML
                console.log(linesHTML);
                outputDiv.innerHTML = linesHTML;
            } else {
                const errorData = await response.json();
                outputDiv.textContent = `Error: ${errorData.error}`;
                console.error('Error:', response.statusText);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }
    


    async function handleCodeConversion(code, language) {
        const apiUrl = 'http://127.0.0.1:5000/codeconverter';
    
        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ code, language }), // Send the code and language to the server
            });
    
            if (response.ok) {
                const data = await response.json();
                const convertedCode = data.converted_code; // Assuming the API response structure
    
                // Display the converted code
                outputDiv.textContent = convertedCode;
            } else {
                // Handle the error response
                const errorData = await response.json();
                outputDiv.textContent = `Error: ${errorData.error}`;
                console.error('Error:', response.statusText);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }
    

    async function handleCodeDebug(code) {
        const apiUrl = 'http://127.0.0.1:5000/codedebugger';
    
        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ code }), // Send the code to the server
            });
    
            if (response.ok) {
                const data = await response.json();
                const qualityResult = data.debugged_code; // Assuming the API response structure
    
                // Split the quality result into lines
                const lines = qualityResult.split('\n');
    
                // Create an HTML string for the lines
                const linesHTML = lines.map(line => `<p>${line}</p>`).join('');
    
                // Update the outputDiv content with the HTML
                console.log(linesHTML);
                outputDiv.innerHTML = linesHTML;
            } else {
                const errorData = await response.json();
                outputDiv.textContent = `Error: ${errorData.error}`;
                console.error('Error:', response.statusText);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }
});
