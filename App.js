import React, { useEffect, useState } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
    const [data, setData] = useState([]);
    const [filteredData, setFilteredData] = useState([]);
    const [selectedYear, setSelectedYear] = useState("");
    const [selectedCountry, setSelectedCountry] = useState("");
    const [selectedTopic, setSelectedTopic] = useState("");

    // Fetch data from Flask API
    useEffect(() => {
        axios.get("http://localhost:5000/data")
            .then(response => {
                setData(response.data);
                setFilteredData(response.data); // Set filtered data initially
            })
            .catch(error => console.error("Error fetching data:", error));
    }, []);

    // Handle Filter Change
    useEffect(() => {
        let filtered = data;
        if (selectedYear) {
            filtered = filtered.filter(item => item.year === parseInt(selectedYear));
        }
        if (selectedCountry) {
            filtered = filtered.filter(item => item.country === selectedCountry);
        }
        if (selectedTopic) {
            filtered = filtered.filter(item => item.topics === selectedTopic);
        }
        setFilteredData(filtered);
    }, [selectedYear, selectedCountry, selectedTopic, data]);

    // Extract unique values for dropdowns
    const years = [...new Set(data.map(item => item.year))].sort();
    const countries = [...new Set(data.map(item => item.country))].sort();
    const topics = [...new Set(data.map(item => item.topics))].sort();

    // Chart Data
    const chartData = {
        labels: filteredData.map(item => item.year),
        datasets: [
            {
                label: "Intensity",
                data: filteredData.map(item => item.intensity),
                backgroundColor: "rgba(75, 192, 192, 0.6)"
            },
            {
                label: "Likelihood",
                data: filteredData.map(item => item.likelihood),
                backgroundColor: "rgba(255, 99, 132, 0.6)"
            }
        ]
    };

    return (
        <div className="container mt-5">
            <h2 className="text-center">Data Visualization Dashboard</h2>

            {/* Filter Controls */}
            <div className="row mb-3">
                <div className="col-md-4">
                    <label>Filter by Year:</label>
                    <select className="form-control" onChange={(e) => setSelectedYear(e.target.value)}>
                        <option value="">All Years</option>
                        {years.map(year => <option key={year} value={year}>{year}</option>)}
                    </select>
                </div>
                <div className="col-md-4">
                    <label>Filter by Country:</label>
                    <select className="form-control" onChange={(e) => setSelectedCountry(e.target.value)}>
                        <option value="">All Countries</option>
                        {countries.map(country => <option key={country} value={country}>{country}</option>)}
                    </select>
                </div>
                <div className="col-md-4">
                    <label>Filter by Topic:</label>
                    <select className="form-control" onChange={(e) => setSelectedTopic(e.target.value)}>
                        <option value="">All Topics</option>
                        {topics.map(topic => <option key={topic} value={topic}>{topic}</option>)}
                    </select>
                </div>
            </div>

            {/* Bar Chart */}
            <div className="card p-3">
                <Bar data={chartData} />
            </div>
        </div>
    );
};

export default App;
