🌌 LexiVerse

Finding needles in a haystack — then sorting them by sharpness.


Welcome to LexiVerse, a high-performance, browser-based search engine that proves you don’t need a massive backend to handle massive datasets.
Built to search over a million entries in milliseconds, LexiVerse is a deep dive into practical algorithm design and frontend optimization.

📜 The Story: A Tale of Two Architectures

Like many good engineering tales, LexiVerse started with a textbook answer:

"If you want ultra-fast search, build a Suffix Trie."

So I did.
And it was a disaster.

Theoretically perfect at O(k) search time, yes — but loading it from a file took 500+ seconds.
It was unusable.

This “failure” became the turning point. I realized real-world engineering is about trade-offs, not just theory.
I scrapped the Trie, replacing it with:

A flat Array for near-zero load times

A custom comparison-based sorting algorithm for relevance ranking

The result? Instant load, instant search, and a smooth user experience — all running entirely in the browser.

✨ Features in Action

Home View
![Demo Screenshot](https://github.com/user-attachments/assets/73b854b5-5d62-4f56-afe5-61d120a5fb28)

Search in Action
![Search Example Screenshot](https://github.com/user-attachments/assets/9b876067-3602-4d6d-91eb-ac90bd309b9b)

🔍 Intelligent Multi-Word Search & Ranking

Handles multi-word queries correctly, ranking by a custom relevance score.
"New York" appears above "New York Buzz" for a reason.

☁️ Real-Time Related Terms Cloud

As you type, LexiVerse analyzes results to generate a cloud of related terms using Hash Map frequency counting.

🎨 Dynamic, Responsive UI

The interface updates with color-coded highlights and live suggestion counts to make searches engaging.

Related Terms Cloud
![Tag Cloud Screenshot](https://github.com/user-attachments/assets/4d16ef34-0860-4aa8-ade9-3b39bd4c0dbe)

Detailed Result View
![Detailed Search Result Screenshot](https://github.com/user-attachments/assets/525cfe7f-fcb5-4762-afd7-f5d86f72f99b)

⚙️ The DSA Powering LexiVerse

The Humble Array — Replaced the Trie for instant load and minimal memory usage.

The Mighty Hash Map — O(1) frequency counting for related terms.

Custom Comparison Sort — Assigns relevance scores for smarter ranking.

🚀 How to Run LexiVerse

1️⃣ Clone the Repository

git clone https://github.com/your-username/lexiverse.git
cd lexiverse


2️⃣ Prepare the Data

Download your source datasets (words_alpha.txt, all-titles-in-ns0.txt) and place them in the project root.
Run:

python generate_dataset.py
python convert_to_json.py


(Note: dataset_clean.txt and data.json are .gitignored to keep the repo light.)

3️⃣ Start a Local Server

python -m http.server


4️⃣ Explore LexiVerse
Open your browser at:

http://localhost:8000

🛠 Tech Stack

Frontend: HTML5, CSS3, JavaScript

Data Handling: JSON, Array, Map

Algorithms: Custom relevance sort, frequency counting

Hosting: Runs entirely client-side — no backend required
