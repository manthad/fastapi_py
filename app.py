from fastapi import FastAPI
from routes.basics import app as basics_app
from routes.enumFiles import app as enumerate_app
from routes.parameters import app as parameters_app
from routes.body import app as body_app
from routes.querypStringValidation import app as query_validation_app
# from routes.basemodel import app as base_model_app
# from routes.Returntypes import app as return_types_app
# from routes.extramodels import app as extra_models_app
# from routes.responsestatuscode import app as response_status_code_app
# from routes.files import app as files_app
# from routes.handlingerrors import app as handling_errors_app


app = FastAPI()

app.include_router(basics_app, prefix="/basics", tags=["Lesson 1 Basics"])
app.include_router(enumerate_app, prefix="/enums", tags=["Lesson 2 Enums"])
app.include_router(parameters_app, prefix="/parameters", tags=["Lesson 3 Parameters"])
app.include_router(body_app, prefix="/body", tags=["Lesson 4 Body"])
app.include_router(query_validation_app, prefix="/query-validation", tags=["Lesson 5 Query Validation"])
# app.include_router(base_model_app, prefix="/base-model", tags=["Lesson 6 Base Model"])
# app.include_router(return_types_app, prefix="/return-types", tags=["Lesson 7 Return Types"])
# app.include_router(extra_models_app, prefix="/extra-models", tags=["Lesson 8 Extra Models"])
# app.include_router(response_status_code_app, prefix="/response-status-code", tags=["Lesson 9 Response Status Code"])
# app.include_router(files_app, prefix="/files", tags=["Lesson 10 Files"])
# app.include_router(handling_errors_app, prefix="/handling-errors", tags=["Lesson 11 Handling Errors"])
