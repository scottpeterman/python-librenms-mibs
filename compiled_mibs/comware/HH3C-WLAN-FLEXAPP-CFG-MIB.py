# SNMP MIB module (HH3C-WLAN-FLEXAPP-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-WLAN-FLEXAPP-CFG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:28 2025
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

(hh3cDot11,) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "hh3cDot11")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cWlanFlexAppCFG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19)
)
if mibBuilder.loadTexts:
    hh3cWlanFlexAppCFG.setRevisions(
        ("2015-05-26 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cWlanModuleConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWlanModuleConfigGroup = _Hh3cWlanModuleConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1)
)
_Hh3cWlanModuleConfigTable_Object = MibTable
hh3cWlanModuleConfigTable = _Hh3cWlanModuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cWlanModuleConfigTable.setStatus("current")
_Hh3cWlanModuleConfigEntry_Object = MibTableRow
hh3cWlanModuleConfigEntry = _Hh3cWlanModuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1, 1)
)
hh3cWlanModuleConfigEntry.setIndexNames(
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanAPSerialID"),
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanModuleID"),
)
if mibBuilder.loadTexts:
    hh3cWlanModuleConfigEntry.setStatus("current")


class _Hh3cWlanAPSerialID_Type(OctetString):
    """Custom type hh3cWlanAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cWlanAPSerialID_Type.__name__ = "OctetString"
_Hh3cWlanAPSerialID_Object = MibTableColumn
hh3cWlanAPSerialID = _Hh3cWlanAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1, 1, 1),
    _Hh3cWlanAPSerialID_Type()
)
hh3cWlanAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanAPSerialID.setStatus("current")


class _Hh3cWlanModuleID_Type(Integer32):
    """Custom type hh3cWlanModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cWlanModuleID_Type.__name__ = "Integer32"
_Hh3cWlanModuleID_Object = MibTableColumn
hh3cWlanModuleID = _Hh3cWlanModuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1, 1, 2),
    _Hh3cWlanModuleID_Type()
)
hh3cWlanModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanModuleID.setStatus("current")


class _Hh3cWlanModuleType_Type(Integer32):
    """Custom type hh3cWlanModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ble", 1),
          ("iot", 2))
    )


_Hh3cWlanModuleType_Type.__name__ = "Integer32"
_Hh3cWlanModuleType_Object = MibTableColumn
hh3cWlanModuleType = _Hh3cWlanModuleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1, 1, 3),
    _Hh3cWlanModuleType_Type()
)
hh3cWlanModuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanModuleType.setStatus("current")
_Hh3cWlanModuleStatus_Type = TruthValue
_Hh3cWlanModuleStatus_Object = MibTableColumn
hh3cWlanModuleStatus = _Hh3cWlanModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1, 1, 4),
    _Hh3cWlanModuleStatus_Type()
)
hh3cWlanModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanModuleStatus.setStatus("current")


class _Hh3cWlanModuleReset_Type(Integer32):
    """Custom type hh3cWlanModuleReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reboot", 1))
    )


_Hh3cWlanModuleReset_Type.__name__ = "Integer32"
_Hh3cWlanModuleReset_Object = MibTableColumn
hh3cWlanModuleReset = _Hh3cWlanModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1, 1, 5),
    _Hh3cWlanModuleReset_Type()
)
hh3cWlanModuleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanModuleReset.setStatus("current")


class _Hh3cWlanModuleRstFac_Type(Integer32):
    """Custom type hh3cWlanModuleRstFac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("restore", 1))
    )


_Hh3cWlanModuleRstFac_Type.__name__ = "Integer32"
_Hh3cWlanModuleRstFac_Object = MibTableColumn
hh3cWlanModuleRstFac = _Hh3cWlanModuleRstFac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1, 1, 6),
    _Hh3cWlanModuleRstFac_Type()
)
hh3cWlanModuleRstFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanModuleRstFac.setStatus("current")
_Hh3cWlanModuleUpWareStatus_Type = TruthValue
_Hh3cWlanModuleUpWareStatus_Object = MibTableColumn
hh3cWlanModuleUpWareStatus = _Hh3cWlanModuleUpWareStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1, 1, 7),
    _Hh3cWlanModuleUpWareStatus_Type()
)
hh3cWlanModuleUpWareStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanModuleUpWareStatus.setStatus("current")


class _Hh3cWlanModuleTxPower_Type(Integer32):
    """Custom type hh3cWlanModuleTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cWlanModuleTxPower_Type.__name__ = "Integer32"
_Hh3cWlanModuleTxPower_Object = MibTableColumn
hh3cWlanModuleTxPower = _Hh3cWlanModuleTxPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1, 1, 8),
    _Hh3cWlanModuleTxPower_Type()
)
hh3cWlanModuleTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanModuleTxPower.setStatus("current")
_Hh3cWlanModuleManualUpdate_Type = OctetString
_Hh3cWlanModuleManualUpdate_Object = MibTableColumn
hh3cWlanModuleManualUpdate = _Hh3cWlanModuleManualUpdate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 1, 1, 9),
    _Hh3cWlanModuleManualUpdate_Type()
)
hh3cWlanModuleManualUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanModuleManualUpdate.setStatus("current")
_Hh3cWlanModuleInfoTable_Object = MibTable
hh3cWlanModuleInfoTable = _Hh3cWlanModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cWlanModuleInfoTable.setStatus("current")
_Hh3cWlanModuleInfoEntry_Object = MibTableRow
hh3cWlanModuleInfoEntry = _Hh3cWlanModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 2, 1)
)
hh3cWlanModuleInfoEntry.setIndexNames(
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cDot11IOTAPSerialID"),
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cDot11IOTModuleID"),
)
if mibBuilder.loadTexts:
    hh3cWlanModuleInfoEntry.setStatus("current")


class _Hh3cDot11IOTAPSerialID_Type(OctetString):
    """Custom type hh3cDot11IOTAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11IOTAPSerialID_Type.__name__ = "OctetString"
_Hh3cDot11IOTAPSerialID_Object = MibTableColumn
hh3cDot11IOTAPSerialID = _Hh3cDot11IOTAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 2, 1, 1),
    _Hh3cDot11IOTAPSerialID_Type()
)
hh3cDot11IOTAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11IOTAPSerialID.setStatus("current")


class _Hh3cDot11IOTModuleID_Type(Integer32):
    """Custom type hh3cDot11IOTModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11IOTModuleID_Type.__name__ = "Integer32"
_Hh3cDot11IOTModuleID_Object = MibTableColumn
hh3cDot11IOTModuleID = _Hh3cDot11IOTModuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 2, 1, 2),
    _Hh3cDot11IOTModuleID_Type()
)
hh3cDot11IOTModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11IOTModuleID.setStatus("current")


class _Hh3cDot11IOTModuleType_Type(Integer32):
    """Custom type hh3cDot11IOTModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("h3c", 1),
          ("iot", 2))
    )


_Hh3cDot11IOTModuleType_Type.__name__ = "Integer32"
_Hh3cDot11IOTModuleType_Object = MibTableColumn
hh3cDot11IOTModuleType = _Hh3cDot11IOTModuleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 2, 1, 3),
    _Hh3cDot11IOTModuleType_Type()
)
hh3cDot11IOTModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11IOTModuleType.setStatus("current")
_Hh3cDot11IOTModuleModel_Type = OctetString
_Hh3cDot11IOTModuleModel_Object = MibTableColumn
hh3cDot11IOTModuleModel = _Hh3cDot11IOTModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 2, 1, 4),
    _Hh3cDot11IOTModuleModel_Type()
)
hh3cDot11IOTModuleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11IOTModuleModel.setStatus("current")
_Hh3cDot11IOTModuleHwVersion_Type = OctetString
_Hh3cDot11IOTModuleHwVersion_Object = MibTableColumn
hh3cDot11IOTModuleHwVersion = _Hh3cDot11IOTModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 2, 1, 5),
    _Hh3cDot11IOTModuleHwVersion_Type()
)
hh3cDot11IOTModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11IOTModuleHwVersion.setStatus("current")
_Hh3cDot11IOTModuleSwVersion_Type = OctetString
_Hh3cDot11IOTModuleSwVersion_Object = MibTableColumn
hh3cDot11IOTModuleSwVersion = _Hh3cDot11IOTModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 2, 1, 6),
    _Hh3cDot11IOTModuleSwVersion_Type()
)
hh3cDot11IOTModuleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11IOTModuleSwVersion.setStatus("current")
_Hh3cDot11IOTModuleSerialId_Type = OctetString
_Hh3cDot11IOTModuleSerialId_Object = MibTableColumn
hh3cDot11IOTModuleSerialId = _Hh3cDot11IOTModuleSerialId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 1, 2, 1, 7),
    _Hh3cDot11IOTModuleSerialId_Type()
)
hh3cDot11IOTModuleSerialId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11IOTModuleSerialId.setStatus("current")
_Hh3cWlanIOTConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWlanIOTConfigGroup = _Hh3cWlanIOTConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 2)
)
_Hh3cWlanIOTConfigTable_Object = MibTable
hh3cWlanIOTConfigTable = _Hh3cWlanIOTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cWlanIOTConfigTable.setStatus("current")
_Hh3cWlanIOTConfigEntry_Object = MibTableRow
hh3cWlanIOTConfigEntry = _Hh3cWlanIOTConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 2, 1, 1)
)
hh3cWlanIOTConfigEntry.setIndexNames(
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanIOTAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cWlanIOTConfigEntry.setStatus("current")


class _Hh3cWlanIOTAPSerialID_Type(OctetString):
    """Custom type hh3cWlanIOTAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cWlanIOTAPSerialID_Type.__name__ = "OctetString"
_Hh3cWlanIOTAPSerialID_Object = MibTableColumn
hh3cWlanIOTAPSerialID = _Hh3cWlanIOTAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 2, 1, 1, 1),
    _Hh3cWlanIOTAPSerialID_Type()
)
hh3cWlanIOTAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanIOTAPSerialID.setStatus("current")
_Hh3cWlanIOTEngineAdd_Type = IpAddress
_Hh3cWlanIOTEngineAdd_Object = MibTableColumn
hh3cWlanIOTEngineAdd = _Hh3cWlanIOTEngineAdd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 2, 1, 1, 2),
    _Hh3cWlanIOTEngineAdd_Type()
)
hh3cWlanIOTEngineAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanIOTEngineAdd.setStatus("current")


class _Hh3cWlanIOTEnginePort_Type(Integer32):
    """Custom type hh3cWlanIOTEnginePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWlanIOTEnginePort_Type.__name__ = "Integer32"
_Hh3cWlanIOTEnginePort_Object = MibTableColumn
hh3cWlanIOTEnginePort = _Hh3cWlanIOTEnginePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 2, 1, 1, 3),
    _Hh3cWlanIOTEnginePort_Type()
)
hh3cWlanIOTEnginePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanIOTEnginePort.setStatus("current")
_Hh3cWlanModuleNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cWlanModuleNotifyGroup = _Hh3cWlanModuleNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3)
)
_Hh3cWlanModuleTraps_ObjectIdentity = ObjectIdentity
hh3cWlanModuleTraps = _Hh3cWlanModuleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 0)
)
_Hh3cWlanModuleTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cWlanModuleTrapVarObjects = _Hh3cWlanModuleTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 1)
)
_Hh3cWlanTrapAPMacAddress_Type = MacAddress
_Hh3cWlanTrapAPMacAddress_Object = MibScalar
hh3cWlanTrapAPMacAddress = _Hh3cWlanTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 1, 1),
    _Hh3cWlanTrapAPMacAddress_Type()
)
hh3cWlanTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWlanTrapAPMacAddress.setStatus("current")
_Hh3cWlanTrapModuleID_Type = Integer32
_Hh3cWlanTrapModuleID_Object = MibScalar
hh3cWlanTrapModuleID = _Hh3cWlanTrapModuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 1, 2),
    _Hh3cWlanTrapModuleID_Type()
)
hh3cWlanTrapModuleID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWlanTrapModuleID.setStatus("current")


class _Hh3cWlanTrapModuleCfgType_Type(Integer32):
    """Custom type hh3cWlanTrapModuleCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("h3c", 1),
          ("iot", 2))
    )


_Hh3cWlanTrapModuleCfgType_Type.__name__ = "Integer32"
_Hh3cWlanTrapModuleCfgType_Object = MibScalar
hh3cWlanTrapModuleCfgType = _Hh3cWlanTrapModuleCfgType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 1, 3),
    _Hh3cWlanTrapModuleCfgType_Type()
)
hh3cWlanTrapModuleCfgType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWlanTrapModuleCfgType.setStatus("current")


class _Hh3cWlanTrapModulePhyType_Type(Integer32):
    """Custom type hh3cWlanTrapModulePhyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("h3c", 1),
          ("iot", 2))
    )


_Hh3cWlanTrapModulePhyType_Type.__name__ = "Integer32"
_Hh3cWlanTrapModulePhyType_Object = MibScalar
hh3cWlanTrapModulePhyType = _Hh3cWlanTrapModulePhyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 1, 4),
    _Hh3cWlanTrapModulePhyType_Type()
)
hh3cWlanTrapModulePhyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWlanTrapModulePhyType.setStatus("current")
_Hh3cWlanTrapModuleModel_Type = OctetString
_Hh3cWlanTrapModuleModel_Object = MibScalar
hh3cWlanTrapModuleModel = _Hh3cWlanTrapModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 1, 5),
    _Hh3cWlanTrapModuleModel_Type()
)
hh3cWlanTrapModuleModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWlanTrapModuleModel.setStatus("current")
_Hh3cWlanTrapModuleHwVersion_Type = OctetString
_Hh3cWlanTrapModuleHwVersion_Object = MibScalar
hh3cWlanTrapModuleHwVersion = _Hh3cWlanTrapModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 1, 6),
    _Hh3cWlanTrapModuleHwVersion_Type()
)
hh3cWlanTrapModuleHwVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWlanTrapModuleHwVersion.setStatus("current")
_Hh3cWlanTrapModuleSwVersion_Type = OctetString
_Hh3cWlanTrapModuleSwVersion_Object = MibScalar
hh3cWlanTrapModuleSwVersion = _Hh3cWlanTrapModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 1, 7),
    _Hh3cWlanTrapModuleSwVersion_Type()
)
hh3cWlanTrapModuleSwVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWlanTrapModuleSwVersion.setStatus("current")
_Hh3cWlanTrapModuleSequenceId_Type = OctetString
_Hh3cWlanTrapModuleSequenceId_Object = MibScalar
hh3cWlanTrapModuleSequenceId = _Hh3cWlanTrapModuleSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 1, 8),
    _Hh3cWlanTrapModuleSequenceId_Type()
)
hh3cWlanTrapModuleSequenceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cWlanTrapModuleSequenceId.setStatus("current")
_Hh3cWlanBLEConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWlanBLEConfigGroup = _Hh3cWlanBLEConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4)
)
_Hh3cWlanBLEConfigTable_Object = MibTable
hh3cWlanBLEConfigTable = _Hh3cWlanBLEConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cWlanBLEConfigTable.setStatus("current")
_Hh3cWlanBLEConfigEntry_Object = MibTableRow
hh3cWlanBLEConfigEntry = _Hh3cWlanBLEConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1)
)
hh3cWlanBLEConfigEntry.setIndexNames(
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanBLEAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cWlanBLEConfigEntry.setStatus("current")


class _Hh3cWlanBLEAPSerialID_Type(OctetString):
    """Custom type hh3cWlanBLEAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cWlanBLEAPSerialID_Type.__name__ = "OctetString"
_Hh3cWlanBLEAPSerialID_Object = MibTableColumn
hh3cWlanBLEAPSerialID = _Hh3cWlanBLEAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 1),
    _Hh3cWlanBLEAPSerialID_Type()
)
hh3cWlanBLEAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanBLEAPSerialID.setStatus("current")
_Hh3cWlanBLEStatus_Type = TruthValue
_Hh3cWlanBLEStatus_Object = MibTableColumn
hh3cWlanBLEStatus = _Hh3cWlanBLEStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 2),
    _Hh3cWlanBLEStatus_Type()
)
hh3cWlanBLEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEStatus.setStatus("current")
_Hh3cWlanBLEEngineAdd_Type = IpAddress
_Hh3cWlanBLEEngineAdd_Object = MibTableColumn
hh3cWlanBLEEngineAdd = _Hh3cWlanBLEEngineAdd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 3),
    _Hh3cWlanBLEEngineAdd_Type()
)
hh3cWlanBLEEngineAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEEngineAdd.setStatus("current")


class _Hh3cWlanBLEEnginePort_Type(Integer32):
    """Custom type hh3cWlanBLEEnginePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWlanBLEEnginePort_Type.__name__ = "Integer32"
_Hh3cWlanBLEEnginePort_Object = MibTableColumn
hh3cWlanBLEEnginePort = _Hh3cWlanBLEEnginePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 4),
    _Hh3cWlanBLEEnginePort_Type()
)
hh3cWlanBLEEnginePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEEnginePort.setStatus("current")


class _Hh3cWlanBLEVendorPort_Type(Integer32):
    """Custom type hh3cWlanBLEVendorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cWlanBLEVendorPort_Type.__name__ = "Integer32"
_Hh3cWlanBLEVendorPort_Object = MibTableColumn
hh3cWlanBLEVendorPort = _Hh3cWlanBLEVendorPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 5),
    _Hh3cWlanBLEVendorPort_Type()
)
hh3cWlanBLEVendorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEVendorPort.setStatus("current")
_Hh3cWlanBLERssiStatus_Type = TruthValue
_Hh3cWlanBLERssiStatus_Object = MibTableColumn
hh3cWlanBLERssiStatus = _Hh3cWlanBLERssiStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 6),
    _Hh3cWlanBLERssiStatus_Type()
)
hh3cWlanBLERssiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLERssiStatus.setStatus("current")


class _Hh3cWlanBLERssiThreshold_Type(Integer32):
    """Custom type hh3cWlanBLERssiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Hh3cWlanBLERssiThreshold_Type.__name__ = "Integer32"
_Hh3cWlanBLERssiThreshold_Object = MibTableColumn
hh3cWlanBLERssiThreshold = _Hh3cWlanBLERssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 7),
    _Hh3cWlanBLERssiThreshold_Type()
)
hh3cWlanBLERssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLERssiThreshold.setStatus("current")


class _Hh3cWlanBLEConnectPassword_Type(OctetString):
    """Custom type hh3cWlanBLEConnectPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_Hh3cWlanBLEConnectPassword_Type.__name__ = "OctetString"
_Hh3cWlanBLEConnectPassword_Object = MibTableColumn
hh3cWlanBLEConnectPassword = _Hh3cWlanBLEConnectPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 8),
    _Hh3cWlanBLEConnectPassword_Type()
)
hh3cWlanBLEConnectPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEConnectPassword.setStatus("current")


class _Hh3cWlanBLECommandPassword_Type(OctetString):
    """Custom type hh3cWlanBLECommandPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(12, 12),
    )


_Hh3cWlanBLECommandPassword_Type.__name__ = "OctetString"
_Hh3cWlanBLECommandPassword_Object = MibTableColumn
hh3cWlanBLECommandPassword = _Hh3cWlanBLECommandPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 9),
    _Hh3cWlanBLECommandPassword_Type()
)
hh3cWlanBLECommandPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLECommandPassword.setStatus("current")
_Hh3cWlanBLEReportStatus_Type = TruthValue
_Hh3cWlanBLEReportStatus_Object = MibTableColumn
hh3cWlanBLEReportStatus = _Hh3cWlanBLEReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 10),
    _Hh3cWlanBLEReportStatus_Type()
)
hh3cWlanBLEReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEReportStatus.setStatus("current")


class _Hh3cWlanBLEReportInterval_Type(Integer32):
    """Custom type hh3cWlanBLEReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_Hh3cWlanBLEReportInterval_Type.__name__ = "Integer32"
_Hh3cWlanBLEReportInterval_Object = MibTableColumn
hh3cWlanBLEReportInterval = _Hh3cWlanBLEReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 11),
    _Hh3cWlanBLEReportInterval_Type()
)
hh3cWlanBLEReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWlanBLEReportInterval.setUnits("Second")


class _Hh3cWlanBLEAgingTime_Type(Integer32):
    """Custom type hh3cWlanBLEAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_Hh3cWlanBLEAgingTime_Type.__name__ = "Integer32"
_Hh3cWlanBLEAgingTime_Object = MibTableColumn
hh3cWlanBLEAgingTime = _Hh3cWlanBLEAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 12),
    _Hh3cWlanBLEAgingTime_Type()
)
hh3cWlanBLEAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWlanBLEAgingTime.setUnits("Second")
_Hh3cWlanBLERealTimeReportStatus_Type = TruthValue
_Hh3cWlanBLERealTimeReportStatus_Object = MibTableColumn
hh3cWlanBLERealTimeReportStatus = _Hh3cWlanBLERealTimeReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 13),
    _Hh3cWlanBLERealTimeReportStatus_Type()
)
hh3cWlanBLERealTimeReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLERealTimeReportStatus.setStatus("current")


class _Hh3cWlanBLERealTimePrefix_Type(OctetString):
    """Custom type hh3cWlanBLERealTimePrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 18),
    )


_Hh3cWlanBLERealTimePrefix_Type.__name__ = "OctetString"
_Hh3cWlanBLERealTimePrefix_Object = MibTableColumn
hh3cWlanBLERealTimePrefix = _Hh3cWlanBLERealTimePrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 1, 1, 14),
    _Hh3cWlanBLERealTimePrefix_Type()
)
hh3cWlanBLERealTimePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLERealTimePrefix.setStatus("current")
_Hh3cWlanBLEModuleConfigTable_Object = MibTable
hh3cWlanBLEModuleConfigTable = _Hh3cWlanBLEModuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cWlanBLEModuleConfigTable.setStatus("current")
_Hh3cWlanBLEModuleConfigEntry_Object = MibTableRow
hh3cWlanBLEModuleConfigEntry = _Hh3cWlanBLEModuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 2, 1)
)
hh3cWlanBLEModuleConfigEntry.setIndexNames(
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanBLEModuleAPSerialID"),
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanBLEModuleID"),
)
if mibBuilder.loadTexts:
    hh3cWlanBLEModuleConfigEntry.setStatus("current")


class _Hh3cWlanBLEModuleAPSerialID_Type(OctetString):
    """Custom type hh3cWlanBLEModuleAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cWlanBLEModuleAPSerialID_Type.__name__ = "OctetString"
_Hh3cWlanBLEModuleAPSerialID_Object = MibTableColumn
hh3cWlanBLEModuleAPSerialID = _Hh3cWlanBLEModuleAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 2, 1, 1),
    _Hh3cWlanBLEModuleAPSerialID_Type()
)
hh3cWlanBLEModuleAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanBLEModuleAPSerialID.setStatus("current")


class _Hh3cWlanBLEModuleID_Type(Integer32):
    """Custom type hh3cWlanBLEModuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cWlanBLEModuleID_Type.__name__ = "Integer32"
_Hh3cWlanBLEModuleID_Object = MibTableColumn
hh3cWlanBLEModuleID = _Hh3cWlanBLEModuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 2, 1, 2),
    _Hh3cWlanBLEModuleID_Type()
)
hh3cWlanBLEModuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanBLEModuleID.setStatus("current")
_Hh3cWlanBLEAdvReportStatus_Type = TruthValue
_Hh3cWlanBLEAdvReportStatus_Object = MibTableColumn
hh3cWlanBLEAdvReportStatus = _Hh3cWlanBLEAdvReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 2, 1, 3),
    _Hh3cWlanBLEAdvReportStatus_Type()
)
hh3cWlanBLEAdvReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEAdvReportStatus.setStatus("current")


class _Hh3cWlanBLEAdvReportInterval_Type(Integer32):
    """Custom type hh3cWlanBLEAdvReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1000),
    )


_Hh3cWlanBLEAdvReportInterval_Type.__name__ = "Integer32"
_Hh3cWlanBLEAdvReportInterval_Object = MibTableColumn
hh3cWlanBLEAdvReportInterval = _Hh3cWlanBLEAdvReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 2, 1, 4),
    _Hh3cWlanBLEAdvReportInterval_Type()
)
hh3cWlanBLEAdvReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEAdvReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWlanBLEAdvReportInterval.setUnits("Second")


class _Hh3cWlanBLEAdvUUID_Type(OctetString):
    """Custom type hh3cWlanBLEAdvUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_Hh3cWlanBLEAdvUUID_Type.__name__ = "OctetString"
_Hh3cWlanBLEAdvUUID_Object = MibTableColumn
hh3cWlanBLEAdvUUID = _Hh3cWlanBLEAdvUUID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 2, 1, 5),
    _Hh3cWlanBLEAdvUUID_Type()
)
hh3cWlanBLEAdvUUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEAdvUUID.setStatus("current")


class _Hh3cWlanBLEAdvMajorID_Type(Integer32):
    """Custom type hh3cWlanBLEAdvMajorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWlanBLEAdvMajorID_Type.__name__ = "Integer32"
_Hh3cWlanBLEAdvMajorID_Object = MibTableColumn
hh3cWlanBLEAdvMajorID = _Hh3cWlanBLEAdvMajorID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 2, 1, 6),
    _Hh3cWlanBLEAdvMajorID_Type()
)
hh3cWlanBLEAdvMajorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEAdvMajorID.setStatus("current")


class _Hh3cWlanBLEAdvMinorID_Type(Integer32):
    """Custom type hh3cWlanBLEAdvMinorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWlanBLEAdvMinorID_Type.__name__ = "Integer32"
_Hh3cWlanBLEAdvMinorID_Object = MibTableColumn
hh3cWlanBLEAdvMinorID = _Hh3cWlanBLEAdvMinorID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 4, 2, 1, 7),
    _Hh3cWlanBLEAdvMinorID_Type()
)
hh3cWlanBLEAdvMinorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanBLEAdvMinorID.setStatus("current")
_Hh3cWlanAEConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWlanAEConfigGroup = _Hh3cWlanAEConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5)
)
_Hh3cWlanAEConfigTable_Object = MibTable
hh3cWlanAEConfigTable = _Hh3cWlanAEConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cWlanAEConfigTable.setStatus("current")
_Hh3cWlanAEConfigEntry_Object = MibTableRow
hh3cWlanAEConfigEntry = _Hh3cWlanAEConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1)
)
hh3cWlanAEConfigEntry.setIndexNames(
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanAEAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cWlanAEConfigEntry.setStatus("current")


class _Hh3cWlanAEAPSerialID_Type(OctetString):
    """Custom type hh3cWlanAEAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cWlanAEAPSerialID_Type.__name__ = "OctetString"
_Hh3cWlanAEAPSerialID_Object = MibTableColumn
hh3cWlanAEAPSerialID = _Hh3cWlanAEAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1, 1),
    _Hh3cWlanAEAPSerialID_Type()
)
hh3cWlanAEAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanAEAPSerialID.setStatus("current")
_Hh3cWlanAEStatus_Type = TruthValue
_Hh3cWlanAEStatus_Object = MibTableColumn
hh3cWlanAEStatus = _Hh3cWlanAEStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1, 2),
    _Hh3cWlanAEStatus_Type()
)
hh3cWlanAEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAEStatus.setStatus("current")
_Hh3cWlanAEEngineAddr_Type = IpAddress
_Hh3cWlanAEEngineAddr_Object = MibTableColumn
hh3cWlanAEEngineAddr = _Hh3cWlanAEEngineAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1, 3),
    _Hh3cWlanAEEngineAddr_Type()
)
hh3cWlanAEEngineAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAEEngineAddr.setStatus("current")


class _Hh3cWlanAEEnginePort_Type(Integer32):
    """Custom type hh3cWlanAEEnginePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWlanAEEnginePort_Type.__name__ = "Integer32"
_Hh3cWlanAEEnginePort_Object = MibTableColumn
hh3cWlanAEEnginePort = _Hh3cWlanAEEnginePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1, 4),
    _Hh3cWlanAEEnginePort_Type()
)
hh3cWlanAEEnginePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAEEnginePort.setStatus("current")


class _Hh3cWlanAEVendorPort_Type(Integer32):
    """Custom type hh3cWlanAEVendorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cWlanAEVendorPort_Type.__name__ = "Integer32"
_Hh3cWlanAEVendorPort_Object = MibTableColumn
hh3cWlanAEVendorPort = _Hh3cWlanAEVendorPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1, 5),
    _Hh3cWlanAEVendorPort_Type()
)
hh3cWlanAEVendorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAEVendorPort.setStatus("current")


class _Hh3cWlanAETimeStamp_Type(Integer32):
    """Custom type hh3cWlanAETimeStamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("relative", 2))
    )


_Hh3cWlanAETimeStamp_Type.__name__ = "Integer32"
_Hh3cWlanAETimeStamp_Object = MibTableColumn
hh3cWlanAETimeStamp = _Hh3cWlanAETimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1, 6),
    _Hh3cWlanAETimeStamp_Type()
)
hh3cWlanAETimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAETimeStamp.setStatus("current")


class _Hh3cWlanAEVersion_Type(Integer32):
    """Custom type hh3cWlanAEVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 2),
          ("v3", 3))
    )


_Hh3cWlanAEVersion_Type.__name__ = "Integer32"
_Hh3cWlanAEVersion_Object = MibTableColumn
hh3cWlanAEVersion = _Hh3cWlanAEVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1, 7),
    _Hh3cWlanAEVersion_Type()
)
hh3cWlanAEVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAEVersion.setStatus("current")
_Hh3cWlanAETagMultiAddr_Type = MacAddress
_Hh3cWlanAETagMultiAddr_Object = MibTableColumn
hh3cWlanAETagMultiAddr = _Hh3cWlanAETagMultiAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1, 8),
    _Hh3cWlanAETagMultiAddr_Type()
)
hh3cWlanAETagMultiAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAETagMultiAddr.setStatus("current")


class _Hh3cWlanAEEngineDetection_Type(Integer32):
    """Custom type hh3cWlanAEEngineDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_Hh3cWlanAEEngineDetection_Type.__name__ = "Integer32"
_Hh3cWlanAEEngineDetection_Object = MibTableColumn
hh3cWlanAEEngineDetection = _Hh3cWlanAEEngineDetection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1, 9),
    _Hh3cWlanAEEngineDetection_Type()
)
hh3cWlanAEEngineDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAEEngineDetection.setStatus("current")


class _Hh3cWlanAEReportMode_Type(Integer32):
    """Custom type hh3cWlanAEReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("central", 2))
    )


_Hh3cWlanAEReportMode_Type.__name__ = "Integer32"
_Hh3cWlanAEReportMode_Object = MibTableColumn
hh3cWlanAEReportMode = _Hh3cWlanAEReportMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 1, 1, 10),
    _Hh3cWlanAEReportMode_Type()
)
hh3cWlanAEReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAEReportMode.setStatus("current")
_Hh3cWlanAERadioConfigTable_Object = MibTable
hh3cWlanAERadioConfigTable = _Hh3cWlanAERadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 2)
)
if mibBuilder.loadTexts:
    hh3cWlanAERadioConfigTable.setStatus("current")
_Hh3cWlanAERadioConfigEntry_Object = MibTableRow
hh3cWlanAERadioConfigEntry = _Hh3cWlanAERadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 2, 1)
)
hh3cWlanAERadioConfigEntry.setIndexNames(
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanAERadioAPSerialID"),
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanAEAPRadioID"),
)
if mibBuilder.loadTexts:
    hh3cWlanAERadioConfigEntry.setStatus("current")


class _Hh3cWlanAERadioAPSerialID_Type(OctetString):
    """Custom type hh3cWlanAERadioAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cWlanAERadioAPSerialID_Type.__name__ = "OctetString"
_Hh3cWlanAERadioAPSerialID_Object = MibTableColumn
hh3cWlanAERadioAPSerialID = _Hh3cWlanAERadioAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 2, 1, 1),
    _Hh3cWlanAERadioAPSerialID_Type()
)
hh3cWlanAERadioAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanAERadioAPSerialID.setStatus("current")


class _Hh3cWlanAEAPRadioID_Type(Integer32):
    """Custom type hh3cWlanAEAPRadioID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cWlanAEAPRadioID_Type.__name__ = "Integer32"
_Hh3cWlanAEAPRadioID_Object = MibTableColumn
hh3cWlanAEAPRadioID = _Hh3cWlanAEAPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 2, 1, 2),
    _Hh3cWlanAEAPRadioID_Type()
)
hh3cWlanAEAPRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanAEAPRadioID.setStatus("current")
_Hh3cWlanAERadioStatus_Type = TruthValue
_Hh3cWlanAERadioStatus_Object = MibTableColumn
hh3cWlanAERadioStatus = _Hh3cWlanAERadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 2, 1, 3),
    _Hh3cWlanAERadioStatus_Type()
)
hh3cWlanAERadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAERadioStatus.setStatus("current")
_Hh3cWlanAEMUStatus_Type = TruthValue
_Hh3cWlanAEMUStatus_Object = MibTableColumn
hh3cWlanAEMUStatus = _Hh3cWlanAEMUStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 2, 1, 4),
    _Hh3cWlanAEMUStatus_Type()
)
hh3cWlanAEMUStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAEMUStatus.setStatus("current")
_Hh3cWlanAETagStatus_Type = TruthValue
_Hh3cWlanAETagStatus_Object = MibTableColumn
hh3cWlanAETagStatus = _Hh3cWlanAETagStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 5, 2, 1, 5),
    _Hh3cWlanAETagStatus_Type()
)
hh3cWlanAETagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanAETagStatus.setStatus("current")
_Hh3cWlanCommonConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWlanCommonConfigGroup = _Hh3cWlanCommonConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6)
)
_Hh3cWlanCommonConfigTable_Object = MibTable
hh3cWlanCommonConfigTable = _Hh3cWlanCommonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cWlanCommonConfigTable.setStatus("current")
_Hh3cWlanCommonConfigEntry_Object = MibTableRow
hh3cWlanCommonConfigEntry = _Hh3cWlanCommonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1)
)
hh3cWlanCommonConfigEntry.setIndexNames(
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanCommonAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cWlanCommonConfigEntry.setStatus("current")


class _Hh3cWlanCommonAPSerialID_Type(OctetString):
    """Custom type hh3cWlanCommonAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cWlanCommonAPSerialID_Type.__name__ = "OctetString"
_Hh3cWlanCommonAPSerialID_Object = MibTableColumn
hh3cWlanCommonAPSerialID = _Hh3cWlanCommonAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 1),
    _Hh3cWlanCommonAPSerialID_Type()
)
hh3cWlanCommonAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanCommonAPSerialID.setStatus("current")
_Hh3cWlanDilutionStatus_Type = TruthValue
_Hh3cWlanDilutionStatus_Object = MibTableColumn
hh3cWlanDilutionStatus = _Hh3cWlanDilutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 2),
    _Hh3cWlanDilutionStatus_Type()
)
hh3cWlanDilutionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanDilutionStatus.setStatus("current")


class _Hh3cWlanDilutionFactor_Type(Integer32):
    """Custom type hh3cWlanDilutionFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Hh3cWlanDilutionFactor_Type.__name__ = "Integer32"
_Hh3cWlanDilutionFactor_Object = MibTableColumn
hh3cWlanDilutionFactor = _Hh3cWlanDilutionFactor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 3),
    _Hh3cWlanDilutionFactor_Type()
)
hh3cWlanDilutionFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanDilutionFactor.setStatus("current")


class _Hh3cWlanDilutionTimeout_Type(Integer32):
    """Custom type hh3cWlanDilutionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Hh3cWlanDilutionTimeout_Type.__name__ = "Integer32"
_Hh3cWlanDilutionTimeout_Object = MibTableColumn
hh3cWlanDilutionTimeout = _Hh3cWlanDilutionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 4),
    _Hh3cWlanDilutionTimeout_Type()
)
hh3cWlanDilutionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanDilutionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWlanDilutionTimeout.setUnits("Second")
_Hh3cWlanIgnoreBeacon_Type = TruthValue
_Hh3cWlanIgnoreBeacon_Object = MibTableColumn
hh3cWlanIgnoreBeacon = _Hh3cWlanIgnoreBeacon_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 5),
    _Hh3cWlanIgnoreBeacon_Type()
)
hh3cWlanIgnoreBeacon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanIgnoreBeacon.setStatus("current")
_Hh3cWlanRateLimitStatus_Type = TruthValue
_Hh3cWlanRateLimitStatus_Object = MibTableColumn
hh3cWlanRateLimitStatus = _Hh3cWlanRateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 6),
    _Hh3cWlanRateLimitStatus_Type()
)
hh3cWlanRateLimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanRateLimitStatus.setStatus("current")


class _Hh3cWlanRateLimitCir_Type(Integer32):
    """Custom type hh3cWlanRateLimitCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 1300000),
    )


_Hh3cWlanRateLimitCir_Type.__name__ = "Integer32"
_Hh3cWlanRateLimitCir_Object = MibTableColumn
hh3cWlanRateLimitCir = _Hh3cWlanRateLimitCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 7),
    _Hh3cWlanRateLimitCir_Type()
)
hh3cWlanRateLimitCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanRateLimitCir.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWlanRateLimitCir.setUnits("Kbps")


class _Hh3cWlanRateLimitCbs_Type(Integer32):
    """Custom type hh3cWlanRateLimitCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(500, 130000000),
    )


_Hh3cWlanRateLimitCbs_Type.__name__ = "Integer32"
_Hh3cWlanRateLimitCbs_Object = MibTableColumn
hh3cWlanRateLimitCbs = _Hh3cWlanRateLimitCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 8),
    _Hh3cWlanRateLimitCbs_Type()
)
hh3cWlanRateLimitCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanRateLimitCbs.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWlanRateLimitCbs.setUnits("Bytes")
_Hh3cWlanClientRateLimitStatus_Type = TruthValue
_Hh3cWlanClientRateLimitStatus_Object = MibTableColumn
hh3cWlanClientRateLimitStatus = _Hh3cWlanClientRateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 9),
    _Hh3cWlanClientRateLimitStatus_Type()
)
hh3cWlanClientRateLimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanClientRateLimitStatus.setStatus("current")


class _Hh3cWlanClientRateLimitCir_Type(Integer32):
    """Custom type hh3cWlanClientRateLimitCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1300000),
    )


_Hh3cWlanClientRateLimitCir_Type.__name__ = "Integer32"
_Hh3cWlanClientRateLimitCir_Object = MibTableColumn
hh3cWlanClientRateLimitCir = _Hh3cWlanClientRateLimitCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 10),
    _Hh3cWlanClientRateLimitCir_Type()
)
hh3cWlanClientRateLimitCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanClientRateLimitCir.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWlanClientRateLimitCir.setUnits("Kbps")


class _Hh3cWlanClientRateLimitCbs_Type(Integer32):
    """Custom type hh3cWlanClientRateLimitCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(80, 130000000),
    )


_Hh3cWlanClientRateLimitCbs_Type.__name__ = "Integer32"
_Hh3cWlanClientRateLimitCbs_Object = MibTableColumn
hh3cWlanClientRateLimitCbs = _Hh3cWlanClientRateLimitCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 11),
    _Hh3cWlanClientRateLimitCbs_Type()
)
hh3cWlanClientRateLimitCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanClientRateLimitCbs.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWlanClientRateLimitCbs.setUnits("Bytes")
_Hh3cWlanRssiStatus_Type = TruthValue
_Hh3cWlanRssiStatus_Object = MibTableColumn
hh3cWlanRssiStatus = _Hh3cWlanRssiStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 12),
    _Hh3cWlanRssiStatus_Type()
)
hh3cWlanRssiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanRssiStatus.setStatus("current")


class _Hh3cWlanRssiThreshold_Type(Integer32):
    """Custom type hh3cWlanRssiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_Hh3cWlanRssiThreshold_Type.__name__ = "Integer32"
_Hh3cWlanRssiThreshold_Object = MibTableColumn
hh3cWlanRssiThreshold = _Hh3cWlanRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 13),
    _Hh3cWlanRssiThreshold_Type()
)
hh3cWlanRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanRssiThreshold.setStatus("current")
_Hh3cWlanIgnoreApFrame_Type = TruthValue
_Hh3cWlanIgnoreApFrame_Object = MibTableColumn
hh3cWlanIgnoreApFrame = _Hh3cWlanIgnoreApFrame_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 6, 1, 1, 14),
    _Hh3cWlanIgnoreApFrame_Type()
)
hh3cWlanIgnoreApFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanIgnoreApFrame.setStatus("current")
_Hh3cWlanCUPIDConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWlanCUPIDConfigGroup = _Hh3cWlanCUPIDConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7)
)
_Hh3cWlanCUPIDConfigTable_Object = MibTable
hh3cWlanCUPIDConfigTable = _Hh3cWlanCUPIDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1)
)
if mibBuilder.loadTexts:
    hh3cWlanCUPIDConfigTable.setStatus("current")
_Hh3cWlanCUPIDConfigEntry_Object = MibTableRow
hh3cWlanCUPIDConfigEntry = _Hh3cWlanCUPIDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1)
)
hh3cWlanCUPIDConfigEntry.setIndexNames(
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanCupidAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cWlanCUPIDConfigEntry.setStatus("current")


class _Hh3cWlanCupidAPSerialID_Type(OctetString):
    """Custom type hh3cWlanCupidAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cWlanCupidAPSerialID_Type.__name__ = "OctetString"
_Hh3cWlanCupidAPSerialID_Object = MibTableColumn
hh3cWlanCupidAPSerialID = _Hh3cWlanCupidAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 1),
    _Hh3cWlanCupidAPSerialID_Type()
)
hh3cWlanCupidAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanCupidAPSerialID.setStatus("current")
_Hh3cWlanCupidStatus_Type = TruthValue
_Hh3cWlanCupidStatus_Object = MibTableColumn
hh3cWlanCupidStatus = _Hh3cWlanCupidStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 2),
    _Hh3cWlanCupidStatus_Type()
)
hh3cWlanCupidStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanCupidStatus.setStatus("current")
_Hh3cWlanCupidEngineAddr_Type = IpAddress
_Hh3cWlanCupidEngineAddr_Object = MibTableColumn
hh3cWlanCupidEngineAddr = _Hh3cWlanCupidEngineAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 3),
    _Hh3cWlanCupidEngineAddr_Type()
)
hh3cWlanCupidEngineAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanCupidEngineAddr.setStatus("current")


class _Hh3cWlanCupidEnginePort_Type(Integer32):
    """Custom type hh3cWlanCupidEnginePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWlanCupidEnginePort_Type.__name__ = "Integer32"
_Hh3cWlanCupidEnginePort_Object = MibTableColumn
hh3cWlanCupidEnginePort = _Hh3cWlanCupidEnginePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 4),
    _Hh3cWlanCupidEnginePort_Type()
)
hh3cWlanCupidEnginePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanCupidEnginePort.setStatus("current")


class _Hh3cWlanCupidVendorPort_Type(Integer32):
    """Custom type hh3cWlanCupidVendorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cWlanCupidVendorPort_Type.__name__ = "Integer32"
_Hh3cWlanCupidVendorPort_Object = MibTableColumn
hh3cWlanCupidVendorPort = _Hh3cWlanCupidVendorPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 5),
    _Hh3cWlanCupidVendorPort_Type()
)
hh3cWlanCupidVendorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanCupidVendorPort.setStatus("current")
_Hh3cWlanCupidReportStatus_Type = TruthValue
_Hh3cWlanCupidReportStatus_Object = MibTableColumn
hh3cWlanCupidReportStatus = _Hh3cWlanCupidReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 6),
    _Hh3cWlanCupidReportStatus_Type()
)
hh3cWlanCupidReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanCupidReportStatus.setStatus("current")


class _Hh3cWlanCupidReportInterval_Type(Integer32):
    """Custom type hh3cWlanCupidReportInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Hh3cWlanCupidReportInterval_Type.__name__ = "Integer32"
_Hh3cWlanCupidReportInterval_Object = MibTableColumn
hh3cWlanCupidReportInterval = _Hh3cWlanCupidReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 7),
    _Hh3cWlanCupidReportInterval_Type()
)
hh3cWlanCupidReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanCupidReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cWlanCupidReportInterval.setUnits("Second")
_Hh3cWlanCupidUnassSta_Type = TruthValue
_Hh3cWlanCupidUnassSta_Object = MibTableColumn
hh3cWlanCupidUnassSta = _Hh3cWlanCupidUnassSta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 8),
    _Hh3cWlanCupidUnassSta_Type()
)
hh3cWlanCupidUnassSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanCupidUnassSta.setStatus("current")
_Hh3cWlanCupidUnassMeasureSta_Type = TruthValue
_Hh3cWlanCupidUnassMeasureSta_Object = MibTableColumn
hh3cWlanCupidUnassMeasureSta = _Hh3cWlanCupidUnassMeasureSta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 9),
    _Hh3cWlanCupidUnassMeasureSta_Type()
)
hh3cWlanCupidUnassMeasureSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanCupidUnassMeasureSta.setStatus("current")


class _Hh3cWlanCupidReportMode_Type(Integer32):
    """Custom type hh3cWlanCupidReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("central", 2))
    )


_Hh3cWlanCupidReportMode_Type.__name__ = "Integer32"
_Hh3cWlanCupidReportMode_Object = MibTableColumn
hh3cWlanCupidReportMode = _Hh3cWlanCupidReportMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 10),
    _Hh3cWlanCupidReportMode_Type()
)
hh3cWlanCupidReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanCupidReportMode.setStatus("current")


class _Hh3cWlanCUPIDReportFormat_Type(Integer32):
    """Custom type hh3cWlanCUPIDReportFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("general", 1),
          ("lightweight", 2))
    )


_Hh3cWlanCUPIDReportFormat_Type.__name__ = "Integer32"
_Hh3cWlanCUPIDReportFormat_Object = MibTableColumn
hh3cWlanCUPIDReportFormat = _Hh3cWlanCUPIDReportFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 7, 1, 1, 11),
    _Hh3cWlanCUPIDReportFormat_Type()
)
hh3cWlanCUPIDReportFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanCUPIDReportFormat.setStatus("current")
_Hh3cWlanFPConfigGroup_ObjectIdentity = ObjectIdentity
hh3cWlanFPConfigGroup = _Hh3cWlanFPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8)
)
_Hh3cWlanFPConfigTable_Object = MibTable
hh3cWlanFPConfigTable = _Hh3cWlanFPConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cWlanFPConfigTable.setStatus("current")
_Hh3cWlanFPConfigEntry_Object = MibTableRow
hh3cWlanFPConfigEntry = _Hh3cWlanFPConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1)
)
hh3cWlanFPConfigEntry.setIndexNames(
    (0, "HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanFPAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cWlanFPConfigEntry.setStatus("current")


class _Hh3cWlanFPAPSerialID_Type(OctetString):
    """Custom type hh3cWlanFPAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cWlanFPAPSerialID_Type.__name__ = "OctetString"
_Hh3cWlanFPAPSerialID_Object = MibTableColumn
hh3cWlanFPAPSerialID = _Hh3cWlanFPAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1, 1),
    _Hh3cWlanFPAPSerialID_Type()
)
hh3cWlanFPAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cWlanFPAPSerialID.setStatus("current")
_Hh3cWlanFPStatus_Type = TruthValue
_Hh3cWlanFPStatus_Object = MibTableColumn
hh3cWlanFPStatus = _Hh3cWlanFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1, 2),
    _Hh3cWlanFPStatus_Type()
)
hh3cWlanFPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanFPStatus.setStatus("current")
_Hh3cWlanFPEngineAddr_Type = IpAddress
_Hh3cWlanFPEngineAddr_Object = MibTableColumn
hh3cWlanFPEngineAddr = _Hh3cWlanFPEngineAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1, 3),
    _Hh3cWlanFPEngineAddr_Type()
)
hh3cWlanFPEngineAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanFPEngineAddr.setStatus("current")


class _Hh3cWlanFPEnginePort_Type(Integer32):
    """Custom type hh3cWlanFPEnginePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWlanFPEnginePort_Type.__name__ = "Integer32"
_Hh3cWlanFPEnginePort_Object = MibTableColumn
hh3cWlanFPEnginePort = _Hh3cWlanFPEnginePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1, 4),
    _Hh3cWlanFPEnginePort_Type()
)
hh3cWlanFPEnginePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanFPEnginePort.setStatus("current")


class _Hh3cWlanFPVendorPort_Type(Integer32):
    """Custom type hh3cWlanFPVendorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cWlanFPVendorPort_Type.__name__ = "Integer32"
_Hh3cWlanFPVendorPort_Object = MibTableColumn
hh3cWlanFPVendorPort = _Hh3cWlanFPVendorPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1, 5),
    _Hh3cWlanFPVendorPort_Type()
)
hh3cWlanFPVendorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanFPVendorPort.setStatus("current")
_Hh3cWlanFPRawFrameReport_Type = TruthValue
_Hh3cWlanFPRawFrameReport_Object = MibTableColumn
hh3cWlanFPRawFrameReport = _Hh3cWlanFPRawFrameReport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1, 6),
    _Hh3cWlanFPRawFrameReport_Type()
)
hh3cWlanFPRawFrameReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanFPRawFrameReport.setStatus("current")
_Hh3cWlanFPMUReport_Type = TruthValue
_Hh3cWlanFPMUReport_Object = MibTableColumn
hh3cWlanFPMUReport = _Hh3cWlanFPMUReport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1, 7),
    _Hh3cWlanFPMUReport_Type()
)
hh3cWlanFPMUReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanFPMUReport.setStatus("current")


class _Hh3cWlanFPReportMode_Type(Integer32):
    """Custom type hh3cWlanFPReportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("central", 2))
    )


_Hh3cWlanFPReportMode_Type.__name__ = "Integer32"
_Hh3cWlanFPReportMode_Object = MibTableColumn
hh3cWlanFPReportMode = _Hh3cWlanFPReportMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1, 8),
    _Hh3cWlanFPReportMode_Type()
)
hh3cWlanFPReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanFPReportMode.setStatus("current")


class _Hh3cWlanFPReportFormat_Type(Integer32):
    """Custom type hh3cWlanFPReportFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("general", 1),
          ("lightweight", 2),
          ("cupidhybrid", 3))
    )


_Hh3cWlanFPReportFormat_Type.__name__ = "Integer32"
_Hh3cWlanFPReportFormat_Object = MibTableColumn
hh3cWlanFPReportFormat = _Hh3cWlanFPReportFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1, 9),
    _Hh3cWlanFPReportFormat_Type()
)
hh3cWlanFPReportFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanFPReportFormat.setStatus("current")
_Hh3cWlanFPTagMultiAddr_Type = MacAddress
_Hh3cWlanFPTagMultiAddr_Object = MibTableColumn
hh3cWlanFPTagMultiAddr = _Hh3cWlanFPTagMultiAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 8, 1, 1, 10),
    _Hh3cWlanFPTagMultiAddr_Type()
)
hh3cWlanFPTagMultiAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWlanFPTagMultiAddr.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cWlanModuleInsertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 0, 1)
)
hh3cWlanModuleInsertTrap.setObjects(
      *(("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapAPMacAddress"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleID"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModulePhyType"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleModel"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleHwVersion"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleSwVersion"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleSequenceId"))
)
if mibBuilder.loadTexts:
    hh3cWlanModuleInsertTrap.setStatus(
        "current"
    )

hh3cWlanModuleRomveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 0, 2)
)
hh3cWlanModuleRomveTrap.setObjects(
      *(("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapAPMacAddress"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleID"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModulePhyType"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleModel"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleHwVersion"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleSwVersion"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleSequenceId"))
)
if mibBuilder.loadTexts:
    hh3cWlanModuleRomveTrap.setStatus(
        "current"
    )

hh3cWlanModuleMissMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 19, 3, 0, 3)
)
hh3cWlanModuleMissMatch.setObjects(
      *(("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapAPMacAddress"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleID"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleCfgType"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModulePhyType"),
        ("HH3C-WLAN-FLEXAPP-CFG-MIB", "hh3cWlanTrapModuleModel"))
)
if mibBuilder.loadTexts:
    hh3cWlanModuleMissMatch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-WLAN-FLEXAPP-CFG-MIB",
    **{"hh3cWlanFlexAppCFG": hh3cWlanFlexAppCFG,
       "hh3cWlanModuleConfigGroup": hh3cWlanModuleConfigGroup,
       "hh3cWlanModuleConfigTable": hh3cWlanModuleConfigTable,
       "hh3cWlanModuleConfigEntry": hh3cWlanModuleConfigEntry,
       "hh3cWlanAPSerialID": hh3cWlanAPSerialID,
       "hh3cWlanModuleID": hh3cWlanModuleID,
       "hh3cWlanModuleType": hh3cWlanModuleType,
       "hh3cWlanModuleStatus": hh3cWlanModuleStatus,
       "hh3cWlanModuleReset": hh3cWlanModuleReset,
       "hh3cWlanModuleRstFac": hh3cWlanModuleRstFac,
       "hh3cWlanModuleUpWareStatus": hh3cWlanModuleUpWareStatus,
       "hh3cWlanModuleTxPower": hh3cWlanModuleTxPower,
       "hh3cWlanModuleManualUpdate": hh3cWlanModuleManualUpdate,
       "hh3cWlanModuleInfoTable": hh3cWlanModuleInfoTable,
       "hh3cWlanModuleInfoEntry": hh3cWlanModuleInfoEntry,
       "hh3cDot11IOTAPSerialID": hh3cDot11IOTAPSerialID,
       "hh3cDot11IOTModuleID": hh3cDot11IOTModuleID,
       "hh3cDot11IOTModuleType": hh3cDot11IOTModuleType,
       "hh3cDot11IOTModuleModel": hh3cDot11IOTModuleModel,
       "hh3cDot11IOTModuleHwVersion": hh3cDot11IOTModuleHwVersion,
       "hh3cDot11IOTModuleSwVersion": hh3cDot11IOTModuleSwVersion,
       "hh3cDot11IOTModuleSerialId": hh3cDot11IOTModuleSerialId,
       "hh3cWlanIOTConfigGroup": hh3cWlanIOTConfigGroup,
       "hh3cWlanIOTConfigTable": hh3cWlanIOTConfigTable,
       "hh3cWlanIOTConfigEntry": hh3cWlanIOTConfigEntry,
       "hh3cWlanIOTAPSerialID": hh3cWlanIOTAPSerialID,
       "hh3cWlanIOTEngineAdd": hh3cWlanIOTEngineAdd,
       "hh3cWlanIOTEnginePort": hh3cWlanIOTEnginePort,
       "hh3cWlanModuleNotifyGroup": hh3cWlanModuleNotifyGroup,
       "hh3cWlanModuleTraps": hh3cWlanModuleTraps,
       "hh3cWlanModuleInsertTrap": hh3cWlanModuleInsertTrap,
       "hh3cWlanModuleRomveTrap": hh3cWlanModuleRomveTrap,
       "hh3cWlanModuleMissMatch": hh3cWlanModuleMissMatch,
       "hh3cWlanModuleTrapVarObjects": hh3cWlanModuleTrapVarObjects,
       "hh3cWlanTrapAPMacAddress": hh3cWlanTrapAPMacAddress,
       "hh3cWlanTrapModuleID": hh3cWlanTrapModuleID,
       "hh3cWlanTrapModuleCfgType": hh3cWlanTrapModuleCfgType,
       "hh3cWlanTrapModulePhyType": hh3cWlanTrapModulePhyType,
       "hh3cWlanTrapModuleModel": hh3cWlanTrapModuleModel,
       "hh3cWlanTrapModuleHwVersion": hh3cWlanTrapModuleHwVersion,
       "hh3cWlanTrapModuleSwVersion": hh3cWlanTrapModuleSwVersion,
       "hh3cWlanTrapModuleSequenceId": hh3cWlanTrapModuleSequenceId,
       "hh3cWlanBLEConfigGroup": hh3cWlanBLEConfigGroup,
       "hh3cWlanBLEConfigTable": hh3cWlanBLEConfigTable,
       "hh3cWlanBLEConfigEntry": hh3cWlanBLEConfigEntry,
       "hh3cWlanBLEAPSerialID": hh3cWlanBLEAPSerialID,
       "hh3cWlanBLEStatus": hh3cWlanBLEStatus,
       "hh3cWlanBLEEngineAdd": hh3cWlanBLEEngineAdd,
       "hh3cWlanBLEEnginePort": hh3cWlanBLEEnginePort,
       "hh3cWlanBLEVendorPort": hh3cWlanBLEVendorPort,
       "hh3cWlanBLERssiStatus": hh3cWlanBLERssiStatus,
       "hh3cWlanBLERssiThreshold": hh3cWlanBLERssiThreshold,
       "hh3cWlanBLEConnectPassword": hh3cWlanBLEConnectPassword,
       "hh3cWlanBLECommandPassword": hh3cWlanBLECommandPassword,
       "hh3cWlanBLEReportStatus": hh3cWlanBLEReportStatus,
       "hh3cWlanBLEReportInterval": hh3cWlanBLEReportInterval,
       "hh3cWlanBLEAgingTime": hh3cWlanBLEAgingTime,
       "hh3cWlanBLERealTimeReportStatus": hh3cWlanBLERealTimeReportStatus,
       "hh3cWlanBLERealTimePrefix": hh3cWlanBLERealTimePrefix,
       "hh3cWlanBLEModuleConfigTable": hh3cWlanBLEModuleConfigTable,
       "hh3cWlanBLEModuleConfigEntry": hh3cWlanBLEModuleConfigEntry,
       "hh3cWlanBLEModuleAPSerialID": hh3cWlanBLEModuleAPSerialID,
       "hh3cWlanBLEModuleID": hh3cWlanBLEModuleID,
       "hh3cWlanBLEAdvReportStatus": hh3cWlanBLEAdvReportStatus,
       "hh3cWlanBLEAdvReportInterval": hh3cWlanBLEAdvReportInterval,
       "hh3cWlanBLEAdvUUID": hh3cWlanBLEAdvUUID,
       "hh3cWlanBLEAdvMajorID": hh3cWlanBLEAdvMajorID,
       "hh3cWlanBLEAdvMinorID": hh3cWlanBLEAdvMinorID,
       "hh3cWlanAEConfigGroup": hh3cWlanAEConfigGroup,
       "hh3cWlanAEConfigTable": hh3cWlanAEConfigTable,
       "hh3cWlanAEConfigEntry": hh3cWlanAEConfigEntry,
       "hh3cWlanAEAPSerialID": hh3cWlanAEAPSerialID,
       "hh3cWlanAEStatus": hh3cWlanAEStatus,
       "hh3cWlanAEEngineAddr": hh3cWlanAEEngineAddr,
       "hh3cWlanAEEnginePort": hh3cWlanAEEnginePort,
       "hh3cWlanAEVendorPort": hh3cWlanAEVendorPort,
       "hh3cWlanAETimeStamp": hh3cWlanAETimeStamp,
       "hh3cWlanAEVersion": hh3cWlanAEVersion,
       "hh3cWlanAETagMultiAddr": hh3cWlanAETagMultiAddr,
       "hh3cWlanAEEngineDetection": hh3cWlanAEEngineDetection,
       "hh3cWlanAEReportMode": hh3cWlanAEReportMode,
       "hh3cWlanAERadioConfigTable": hh3cWlanAERadioConfigTable,
       "hh3cWlanAERadioConfigEntry": hh3cWlanAERadioConfigEntry,
       "hh3cWlanAERadioAPSerialID": hh3cWlanAERadioAPSerialID,
       "hh3cWlanAEAPRadioID": hh3cWlanAEAPRadioID,
       "hh3cWlanAERadioStatus": hh3cWlanAERadioStatus,
       "hh3cWlanAEMUStatus": hh3cWlanAEMUStatus,
       "hh3cWlanAETagStatus": hh3cWlanAETagStatus,
       "hh3cWlanCommonConfigGroup": hh3cWlanCommonConfigGroup,
       "hh3cWlanCommonConfigTable": hh3cWlanCommonConfigTable,
       "hh3cWlanCommonConfigEntry": hh3cWlanCommonConfigEntry,
       "hh3cWlanCommonAPSerialID": hh3cWlanCommonAPSerialID,
       "hh3cWlanDilutionStatus": hh3cWlanDilutionStatus,
       "hh3cWlanDilutionFactor": hh3cWlanDilutionFactor,
       "hh3cWlanDilutionTimeout": hh3cWlanDilutionTimeout,
       "hh3cWlanIgnoreBeacon": hh3cWlanIgnoreBeacon,
       "hh3cWlanRateLimitStatus": hh3cWlanRateLimitStatus,
       "hh3cWlanRateLimitCir": hh3cWlanRateLimitCir,
       "hh3cWlanRateLimitCbs": hh3cWlanRateLimitCbs,
       "hh3cWlanClientRateLimitStatus": hh3cWlanClientRateLimitStatus,
       "hh3cWlanClientRateLimitCir": hh3cWlanClientRateLimitCir,
       "hh3cWlanClientRateLimitCbs": hh3cWlanClientRateLimitCbs,
       "hh3cWlanRssiStatus": hh3cWlanRssiStatus,
       "hh3cWlanRssiThreshold": hh3cWlanRssiThreshold,
       "hh3cWlanIgnoreApFrame": hh3cWlanIgnoreApFrame,
       "hh3cWlanCUPIDConfigGroup": hh3cWlanCUPIDConfigGroup,
       "hh3cWlanCUPIDConfigTable": hh3cWlanCUPIDConfigTable,
       "hh3cWlanCUPIDConfigEntry": hh3cWlanCUPIDConfigEntry,
       "hh3cWlanCupidAPSerialID": hh3cWlanCupidAPSerialID,
       "hh3cWlanCupidStatus": hh3cWlanCupidStatus,
       "hh3cWlanCupidEngineAddr": hh3cWlanCupidEngineAddr,
       "hh3cWlanCupidEnginePort": hh3cWlanCupidEnginePort,
       "hh3cWlanCupidVendorPort": hh3cWlanCupidVendorPort,
       "hh3cWlanCupidReportStatus": hh3cWlanCupidReportStatus,
       "hh3cWlanCupidReportInterval": hh3cWlanCupidReportInterval,
       "hh3cWlanCupidUnassSta": hh3cWlanCupidUnassSta,
       "hh3cWlanCupidUnassMeasureSta": hh3cWlanCupidUnassMeasureSta,
       "hh3cWlanCupidReportMode": hh3cWlanCupidReportMode,
       "hh3cWlanCUPIDReportFormat": hh3cWlanCUPIDReportFormat,
       "hh3cWlanFPConfigGroup": hh3cWlanFPConfigGroup,
       "hh3cWlanFPConfigTable": hh3cWlanFPConfigTable,
       "hh3cWlanFPConfigEntry": hh3cWlanFPConfigEntry,
       "hh3cWlanFPAPSerialID": hh3cWlanFPAPSerialID,
       "hh3cWlanFPStatus": hh3cWlanFPStatus,
       "hh3cWlanFPEngineAddr": hh3cWlanFPEngineAddr,
       "hh3cWlanFPEnginePort": hh3cWlanFPEnginePort,
       "hh3cWlanFPVendorPort": hh3cWlanFPVendorPort,
       "hh3cWlanFPRawFrameReport": hh3cWlanFPRawFrameReport,
       "hh3cWlanFPMUReport": hh3cWlanFPMUReport,
       "hh3cWlanFPReportMode": hh3cWlanFPReportMode,
       "hh3cWlanFPReportFormat": hh3cWlanFPReportFormat,
       "hh3cWlanFPTagMultiAddr": hh3cWlanFPTagMultiAddr}
)
