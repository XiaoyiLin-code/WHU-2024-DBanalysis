# to regenerate this from scratch, run scripts/regenerate_python_stubs.sh .
# be warned - currently there are still tweaks needed after this file is
# generated. These should be annotated with a comment like
# # stubgen override
# to help the sanity of maintainers.

import duckdb.typing as typing
import duckdb.functional as functional
from duckdb.typing import DuckDBPyType
from duckdb.functional import FunctionNullHandling, PythonUDFType
from duckdb.value.constant import (
    Value,
    NullValue,
    BooleanValue,
    UnsignedBinaryValue,
    UnsignedShortValue,
    UnsignedIntegerValue,
    UnsignedLongValue,
    BinaryValue,
    ShortValue,
    IntegerValue,
    LongValue,
    HugeIntegerValue,
    FloatValue,
    DoubleValue,
    DecimalValue,
    StringValue,
    UUIDValue,
    BitValue,
    BlobValue,
    DateValue,
    IntervalValue,
    TimestampValue,
    TimestampSecondValue,
    TimestampMilisecondValue,
    TimestampNanosecondValue,
    TimestampTimeZoneValue,
    TimeValue,
    TimeTimeZoneValue,
)

# We also run this in python3.7, where this is needed
from typing_extensions import Literal
# stubgen override - missing import of Set
from typing import Any, ClassVar, Set, Optional, Callable
from io import StringIO, TextIOBase

from typing import overload, Dict, List, Union
import pandas
# stubgen override - unfortunately we need this for version checks
import sys
import fsspec
import pyarrow.lib
import polars
# stubgen override - This should probably not be exposed
apilevel: str
comment: token_type
default_connection: DuckDBPyConnection
identifier: token_type
keyword: token_type
numeric_const: token_type
operator: token_type
paramstyle: str
string_const: token_type
threadsafety: int
__standard_vector_size__: int
STANDARD: ExplainType
ANALYZE: ExplainType
DEFAULT: PythonExceptionHandling
RETURN_NULL: PythonExceptionHandling
ROWS: RenderMode
COLUMNS: RenderMode

__version__: str

__interactive__: bool
__jupyter__: bool

class BinderException(ProgrammingError): ...

class CatalogException(ProgrammingError): ...

class ConnectionException(OperationalError): ...

class ConstraintException(IntegrityError): ...

class ConversionException(DataError): ...

class DataError(Error): ...

class ExplainType:
    STANDARD: ExplainType
    ANALYZE: ExplainType
    def __int__(self) -> int: ...
    def __index__(self) -> int: ...
    @property
    def __members__(self) -> Dict[str, ExplainType]: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class RenderMode:
    ROWS: RenderMode
    COLUMNS: RenderMode
    def __int__(self) -> int: ...
    def __index__(self) -> int: ...
    @property
    def __members__(self) -> Dict[str, RenderMode]: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class PythonExceptionHandling:
    DEFAULT: PythonExceptionHandling
    RETURN_NULL: PythonExceptionHandling
    def __int__(self) -> int: ...
    def __index__(self) -> int: ...
    @property
    def __members__(self) -> Dict[str, PythonExceptionHandling]: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Expression:
    def __init__(self, *args, **kwargs) -> None: ...
    def __neg__(self) -> "Expression": ...

    def __add__(self, expr: "Expression") -> "Expression": ...
    def __radd__(self, expr: "Expression") -> "Expression": ...

    def __sub__(self, expr: "Expression") -> "Expression": ...
    def __rsub__(self, expr: "Expression") -> "Expression": ...

    def __mul__(self, expr: "Expression") -> "Expression": ...
    def __rmul__(self, expr: "Expression") -> "Expression": ...

    def __div__(self, expr: "Expression") -> "Expression": ...
    def __rdiv__(self, expr: "Expression") -> "Expression": ...

    def __truediv__(self, expr: "Expression") -> "Expression": ...
    def __rtruediv__(self, expr: "Expression") -> "Expression": ...

    def __floordiv__(self, expr: "Expression") -> "Expression": ...
    def __rfloordiv__(self, expr: "Expression") -> "Expression": ...

    def __mod__(self, expr: "Expression") -> "Expression": ...
    def __rmod__(self, expr: "Expression") -> "Expression": ...

    def __pow__(self, expr: "Expression") -> "Expression": ...
    def __rpow__(self, expr: "Expression") -> "Expression": ...

    def __and__(self, expr: "Expression") -> "Expression": ...
    def __rand__(self, expr: "Expression") -> "Expression": ...
    def __or__(self, expr: "Expression") -> "Expression": ...
    def __ror__(self, expr: "Expression") -> "Expression": ...
    def __invert__(self) -> "Expression": ...

    def __eq__(# type: ignore[override]
        self, expr: "Expression") -> "Expression": ...
    def __ne__(# type: ignore[override]
        self, expr: "Expression") -> "Expression": ...
    def __gt__(self, expr: "Expression") -> "Expression": ...
    def __ge__(self, expr: "Expression") -> "Expression": ...
    def __lt__(self, expr: "Expression") -> "Expression": ...
    def __le__(self, expr: "Expression") -> "Expression": ...

    def show(self, max_width: Optional[int] = None, max_rows: Optional[int] = None, max_col_width: Optional[int] = None, null_value: Optional[str] = None, render_mode: Optional[RenderMode] = None) -> None: ...
    def __repr__(self) -> str: ...
    def alias(self, alias: str) -> None: ...
    def when(self, condition: "Expression", value: "Expression") -> "Expression": ...
    def otherwise(self, value: "Expression") -> "Expression": ...
    def cast(self, type: DuckDBPyType) -> "Expression": ...
    def asc(self) -> "Expression": ...
    def desc(self) -> "Expression": ...
    def nulls_first(self) -> "Expression": ...
    def nulls_last(self) -> "Expression": ...
    def isin(self, *cols: "Expression") -> "Expression": ...
    def isnotin(self, *cols: "Expression") -> "Expression": ...

def StarExpression(exclude: Optional[List[str]]) -> Expression: ...
def ColumnExpression(column: str) -> Expression: ...
def ConstantExpression(val: Any) -> Expression: ...
def CaseExpression(condition: Expression, value: Expression) -> Expression: ...
def FunctionExpression(function: str, *cols: Expression) -> Expression: ...

class DuckDBPyConnection:
    def __init__(self, *args, **kwargs) -> None: ...
    def append(self, table_name: str, df: pandas.DataFrame) -> DuckDBPyConnection: ...
    def arrow(self, rows_per_batch: int = ...) -> pyarrow.lib.Table: ...
    def begin(self) -> DuckDBPyConnection: ...
    def close(self) -> None: ...
    def commit(self) -> DuckDBPyConnection: ...
    def cursor(self) -> DuckDBPyConnection: ...
    def df(self) -> pandas.DataFrame: ...
    def duplicate(self) -> DuckDBPyConnection: ...
    def execute(self, query: str, parameters: object = ..., multiple_parameter_sets: bool = ...) -> DuckDBPyConnection: ...
    def executemany(self, query: str, parameters: object = ...) -> DuckDBPyConnection: ...
    def fetch_arrow_table(self, rows_per_batch: int = ...) -> pyarrow.lib.Table: ...
    def fetch_df(self, *args, **kwargs) -> pandas.DataFrame: ...
    def fetch_df_chunk(self, *args, **kwargs) -> pandas.DataFrame: ...
    def fetch_record_batch(self, rows_per_batch: int = ...) -> pyarrow.lib.RecordBatchReader: ...
    def fetchall(self) -> List[Any]: ...
    def fetchdf(self, *args, **kwargs) -> pandas.DataFrame: ...
    def fetchmany(self, size: int = ...) -> List[Any]: ...
    def fetchnumpy(self) -> dict: ...
    def fetchone(self) -> Optional[tuple]: ...
    def from_arrow(self, arrow_object: object) -> DuckDBPyRelation: ...
    def read_json(
        self,
        file_name: str,
        columns: Optional[Dict[str,str]] = None,
        sample_size: Optional[int] = None,
        maximum_depth: Optional[int] = None,
        records: Optional[str] = None,
        format: Optional[str] = None
    ) -> DuckDBPyRelation: ...
    def read_csv(
        self,
        path_or_buffer: Union[str, StringIO, TextIOBase],
        header: Optional[bool | int] = None,
        compression: Optional[str] = None,
        sep: Optional[str] = None,
        delimiter: Optional[str] = None,
        dtype: Optional[Dict[str, str] | List[str]] = None,
        na_values: Optional[str] = None,
        skiprows: Optional[int] = None,
        quotechar: Optional[str] = None,
        escapechar: Optional[str] = None,
        encoding: Optional[str] = None,
        parallel: Optional[bool] = None,
        date_format: Optional[str] = None,
        timestamp_format: Optional[str] = None,
        sample_size: Optional[int] = None,
        all_varchar: Optional[bool] = None,
        normalize_names: Optional[bool] = None,
        filename: Optional[bool] = None,
        null_padding: Optional[bool] = None,
        names: Optional[List[str]] = None
    ) -> DuckDBPyRelation: ...
    def from_csv_auto(
        self,
        path_or_buffer: Union[str, StringIO, TextIOBase],
        header: Optional[bool | int] = None,
        compression: Optional[str] = None,
        sep: Optional[str] = None,
        delimiter: Optional[str] = None,
        dtype: Optional[Dict[str, str] | List[str]] = None,
        na_values: Optional[str] = None,
        skiprows: Optional[int] = None,
        quotechar: Optional[str] = None,
        escapechar: Optional[str] = None,
        encoding: Optional[str] = None,
        parallel: Optional[bool] = None,
        date_format: Optional[str] = None,
        timestamp_format: Optional[str] = None,
        sample_size: Optional[int] = None,
        all_varchar: Optional[bool] = None,
        normalize_names: Optional[bool] = None,
        filename: Optional[bool] = None,
        null_padding: Optional[bool] = None,
        names: Optional[List[str]] = None
    ) -> DuckDBPyRelation: ...
    def from_df(self, df: pandas.DataFrame = ...) -> DuckDBPyRelation: ...
    @overload
    def read_parquet(self, file_glob: str, binary_as_string: bool = ..., *, file_row_number: bool = ..., filename: bool = ..., hive_partitioning: bool = ..., union_by_name: bool = ...) -> DuckDBPyRelation: ...
    @overload
    def read_parquet(self, file_globs: List[str], binary_as_string: bool = ..., *, file_row_number: bool = ..., filename: bool = ..., hive_partitioning: bool = ..., union_by_name: bool = ...) -> DuckDBPyRelation: ...
    @overload
    def from_parquet(self, file_glob: str, binary_as_string: bool = ..., *, file_row_number: bool = ..., filename: bool = ..., hive_partitioning: bool = ..., union_by_name: bool = ...) -> DuckDBPyRelation: ...
    @overload
    def from_parquet(self, file_globs: List[str], binary_as_string: bool = ..., *, file_row_number: bool = ..., filename: bool = ..., hive_partitioning: bool = ..., union_by_name: bool = ...) -> DuckDBPyRelation: ...
    def from_substrait(self, proto: bytes) -> DuckDBPyRelation: ...
    def get_substrait(self, query: str) -> DuckDBPyRelation: ...
    def get_substrait_json(self, query: str) -> DuckDBPyRelation: ...
    def from_substrait_json(self, json: str) -> DuckDBPyRelation: ...
    def get_table_names(self, query: str) -> Set[str]: ...
    def install_extension(self, *args, **kwargs) -> None: ...
    def interrupt(self) -> None: ...
    def list_filesystems(self) -> List[Any]: ...
    def filesystem_is_registered(self, name: str) -> bool: ...
    def load_extension(self, extension: str) -> None: ...
    def pl(self, rows_per_batch: int = ..., connection: DuckDBPyConnection = ...) -> polars.DataFrame: ...
    def torch(self, connection: DuckDBPyConnection = ...) -> dict: ...
    def tf(self, connection: DuckDBPyConnection = ...) -> dict: ...

    def from_query(self, query: str, **kwargs) -> DuckDBPyRelation: ...
    def query(self, query: str, **kwargs) -> DuckDBPyRelation: ...
    def sql(self, query: str, **kwargs) -> DuckDBPyRelation: ...

    def register(self, view_name: str, python_object: object) -> DuckDBPyConnection: ...
    def remove_function(self, name: str) -> DuckDBPyConnection: ...
    def create_function(
        self,
        name: str,
        func: Callable,
        parameters: Optional[List[DuckDBPyType]] = None,
        return_type: Optional[DuckDBPyType] = None,
        type: Optional[PythonUDFType] = PythonUDFType.NATIVE,
        null_handling: Optional[FunctionNullHandling] = FunctionNullHandling.DEFAULT,
        exception_handling: Optional[PythonExceptionHandling] = PythonExceptionHandling.DEFAULT,
        side_effects: Optional[bool] = False)  -> DuckDBPyConnection: ...
    def register_filesystem(self, filesystem: fsspec.AbstractFileSystem) -> None: ...
    def rollback(self) -> DuckDBPyConnection: ...
    def table(self, table_name: str) -> DuckDBPyRelation: ...
    def table_function(self, name: str, parameters: object = ...) -> DuckDBPyRelation: ...
    def unregister(self, view_name: str) -> DuckDBPyConnection: ...
    def unregister_filesystem(self, name: str) -> None: ...
    def values(self, values: object) -> DuckDBPyRelation: ...
    def view(self, view_name: str) -> DuckDBPyRelation: ...
    def sqltype(self, type_str: str) -> DuckDBPyType: ...
    def dtype(self, type_str: str) -> DuckDBPyType: ...
    def type(self, type_str: str) -> DuckDBPyType: ...
    def struct_type(self, fields: Union[Dict[str, DuckDBPyType], List[str]]) -> DuckDBPyType: ...
    def row_type(self, fields: Union[Dict[str, DuckDBPyType], List[str]]) -> DuckDBPyType: ...
    def union_type(self, members: Union[Dict[str, DuckDBPyType], List[str]]) -> DuckDBPyType: ...
    def string_type(self, collation: str = "") -> DuckDBPyType: ...
    def enum_type(self, name: str, type: DuckDBPyType, values: List[Any]) -> DuckDBPyType: ...
    def decimal_type(self, width: int, scale: int) -> DuckDBPyType: ...
    def list_type(self, type: DuckDBPyType) -> DuckDBPyType: ...
    def array_type(self, type: DuckDBPyType, size: int) -> DuckDBPyType: ...
    def map_type(self, key: DuckDBPyType, value: DuckDBPyType) -> DuckDBPyType: ...
    def __enter__(self) -> DuckDBPyConnection: ...
    def __exit__(self, exc_type: object, exc: object, traceback: object) -> None: ...
    @property
    def description(self) -> Optional[List[Any]]: ...
    @property
    def rowcount(self) -> int: ...

class DuckDBPyRelation:
    def close(self) -> None: ...
    def __getattr__(self, name: str) -> DuckDBPyRelation: ...
    def __getitem__(self, name: str) -> DuckDBPyRelation: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __contains__(self, name: str) -> bool: ...
    def aggregate(self, aggr_expr: str, group_expr: str = ...) -> DuckDBPyRelation: ...
    def apply(self, function_name: str, function_aggr: str, group_expr: str = ..., function_parameter: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...

    def cume_dist(self, window_spec: str, projected_columns: str = ...) -> DuckDBPyRelation: ...
    def dense_rank(self, window_spec: str, projected_columns: str = ...) -> DuckDBPyRelation: ...
    def percent_rank(self, window_spec: str, projected_columns: str = ...) -> DuckDBPyRelation: ...
    def rank(self, window_spec: str, projected_columns: str = ...) -> DuckDBPyRelation: ...
    def rank_dense(self, window_spec: str, projected_columns: str = ...) -> DuckDBPyRelation: ...
    def row_number(self, window_spec: str, projected_columns: str = ...) -> DuckDBPyRelation: ...

    def lag(self, column: str, window_spec: str, offset: int, default_value: str, ignore_nulls: bool, projected_columns: str = ...) -> DuckDBPyRelation: ...
    def lead(self, column: str, window_spec: str, offset: int, default_value: str, ignore_nulls: bool, projected_columns: str = ...) -> DuckDBPyRelation: ...
    def nth_value(self, column: str, window_spec: str, offset: int, ignore_nulls: bool = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...

    def value_counts(self, column: str, groups: str = ...) -> DuckDBPyRelation: ...
    def geomean(self, column: str, groups: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def first(self, column: str, groups: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def first_value(self, column: str, window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def last(self, column: str, groups: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def last_value(self, column: str, window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def mode(self, aggregation_columns: str, group_columns: str = ...) -> DuckDBPyRelation: ...
    def n_tile(self, window_spec: str, num_buckets: int, projected_columns: str = ...) -> DuckDBPyRelation: ...
    def quantile_cont(self, column: str, q: Union[float, List[float]] = ..., groups: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def quantile_disc(self, column: str, q: Union[float, List[float]] = ..., groups: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def sum(self, sum_aggr: str, group_expr: str = ...) -> DuckDBPyRelation: ...

    def any_value(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def arg_max(self, arg_column: str, value_column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def arg_min(self, arg_column: str, value_column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def avg(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def bit_and(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def bit_or(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def bit_xor(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def bitstring_agg(self, column: str, min: Optional[int], max: Optional[int], groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def bool_and(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def bool_or(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def count(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def favg(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def fsum(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def histogram(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def max(self, max_aggr: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def min(self, min_aggr: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def mean(self, mean_aggr: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def median(self, median_aggr: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def product(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def quantile(self, q: str, quantile_aggr: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def std(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def stddev(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def stddev_pop(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def stddev_samp(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def string_agg(self, column: str, sep: str = ..., groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def var(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def var_pop(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def var_samp(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def variance(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...
    def list(self, column: str, groups: str = ..., window_spec: str = ..., projected_columns: str = ...) -> DuckDBPyRelation: ...

    def arrow(self, batch_size: int = ...) -> pyarrow.lib.Table: ...
    def create(self, table_name: str) -> None: ...
    def create_view(self, view_name: str, replace: bool = ...) -> DuckDBPyRelation: ...
    def describe(self) -> DuckDBPyRelation: ...
    def df(self, *args, **kwargs) -> pandas.DataFrame: ...
    def distinct(self) -> DuckDBPyRelation: ...
    def except_(self, other_rel: DuckDBPyRelation) -> DuckDBPyRelation: ...
    def execute(self, *args, **kwargs) -> DuckDBPyRelation: ...
    def explain(self, type: Optional[Literal['standard', 'analyze'] | int] = 'standard') -> str: ...
    def fetchall(self) -> List[Any]: ...
    def fetchmany(self, size: int = ...) -> List[Any]: ...
    def fetchnumpy(self) -> dict: ...
    def fetchone(self) -> Optional[tuple]: ...
    def fetchdf(self, *args, **kwargs) -> Any: ...
    def fetch_arrow_reader(self, batch_size: int = ...) -> pyarrow.lib.RecordBatchReader: ...
    def fetch_arrow_table(self, rows_per_batch: int = ...) -> pyarrow.lib.Table: ...
    def filter(self, filter_expr: Union[Expression, str]) -> DuckDBPyRelation: ...
    def insert(self, values: object) -> None: ...
    def insert_into(self, table_name: str) -> None: ...
    def intersect(self, other_rel: DuckDBPyRelation) -> DuckDBPyRelation: ...
    def join(self, other_rel: DuckDBPyRelation, condition: str, how: str = ...) -> DuckDBPyRelation: ...
    def limit(self, n: int, offset: int = ...) -> DuckDBPyRelation: ...
    def map(self, map_function: function, schema: Optional[Dict[str, DuckDBPyType]]) -> DuckDBPyRelation: ...
    def order(self, order_expr: str) -> DuckDBPyRelation: ...
    def sort(self, *cols: Expression) -> DuckDBPyRelation: ...
    def project(self, *cols: Union[str, Expression]) -> DuckDBPyRelation: ...
    def select(self, *cols: Union[str, Expression]) -> DuckDBPyRelation: ...
    def pl(self, rows_per_batch: int = ..., connection: DuckDBPyConnection = ...) -> polars.DataFrame: ...
    def query(self, virtual_table_name: str, sql_query: str) -> DuckDBPyRelation: ...
    def record_batch(self, batch_size: int = ...) -> pyarrow.lib.RecordBatchReader: ...
    def select_types(self, types: List[Union[str, DuckDBPyType]]) -> DuckDBPyRelation: ...
    def select_dtypes(self, types: List[Union[str, DuckDBPyType]]) -> DuckDBPyRelation: ...
    def set_alias(self, alias: str) -> DuckDBPyRelation: ...
    def show(self) -> None: ...
    def sql_query(self) -> str: ...
    def to_arrow_table(self, batch_size: int = ...) -> pyarrow.lib.Table: ...
    def to_csv(
            self,
            file_name: str,
            sep: Optional[str],
            na_rep: Optional[str],
            header: Optional[bool],
            quotechar: Optional[str],
            escapechar: Optional[str],
            date_format: Optional[str],
            timestamp_format: Optional[str],
            quoting: Optional[str | int],
            encoding: Optional[str],
            compression: Optional[str]
    ) -> None: ...
    def to_df(self, *args, **kwargs) -> pandas.DataFrame: ...
    def to_parquet(
            self,
            file_name: str,
            compression: Optional[str]
    ) -> None: ...
    def to_table(self, table_name: str) -> None: ...
    def to_view(self, view_name: str, replace: bool = ...) -> DuckDBPyRelation: ...
    def torch(self, connection: DuckDBPyConnection = ...) -> dict: ...
    def tf(self, connection: DuckDBPyConnection = ...) -> dict: ...
    def union(self, union_rel: DuckDBPyRelation) -> DuckDBPyRelation: ...
    def unique(self, unique_aggr: str) -> DuckDBPyRelation: ...
    def write_csv(
            self,
            file_name: str,
            sep: Optional[str],
            na_rep: Optional[str],
            header: Optional[bool],
            quotechar: Optional[str],
            escapechar: Optional[str],
            date_format: Optional[str],
            timestamp_format: Optional[str],
            quoting: Optional[str | int],
            encoding: Optional[str],
            compression: Optional[str]
    ) -> None: ...
    def write_parquet(
            self,
            file_name: str,
            compression: Optional[str]
    ) -> None: ...
    def __len__(self) -> int: ...
    @property
    def alias(self) -> str: ...
    @property
    def columns(self) -> List[Any]: ...
    @property
    def dtypes(self) -> List[DuckDBPyType]: ...
    @property
    def description(self) -> List[Any]: ...
    @property
    def shape(self) -> tuple: ...
    @property
    def type(self) -> str: ...
    @property
    def types(self) -> List[DuckDBPyType]: ...

class Error(Exception): ...

class FatalException(Error): ...

class HTTPException(IOException):
    status_code: int
    body: str
    reason: str
    headers: Dict[str, str]

class IOException(OperationalError): ...

class IntegrityError(Error): ...

class InternalError(Error): ...

class InternalException(InternalError): ...

class InterruptException(Error): ...

class InvalidInputException(ProgrammingError): ...

class InvalidTypeException(ProgrammingError): ...

class NotImplementedException(NotSupportedError): ...

class NotSupportedError(Error): ...

class OperationalError(Error): ...

class OutOfMemoryException(OperationalError): ...

class OutOfRangeException(DataError): ...

class ParserException(ProgrammingError): ...

class PermissionException(Error): ...

class ProgrammingError(Error): ...

class SequenceException(Error): ...

class SerializationException(OperationalError): ...

class SyntaxException(ProgrammingError): ...

class TransactionException(OperationalError): ...

class TypeMismatchException(DataError): ...

class Warning(Exception): ...

class token_type:
    # stubgen override - these make mypy sad
    #__doc__: ClassVar[str] = ...  # read-only
    #__members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    comment: ClassVar[token_type] = ...
    identifier: ClassVar[token_type] = ...
    keyword: ClassVar[token_type] = ...
    numeric_const: ClassVar[token_type] = ...
    operator: ClassVar[token_type] = ...
    string_const: ClassVar[token_type] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    # stubgen override - pybind only puts index in python >= 3.8: https://github.com/EricCousineau-TRI/pybind11/blob/54430436/include/pybind11/pybind11.h#L1789
    if sys.version_info >= (3, 7):
        def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...
    @property
    # stubgen override - this gets removed by stubgen but it shouldn't
    def __members__(self) -> object: ...

def aggregate(df: pandas.DataFrame, aggr_expr: str, group_expr: str = ..., connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def alias(df: pandas.DataFrame, alias: str, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def connect(database: str = ..., read_only: bool = ..., config: dict = ...) -> DuckDBPyConnection: ...
def distinct(df: pandas.DataFrame, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def filter(df: pandas.DataFrame, filter_expr: str, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def from_substrait_json(jsonm: str, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def limit(df: pandas.DataFrame, n: int, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def order(df: pandas.DataFrame, order_expr: str, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def project(df: pandas.DataFrame, project_expr: str, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def write_csv(df: pandas.DataFrame, file_name: str, connection: DuckDBPyConnection = ...) -> None: ...
def read_json(
    file_name: str,
    columns: Optional[Dict[str,str]] = None,
    sample_size: Optional[int] = None,
    maximum_depth: Optional[int] = None,
    format: Optional[str] = None,
    records: Optional[str] = None,
    connection: DuckDBPyConnection = ...
) -> DuckDBPyRelation: ...
def read_csv(
    path_or_buffer: Union[str, StringIO, TextIOBase],
    header: Optional[bool | int] = None,
    compression: Optional[str] = None,
    sep: Optional[str] = None,
    delimiter: Optional[str] = None,
    dtype: Optional[Dict[str, str] | List[str]] = None,
    na_values: Optional[str] = None,
    skiprows: Optional[int] = None,
    quotechar: Optional[str] = None,
    escapechar: Optional[str] = None,
    encoding: Optional[str] = None,
    parallel: Optional[bool] = None,
    date_format: Optional[str] = None,
    timestamp_format: Optional[str] = None,
    sample_size: Optional[int] = None,
    all_varchar: Optional[bool] = None,
    normalize_names: Optional[bool] = None,
    filename: Optional[bool] = None,
    connection: DuckDBPyConnection = ...
) -> DuckDBPyRelation: ...
def from_csv_auto(
    name: str,
    header: Optional[bool | int] = None,
    compression: Optional[str] = None,
    sep: Optional[str] = None,
    delimiter: Optional[str] = None,
    dtype: Optional[Dict[str, str] | List[str]] = None,
    na_values: Optional[str] = None,
    skiprows: Optional[int] = None,
    quotechar: Optional[str] = None,
    escapechar: Optional[str] = None,
    encoding: Optional[str] = None,
    parallel: Optional[bool] = None,
    date_format: Optional[str] = None,
    timestamp_format: Optional[str] = None,
    sample_size: Optional[int] = None,
    all_varchar: Optional[bool] = None,
    normalize_names: Optional[bool] = None,
    filename: Optional[bool] = None,
    null_padding: Optional[bool] = None,
    connection: DuckDBPyConnection = ...
) -> DuckDBPyRelation: ...

def append(table_name: str, df: pandas.DataFrame, connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def arrow(rows_per_batch: int = ..., connection: DuckDBPyConnection = ...) -> pyarrow.lib.Table: ...
def begin(connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def close(connection: DuckDBPyConnection = ...) -> None: ...
def commit(connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def cursor(connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def df(connection: DuckDBPyConnection = ...) -> pandas.DataFrame: ...
def description(connection: DuckDBPyConnection = ...) -> Optional[List[Any]]: ...
def rowcount(connection: DuckDBPyConnection = ...) -> int: ...
def duplicate(connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def execute(query: str, parameters: object = ..., multiple_parameter_sets: bool = ..., connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def executemany(query: str, parameters: object = ..., connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def fetch_arrow_table(rows_per_batch: int = ..., connection: DuckDBPyConnection = ...) -> pyarrow.lib.Table: ...
def fetch_df(*args, connection: DuckDBPyConnection = ..., **kwargs) -> pandas.DataFrame: ...
def fetch_df_chunk(*args, connection: DuckDBPyConnection = ..., **kwargs) -> pandas.DataFrame: ...
def fetch_record_batch(rows_per_batch: int = ..., connection: DuckDBPyConnection = ...) -> pyarrow.lib.RecordBatchReader: ...
def fetchall(connection: DuckDBPyConnection = ...) -> List[Any]: ...
def fetchdf(*args, connection: DuckDBPyConnection = ..., **kwargs) -> pandas.DataFrame: ...
def fetchmany(size: int = ..., connection: DuckDBPyConnection = ...) -> List[Any]: ...
def fetchnumpy(connection: DuckDBPyConnection = ...) -> dict: ...
def fetchone(connection: DuckDBPyConnection = ...) -> Optional[tuple]: ...
def from_arrow(arrow_object: object, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def from_df(df: pandas.DataFrame = ..., connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
@overload
def read_parquet(file_glob: str, binary_as_string: bool = ..., *, file_row_number: bool = ..., filename: bool = ..., hive_partitioning: bool = ..., union_by_name: bool = ..., connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
@overload
def read_parquet(file_globs: List[str], binary_as_string: bool = ..., *, file_row_number: bool = ..., filename: bool = ..., hive_partitioning: bool = ..., union_by_name: bool = ..., connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
@overload
def from_parquet(file_glob: str, binary_as_string: bool = ..., *, file_row_number: bool = ..., filename: bool = ..., hive_partitioning: bool = ..., union_by_name: bool = ..., connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
@overload
def from_parquet(file_globs: List[str], binary_as_string: bool = ..., *, file_row_number: bool = ..., filename: bool = ..., hive_partitioning: bool = ..., union_by_name: bool = ..., connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def from_substrait(proto: bytes, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def get_substrait(query: str, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def get_substrait_json(query: str, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def get_table_names(query: str, connection: DuckDBPyConnection = ...) -> Set[str]: ...
def install_extension(*args, connection: DuckDBPyConnection = ..., **kwargs) -> None: ...
def interrupt(connection: DuckDBPyConnection = ...) -> None: ...
def list_filesystems(connection: DuckDBPyConnection = ...) -> List[Any]: ...
def filesystem_is_registered(name: str, connection: DuckDBPyConnection = ...) -> bool: ...
def load_extension(extension: str, connection: DuckDBPyConnection = ...) -> None: ...
def pl(rows_per_batch: int = ..., connection: DuckDBPyConnection = ...) -> polars.DataFrame: ...
def torch(connection: DuckDBPyConnection = ...) -> dict: ...
def tf(self, connection: DuckDBPyConnection = ...) -> dict: ...
def register(view_name: str, python_object: object, connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def remove_function(name: str, connection : DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def create_function(
    name: str,
    func: Callable,
    parameters: Optional[List[DuckDBPyType]] = None,
    return_type: Optional[DuckDBPyType] = None,
    type: Optional[PythonUDFType] = PythonUDFType.NATIVE,
    null_handling: Optional[FunctionNullHandling] = FunctionNullHandling.DEFAULT,
    exception_handling: Optional[PythonExceptionHandling] = PythonExceptionHandling.DEFAULT,
    side_effects: Optional[bool] = False,
    connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def register_filesystem(filesystem: fsspec.AbstractFileSystem, connection: DuckDBPyConnection = ...) -> None: ...
def rollback(connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...

def query(query: str, connection: DuckDBPyConnection = ..., **kwargs) -> DuckDBPyRelation: ...
def sql(query: str, connection: DuckDBPyConnection = ..., **kwargs) -> DuckDBPyRelation: ...
def from_query(query: str, connection: DuckDBPyConnection = ..., **kwargs) -> DuckDBPyRelation: ...

def table(table_name: str, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def table_function(name: str, parameters: object = ..., connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def unregister(view_name: str, connection: DuckDBPyConnection = ...) -> DuckDBPyConnection: ...
def query_df(df: pandas.DataFrame, virtual_table_name: str, sql_query: str, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def unregister_filesystem(name: str, connection: DuckDBPyConnection = ...) -> None: ...
def tokenize(query: str) -> List[Any]: ...
def values(values: object, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def view(view_name: str, connection: DuckDBPyConnection = ...) -> DuckDBPyRelation: ...
def sqltype(type_str: str, connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def dtype(type_str: str, connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def type(type_str: str, connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def struct_type(fields: Union[Dict[str, DuckDBPyType], List[str]], connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def row_type(fields: Union[Dict[str, DuckDBPyType], List[str]], connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def union_type(members: Union[Dict[str, DuckDBPyType], List[str]], connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def string_type(collation: str = "", connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def enum_type(name: str, type: DuckDBPyType, values: List[Any], connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def decimal_type(width: int, scale: int, connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def array_type(type: DuckDBPyType, size: int, connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def list_type(type: DuckDBPyType, connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
def map_type(key: DuckDBPyType, value: DuckDBPyType, connection: DuckDBPyConnection = ...) -> DuckDBPyType: ...
