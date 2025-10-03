# SNMP MIB module (NSCRTV-HFCEMS-PROPERTY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cdata\NSCRTV-HFCEMS-PROPERTY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:24:01 2025
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

(propertyIdent,) = mibBuilder.importSymbols(
    "NSCRTV-ROOT",
    "propertyIdent")

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
 TimeTicks,
 Unsigned32,
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
    "TimeTicks",
    "Unsigned32",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AnalogPropertyTable_Object = MibTable
analogPropertyTable = _AnalogPropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1)
)
if mibBuilder.loadTexts:
    analogPropertyTable.setStatus("mandatory")
_AnalogPropertyEntry_Object = MibTableRow
analogPropertyEntry = _AnalogPropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1)
)
analogPropertyEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-PROPERTY-MIB", "analogParameterOID"),
)
if mibBuilder.loadTexts:
    analogPropertyEntry.setStatus("mandatory")
_AnalogParameterOID_Type = ObjectIdentifier
_AnalogParameterOID_Object = MibTableColumn
analogParameterOID = _AnalogParameterOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 1),
    _AnalogParameterOID_Type()
)
analogParameterOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogParameterOID.setStatus("mandatory")


class _AlarmEnable_Type(OctetString):
    """Custom type alarmEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_AlarmEnable_Type.__name__ = "OctetString"
_AlarmEnable_Object = MibTableColumn
alarmEnable = _AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 2),
    _AlarmEnable_Type()
)
alarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmEnable.setStatus("mandatory")


class _AnalogAlarmState_Type(Integer32):
    """Custom type analogAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aasNominal", 1),
          ("aasHIHI", 2),
          ("aasHI", 3),
          ("aasLO", 4),
          ("aasLOLO", 5))
    )


_AnalogAlarmState_Type.__name__ = "Integer32"
_AnalogAlarmState_Object = MibTableColumn
analogAlarmState = _AnalogAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 3),
    _AnalogAlarmState_Type()
)
analogAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogAlarmState.setStatus("mandatory")
_AnalogAlarmHIHI_Type = Integer32
_AnalogAlarmHIHI_Object = MibTableColumn
analogAlarmHIHI = _AnalogAlarmHIHI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 4),
    _AnalogAlarmHIHI_Type()
)
analogAlarmHIHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmHIHI.setStatus("mandatory")
_AnalogAlarmHI_Type = Integer32
_AnalogAlarmHI_Object = MibTableColumn
analogAlarmHI = _AnalogAlarmHI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 5),
    _AnalogAlarmHI_Type()
)
analogAlarmHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmHI.setStatus("mandatory")
_AnalogAlarmLO_Type = Integer32
_AnalogAlarmLO_Object = MibTableColumn
analogAlarmLO = _AnalogAlarmLO_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 6),
    _AnalogAlarmLO_Type()
)
analogAlarmLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmLO.setStatus("mandatory")
_AnalogAlarmLOLO_Type = Integer32
_AnalogAlarmLOLO_Object = MibTableColumn
analogAlarmLOLO = _AnalogAlarmLOLO_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 7),
    _AnalogAlarmLOLO_Type()
)
analogAlarmLOLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmLOLO.setStatus("mandatory")
_AnalogAlarmDeadband_Type = Integer32
_AnalogAlarmDeadband_Object = MibTableColumn
analogAlarmDeadband = _AnalogAlarmDeadband_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 1, 1, 8),
    _AnalogAlarmDeadband_Type()
)
analogAlarmDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogAlarmDeadband.setStatus("mandatory")
_DiscretePropertyTable_Object = MibTable
discretePropertyTable = _DiscretePropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2)
)
if mibBuilder.loadTexts:
    discretePropertyTable.setStatus("mandatory")
_DiscretePropertyEntry_Object = MibTableRow
discretePropertyEntry = _DiscretePropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1)
)
discretePropertyEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-PROPERTY-MIB", "discreteParameterOID"),
    (0, "NSCRTV-HFCEMS-PROPERTY-MIB", "discreteAlarmValue"),
)
if mibBuilder.loadTexts:
    discretePropertyEntry.setStatus("mandatory")
_DiscreteParameterOID_Type = ObjectIdentifier
_DiscreteParameterOID_Object = MibTableColumn
discreteParameterOID = _DiscreteParameterOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 1),
    _DiscreteParameterOID_Type()
)
discreteParameterOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discreteParameterOID.setStatus("mandatory")
_DiscreteAlarmValue_Type = Integer32
_DiscreteAlarmValue_Object = MibTableColumn
discreteAlarmValue = _DiscreteAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 2),
    _DiscreteAlarmValue_Type()
)
discreteAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discreteAlarmValue.setStatus("mandatory")


class _DiscreteAlarmEnable_Type(Integer32):
    """Custom type discreteAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableMajor", 2),
          ("enableMinor", 3))
    )


_DiscreteAlarmEnable_Type.__name__ = "Integer32"
_DiscreteAlarmEnable_Object = MibTableColumn
discreteAlarmEnable = _DiscreteAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 3),
    _DiscreteAlarmEnable_Type()
)
discreteAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    discreteAlarmEnable.setStatus("mandatory")


class _DiscreteAlarmState_Type(Integer32):
    """Custom type discreteAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dasNominal", 1),
          ("dasDiscreteMajor", 6),
          ("dasDiscreteMinor", 7))
    )


_DiscreteAlarmState_Type.__name__ = "Integer32"
_DiscreteAlarmState_Object = MibTableColumn
discreteAlarmState = _DiscreteAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 2, 1, 4),
    _DiscreteAlarmState_Type()
)
discreteAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discreteAlarmState.setStatus("mandatory")
_CurrentAlarmTable_Object = MibTable
currentAlarmTable = _CurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 3)
)
if mibBuilder.loadTexts:
    currentAlarmTable.setStatus("mandatory")
_CurrentAlarmEntry_Object = MibTableRow
currentAlarmEntry = _CurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1)
)
currentAlarmEntry.setIndexNames(
    (0, "NSCRTV-HFCEMS-PROPERTY-MIB", "currentAlarmOID"),
)
if mibBuilder.loadTexts:
    currentAlarmEntry.setStatus("mandatory")
_CurrentAlarmOID_Type = ObjectIdentifier
_CurrentAlarmOID_Object = MibTableColumn
currentAlarmOID = _CurrentAlarmOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1, 1),
    _CurrentAlarmOID_Type()
)
currentAlarmOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmOID.setStatus("mandatory")


class _CurrentAlarmState_Type(Integer32):
    """Custom type currentAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("caasHIHI", 2),
          ("caasHI", 3),
          ("caasLO", 4),
          ("caasLOLO", 5),
          ("caasDiscreteMajor", 6),
          ("caasDiscreteMinor", 7))
    )


_CurrentAlarmState_Type.__name__ = "Integer32"
_CurrentAlarmState_Object = MibTableColumn
currentAlarmState = _CurrentAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1, 2),
    _CurrentAlarmState_Type()
)
currentAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmState.setStatus("mandatory")
_CurrentAlarmValue_Type = Integer32
_CurrentAlarmValue_Object = MibTableColumn
currentAlarmValue = _CurrentAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 17409, 1, 1, 3, 1, 3),
    _CurrentAlarmValue_Type()
)
currentAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentAlarmValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-HFCEMS-PROPERTY-MIB",
    **{"analogPropertyTable": analogPropertyTable,
       "analogPropertyEntry": analogPropertyEntry,
       "analogParameterOID": analogParameterOID,
       "alarmEnable": alarmEnable,
       "analogAlarmState": analogAlarmState,
       "analogAlarmHIHI": analogAlarmHIHI,
       "analogAlarmHI": analogAlarmHI,
       "analogAlarmLO": analogAlarmLO,
       "analogAlarmLOLO": analogAlarmLOLO,
       "analogAlarmDeadband": analogAlarmDeadband,
       "discretePropertyTable": discretePropertyTable,
       "discretePropertyEntry": discretePropertyEntry,
       "discreteParameterOID": discreteParameterOID,
       "discreteAlarmValue": discreteAlarmValue,
       "discreteAlarmEnable": discreteAlarmEnable,
       "discreteAlarmState": discreteAlarmState,
       "currentAlarmTable": currentAlarmTable,
       "currentAlarmEntry": currentAlarmEntry,
       "currentAlarmOID": currentAlarmOID,
       "currentAlarmState": currentAlarmState,
       "currentAlarmValue": currentAlarmValue}
)
