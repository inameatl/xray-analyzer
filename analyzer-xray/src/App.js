import { useState } from "react";
import axios from "axios";
import UploadBox from "./components/UploadBox";
import CommentBox from "./components/CommentBox";
import ResultCard from "./components/ResultCard";

export default function App() {
  const [file, setFile] = useState(null);
  const [comment, setComment] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!file || !comment.trim()) return;
    const formData = new FormData();
    formData.append("file", file);
    formData.append("comment", comment);
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:8000/analyze/", formData);
      setResult(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-6">💬 X-Ray Comment Analyzer</h1>
      <div className="max-w-2xl mx-auto space-y-6">
        <UploadBox onFileSelect={setFile} />
        <CommentBox comment={comment} setComment={setComment} />
        <button
          onClick={handleAnalyze}
          className="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-xl"
        >
          {loading ? "Analyzing..." : "🔍 Evaluate My Analysis"}
        </button>
        {result && <ResultCard result={result} />}
      </div>
    </div>
  );
}
