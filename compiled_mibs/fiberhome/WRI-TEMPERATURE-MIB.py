# SNMP MIB module (WRI-TEMPERATURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fiberhome\WRI-TEMPERATURE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:15 2025
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

(wri,
 wriProducts) = mibBuilder.importSymbols(
    "WRI-SMI",
    "wri",
    "wriProducts")


# MODULE-IDENTITY

msppTemperature = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6)
)
if mibBuilder.loadTexts:
    msppTemperature.setRevisions(
        ("2010-01-11 00:00",
         "2009-01-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayString(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Mspp_ObjectIdentity = ObjectIdentity
mspp = _Mspp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012)
)
_MsppChassis_ObjectIdentity = ObjectIdentity
msppChassis = _MsppChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1)
)
_TemperatureGeneral_ObjectIdentity = ObjectIdentity
temperatureGeneral = _TemperatureGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 1)
)


class _TemperatureTrapEnable_Type(Integer32):
    """Custom type temperatureTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TemperatureTrapEnable_Type.__name__ = "Integer32"
_TemperatureTrapEnable_Object = MibScalar
temperatureTrapEnable = _TemperatureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 1, 1),
    _TemperatureTrapEnable_Type()
)
temperatureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureTrapEnable.setStatus("current")


class _TemperatureMonitorEnable_Type(Integer32):
    """Custom type temperatureMonitorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TemperatureMonitorEnable_Type.__name__ = "Integer32"
_TemperatureMonitorEnable_Object = MibScalar
temperatureMonitorEnable = _TemperatureMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 1, 2),
    _TemperatureMonitorEnable_Type()
)
temperatureMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureMonitorEnable.setStatus("current")
_TemperatureNumber_Type = Integer32
_TemperatureNumber_Object = MibScalar
temperatureNumber = _TemperatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 1, 3),
    _TemperatureNumber_Type()
)
temperatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureNumber.setStatus("current")
_TemperatureTable_Object = MibTable
temperatureTable = _TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2)
)
if mibBuilder.loadTexts:
    temperatureTable.setStatus("current")
_TemperatureEntry_Object = MibTableRow
temperatureEntry = _TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1)
)
temperatureEntry.setIndexNames(
    (0, "WRI-TEMPERATURE-MIB", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    temperatureEntry.setStatus("current")
_TemperatureIndex_Type = Unsigned32
_TemperatureIndex_Object = MibTableColumn
temperatureIndex = _TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1, 1),
    _TemperatureIndex_Type()
)
temperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureIndex.setStatus("current")


class _TemperatureDescr_Type(DisplayString):
    """Custom type temperatureDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TemperatureDescr_Type.__name__ = "DisplayString"
_TemperatureDescr_Object = MibTableColumn
temperatureDescr = _TemperatureDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1, 2),
    _TemperatureDescr_Type()
)
temperatureDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureDescr.setStatus("current")
_TemperatureLThreshold_Type = Integer32
_TemperatureLThreshold_Object = MibTableColumn
temperatureLThreshold = _TemperatureLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1, 3),
    _TemperatureLThreshold_Type()
)
temperatureLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureLThreshold.setStatus("current")
_TemperatureHThreshold_Type = Integer32
_TemperatureHThreshold_Object = MibTableColumn
temperatureHThreshold = _TemperatureHThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1, 4),
    _TemperatureHThreshold_Type()
)
temperatureHThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureHThreshold.setStatus("current")
_TemperatureValue_Type = Integer32
_TemperatureValue_Object = MibTableColumn
temperatureValue = _TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1, 5),
    _TemperatureValue_Type()
)
temperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureValue.setStatus("current")


class _TemperatureState_Type(Integer32):
    """Custom type temperatureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("lowtrap", 1),
          ("hightrap", 2))
    )


_TemperatureState_Type.__name__ = "Integer32"
_TemperatureState_Object = MibTableColumn
temperatureState = _TemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1, 6),
    _TemperatureState_Type()
)
temperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureState.setStatus("current")


class _TemperatureTrapEna_Type(Integer32):
    """Custom type temperatureTrapEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TemperatureTrapEna_Type.__name__ = "Integer32"
_TemperatureTrapEna_Object = MibTableColumn
temperatureTrapEna = _TemperatureTrapEna_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1, 7),
    _TemperatureTrapEna_Type()
)
temperatureTrapEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureTrapEna.setStatus("current")
_TemperatureAllSetting_Type = OctetString
_TemperatureAllSetting_Object = MibTableColumn
temperatureAllSetting = _TemperatureAllSetting_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1, 8),
    _TemperatureAllSetting_Type()
)
temperatureAllSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureAllSetting.setStatus("current")
_TemperatureIndexDescr_Type = OctetString
_TemperatureIndexDescr_Object = MibTableColumn
temperatureIndexDescr = _TemperatureIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1, 9),
    _TemperatureIndexDescr_Type()
)
temperatureIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureIndexDescr.setStatus("current")
_TemperatureRebootHThreshold_Type = Integer32
_TemperatureRebootHThreshold_Object = MibTableColumn
temperatureRebootHThreshold = _TemperatureRebootHThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 2, 1, 10),
    _TemperatureRebootHThreshold_Type()
)
temperatureRebootHThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureRebootHThreshold.setStatus("current")
_TemperatureTrap_ObjectIdentity = ObjectIdentity
temperatureTrap = _TemperatureTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 3)
)

# Managed Objects groups


# Notification objects

temperatureOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 3, 1)
)
temperatureOk.setObjects(
      *(("WRI-TEMPERATURE-MIB", "temperatureDescr"),
        ("WRI-TEMPERATURE-MIB", "temperatureValue"))
)
if mibBuilder.loadTexts:
    temperatureOk.setStatus(
        "current"
    )

temperatureFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3807, 1, 8012, 1, 6, 3, 2)
)
temperatureFault.setObjects(
      *(("WRI-TEMPERATURE-MIB", "temperatureDescr"),
        ("WRI-TEMPERATURE-MIB", "temperatureValue"),
        ("WRI-TEMPERATURE-MIB", "temperatureLThreshold"),
        ("WRI-TEMPERATURE-MIB", "temperatureHThreshold"))
)
if mibBuilder.loadTexts:
    temperatureFault.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WRI-TEMPERATURE-MIB",
    **{"DisplayString": DisplayString,
       "mspp": mspp,
       "msppChassis": msppChassis,
       "msppTemperature": msppTemperature,
       "temperatureGeneral": temperatureGeneral,
       "temperatureTrapEnable": temperatureTrapEnable,
       "temperatureMonitorEnable": temperatureMonitorEnable,
       "temperatureNumber": temperatureNumber,
       "temperatureTable": temperatureTable,
       "temperatureEntry": temperatureEntry,
       "temperatureIndex": temperatureIndex,
       "temperatureDescr": temperatureDescr,
       "temperatureLThreshold": temperatureLThreshold,
       "temperatureHThreshold": temperatureHThreshold,
       "temperatureValue": temperatureValue,
       "temperatureState": temperatureState,
       "temperatureTrapEna": temperatureTrapEna,
       "temperatureAllSetting": temperatureAllSetting,
       "temperatureIndexDescr": temperatureIndexDescr,
       "temperatureRebootHThreshold": temperatureRebootHThreshold,
       "temperatureTrap": temperatureTrap,
       "temperatureOk": temperatureOk,
       "temperatureFault": temperatureFault}
)
