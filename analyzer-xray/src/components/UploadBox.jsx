export default function UploadBox({ onFileSelect }) {
  return (
    <div className="border-2 border-dashed rounded-xl p-6 bg-white text-center">
      <h3 className="text-lg font-semibold mb-2">📁 Upload X-Ray Image</h3>
      <input
        type="file"
        accept="image/*"
        onChange={(e) => onFileSelect(e.target.files[0])}
        className="block mx-auto"
      />
    </div>
  );
}
