def preprocess_data(contract, personal, phone, internet):
    # Crear un nuevo dataset con la unión de las tres tablas
    dataset = (
        contract
        .merge(personal, on="customerID", how="left")
        .merge(phone, on="customerID", how="left")
        .merge(internet, on="customerID", how="left")
    )

    # Crear nueva columna en el dataset con base en la columna EndDate de la tabla original Contract
    dataset["Churn"] = (~(dataset["EndDate"] == "No")).astype("int8")
    return dataset