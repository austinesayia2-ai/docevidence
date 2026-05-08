async function analyze() {

    const text = document.getElementById("text").value;
    const student = document.getElementById("student").value;
    const className = document.getElementById("class").value;
    const assignment = document.getElementById("assignment").value;

    const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();

    document.getElementById("output").innerText =
`
Student: ${student}
Class: ${className}
Assignment: ${assignment}

Plagiarism: ${data.plagiarism}%
AI Signal: ${data.ai_signal}%
Final Score: ${data.final_score}
`;
}