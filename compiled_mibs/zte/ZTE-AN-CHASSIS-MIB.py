# SNMP MIB module (ZTE-AN-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zte\ZTE-AN-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:41 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxAccessNode,
 zxAnEquipment) = mibBuilder.importSymbols(
    "ZTE-AN-SMI",
    "zxAccessNode",
    "zxAnEquipment")


# MODULE-IDENTITY

zxAnChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1)
)
if mibBuilder.loadTexts:
    zxAnChassisMib.setRevisions(
        ("2014-05-22 00:00",
         "2014-05-14 00:00",
         "2011-05-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnChassisGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnChassisGlobalObjects = _ZxAnChassisGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 1)
)


class _ZxAnChassisSysReboot_Type(Integer32):
    """Custom type zxAnChassisSysReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rebootSystem", 1)
    )


_ZxAnChassisSysReboot_Type.__name__ = "Integer32"
_ZxAnChassisSysReboot_Object = MibScalar
zxAnChassisSysReboot = _ZxAnChassisSysReboot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 1, 1),
    _ZxAnChassisSysReboot_Type()
)
zxAnChassisSysReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnChassisSysReboot.setStatus("current")


class _ZxAnChassisSysLastRebootReason_Type(Integer32):
    """Custom type zxAnChassisSysLastRebootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("byCli", 1),
          ("byNms", 2),
          ("byWatchdog", 3),
          ("byPowerOff", 4),
          ("bySoftwareRestart", 5),
          ("byProcessSuspended", 6),
          ("unknown", 99))
    )


_ZxAnChassisSysLastRebootReason_Type.__name__ = "Integer32"
_ZxAnChassisSysLastRebootReason_Object = MibScalar
zxAnChassisSysLastRebootReason = _ZxAnChassisSysLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 1, 2),
    _ZxAnChassisSysLastRebootReason_Type()
)
zxAnChassisSysLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnChassisSysLastRebootReason.setStatus("current")


class _ZxAnChassisSysLastSwapReason_Type(Integer32):
    """Custom type zxAnChassisSysLastSwapReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("forced", 1),
          ("cardOffline", 2),
          ("reset", 3),
          ("cardDown", 99))
    )


_ZxAnChassisSysLastSwapReason_Type.__name__ = "Integer32"
_ZxAnChassisSysLastSwapReason_Object = MibScalar
zxAnChassisSysLastSwapReason = _ZxAnChassisSysLastSwapReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 1, 3),
    _ZxAnChassisSysLastSwapReason_Type()
)
zxAnChassisSysLastSwapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnChassisSysLastSwapReason.setStatus("current")


class _ZxAnChassisPnpMode_Type(Integer32):
    """Custom type zxAnChassisPnpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnChassisPnpMode_Type.__name__ = "Integer32"
_ZxAnChassisPnpMode_Object = MibScalar
zxAnChassisPnpMode = _ZxAnChassisPnpMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 1, 4),
    _ZxAnChassisPnpMode_Type()
)
zxAnChassisPnpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnChassisPnpMode.setStatus("current")
_ZxAnChassisObjects_ObjectIdentity = ObjectIdentity
zxAnChassisObjects = _ZxAnChassisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2)
)
_ZxAnRackTable_Object = MibTable
zxAnRackTable = _ZxAnRackTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnRackTable.setStatus("current")
_ZxAnRackEntry_Object = MibTableRow
zxAnRackEntry = _ZxAnRackEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 2, 1)
)
zxAnRackEntry.setIndexNames(
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnRack"),
)
if mibBuilder.loadTexts:
    zxAnRackEntry.setStatus("current")
_ZxAnRack_Type = Integer32
_ZxAnRack_Object = MibTableColumn
zxAnRack = _ZxAnRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 2, 1, 1),
    _ZxAnRack_Type()
)
zxAnRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRack.setStatus("current")
_ZxAnRackActualType_Type = Integer32
_ZxAnRackActualType_Object = MibTableColumn
zxAnRackActualType = _ZxAnRackActualType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 2, 1, 2),
    _ZxAnRackActualType_Type()
)
zxAnRackActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRackActualType.setStatus("current")
_ZxAnRackConfType_Type = Integer32
_ZxAnRackConfType_Object = MibTableColumn
zxAnRackConfType = _ZxAnRackConfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 2, 1, 3),
    _ZxAnRackConfType_Type()
)
zxAnRackConfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRackConfType.setStatus("current")


class _ZxAnRackInvSn_Type(DisplayString):
    """Custom type zxAnRackInvSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnRackInvSn_Type.__name__ = "DisplayString"
_ZxAnRackInvSn_Object = MibTableColumn
zxAnRackInvSn = _ZxAnRackInvSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 2, 1, 4),
    _ZxAnRackInvSn_Type()
)
zxAnRackInvSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRackInvSn.setStatus("current")
_ZxAnRackRowStatus_Type = RowStatus
_ZxAnRackRowStatus_Object = MibTableColumn
zxAnRackRowStatus = _ZxAnRackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 2, 1, 50),
    _ZxAnRackRowStatus_Type()
)
zxAnRackRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRackRowStatus.setStatus("current")
_ZxAnShelfTable_Object = MibTable
zxAnShelfTable = _ZxAnShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnShelfTable.setStatus("current")
_ZxAnShelfEntry_Object = MibTableRow
zxAnShelfEntry = _ZxAnShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 3, 1)
)
zxAnShelfEntry.setIndexNames(
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnRack"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnShelf"),
)
if mibBuilder.loadTexts:
    zxAnShelfEntry.setStatus("current")
_ZxAnShelf_Type = Integer32
_ZxAnShelf_Object = MibTableColumn
zxAnShelf = _ZxAnShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 3, 1, 1),
    _ZxAnShelf_Type()
)
zxAnShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnShelf.setStatus("current")


class _ZxAnShelfHardwareVersion_Type(DisplayString):
    """Custom type zxAnShelfHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnShelfHardwareVersion_Type.__name__ = "DisplayString"
_ZxAnShelfHardwareVersion_Object = MibTableColumn
zxAnShelfHardwareVersion = _ZxAnShelfHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 3, 1, 2),
    _ZxAnShelfHardwareVersion_Type()
)
zxAnShelfHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShelfHardwareVersion.setStatus("current")
_ZxAnShelfActualType_Type = Integer32
_ZxAnShelfActualType_Object = MibTableColumn
zxAnShelfActualType = _ZxAnShelfActualType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 3, 1, 3),
    _ZxAnShelfActualType_Type()
)
zxAnShelfActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShelfActualType.setStatus("current")
_ZxAnShelfConfType_Type = Integer32
_ZxAnShelfConfType_Object = MibTableColumn
zxAnShelfConfType = _ZxAnShelfConfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 3, 1, 4),
    _ZxAnShelfConfType_Type()
)
zxAnShelfConfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnShelfConfType.setStatus("current")


class _ZxAnShelfInvSn_Type(DisplayString):
    """Custom type zxAnShelfInvSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnShelfInvSn_Type.__name__ = "DisplayString"
_ZxAnShelfInvSn_Object = MibTableColumn
zxAnShelfInvSn = _ZxAnShelfInvSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 3, 1, 5),
    _ZxAnShelfInvSn_Type()
)
zxAnShelfInvSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnShelfInvSn.setStatus("current")


class _ZxAnShelfCleiCode_Type(DisplayString):
    """Custom type zxAnShelfCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnShelfCleiCode_Type.__name__ = "DisplayString"
_ZxAnShelfCleiCode_Object = MibTableColumn
zxAnShelfCleiCode = _ZxAnShelfCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 3, 1, 6),
    _ZxAnShelfCleiCode_Type()
)
zxAnShelfCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnShelfCleiCode.setStatus("current")
_ZxAnLogicShelfNo_Type = Integer32
_ZxAnLogicShelfNo_Object = MibTableColumn
zxAnLogicShelfNo = _ZxAnLogicShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 3, 1, 7),
    _ZxAnLogicShelfNo_Type()
)
zxAnLogicShelfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnLogicShelfNo.setStatus("current")
_ZxAnShelfRowStatus_Type = RowStatus
_ZxAnShelfRowStatus_Object = MibTableColumn
zxAnShelfRowStatus = _ZxAnShelfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 3, 1, 50),
    _ZxAnShelfRowStatus_Type()
)
zxAnShelfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnShelfRowStatus.setStatus("current")
_ZxAnCardTable_Object = MibTable
zxAnCardTable = _ZxAnCardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnCardTable.setStatus("current")
_ZxAnCardEntry_Object = MibTableRow
zxAnCardEntry = _ZxAnCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1)
)
zxAnCardEntry.setIndexNames(
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnRack"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnShelf"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnSlot"),
)
if mibBuilder.loadTexts:
    zxAnCardEntry.setStatus("current")
_ZxAnSlot_Type = Integer32
_ZxAnSlot_Object = MibTableColumn
zxAnSlot = _ZxAnSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 1),
    _ZxAnSlot_Type()
)
zxAnSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSlot.setStatus("current")
_ZxAnCardConfMainType_Type = Integer32
_ZxAnCardConfMainType_Object = MibTableColumn
zxAnCardConfMainType = _ZxAnCardConfMainType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 2),
    _ZxAnCardConfMainType_Type()
)
zxAnCardConfMainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardConfMainType.setStatus("current")
_ZxAnCardActualMainType_Type = Integer32
_ZxAnCardActualMainType_Object = MibTableColumn
zxAnCardActualMainType = _ZxAnCardActualMainType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 3),
    _ZxAnCardActualMainType_Type()
)
zxAnCardActualMainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardActualMainType.setStatus("current")


class _ZxAnCardActualType_Type(DisplayString):
    """Custom type zxAnCardActualType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnCardActualType_Type.__name__ = "DisplayString"
_ZxAnCardActualType_Object = MibTableColumn
zxAnCardActualType = _ZxAnCardActualType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 4),
    _ZxAnCardActualType_Type()
)
zxAnCardActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardActualType.setStatus("current")


class _ZxAnCardOperStatus_Type(Integer32):
    """Custom type zxAnCardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              34)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("notInService", 2),
          ("hwOnline", 3),
          ("hwOffline", 4),
          ("configuring", 5),
          ("configFailed", 6),
          ("typeMismatch", 7),
          ("deactived", 8),
          ("faulty", 9),
          ("invalid", 10),
          ("noPower", 11),
          ("unauthorized", 12),
          ("powerSaving", 34))
    )


_ZxAnCardOperStatus_Type.__name__ = "Integer32"
_ZxAnCardOperStatus_Object = MibTableColumn
zxAnCardOperStatus = _ZxAnCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 5),
    _ZxAnCardOperStatus_Type()
)
zxAnCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardOperStatus.setStatus("current")


class _ZxAnCardAdminStatus_Type(Integer32):
    """Custom type zxAnCardAdminStatus based on Integer32"""
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
        *(("reset", 1),
          ("switch", 2),
          ("stopService", 3),
          ("active", 4),
          ("deactive", 5))
    )


_ZxAnCardAdminStatus_Type.__name__ = "Integer32"
_ZxAnCardAdminStatus_Object = MibTableColumn
zxAnCardAdminStatus = _ZxAnCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 6),
    _ZxAnCardAdminStatus_Type()
)
zxAnCardAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardAdminStatus.setStatus("current")
_ZxAnCardPortNums_Type = Integer32
_ZxAnCardPortNums_Object = MibTableColumn
zxAnCardPortNums = _ZxAnCardPortNums_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 7),
    _ZxAnCardPortNums_Type()
)
zxAnCardPortNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardPortNums.setStatus("current")
_ZxAnCardActivePortNums_Type = Integer32
_ZxAnCardActivePortNums_Object = MibTableColumn
zxAnCardActivePortNums = _ZxAnCardActivePortNums_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 8),
    _ZxAnCardActivePortNums_Type()
)
zxAnCardActivePortNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardActivePortNums.setStatus("current")


class _ZxAnCardCpuLoad_Type(Integer32):
    """Custom type zxAnCardCpuLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnCardCpuLoad_Type.__name__ = "Integer32"
_ZxAnCardCpuLoad_Object = MibTableColumn
zxAnCardCpuLoad = _ZxAnCardCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 9),
    _ZxAnCardCpuLoad_Type()
)
zxAnCardCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardCpuLoad.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardCpuLoad.setUnits("percent")


class _ZxAnCardCpuLoadThreshold_Type(Integer32):
    """Custom type zxAnCardCpuLoadThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ZxAnCardCpuLoadThreshold_Type.__name__ = "Integer32"
_ZxAnCardCpuLoadThreshold_Object = MibTableColumn
zxAnCardCpuLoadThreshold = _ZxAnCardCpuLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 10),
    _ZxAnCardCpuLoadThreshold_Type()
)
zxAnCardCpuLoadThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardCpuLoadThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardCpuLoadThreshold.setUnits("percent")


class _ZxAnCardMemUsage_Type(Integer32):
    """Custom type zxAnCardMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnCardMemUsage_Type.__name__ = "Integer32"
_ZxAnCardMemUsage_Object = MibTableColumn
zxAnCardMemUsage = _ZxAnCardMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 11),
    _ZxAnCardMemUsage_Type()
)
zxAnCardMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardMemUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardMemUsage.setUnits("percent")


class _ZxAnCardMemUsageThreshold_Type(Integer32):
    """Custom type zxAnCardMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ZxAnCardMemUsageThreshold_Type.__name__ = "Integer32"
_ZxAnCardMemUsageThreshold_Object = MibTableColumn
zxAnCardMemUsageThreshold = _ZxAnCardMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 12),
    _ZxAnCardMemUsageThreshold_Type()
)
zxAnCardMemUsageThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardMemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardMemUsageThreshold.setUnits("percent")


class _ZxAnCardStandbyStatus_Type(Integer32):
    """Custom type zxAnCardStandbyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("standby", 2),
          ("unknown", 15))
    )


_ZxAnCardStandbyStatus_Type.__name__ = "Integer32"
_ZxAnCardStandbyStatus_Object = MibTableColumn
zxAnCardStandbyStatus = _ZxAnCardStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 13),
    _ZxAnCardStandbyStatus_Type()
)
zxAnCardStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardStandbyStatus.setStatus("current")


class _ZxAnCardInvSn_Type(DisplayString):
    """Custom type zxAnCardInvSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnCardInvSn_Type.__name__ = "DisplayString"
_ZxAnCardInvSn_Object = MibTableColumn
zxAnCardInvSn = _ZxAnCardInvSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 14),
    _ZxAnCardInvSn_Type()
)
zxAnCardInvSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardInvSn.setStatus("current")


class _ZxAnCardCleiCode_Type(DisplayString):
    """Custom type zxAnCardCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnCardCleiCode_Type.__name__ = "DisplayString"
_ZxAnCardCleiCode_Object = MibTableColumn
zxAnCardCleiCode = _ZxAnCardCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 15),
    _ZxAnCardCleiCode_Type()
)
zxAnCardCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardCleiCode.setStatus("current")


class _ZxAnCardAccessoriesType_Type(DisplayString):
    """Custom type zxAnCardAccessoriesType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnCardAccessoriesType_Type.__name__ = "DisplayString"
_ZxAnCardAccessoriesType_Object = MibTableColumn
zxAnCardAccessoriesType = _ZxAnCardAccessoriesType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 16),
    _ZxAnCardAccessoriesType_Type()
)
zxAnCardAccessoriesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardAccessoriesType.setStatus("current")


class _ZxAnCardAccessoriesOperStatus_Type(Integer32):
    """Custom type zxAnCardAccessoriesOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknow", 4))
    )


_ZxAnCardAccessoriesOperStatus_Type.__name__ = "Integer32"
_ZxAnCardAccessoriesOperStatus_Object = MibTableColumn
zxAnCardAccessoriesOperStatus = _ZxAnCardAccessoriesOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 17),
    _ZxAnCardAccessoriesOperStatus_Type()
)
zxAnCardAccessoriesOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardAccessoriesOperStatus.setStatus("current")
_ZxAnCardMemSize_Type = Integer32
_ZxAnCardMemSize_Object = MibTableColumn
zxAnCardMemSize = _ZxAnCardMemSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 19),
    _ZxAnCardMemSize_Type()
)
zxAnCardMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardMemSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardMemSize.setUnits("MB")
_ZxAnCardAvailableStorageSize_Type = Integer32
_ZxAnCardAvailableStorageSize_Object = MibTableColumn
zxAnCardAvailableStorageSize = _ZxAnCardAvailableStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 21),
    _ZxAnCardAvailableStorageSize_Type()
)
zxAnCardAvailableStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardAvailableStorageSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardAvailableStorageSize.setUnits("KB")
_ZxAnCardTotalStorageSize_Type = Integer32
_ZxAnCardTotalStorageSize_Object = MibTableColumn
zxAnCardTotalStorageSize = _ZxAnCardTotalStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 22),
    _ZxAnCardTotalStorageSize_Type()
)
zxAnCardTotalStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardTotalStorageSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardTotalStorageSize.setUnits("KB")


class _ZxAnCardHardwareVersion_Type(DisplayString):
    """Custom type zxAnCardHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnCardHardwareVersion_Type.__name__ = "DisplayString"
_ZxAnCardHardwareVersion_Object = MibTableColumn
zxAnCardHardwareVersion = _ZxAnCardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 23),
    _ZxAnCardHardwareVersion_Type()
)
zxAnCardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardHardwareVersion.setStatus("current")


class _ZxAnCardPowerSavingEnable_Type(Integer32):
    """Custom type zxAnCardPowerSavingEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnCardPowerSavingEnable_Type.__name__ = "Integer32"
_ZxAnCardPowerSavingEnable_Object = MibTableColumn
zxAnCardPowerSavingEnable = _ZxAnCardPowerSavingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 24),
    _ZxAnCardPowerSavingEnable_Type()
)
zxAnCardPowerSavingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardPowerSavingEnable.setStatus("current")
_ZxAnCardLastStartupTime_Type = DateAndTime
_ZxAnCardLastStartupTime_Object = MibTableColumn
zxAnCardLastStartupTime = _ZxAnCardLastStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 25),
    _ZxAnCardLastStartupTime_Type()
)
zxAnCardLastStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardLastStartupTime.setStatus("current")


class _ZxAnCardCpldVersion_Type(DisplayString):
    """Custom type zxAnCardCpldVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnCardCpldVersion_Type.__name__ = "DisplayString"
_ZxAnCardCpldVersion_Object = MibTableColumn
zxAnCardCpldVersion = _ZxAnCardCpldVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 26),
    _ZxAnCardCpldVersion_Type()
)
zxAnCardCpldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardCpldVersion.setStatus("current")


class _ZxAnCardFirmwareVersion_Type(DisplayString):
    """Custom type zxAnCardFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnCardFirmwareVersion_Type.__name__ = "DisplayString"
_ZxAnCardFirmwareVersion_Object = MibTableColumn
zxAnCardFirmwareVersion = _ZxAnCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 27),
    _ZxAnCardFirmwareVersion_Type()
)
zxAnCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardFirmwareVersion.setStatus("current")


class _ZxAnCardOtherFirmwareVersions_Type(DisplayString):
    """Custom type zxAnCardOtherFirmwareVersions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnCardOtherFirmwareVersions_Type.__name__ = "DisplayString"
_ZxAnCardOtherFirmwareVersions_Object = MibTableColumn
zxAnCardOtherFirmwareVersions = _ZxAnCardOtherFirmwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 28),
    _ZxAnCardOtherFirmwareVersions_Type()
)
zxAnCardOtherFirmwareVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardOtherFirmwareVersions.setStatus("current")
_ZxAnCardRowStatus_Type = RowStatus
_ZxAnCardRowStatus_Object = MibTableColumn
zxAnCardRowStatus = _ZxAnCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 4, 1, 50),
    _ZxAnCardRowStatus_Type()
)
zxAnCardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardRowStatus.setStatus("current")
_ZxAnSubcardTable_Object = MibTable
zxAnSubcardTable = _ZxAnSubcardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnSubcardTable.setStatus("current")
_ZxAnSubcardEntry_Object = MibTableRow
zxAnSubcardEntry = _ZxAnSubcardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1)
)
zxAnSubcardEntry.setIndexNames(
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnRack"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnShelf"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnSlot"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnSubcard"),
)
if mibBuilder.loadTexts:
    zxAnSubcardEntry.setStatus("current")
_ZxAnSubcard_Type = Integer32
_ZxAnSubcard_Object = MibTableColumn
zxAnSubcard = _ZxAnSubcard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 1),
    _ZxAnSubcard_Type()
)
zxAnSubcard.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSubcard.setStatus("current")
_ZxAnSubcardConfMainType_Type = Integer32
_ZxAnSubcardConfMainType_Object = MibTableColumn
zxAnSubcardConfMainType = _ZxAnSubcardConfMainType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 2),
    _ZxAnSubcardConfMainType_Type()
)
zxAnSubcardConfMainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSubcardConfMainType.setStatus("current")
_ZxAnSubcardActualMainType_Type = Integer32
_ZxAnSubcardActualMainType_Object = MibTableColumn
zxAnSubcardActualMainType = _ZxAnSubcardActualMainType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 3),
    _ZxAnSubcardActualMainType_Type()
)
zxAnSubcardActualMainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardActualMainType.setStatus("current")


class _ZxAnSubcardActualType_Type(DisplayString):
    """Custom type zxAnSubcardActualType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnSubcardActualType_Type.__name__ = "DisplayString"
_ZxAnSubcardActualType_Object = MibTableColumn
zxAnSubcardActualType = _ZxAnSubcardActualType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 4),
    _ZxAnSubcardActualType_Type()
)
zxAnSubcardActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardActualType.setStatus("current")


class _ZxAnSubcardOperStatus_Type(Integer32):
    """Custom type zxAnSubcardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("notInService", 2),
          ("hwOnline", 3),
          ("hwOffline", 4),
          ("configuring", 5),
          ("configFailed", 6),
          ("typeMismatch", 7),
          ("deactived", 8),
          ("faulty", 9),
          ("invalid", 10))
    )


_ZxAnSubcardOperStatus_Type.__name__ = "Integer32"
_ZxAnSubcardOperStatus_Object = MibTableColumn
zxAnSubcardOperStatus = _ZxAnSubcardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 5),
    _ZxAnSubcardOperStatus_Type()
)
zxAnSubcardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardOperStatus.setStatus("current")


class _ZxAnSubcardAdminStatus_Type(Integer32):
    """Custom type zxAnSubcardAdminStatus based on Integer32"""
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
        *(("reset", 1),
          ("switch", 2),
          ("stopService", 3),
          ("active", 4),
          ("deactive", 5))
    )


_ZxAnSubcardAdminStatus_Type.__name__ = "Integer32"
_ZxAnSubcardAdminStatus_Object = MibTableColumn
zxAnSubcardAdminStatus = _ZxAnSubcardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 6),
    _ZxAnSubcardAdminStatus_Type()
)
zxAnSubcardAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSubcardAdminStatus.setStatus("current")
_ZxAnSubcardPortNums_Type = Integer32
_ZxAnSubcardPortNums_Object = MibTableColumn
zxAnSubcardPortNums = _ZxAnSubcardPortNums_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 7),
    _ZxAnSubcardPortNums_Type()
)
zxAnSubcardPortNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardPortNums.setStatus("current")
_ZxAnSubcardActivePortNums_Type = Integer32
_ZxAnSubcardActivePortNums_Object = MibTableColumn
zxAnSubcardActivePortNums = _ZxAnSubcardActivePortNums_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 8),
    _ZxAnSubcardActivePortNums_Type()
)
zxAnSubcardActivePortNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardActivePortNums.setStatus("current")
_ZxAnSubcardCpuLoad_Type = Integer32
_ZxAnSubcardCpuLoad_Object = MibTableColumn
zxAnSubcardCpuLoad = _ZxAnSubcardCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 9),
    _ZxAnSubcardCpuLoad_Type()
)
zxAnSubcardCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardCpuLoad.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSubcardCpuLoad.setUnits("percent")
_ZxAnSubcardMemUsage_Type = Integer32
_ZxAnSubcardMemUsage_Object = MibTableColumn
zxAnSubcardMemUsage = _ZxAnSubcardMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 10),
    _ZxAnSubcardMemUsage_Type()
)
zxAnSubcardMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardMemUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSubcardMemUsage.setUnits("percent")


class _ZxAnSubcardInvSn_Type(DisplayString):
    """Custom type zxAnSubcardInvSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSubcardInvSn_Type.__name__ = "DisplayString"
_ZxAnSubcardInvSn_Object = MibTableColumn
zxAnSubcardInvSn = _ZxAnSubcardInvSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 11),
    _ZxAnSubcardInvSn_Type()
)
zxAnSubcardInvSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSubcardInvSn.setStatus("current")


class _ZxAnSubcardCleiCode_Type(DisplayString):
    """Custom type zxAnSubcardCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSubcardCleiCode_Type.__name__ = "DisplayString"
_ZxAnSubcardCleiCode_Object = MibTableColumn
zxAnSubcardCleiCode = _ZxAnSubcardCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 12),
    _ZxAnSubcardCleiCode_Type()
)
zxAnSubcardCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardCleiCode.setStatus("current")
_ZxAnSubcardMemSize_Type = Integer32
_ZxAnSubcardMemSize_Object = MibTableColumn
zxAnSubcardMemSize = _ZxAnSubcardMemSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 13),
    _ZxAnSubcardMemSize_Type()
)
zxAnSubcardMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardMemSize.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSubcardMemSize.setUnits("MB")


class _ZxAnSubcardHardwareVersion_Type(DisplayString):
    """Custom type zxAnSubcardHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnSubcardHardwareVersion_Type.__name__ = "DisplayString"
_ZxAnSubcardHardwareVersion_Object = MibTableColumn
zxAnSubcardHardwareVersion = _ZxAnSubcardHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 14),
    _ZxAnSubcardHardwareVersion_Type()
)
zxAnSubcardHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSubcardHardwareVersion.setStatus("current")
_ZxAnSubcardRowStatus_Type = RowStatus
_ZxAnSubcardRowStatus_Object = MibTableColumn
zxAnSubcardRowStatus = _ZxAnSubcardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 5, 1, 50),
    _ZxAnSubcardRowStatus_Type()
)
zxAnSubcardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSubcardRowStatus.setStatus("current")
_ZxAnCardCpuTable_Object = MibTable
zxAnCardCpuTable = _ZxAnCardCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 6)
)
if mibBuilder.loadTexts:
    zxAnCardCpuTable.setStatus("current")
_ZxAnCardCpuEntry_Object = MibTableRow
zxAnCardCpuEntry = _ZxAnCardCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 6, 1)
)
zxAnCardCpuEntry.setIndexNames(
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnRack"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnShelf"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnSlot"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnCardCpuId"),
)
if mibBuilder.loadTexts:
    zxAnCardCpuEntry.setStatus("current")
_ZxAnCardCpuId_Type = Integer32
_ZxAnCardCpuId_Object = MibTableColumn
zxAnCardCpuId = _ZxAnCardCpuId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 6, 1, 1),
    _ZxAnCardCpuId_Type()
)
zxAnCardCpuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCardCpuId.setStatus("current")


class _ZxAnCardCpuUsage_Type(Integer32):
    """Custom type zxAnCardCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnCardCpuUsage_Type.__name__ = "Integer32"
_ZxAnCardCpuUsage_Object = MibTableColumn
zxAnCardCpuUsage = _ZxAnCardCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 6, 1, 2),
    _ZxAnCardCpuUsage_Type()
)
zxAnCardCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardCpuUsage.setUnits("percent")
_ZxAnStorageDeviceTable_Object = MibTable
zxAnStorageDeviceTable = _ZxAnStorageDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 7)
)
if mibBuilder.loadTexts:
    zxAnStorageDeviceTable.setStatus("current")
_ZxAnStorageDeviceEntry_Object = MibTableRow
zxAnStorageDeviceEntry = _ZxAnStorageDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 7, 1)
)
zxAnStorageDeviceEntry.setIndexNames(
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnRack"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnShelf"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnSlot"),
    (0, "ZTE-AN-CHASSIS-MIB", "zxAnStorageDeviceId"),
)
if mibBuilder.loadTexts:
    zxAnStorageDeviceEntry.setStatus("current")
_ZxAnStorageDeviceId_Type = Integer32
_ZxAnStorageDeviceId_Object = MibTableColumn
zxAnStorageDeviceId = _ZxAnStorageDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 7, 1, 1),
    _ZxAnStorageDeviceId_Type()
)
zxAnStorageDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnStorageDeviceId.setStatus("current")


class _ZxAnStorageDeviceAccessEnable_Type(Integer32):
    """Custom type zxAnStorageDeviceAccessEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnStorageDeviceAccessEnable_Type.__name__ = "Integer32"
_ZxAnStorageDeviceAccessEnable_Object = MibTableColumn
zxAnStorageDeviceAccessEnable = _ZxAnStorageDeviceAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 7, 1, 2),
    _ZxAnStorageDeviceAccessEnable_Type()
)
zxAnStorageDeviceAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnStorageDeviceAccessEnable.setStatus("current")


class _ZxAnStorageDeviceOperStatus_Type(Integer32):
    """Custom type zxAnStorageDeviceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_ZxAnStorageDeviceOperStatus_Type.__name__ = "Integer32"
_ZxAnStorageDeviceOperStatus_Object = MibTableColumn
zxAnStorageDeviceOperStatus = _ZxAnStorageDeviceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 7, 1, 3),
    _ZxAnStorageDeviceOperStatus_Type()
)
zxAnStorageDeviceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnStorageDeviceOperStatus.setStatus("current")


class _ZxAnStorageDeviceAccessStatus_Type(Integer32):
    """Custom type zxAnStorageDeviceAccessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("busy", 2),
          ("locked", 3),
          ("unknown", 255))
    )


_ZxAnStorageDeviceAccessStatus_Type.__name__ = "Integer32"
_ZxAnStorageDeviceAccessStatus_Object = MibTableColumn
zxAnStorageDeviceAccessStatus = _ZxAnStorageDeviceAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 7, 1, 4),
    _ZxAnStorageDeviceAccessStatus_Type()
)
zxAnStorageDeviceAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnStorageDeviceAccessStatus.setStatus("current")
_ZxAnStorageDeviceTotalSpace_Type = Integer32
_ZxAnStorageDeviceTotalSpace_Object = MibTableColumn
zxAnStorageDeviceTotalSpace = _ZxAnStorageDeviceTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 7, 1, 5),
    _ZxAnStorageDeviceTotalSpace_Type()
)
zxAnStorageDeviceTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnStorageDeviceTotalSpace.setStatus("current")
if mibBuilder.loadTexts:
    zxAnStorageDeviceTotalSpace.setUnits("MB")
_ZxAnStorageDeviceAvailableSpace_Type = Integer32
_ZxAnStorageDeviceAvailableSpace_Object = MibTableColumn
zxAnStorageDeviceAvailableSpace = _ZxAnStorageDeviceAvailableSpace_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 2, 7, 1, 6),
    _ZxAnStorageDeviceAvailableSpace_Type()
)
zxAnStorageDeviceAvailableSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnStorageDeviceAvailableSpace.setStatus("current")
if mibBuilder.loadTexts:
    zxAnStorageDeviceAvailableSpace.setUnits("MB")
_ZxAnChassisNotifications_ObjectIdentity = ObjectIdentity
zxAnChassisNotifications = _ZxAnChassisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3)
)
_ZxAnChassisSysTraps_ObjectIdentity = ObjectIdentity
zxAnChassisSysTraps = _ZxAnChassisSysTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 1)
)
_ZxAnChassisCardTraps_ObjectIdentity = ObjectIdentity
zxAnChassisCardTraps = _ZxAnChassisCardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2)
)
_ZxAnChassisSubcardTraps_ObjectIdentity = ObjectIdentity
zxAnChassisSubcardTraps = _ZxAnChassisSubcardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 3)
)
_ZxAnChassisConformance_ObjectIdentity = ObjectIdentity
zxAnChassisConformance = _ZxAnChassisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4)
)
_ZxAnChassisCompliances_ObjectIdentity = ObjectIdentity
zxAnChassisCompliances = _ZxAnChassisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4, 1)
)
_ZxAnChassisGroups_ObjectIdentity = ObjectIdentity
zxAnChassisGroups = _ZxAnChassisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4, 2)
)

# Managed Objects groups

zxAnChassisSysMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4, 2, 1)
)
zxAnChassisSysMgmtGroup.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnChassisSysReboot"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisSysLastRebootReason"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisSysLastSwapReason"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisPnpMode"))
)
if mibBuilder.loadTexts:
    zxAnChassisSysMgmtGroup.setStatus("current")

zxAnChassisRackMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4, 2, 2)
)
zxAnChassisRackMgmtGroup.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnRackActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnRackConfType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnRackInvSn"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnRackRowStatus"))
)
if mibBuilder.loadTexts:
    zxAnChassisRackMgmtGroup.setStatus("current")

zxAnChassisShelfMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4, 2, 3)
)
zxAnChassisShelfMgmtGroup.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnShelfHardwareVersion"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnShelfActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnShelfConfType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnShelfInvSn"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnShelfCleiCode"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnLogicShelfNo"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnShelfRowStatus"))
)
if mibBuilder.loadTexts:
    zxAnChassisShelfMgmtGroup.setStatus("current")

zxAnChassisCardMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4, 2, 4)
)
zxAnChassisCardMgmtGroup.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardPortNums"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActivePortNums"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardCpuLoad"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardCpuLoadThreshold"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardMemUsage"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardMemUsageThreshold"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardStandbyStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardInvSn"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardCleiCode"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAccessoriesType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAccessoriesOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardMemSize"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAvailableStorageSize"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardTotalStorageSize"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardHardwareVersion"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardRowStatus"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardMgmtGroup.setStatus("current")

zxAnChassisSubCardMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4, 2, 5)
)
zxAnChassisSubCardMgmtGroup.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnSubcardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardAdminStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardPortNums"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardActivePortNums"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardCpuLoad"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardMemUsage"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardInvSn"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardCleiCode"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardMemSize"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardHardwareVersion"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardRowStatus"))
)
if mibBuilder.loadTexts:
    zxAnChassisSubCardMgmtGroup.setStatus("current")

zxAnChassisSysTrapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4, 2, 6)
)
zxAnChassisSysTrapsGroup.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnChassisCtrlCardSwappedAlm"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCtrlCardSwappedClr"))
)
if mibBuilder.loadTexts:
    zxAnChassisSysTrapsGroup.setStatus("current")

zxAnChassisCardTrapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4, 2, 7)
)
zxAnChassisCardTrapsGroup.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardOffline"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardOnline"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardTypeMismatchAlm"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardTypeMismatchClr"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardNotConfiguredAlm"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardNotConfiguredClr"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardNotRunningAlm"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardNotRunningClr"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardCpuOverloadAlm"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardCpuOverloadClr"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardMemOverloadAlm"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardMemOverloadClr"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardResourceAdded"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardResourceDeleted"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardTrapsGroup.setStatus("current")


# Notification objects

zxAnChassisCtrlCardSwappedAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 1, 2)
)
zxAnChassisCtrlCardSwappedAlm.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisSysLastSwapReason"))
)
if mibBuilder.loadTexts:
    zxAnChassisCtrlCardSwappedAlm.setStatus(
        "current"
    )

zxAnChassisCtrlCardSwappedClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnChassisCtrlCardSwappedClr.setStatus(
        "current"
    )

zxAnChassisCardOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 1)
)
zxAnChassisCardOffline.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardOffline.setStatus(
        "current"
    )

zxAnChassisCardOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 2)
)
zxAnChassisCardOnline.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardOnline.setStatus(
        "current"
    )

zxAnChassisCardTypeMismatchAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 3)
)
zxAnChassisCardTypeMismatchAlm.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardTypeMismatchAlm.setStatus(
        "current"
    )

zxAnChassisCardTypeMismatchClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 4)
)
zxAnChassisCardTypeMismatchClr.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardTypeMismatchClr.setStatus(
        "current"
    )

zxAnChassisCardNotRunningAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 5)
)
zxAnChassisCardNotRunningAlm.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardNotRunningAlm.setStatus(
        "current"
    )

zxAnChassisCardNotRunningClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 6)
)
zxAnChassisCardNotRunningClr.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardNotRunningClr.setStatus(
        "current"
    )

zxAnChassisCardNotConfiguredAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 7)
)
zxAnChassisCardNotConfiguredAlm.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardNotConfiguredAlm.setStatus(
        "current"
    )

zxAnChassisCardNotConfiguredClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 8)
)
zxAnChassisCardNotConfiguredClr.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardAdminStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardOperStatus"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardInvSn"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardNotConfiguredClr.setStatus(
        "current"
    )

zxAnChassisCardCpuOverloadAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 20)
)
zxAnChassisCardCpuOverloadAlm.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardCpuLoad"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardCpuLoadThreshold"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardCpuOverloadAlm.setStatus(
        "current"
    )

zxAnChassisCardCpuOverloadClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 21)
)
zxAnChassisCardCpuOverloadClr.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardCpuLoad"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardCpuLoadThreshold"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardCpuOverloadClr.setStatus(
        "current"
    )

zxAnChassisCardMemOverloadAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 22)
)
zxAnChassisCardMemOverloadAlm.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardMemUsage"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardMemOverloadAlm.setStatus(
        "current"
    )

zxAnChassisCardMemOverloadClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 23)
)
zxAnChassisCardMemOverloadClr.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardMemUsage"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardMemOverloadClr.setStatus(
        "current"
    )

zxAnChassisCardResourceAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 24)
)
zxAnChassisCardResourceAdded.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardPortNums"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSwCardVersion"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardHardwareVersion"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardResourceAdded.setStatus(
        "current"
    )

zxAnChassisCardResourceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 2, 25)
)
zxAnChassisCardResourceDeleted.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnCardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardPortNums"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSwCardVersion"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnCardHardwareVersion"))
)
if mibBuilder.loadTexts:
    zxAnChassisCardResourceDeleted.setStatus(
        "current"
    )

zxAnChassisSubcardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 3, 1)
)
zxAnChassisSubcardDown.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnSubcardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardOperStatus"))
)
if mibBuilder.loadTexts:
    zxAnChassisSubcardDown.setStatus(
        "current"
    )

zxAnChassisSubcardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 3, 3, 2)
)
zxAnChassisSubcardUp.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnSubcardConfMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardActualMainType"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnSubcardOperStatus"))
)
if mibBuilder.loadTexts:
    zxAnChassisSubcardUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

zxAnChassisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 1, 4, 1, 1)
)
zxAnChassisCompliance.setObjects(
      *(("ZTE-AN-CHASSIS-MIB", "zxAnChassisSysMgmtGroup"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisRackMgmtGroup"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisShelfMgmtGroup"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardMgmtGroup"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisSubCardMgmtGroup"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisSysTrapsGroup"),
        ("ZTE-AN-CHASSIS-MIB", "zxAnChassisCardTrapsGroup"))
)
if mibBuilder.loadTexts:
    zxAnChassisCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-CHASSIS-MIB",
    **{"zxAnChassisMib": zxAnChassisMib,
       "zxAnChassisGlobalObjects": zxAnChassisGlobalObjects,
       "zxAnChassisSysReboot": zxAnChassisSysReboot,
       "zxAnChassisSysLastRebootReason": zxAnChassisSysLastRebootReason,
       "zxAnChassisSysLastSwapReason": zxAnChassisSysLastSwapReason,
       "zxAnChassisPnpMode": zxAnChassisPnpMode,
       "zxAnChassisObjects": zxAnChassisObjects,
       "zxAnRackTable": zxAnRackTable,
       "zxAnRackEntry": zxAnRackEntry,
       "zxAnRack": zxAnRack,
       "zxAnRackActualType": zxAnRackActualType,
       "zxAnRackConfType": zxAnRackConfType,
       "zxAnRackInvSn": zxAnRackInvSn,
       "zxAnRackRowStatus": zxAnRackRowStatus,
       "zxAnShelfTable": zxAnShelfTable,
       "zxAnShelfEntry": zxAnShelfEntry,
       "zxAnShelf": zxAnShelf,
       "zxAnShelfHardwareVersion": zxAnShelfHardwareVersion,
       "zxAnShelfActualType": zxAnShelfActualType,
       "zxAnShelfConfType": zxAnShelfConfType,
       "zxAnShelfInvSn": zxAnShelfInvSn,
       "zxAnShelfCleiCode": zxAnShelfCleiCode,
       "zxAnLogicShelfNo": zxAnLogicShelfNo,
       "zxAnShelfRowStatus": zxAnShelfRowStatus,
       "zxAnCardTable": zxAnCardTable,
       "zxAnCardEntry": zxAnCardEntry,
       "zxAnSlot": zxAnSlot,
       "zxAnCardConfMainType": zxAnCardConfMainType,
       "zxAnCardActualMainType": zxAnCardActualMainType,
       "zxAnCardActualType": zxAnCardActualType,
       "zxAnCardOperStatus": zxAnCardOperStatus,
       "zxAnCardAdminStatus": zxAnCardAdminStatus,
       "zxAnCardPortNums": zxAnCardPortNums,
       "zxAnCardActivePortNums": zxAnCardActivePortNums,
       "zxAnCardCpuLoad": zxAnCardCpuLoad,
       "zxAnCardCpuLoadThreshold": zxAnCardCpuLoadThreshold,
       "zxAnCardMemUsage": zxAnCardMemUsage,
       "zxAnCardMemUsageThreshold": zxAnCardMemUsageThreshold,
       "zxAnCardStandbyStatus": zxAnCardStandbyStatus,
       "zxAnCardInvSn": zxAnCardInvSn,
       "zxAnCardCleiCode": zxAnCardCleiCode,
       "zxAnCardAccessoriesType": zxAnCardAccessoriesType,
       "zxAnCardAccessoriesOperStatus": zxAnCardAccessoriesOperStatus,
       "zxAnCardMemSize": zxAnCardMemSize,
       "zxAnCardAvailableStorageSize": zxAnCardAvailableStorageSize,
       "zxAnCardTotalStorageSize": zxAnCardTotalStorageSize,
       "zxAnCardHardwareVersion": zxAnCardHardwareVersion,
       "zxAnCardPowerSavingEnable": zxAnCardPowerSavingEnable,
       "zxAnCardLastStartupTime": zxAnCardLastStartupTime,
       "zxAnCardCpldVersion": zxAnCardCpldVersion,
       "zxAnCardFirmwareVersion": zxAnCardFirmwareVersion,
       "zxAnCardOtherFirmwareVersions": zxAnCardOtherFirmwareVersions,
       "zxAnCardRowStatus": zxAnCardRowStatus,
       "zxAnSubcardTable": zxAnSubcardTable,
       "zxAnSubcardEntry": zxAnSubcardEntry,
       "zxAnSubcard": zxAnSubcard,
       "zxAnSubcardConfMainType": zxAnSubcardConfMainType,
       "zxAnSubcardActualMainType": zxAnSubcardActualMainType,
       "zxAnSubcardActualType": zxAnSubcardActualType,
       "zxAnSubcardOperStatus": zxAnSubcardOperStatus,
       "zxAnSubcardAdminStatus": zxAnSubcardAdminStatus,
       "zxAnSubcardPortNums": zxAnSubcardPortNums,
       "zxAnSubcardActivePortNums": zxAnSubcardActivePortNums,
       "zxAnSubcardCpuLoad": zxAnSubcardCpuLoad,
       "zxAnSubcardMemUsage": zxAnSubcardMemUsage,
       "zxAnSubcardInvSn": zxAnSubcardInvSn,
       "zxAnSubcardCleiCode": zxAnSubcardCleiCode,
       "zxAnSubcardMemSize": zxAnSubcardMemSize,
       "zxAnSubcardHardwareVersion": zxAnSubcardHardwareVersion,
       "zxAnSubcardRowStatus": zxAnSubcardRowStatus,
       "zxAnCardCpuTable": zxAnCardCpuTable,
       "zxAnCardCpuEntry": zxAnCardCpuEntry,
       "zxAnCardCpuId": zxAnCardCpuId,
       "zxAnCardCpuUsage": zxAnCardCpuUsage,
       "zxAnStorageDeviceTable": zxAnStorageDeviceTable,
       "zxAnStorageDeviceEntry": zxAnStorageDeviceEntry,
       "zxAnStorageDeviceId": zxAnStorageDeviceId,
       "zxAnStorageDeviceAccessEnable": zxAnStorageDeviceAccessEnable,
       "zxAnStorageDeviceOperStatus": zxAnStorageDeviceOperStatus,
       "zxAnStorageDeviceAccessStatus": zxAnStorageDeviceAccessStatus,
       "zxAnStorageDeviceTotalSpace": zxAnStorageDeviceTotalSpace,
       "zxAnStorageDeviceAvailableSpace": zxAnStorageDeviceAvailableSpace,
       "zxAnChassisNotifications": zxAnChassisNotifications,
       "zxAnChassisSysTraps": zxAnChassisSysTraps,
       "zxAnChassisCtrlCardSwappedAlm": zxAnChassisCtrlCardSwappedAlm,
       "zxAnChassisCtrlCardSwappedClr": zxAnChassisCtrlCardSwappedClr,
       "zxAnChassisCardTraps": zxAnChassisCardTraps,
       "zxAnChassisCardOffline": zxAnChassisCardOffline,
       "zxAnChassisCardOnline": zxAnChassisCardOnline,
       "zxAnChassisCardTypeMismatchAlm": zxAnChassisCardTypeMismatchAlm,
       "zxAnChassisCardTypeMismatchClr": zxAnChassisCardTypeMismatchClr,
       "zxAnChassisCardNotRunningAlm": zxAnChassisCardNotRunningAlm,
       "zxAnChassisCardNotRunningClr": zxAnChassisCardNotRunningClr,
       "zxAnChassisCardNotConfiguredAlm": zxAnChassisCardNotConfiguredAlm,
       "zxAnChassisCardNotConfiguredClr": zxAnChassisCardNotConfiguredClr,
       "zxAnChassisCardCpuOverloadAlm": zxAnChassisCardCpuOverloadAlm,
       "zxAnChassisCardCpuOverloadClr": zxAnChassisCardCpuOverloadClr,
       "zxAnChassisCardMemOverloadAlm": zxAnChassisCardMemOverloadAlm,
       "zxAnChassisCardMemOverloadClr": zxAnChassisCardMemOverloadClr,
       "zxAnChassisCardResourceAdded": zxAnChassisCardResourceAdded,
       "zxAnChassisCardResourceDeleted": zxAnChassisCardResourceDeleted,
       "zxAnChassisSubcardTraps": zxAnChassisSubcardTraps,
       "zxAnChassisSubcardDown": zxAnChassisSubcardDown,
       "zxAnChassisSubcardUp": zxAnChassisSubcardUp,
       "zxAnChassisConformance": zxAnChassisConformance,
       "zxAnChassisCompliances": zxAnChassisCompliances,
       "zxAnChassisCompliance": zxAnChassisCompliance,
       "zxAnChassisGroups": zxAnChassisGroups,
       "zxAnChassisSysMgmtGroup": zxAnChassisSysMgmtGroup,
       "zxAnChassisRackMgmtGroup": zxAnChassisRackMgmtGroup,
       "zxAnChassisShelfMgmtGroup": zxAnChassisShelfMgmtGroup,
       "zxAnChassisCardMgmtGroup": zxAnChassisCardMgmtGroup,
       "zxAnChassisSubCardMgmtGroup": zxAnChassisSubCardMgmtGroup,
       "zxAnChassisSysTrapsGroup": zxAnChassisSysTrapsGroup,
       "zxAnChassisCardTrapsGroup": zxAnChassisCardTrapsGroup}
)
