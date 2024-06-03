from router import create_app as router

if __name__ == "__main__":
    import uvicorn
    print("Server is running...")

    app = router

    uvicorn.run(app, host="0.0.0.0", port=8000)
