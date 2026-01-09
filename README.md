<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
</head>
<body>


<h1>📊 Grade Calculator</h1>

<p>
A <strong>relative grading system</strong> based on class
<strong>Mean</strong> and <strong>Standard Deviation</strong>,
supporting both a <strong>CLI</strong> and a <strong>Streamlit web UI</strong>.
</p>
<p>
Live Demo:
<a href="https://relative-grade-calculator-kunal.streamlit.app/" target="_blank">
    https://relative-grade-calculator-kunal.streamlit.app/
</a>
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
    <li>Relative grading using Mean &amp; SD</li>
    <li>Official SD-based grading policy with caps</li>
    <li>Multiple input modes:
        <ul>
            <li>CSV (full class)</li>
            <li>Manual entry (full class)</li>
            <li>Known Mean &amp; SD (multiple students)</li>
            <li><strong>Single-student grading</strong></li>
        </ul>
    </li>
    <li>CLI application and Streamlit web interface</li>
    <li>Robust CSV handling (case-insensitive column names)</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>
<pre>
grade_calculator/
├── statistics.py
├── grading_policy.py
├── grading_engine.py
├── input_layer.py
├── main.py
└── app.py
</pre>

<hr>

<h2>⚙️ Setup</h2>
<pre>
pip install pandas streamlit
</pre>

<hr>

<h2>▶️ Run the CLI</h2>
<pre>
python main.py
</pre>

<hr>

<h2>🌐 Run the Streamlit App</h2>
<pre>
streamlit run app.py
</pre>

<hr>

<h2>📂 CSV Format</h2>
<ul>
    <li>CSV must contain a <code>marks</code> column</li>
    <li>Column name is case-insensitive</li>
</ul>

<hr>

<h2>🎯 Best Use Cases</h2>
<ul>
    <li>Full class grading → CSV / Manual</li>
    <li>Re-evaluation or late entry → Single-student mode</li>
    <li>Quick grade lookup → Single-student mode</li>
</ul>

<hr>

<h2>🧠 Core Idea</h2>
<p>
Once class <strong>Mean</strong> and <strong>Standard Deviation</strong> are known,
<strong>only the student’s marks are required</strong> to determine the grade.
</p>

</body>
</html>
