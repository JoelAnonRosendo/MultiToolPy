import React, { useState } from 'react';
import { ArrowRight, Settings, HelpCircle } from 'lucide-react';

const Dashboard = () => {
  const [selectedFile, setSelectedFile] = useState('MultiToolPy_tkinter.py');
  
  const files = [
    'MultiToolPy_tkinter.py',
    'Calculator.py',
    'EmailGenerator.py',
    'PasswordGenerator.py',
    'ConversionApp.py',
    'SaveKeysManager.py',
    'WitAIChat.py'
  ];

  const codeContent = `# Importing necessary libraries
import sys
import subprocess

# List of packages to install
packages = ["requests", "cryptography"]

# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install each package in the list
for package in packages:
    install(package)

print("All dependencies installed successfully.")

import os
import json
import random
import string
import requests
import tkinter as tk
from datetime import datetime
from tkinter import scrolledtext
from cryptography.fernet import Fernet
from tkinter import ttk, simpledialog, messagebox, filedialog

API_KEY = '03461bb35e9c5fccbb7f7db5'
FECHA_ACTUAL = datetime.now()
FORMATO = FECHA_ACTUAL.strftime("%Y-%m-%d-%H-%M")

class MultiToolPy(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MultiToolPy")
        self.geometry("790x450")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.create_calculator_tab()
        self.create_email_generator_tab()
        self.create_password_generator_tab()
        self.create_conversions_tab()
        self.create_save_keys_tab() 
        self.create_chat_ia_tab() 

    # ... (rest of the code)
`;

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <div className="w-64 bg-white shadow-lg">
        <div className="p-4">
          <img src="/api/placeholder/150/50" alt="Aurelius Logo" className="mb-4" />
          <nav>
            {files.map((file, index) => (
              <a
                key={index}
                href="#"
                className={`flex items-center py-2 ${
                  selectedFile === file ? 'text-blue-600 font-semibold' : 'text-gray-600 hover:text-gray-900'
                }`}
                onClick={() => setSelectedFile(file)}
              >
                <ArrowRight className="mr-2" size={20} />
                {file}
              </a>
            ))}
          </nav>
        </div>
        <div className="mt-auto p-4">
          <a href="#" className="text-sm text-gray-600 hover:text-gray-900">About Us</a>
          <a href="#" className="ml-4 text-sm text-gray-600 hover:text-gray-900">Settings</a>
        </div>
      </div>

      {/* Main content */}
      <div className="flex-1 p-8 overflow-auto">
        <h1 className="text-3xl font-bold mb-8">MultiToolPy Code Viewer</h1>
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-2xl font-bold mb-4">{selectedFile}</h2>
          <pre className="bg-gray-100 p-4 rounded-lg overflow-x-auto">
            <code className="text-sm">{codeContent}</code>
          </pre>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;