<div align="center">
  <h1>Python Telegram Bot Patterns (aiogram 3.x)</h1>
  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=for-the-badge&logo=python" alt="Python Version">
    <img src="https://img.shields.io/badge/aiogram-3.x-2CA5E0.svg?style=for-the-badge&logo=telegram" alt="Aiogram Version">
    <img src="https://img.shields.io/github/stars/YOUR_USERNAME/aiogram-patterns?style=for-the-badge&logo=github&label=Stars" alt="GitHub Stars">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License">
  </p>
</div>

<details>
<summary><strong>🇷🇺 Русская версия (Нажмите, чтобы развернуть)</strong></summary>

<br>

<p>Репозиторий с готовыми паттернами кода для разработки <strong>Telegram-ботов на Python</strong> с использованием фреймворка <strong>aiogram 3.x</strong>. Здесь вы найдете рабочие примеры для FSM, кастомных клавиатур, middleware и других задач, что значительно ускорит ваше <strong>bot development</strong>-путешествие.</p>

<hr>

<h2>🚀 Что такое Aiogram Patterns?</h2>
<p>Этот репозиторий — практическое руководство и набор готовых решений для разработчиков <strong>Python Telegram ботов</strong>. Вместо того чтобы искать решения по всему интернету, вы можете взять готовый, чистый и проверенный код для самых частых задач.</p>
<ul>
    <li>✅ <strong>Практический пример</strong>: Файл <code>example_bot</code> показывает, как все <strong>aiogram паттерны</strong> работают вместе.</li>
    <li>✅ <strong>Готовые решения</strong>: Просто скопируйте нужные модули (например, <code>middleware</code> для проверки подписки) в ваш проект.</li>
    <li>✅ <strong>Современный стек</strong>: Весь код написан для <strong>aiogram 3.x</strong> с использованием <code>asyncio</code> и лучших практик.</li>
</ul>

<hr>

<h2>⚡ Быстрый старт: запуск демонстрационного бота</h2>
<p>Следуйте этим шагам, чтобы запустить <strong>example bot</strong> и протестировать все паттерны.</p>

<h3>1. Клонируйте репозиторий</h3>
<pre><code>git clone https://github.com/YOUR_USERNAME/aiogram-patterns.git
cd aiogram-patterns</code></pre>

<h3>2. Создайте и активируйте виртуальное окружение</h3>
<p><em>Для Windows:</em></p>
<pre><code>python -m venv venv && .\venv\Scripts\activate</code></pre>
<p><em>Для macOS/Linux:</em></p>
<pre><code>python3 -m venv venv && source venv/bin/activate</code></pre>

<h3>3. Установите зависимости</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>4. Настройте <code>.env</code> файл</h3>
<ul>
    <li>Скопируйте <code>.env.example</code> в новый файл <code>.env</code>.</li>
    <li>Впишите ваш <code>BOT_TOKEN</code> и <code>YOUR_CHANNEL_ID</code>.</li>
</ul>

<h3>5. Запустите Python Telegram Bot</h3>
<pre><code>python example_bot</code></pre>

<hr>

<h2>🛠️ Паттерны кода для Aiogram 3</h2>

<h3>1. Фабрика клавиатур: Динамические Telegram клавиатуры</h3>
<p><strong>Файл:</strong> <code>keyboards/keyboard_factory.py</code></p>
<p><strong>Что это?</strong> Универсальная фабрика для создания инлайн-клавиатур в <code>aiogram</code> без лишнего кода. Идеально для меню и навигации.</p>

<h3>2. FSM States: Управление диалогами</h3>
<p><strong>Файл:</strong> <code>fsm_states/survey_states.py</code></p>
<p><strong>Что это?</strong> Пример реализации <strong>Finite State Machine (FSM)</strong> для управления состояниями диалога. Используется для пошаговых сценариев, таких как регистрация или квизы.</p>

<h3>3. Subscription Middleware: Проверка подписки на канал</h3>
<p><strong>Файл:</strong> <code>middlewares/subscription.py</code></p>
<p><strong>Что это?</strong> Готовый <strong>middleware</strong> для <code>aiogram</code>, который проверяет подписку пользователя на ваш Telegram-канал.</p>

<h3>4. Deployment Guides: Развертывание Telegram-бота</h3>
<p><strong>Папка:</strong> <code>deployment/</code></p>
<p><strong>Что это?</strong> Инструкции, как сделать <strong>деплой Telegram-бота</strong> на популярных хостинг-платформах.</p>

<hr>

<h2>🤝 Вклад в проект</h2>
<p>Мы приветствуем вклад в проект! Если вы хотите добавить новые <strong>aiogram примеры</strong> или улучшить существующие, ознакомьтесь с файлом <a href="CONTRIBUTING.md">CONTRIBUTING.md</a>.</p>

<h2>📄 Лицензия</h2>
<p>Этот проект распространяется под лицензией MIT. Подробности можно найти в файле <a href="LICENSE">LICENSE</a>.</p>

</details>

<br>

<details open>
<summary><strong>🇬🇧 English Version (Click to expand)</strong></summary>

<br>

<p>A repository with production-ready code patterns for <strong>Python Telegram bot development</strong> using the <strong>aiogram 3.x</strong> framework. Find working examples for FSM, custom keyboards, middleware, and other common tasks to accelerate your bot development journey.</p>

<hr>

<h2>🚀 What is Aiogram Patterns?</h2>
<p>This repository is a practical guide and a set of ready-to-use solutions for <strong>Python Telegram bot</strong> developers. Instead of searching for solutions across the internet, you can grab clean, tested code for the most common tasks.</p>
<ul>
    <li>✅ <strong>Practical Example</strong>: The <code>example_bot</code> file shows how all <strong>aiogram patterns</strong> work together.</li>
    <li>✅ <strong>Ready-to-use Solutions</strong>: Simply copy the modules you need (e.g., the subscription <code>middleware</code>) into your project.</li>
    <li>✅ <strong>Modern Stack</strong>: All code is written for <strong>aiogram 3.x</strong> using <code>asyncio</code> and best practices.</li>
</ul>

<hr>

<h2>⚡ Quick Start: Running the Example Bot</h2>
<p>Follow these steps to run the <strong>example bot</strong> and test all the patterns.</p>

<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/YOUR_USERNAME/aiogram-patterns.git
cd aiogram-patterns</code></pre>

<h3>2. Create and activate a virtual environment</h3>
<p><em>For Windows:</em></p>
<pre><code>python -m venv venv && .\venv\Scripts\activate</code></pre>
<p><em>For macOS/Linux:</em></p>
<pre><code>python3 -m venv venv && source venv/bin/activate</code></pre>

<h3>3. Install dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>4. Configure the <code>.env</code> file</h3>
<ul>
    <li>Copy <code>.env.example</code> to a new file named <code>.env</code>.</li>
    <li>Enter your <code>BOT_TOKEN</code> and <code>YOUR_CHANNEL_ID</code>.</li>
</ul>

<h3>5. Run the Python Telegram Bot</h3>
<pre><code>python example_bot</code></pre>

<hr>

<h2>🛠️ Code Patterns for Aiogram 3</h2>

<h3>1. Keyboard Factory: Dynamic Telegram Keyboards</h3>
<p><strong>File:</strong> <code>keyboards/keyboard_factory.py</code></p>
<p><strong>What is it?</strong> A universal factory for creating inline keyboards in <code>aiogram</code> without boilerplate code. Perfect for menus and navigation.</p>

<h3>2. FSM States: Managing Dialogues</h3>
<p><strong>File:</strong> <code>fsm_states/survey_states.py</code></p>
<p><strong>What is it?</strong> An example of a <strong>Finite State Machine (FSM)</strong> implementation to manage dialogue states. Used for step-by-step scenarios like registration or quizzes.</p>

<h3>3. Subscription Middleware: Check Channel Subscription</h3>
<p><strong>File:</strong> <code>middlewares/subscription.py</code></p>
<p><strong>What is it?</strong> A ready-to-use <strong>middleware</strong> for <code>aiogram</code> that checks if a user is subscribed to your Telegram channel.</p>

<h3>4. Deployment Guides: Deploying a Telegram Bot</h3>
<p><strong>Folder:</strong> <code>deployment/</code></p>
<p><strong>What is it?</strong> Guides on how to <strong>deploy your Telegram bot</strong> to popular hosting platforms.</p>

<hr>

<h2>🤝 Contributing</h2>
<p>Contributions are welcome! If you want to add new <strong>aiogram examples</strong> or improve existing ones, please read the <a href="CONTRIBUTING.md">CONTRIBUTING.md</a> file.</p>

<h2>📄 License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

</details>
