import React, { useState } from "react";
import axios from "axios"; // Import axios for making HTTP requests
import "../App.css"; // Ensure your CSS file includes the necessary styles

const NewChat = ({ setChatLog, setShowMenu }) => {
  const [showDialog, setShowDialog] = useState(false);

  const handleFolderSelect = async (event) => {
    const files = event.target.files;

    if (files.length > 0) {
      // Extract the folder path from the first file's webkitRelativePath
      console.log(files[0])
      var folderPath = files[0].webkitRelativePath.split("/").slice(0, -1).join("/");
      folderPath  = "/Users/shreyanshrai/Desktop/" + folderPath
      console.log(`Selected folder path: ${folderPath}`);

      // Prepare the payload for the Flask server
      const payload = {
        path: folderPath,
      };
      try {
        // Make the API request to the Flask server
        const response = await axios.post(
          "http://127.0.0.1:5000/process-folder", // Update to your Flask server endpoint
          payload
        );

        // Log the response data
        console.log("Server Response:", response.data);

        // Optionally, handle the response data (e.g., update the chat log)
        setChatLog(response.data.results);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }
    setShowDialog(false); // Close the dialog after selection
  };

  return (
    <div>
      <div
        className="sideMenuButton"
        onClick={() => {
          setChatLog([]);
          setShowMenu(false);
          setShowDialog(true);
        }}
      >
        <span>+</span>
        Add Folder
      </div>

      {showDialog && (
        <div className="overlay">
          <div className="modal">
            <div className="modalContent">
              <h3>Select a folder to process</h3>
              <div className="uploadOptions">
                <label className="uploadButton">
                  Select Folder
                  <input
                    type="file"
                    webkitdirectory=""
                    directory=""
                    onChange={handleFolderSelect}
                    style={{ display: "none" }} // Hide the file input
                  />
                  <span>Select Folder</span>
                </label>

                <button
                  className="uploadButton"
                  onClick={() => {
                    document.querySelector('input[type="file"]').click(); // Trigger folder selection
                  }}
                >
                  Open Folder Selector
                </button>

                <button
                  className="uploadButton"
                  onClick={() => setShowDialog(false)}
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default NewChat;
