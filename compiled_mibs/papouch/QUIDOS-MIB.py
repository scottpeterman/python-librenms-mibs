# SNMP MIB module (QUIDOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\papouch\QUIDOS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:25 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class OnOff(Integer32):
    """Custom type OnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )





class StatCit(Integer32):
    """Custom type StatCit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("falling", 1),
          ("rising", 2),
          ("both", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PapouchProjekt_ObjectIdentity = ObjectIdentity
papouchProjekt = _PapouchProjekt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248)
)
_Quidos_ObjectIdentity = ObjectIdentity
quidos = _Quidos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 16)
)
_Quido_var_ObjectIdentity = ObjectIdentity
quido_var = _Quido_var_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 16, 1)
)
_TemperatureReading_Type = Integer32
_TemperatureReading_Object = MibScalar
temperatureReading = _TemperatureReading_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 1, 1),
    _TemperatureReading_Type()
)
temperatureReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureReading.setStatus("current")
_Temperature_S_Reading_Type = DisplayString
_Temperature_S_Reading_Object = MibScalar
temperature_S_Reading = _Temperature_S_Reading_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 1, 2),
    _Temperature_S_Reading_Type()
)
temperature_S_Reading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature_S_Reading.setStatus("current")
_User_name_Type = DisplayString
_User_name_Object = MibScalar
user_name = _User_name_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 1, 3),
    _User_name_Type()
)
user_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    user_name.setStatus("current")
_Device_msg_Type = DisplayString
_Device_msg_Object = MibScalar
device_msg = _Device_msg_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 1, 4),
    _Device_msg_Type()
)
device_msg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    device_msg.setStatus("current")
_Table_in_ObjectIdentity = ObjectIdentity
table_in = _Table_in_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 16, 2)
)
_InTable_Object = MibTable
inTable = _InTable_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 2, 1)
)
if mibBuilder.loadTexts:
    inTable.setStatus("current")
_InEntry_Object = MibTableRow
inEntry = _InEntry_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1)
)
inEntry.setIndexNames(
    (0, "QUIDOS-MIB", "index"),
)
if mibBuilder.loadTexts:
    inEntry.setStatus("current")
__pysmi_in_Type = OnOff
__pysmi_in_Object = MibTableColumn
_pysmi_in = __pysmi_in_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 1),
    __pysmi_in_Type()
)
_pysmi_in.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    _pysmi_in.setStatus("current")
_In_name_Type = DisplayString
_In_name_Object = MibTableColumn
in_name = _In_name_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 2),
    _In_name_Type()
)
in_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    in_name.setStatus("current")
_CitrwS_Type = StatCit
_CitrwS_Object = MibTableColumn
citrwS = _CitrwS_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 3),
    _CitrwS_Type()
)
citrwS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    citrwS.setStatus("current")


class _Citrw_Type(Integer32):
    """Custom type citrw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Citrw_Type.__name__ = "Integer32"
_Citrw_Object = MibTableColumn
citrw = _Citrw_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 2, 1, 1, 4),
    _Citrw_Type()
)
citrw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    citrw.setStatus("current")
_Table_out_ObjectIdentity = ObjectIdentity
table_out = _Table_out_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 16, 3)
)
_OutTable_Object = MibTable
outTable = _OutTable_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 3, 1)
)
if mibBuilder.loadTexts:
    outTable.setStatus("current")
_OutEntry_Object = MibTableRow
outEntry = _OutEntry_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1)
)
outEntry.setIndexNames(
    (0, "QUIDOS-MIB", "index"),
)
if mibBuilder.loadTexts:
    outEntry.setStatus("current")
_Out_Type = OnOff
_Out_Object = MibTableColumn
out = _Out_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1, 1),
    _Out_Type()
)
out.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    out.setStatus("current")
_Out_name_Type = DisplayString
_Out_name_Object = MibTableColumn
out_name = _Out_name_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1, 2),
    _Out_name_Type()
)
out_name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    out_name.setStatus("current")
_OutTwr_Type = Integer32
_OutTwr_Object = MibTableColumn
outTwr = _OutTwr_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 3, 1, 1, 3),
    _OutTwr_Type()
)
outTwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outTwr.setStatus("current")
_Table_term_ObjectIdentity = ObjectIdentity
table_term = _Table_term_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 16, 4)
)
_TermTable_Object = MibTable
termTable = _TermTable_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 4, 1)
)
if mibBuilder.loadTexts:
    termTable.setStatus("current")
_TermEntry_Object = MibTableRow
termEntry = _TermEntry_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1)
)
termEntry.setIndexNames(
    (0, "QUIDOS-MIB", "index"),
)
if mibBuilder.loadTexts:
    termEntry.setStatus("current")


class _ModeTerm_Type(Integer32):
    """Custom type modeTerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_ModeTerm_Type.__name__ = "Integer32"
_ModeTerm_Object = MibTableColumn
modeTerm = _ModeTerm_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 1),
    _ModeTerm_Type()
)
modeTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modeTerm.setStatus("current")


class _MezHi_Type(Integer32):
    """Custom type mezHi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_MezHi_Type.__name__ = "Integer32"
_MezHi_Object = MibTableColumn
mezHi = _MezHi_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 2),
    _MezHi_Type()
)
mezHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mezHi.setStatus("current")


class _MezLo_Type(Integer32):
    """Custom type mezLo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-550, 1250),
    )


_MezLo_Type.__name__ = "Integer32"
_MezLo_Object = MibTableColumn
mezLo = _MezLo_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 3),
    _MezLo_Type()
)
mezLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mezLo.setStatus("current")


class _Time_Type(Integer32):
    """Custom type time based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Time_Type.__name__ = "Integer32"
_Time_Object = MibTableColumn
time = _Time_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 4),
    _Time_Type()
)
time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time.setStatus("current")


class _Err_Type(Integer32):
    """Custom type err based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Err_Type.__name__ = "Integer32"
_Err_Object = MibTableColumn
err = _Err_Object(
    (1, 3, 6, 1, 4, 1, 18248, 16, 4, 1, 1, 5),
    _Err_Type()
)
err.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    err.setStatus("current")

# Managed Objects groups


# Notification objects

temp_msg = NotificationType(
    (1, 3, 6, 1, 4, 1, 18248, 16, 1, 0, 1)
)
temp_msg.setObjects(
      *(("QUIDOS-MIB", "user-name"),
        ("QUIDOS-MIB", "device-msg"))
)
if mibBuilder.loadTexts:
    temp_msg.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QUIDOS-MIB",
    **{"PositiveInteger": PositiveInteger,
       "OnOff": OnOff,
       "StatCit": StatCit,
       "papouchProjekt": papouchProjekt,
       "quidos": quidos,
       "quido-var": quido_var,
       "temp-msg": temp_msg,
       "temperatureReading": temperatureReading,
       "temperature-S-Reading": temperature_S_Reading,
       "user-name": user_name,
       "device-msg": device_msg,
       "table-in": table_in,
       "inTable": inTable,
       "inEntry": inEntry,
       "in": _pysmi_in,
       "in-name": in_name,
       "citrwS": citrwS,
       "citrw": citrw,
       "table-out": table_out,
       "outTable": outTable,
       "outEntry": outEntry,
       "out": out,
       "out-name": out_name,
       "outTwr": outTwr,
       "table-term": table_term,
       "termTable": termTable,
       "termEntry": termEntry,
       "modeTerm": modeTerm,
       "mezHi": mezHi,
       "mezLo": mezLo,
       "time": time,
       "err": err}
)
