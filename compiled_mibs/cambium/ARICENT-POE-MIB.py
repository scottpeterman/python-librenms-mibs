# SNMP MIB module (ARICENT-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cambium\cnmatrix\ARICENT-POE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:35 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fspoe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 103)
)
if mibBuilder.loadTexts:
    fspoe.setRevisions(
        ("2021-12-20 00:00",
         "2019-06-24 00:00",
         "2012-09-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPoeSystem_ObjectIdentity = ObjectIdentity
fsPoeSystem = _FsPoeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1)
)


class _FsPoeGlobalAdminStatus_Type(Integer32):
    """Custom type fsPoeGlobalAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsPoeGlobalAdminStatus_Type.__name__ = "Integer32"
_FsPoeGlobalAdminStatus_Object = MibScalar
fsPoeGlobalAdminStatus = _FsPoeGlobalAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 1),
    _FsPoeGlobalAdminStatus_Type()
)
fsPoeGlobalAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPoeGlobalAdminStatus.setStatus("current")
_FsPoeMacTable_Object = MibTable
fsPoeMacTable = _FsPoeMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 2)
)
if mibBuilder.loadTexts:
    fsPoeMacTable.setStatus("current")
_FsPoeMacEntry_Object = MibTableRow
fsPoeMacEntry = _FsPoeMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1)
)
fsPoeMacEntry.setIndexNames(
    (0, "ARICENT-POE-MIB", "fsPoePdMacAddress"),
)
if mibBuilder.loadTexts:
    fsPoeMacEntry.setStatus("current")
_FsPoePdMacAddress_Type = MacAddress
_FsPoePdMacAddress_Object = MibTableColumn
fsPoePdMacAddress = _FsPoePdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1, 1),
    _FsPoePdMacAddress_Type()
)
fsPoePdMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPoePdMacAddress.setStatus("current")
_FsPoePdMacPort_Type = InterfaceIndex
_FsPoePdMacPort_Object = MibTableColumn
fsPoePdMacPort = _FsPoePdMacPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1, 2),
    _FsPoePdMacPort_Type()
)
fsPoePdMacPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPoePdMacPort.setStatus("current")
_FsPoePdMacRowStatus_Type = RowStatus
_FsPoePdMacRowStatus_Object = MibTableColumn
fsPoePdMacRowStatus = _FsPoePdMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 2, 1, 3),
    _FsPoePdMacRowStatus_Type()
)
fsPoePdMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPoePdMacRowStatus.setStatus("current")
_FsPethPsePortTable_Object = MibTable
fsPethPsePortTable = _FsPethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 3)
)
if mibBuilder.loadTexts:
    fsPethPsePortTable.setStatus("current")
_FsPethPsePortEntry_Object = MibTableRow
fsPethPsePortEntry = _FsPethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 3, 1)
)
fsPethPsePortEntry.setIndexNames(
    (0, "ARICENT-POE-MIB", "fsPethPsePortGroupIndex"),
    (0, "ARICENT-POE-MIB", "fsPethPsePortIndex"),
)
if mibBuilder.loadTexts:
    fsPethPsePortEntry.setStatus("current")


class _FsPethPsePortGroupIndex_Type(Integer32):
    """Custom type fsPethPsePortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsPethPsePortGroupIndex_Type.__name__ = "Integer32"
_FsPethPsePortGroupIndex_Object = MibTableColumn
fsPethPsePortGroupIndex = _FsPethPsePortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 3, 1, 1),
    _FsPethPsePortGroupIndex_Type()
)
fsPethPsePortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPethPsePortGroupIndex.setStatus("current")


class _FsPethPsePortIndex_Type(Integer32):
    """Custom type fsPethPsePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsPethPsePortIndex_Type.__name__ = "Integer32"
_FsPethPsePortIndex_Object = MibTableColumn
fsPethPsePortIndex = _FsPethPsePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 3, 1, 2),
    _FsPethPsePortIndex_Type()
)
fsPethPsePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPethPsePortIndex.setStatus("current")


class _FsPethPsPortPowerMeasurementsAmperage_Type(Integer32):
    """Custom type fsPethPsPortPowerMeasurementsAmperage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsPethPsPortPowerMeasurementsAmperage_Type.__name__ = "Integer32"
_FsPethPsPortPowerMeasurementsAmperage_Object = MibTableColumn
fsPethPsPortPowerMeasurementsAmperage = _FsPethPsPortPowerMeasurementsAmperage_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 3, 1, 3),
    _FsPethPsPortPowerMeasurementsAmperage_Type()
)
fsPethPsPortPowerMeasurementsAmperage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPethPsPortPowerMeasurementsAmperage.setStatus("current")


class _FsPethPsPortPowerMeasurementsVoltage_Type(Integer32):
    """Custom type fsPethPsPortPowerMeasurementsVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsPethPsPortPowerMeasurementsVoltage_Type.__name__ = "Integer32"
_FsPethPsPortPowerMeasurementsVoltage_Object = MibTableColumn
fsPethPsPortPowerMeasurementsVoltage = _FsPethPsPortPowerMeasurementsVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 3, 1, 4),
    _FsPethPsPortPowerMeasurementsVoltage_Type()
)
fsPethPsPortPowerMeasurementsVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPethPsPortPowerMeasurementsVoltage.setStatus("current")


class _FsPethPsPortPowerMeasurementsWattage_Type(Integer32):
    """Custom type fsPethPsPortPowerMeasurementsWattage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsPethPsPortPowerMeasurementsWattage_Type.__name__ = "Integer32"
_FsPethPsPortPowerMeasurementsWattage_Object = MibTableColumn
fsPethPsPortPowerMeasurementsWattage = _FsPethPsPortPowerMeasurementsWattage_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 3, 1, 5),
    _FsPethPsPortPowerMeasurementsWattage_Type()
)
fsPethPsPortPowerMeasurementsWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPethPsPortPowerMeasurementsWattage.setStatus("current")


class _FsPethPsPortPowerPriorityStatic_Type(Integer32):
    """Custom type fsPethPsPortPowerPriorityStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_FsPethPsPortPowerPriorityStatic_Type.__name__ = "Integer32"
_FsPethPsPortPowerPriorityStatic_Object = MibTableColumn
fsPethPsPortPowerPriorityStatic = _FsPethPsPortPowerPriorityStatic_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 3, 1, 6),
    _FsPethPsPortPowerPriorityStatic_Type()
)
fsPethPsPortPowerPriorityStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPethPsPortPowerPriorityStatic.setStatus("current")


class _FsPethPsPortPowerMode_Type(Integer32):
    """Custom type fsPethPsPortPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("std802d3", 1),
          ("passive-24v", 2),
          ("passive-54v", 3),
          ("force-power", 4))
    )


_FsPethPsPortPowerMode_Type.__name__ = "Integer32"
_FsPethPsPortPowerMode_Object = MibTableColumn
fsPethPsPortPowerMode = _FsPethPsPortPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 3, 1, 7),
    _FsPethPsPortPowerMode_Type()
)
fsPethPsPortPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPethPsPortPowerMode.setStatus("current")


class _FsPethPsPortPowerModeDynamic_Type(Integer32):
    """Custom type fsPethPsPortPowerModeDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonDynamic", 0),
          ("dynamic", 1))
    )


_FsPethPsPortPowerModeDynamic_Type.__name__ = "Integer32"
_FsPethPsPortPowerModeDynamic_Object = MibTableColumn
fsPethPsPortPowerModeDynamic = _FsPethPsPortPowerModeDynamic_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 3, 1, 8),
    _FsPethPsPortPowerModeDynamic_Type()
)
fsPethPsPortPowerModeDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPethPsPortPowerModeDynamic.setStatus("current")


class _FsPowerModeAutoDetect_Type(Bits):
    """Custom type fsPowerModeAutoDetect based on Bits"""
    namedValues = NamedValues(
        *(("cnMedusaOn", 0),
          ("cnMedusaOff", 1),
          ("cnWaveOn", 2),
          ("cnWaveOff", 3))
    )

_FsPowerModeAutoDetect_Type.__name__ = "Bits"
_FsPowerModeAutoDetect_Object = MibScalar
fsPowerModeAutoDetect = _FsPowerModeAutoDetect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 4),
    _FsPowerModeAutoDetect_Type()
)
fsPowerModeAutoDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPowerModeAutoDetect.setStatus("current")


class _FsPowerModePassiveSafe_Type(Integer32):
    """Custom type fsPowerModePassiveSafe based on Integer32"""
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


_FsPowerModePassiveSafe_Type.__name__ = "Integer32"
_FsPowerModePassiveSafe_Object = MibScalar
fsPowerModePassiveSafe = _FsPowerModePassiveSafe_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 5),
    _FsPowerModePassiveSafe_Type()
)
fsPowerModePassiveSafe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPowerModePassiveSafe.setStatus("current")


class _FsPowerModeHighTemperature_Type(Integer32):
    """Custom type fsPowerModeHighTemperature based on Integer32"""
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


_FsPowerModeHighTemperature_Type.__name__ = "Integer32"
_FsPowerModeHighTemperature_Object = MibScalar
fsPowerModeHighTemperature = _FsPowerModeHighTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 6),
    _FsPowerModeHighTemperature_Type()
)
fsPowerModeHighTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPowerModeHighTemperature.setStatus("current")


class _FsPowerFirmwareVersion_Type(DisplayString):
    """Custom type fsPowerFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FsPowerFirmwareVersion_Type.__name__ = "DisplayString"
_FsPowerFirmwareVersion_Object = MibScalar
fsPowerFirmwareVersion = _FsPowerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 7),
    _FsPowerFirmwareVersion_Type()
)
fsPowerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPowerFirmwareVersion.setStatus("current")


class _FsPowerModeDCinVoltageRange_Type(Integer32):
    """Custom type fsPowerModeDCinVoltageRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("range9-29V", 1),
          ("range30-60V", 2))
    )


_FsPowerModeDCinVoltageRange_Type.__name__ = "Integer32"
_FsPowerModeDCinVoltageRange_Object = MibScalar
fsPowerModeDCinVoltageRange = _FsPowerModeDCinVoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 2076, 103, 1, 8),
    _FsPowerModeDCinVoltageRange_Type()
)
fsPowerModeDCinVoltageRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPowerModeDCinVoltageRange.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-POE-MIB",
    **{"fspoe": fspoe,
       "fsPoeSystem": fsPoeSystem,
       "fsPoeGlobalAdminStatus": fsPoeGlobalAdminStatus,
       "fsPoeMacTable": fsPoeMacTable,
       "fsPoeMacEntry": fsPoeMacEntry,
       "fsPoePdMacAddress": fsPoePdMacAddress,
       "fsPoePdMacPort": fsPoePdMacPort,
       "fsPoePdMacRowStatus": fsPoePdMacRowStatus,
       "fsPethPsePortTable": fsPethPsePortTable,
       "fsPethPsePortEntry": fsPethPsePortEntry,
       "fsPethPsePortGroupIndex": fsPethPsePortGroupIndex,
       "fsPethPsePortIndex": fsPethPsePortIndex,
       "fsPethPsPortPowerMeasurementsAmperage": fsPethPsPortPowerMeasurementsAmperage,
       "fsPethPsPortPowerMeasurementsVoltage": fsPethPsPortPowerMeasurementsVoltage,
       "fsPethPsPortPowerMeasurementsWattage": fsPethPsPortPowerMeasurementsWattage,
       "fsPethPsPortPowerPriorityStatic": fsPethPsPortPowerPriorityStatic,
       "fsPethPsPortPowerMode": fsPethPsPortPowerMode,
       "fsPethPsPortPowerModeDynamic": fsPethPsPortPowerModeDynamic,
       "fsPowerModeAutoDetect": fsPowerModeAutoDetect,
       "fsPowerModePassiveSafe": fsPowerModePassiveSafe,
       "fsPowerModeHighTemperature": fsPowerModeHighTemperature,
       "fsPowerFirmwareVersion": fsPowerFirmwareVersion,
       "fsPowerModeDCinVoltageRange": fsPowerModeDCinVoltageRange}
)
