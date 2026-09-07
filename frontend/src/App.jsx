import { useEffect, useState } from "react";

function App() {
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/photos/")
      .then((response) => response.json())
      .then((data) => setPhotos(data));
  }, []);

  return (
    <main>
      <h1>Event Photos</h1>

      {photos.map((photo) => (
        <div key={photo.id}>
          <strong>{photo.filename}</strong>
          <p>{photo.event_name}</p>
        </div>
      ))}
    </main>
  );
}

export default App;