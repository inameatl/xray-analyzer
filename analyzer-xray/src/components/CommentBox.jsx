export default function CommentBox({ comment, setComment }) {
  return (
    <div className="bg-blue-50 p-4 rounded-xl">
      <h3 className="font-semibold mb-1">📝 Describe what you see</h3>
      <textarea
        className="w-full border rounded-xl p-2"
        rows="4"
        placeholder="Example: Bilateral ground glass opacities..."
        value={comment}
        onChange={(e) => setComment(e.target.value)}
      />
    </div>
  );
}
