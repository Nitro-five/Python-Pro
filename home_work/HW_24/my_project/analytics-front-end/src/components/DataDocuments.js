import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DataDocuments = () => {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .post('http://127.0.0.1:8000/graphql/', {
        query: `
          query {
            all_data_documents {
              id
              title
              description
            }
          }
        `,
      })
      .then((response) => {
        console.log('API response:', response.data);
        setData(response.data.data.all_data_documents);
      })
      .catch((err) => {
        console.error('Ошибка загрузки данных:', err);
        setError(err.message);
      });
  }, []);

  if (error) {
    return <div>Ошибка: {error}</div>;
  }

  return (
    <div>
      <h1>Documents</h1>
      {data.length > 0 ? (
        data.map((doc) => (
          <div key={doc.id}>
            <h3>{doc.title}</h3>
            <p>{doc.description}</p>
          </div>
        ))
      ) : (
        <p>Загрузка...</p>
      )}
    </div>
  );
};

export default DataDocuments;
