export default function ResultCard({ result }) {
  const { comment_prediction, ai_prediction, ai_confidence, prediction_match } = result;
  return (
    <div className="bg-white shadow-md rounded-xl p-6">
      <h2 className="text-xl font-bold mb-2">📊 Analysis Results</h2>
      <p><strong>💬 Your Comment Diagnosis:</strong> {comment_prediction.predicted_disease} ({comment_prediction.confidence.toFixed(1)}%)</p>
      <p><strong>🤖 AI Diagnosis:</strong> {ai_prediction} ({(ai_confidence*100).toFixed(1)}%)</p>
      {prediction_match ? (
        <div className="bg-green-100 border border-green-500 text-green-800 p-3 rounded-xl mt-3">
          ✅ Excellent! Your analysis matches the AI
        </div>
      ) : (
        <div className="bg-red-100 border border-red-500 text-red-800 p-3 rounded-xl mt-3">
          ❌ Mismatch! Your comment suggests {comment_prediction.predicted_disease} but AI detected {ai_prediction}.
        </div>
      )}
    </div>
  );
}
