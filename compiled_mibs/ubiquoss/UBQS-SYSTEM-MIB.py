# SNMP MIB module (UBQS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubiquoss\UBQS-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:34 2025
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

(ubiMgmtv2,) = mibBuilder.importSymbols(
    "UBQS-SMI",
    "ubiMgmtv2")


# MODULE-IDENTITY

ubiSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1)
)
if mibBuilder.loadTexts:
    ubiSystemMIB.setRevisions(
        ("2010-12-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbiSystemMIBObjects_ObjectIdentity = ObjectIdentity
ubiSystemMIBObjects = _UbiSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1)
)


class _UbiSysReset_Type(Integer32):
    """Custom type ubiSysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_UbiSysReset_Type.__name__ = "Integer32"
_UbiSysReset_Object = MibScalar
ubiSysReset = _UbiSysReset_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 1),
    _UbiSysReset_Type()
)
ubiSysReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ubiSysReset.setStatus("mandatory")
_UbiSysInfo_ObjectIdentity = ObjectIdentity
ubiSysInfo = _UbiSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2)
)
_UbiSysModel_Type = ObjectIdentifier
_UbiSysModel_Object = MibScalar
ubiSysModel = _UbiSysModel_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 1),
    _UbiSysModel_Type()
)
ubiSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysModel.setStatus("mandatory")
_UbiHwVersion_Type = DisplayString
_UbiHwVersion_Object = MibScalar
ubiHwVersion = _UbiHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 2),
    _UbiHwVersion_Type()
)
ubiHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiHwVersion.setStatus("mandatory")
_UbiSwVersion_Type = DisplayString
_UbiSwVersion_Object = MibScalar
ubiSwVersion = _UbiSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 3),
    _UbiSwVersion_Type()
)
ubiSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSwVersion.setStatus("mandatory")
_UbiReleaseDate_Type = DisplayString
_UbiReleaseDate_Object = MibScalar
ubiReleaseDate = _UbiReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 4),
    _UbiReleaseDate_Type()
)
ubiReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiReleaseDate.setStatus("mandatory")
_UbiSerialNumber_Type = DisplayString
_UbiSerialNumber_Object = MibScalar
ubiSerialNumber = _UbiSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 5),
    _UbiSerialNumber_Type()
)
ubiSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSerialNumber.setStatus("mandatory")
_UbiSysPhysAddress_Type = PhysAddress
_UbiSysPhysAddress_Object = MibScalar
ubiSysPhysAddress = _UbiSysPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 6),
    _UbiSysPhysAddress_Type()
)
ubiSysPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysPhysAddress.setStatus("mandatory")
_UbiSysClock_Type = DisplayString
_UbiSysClock_Object = MibScalar
ubiSysClock = _UbiSysClock_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 7),
    _UbiSysClock_Type()
)
ubiSysClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysClock.setStatus("mandatory")
_UbiSysTimeZone_ObjectIdentity = ObjectIdentity
ubiSysTimeZone = _UbiSysTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 8)
)
_UbiSysTimeZoneName_Type = DisplayString
_UbiSysTimeZoneName_Object = MibScalar
ubiSysTimeZoneName = _UbiSysTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 8, 1),
    _UbiSysTimeZoneName_Type()
)
ubiSysTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysTimeZoneName.setStatus("current")
_UbiSysTimeZoneOffset_Type = DisplayString
_UbiSysTimeZoneOffset_Object = MibScalar
ubiSysTimeZoneOffset = _UbiSysTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 8, 2),
    _UbiSysTimeZoneOffset_Type()
)
ubiSysTimeZoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysTimeZoneOffset.setStatus("current")
_UbiSysBanner_ObjectIdentity = ObjectIdentity
ubiSysBanner = _UbiSysBanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 9)
)
_UbiSysBannerLogin_Type = DisplayString
_UbiSysBannerLogin_Object = MibScalar
ubiSysBannerLogin = _UbiSysBannerLogin_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 9, 1),
    _UbiSysBannerLogin_Type()
)
ubiSysBannerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysBannerLogin.setStatus("current")
_UbiSysBannerMotd_Type = DisplayString
_UbiSysBannerMotd_Object = MibScalar
ubiSysBannerMotd = _UbiSysBannerMotd_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 9, 2),
    _UbiSysBannerMotd_Type()
)
ubiSysBannerMotd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiSysBannerMotd.setStatus("current")
_UbiShelfPhysAddress_Type = PhysAddress
_UbiShelfPhysAddress_Object = MibScalar
ubiShelfPhysAddress = _UbiShelfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 10),
    _UbiShelfPhysAddress_Type()
)
ubiShelfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiShelfPhysAddress.setStatus("mandatory")
_UbiBspVersion_Type = DisplayString
_UbiBspVersion_Object = MibScalar
ubiBspVersion = _UbiBspVersion_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 11),
    _UbiBspVersion_Type()
)
ubiBspVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiBspVersion.setStatus("mandatory")
_UbiSysResetReason_Type = DisplayString
_UbiSysResetReason_Object = MibScalar
ubiSysResetReason = _UbiSysResetReason_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 2, 12),
    _UbiSysResetReason_Type()
)
ubiSysResetReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ubiSysResetReason.setStatus("mandatory")
_UbiSysLedTest_ObjectIdentity = ObjectIdentity
ubiSysLedTest = _UbiSysLedTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 6)
)


class _UbiLedTestTimeout_Type(Integer32):
    """Custom type ubiLedTestTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_UbiLedTestTimeout_Type.__name__ = "Integer32"
_UbiLedTestTimeout_Object = MibScalar
ubiLedTestTimeout = _UbiLedTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 6, 1),
    _UbiLedTestTimeout_Type()
)
ubiLedTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLedTestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ubiLedTestTimeout.setUnits("seconds")


class _UbiLedTestTrigger_Type(Integer32):
    """Custom type ubiLedTestTrigger based on Integer32"""
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
          ("testing", 1),
          ("stop", 2))
    )


_UbiLedTestTrigger_Type.__name__ = "Integer32"
_UbiLedTestTrigger_Object = MibScalar
ubiLedTestTrigger = _UbiLedTestTrigger_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 6, 2),
    _UbiLedTestTrigger_Type()
)
ubiLedTestTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLedTestTrigger.setStatus("current")
_UbiLedTestSlotId_Type = Integer32
_UbiLedTestSlotId_Object = MibScalar
ubiLedTestSlotId = _UbiLedTestSlotId_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 6, 3),
    _UbiLedTestSlotId_Type()
)
ubiLedTestSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ubiLedTestSlotId.setStatus("current")
_UbiSysRedundancy_ObjectIdentity = ObjectIdentity
ubiSysRedundancy = _UbiSysRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 7)
)
_UbiSysRedundancyInfoTable_Object = MibTable
ubiSysRedundancyInfoTable = _UbiSysRedundancyInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ubiSysRedundancyInfoTable.setStatus("current")
_UbiSysRedundancyInfoEntry_Object = MibTableRow
ubiSysRedundancyInfoEntry = _UbiSysRedundancyInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 7, 1, 1)
)
ubiSysRedundancyInfoEntry.setIndexNames(
    (0, "UBQS-SYSTEM-MIB", "ubiSCURedundancyRole"),
)
if mibBuilder.loadTexts:
    ubiSysRedundancyInfoEntry.setStatus("current")


class _UbiSCURedundancyRole_Type(Integer32):
    """Custom type ubiSCURedundancyRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_UbiSCURedundancyRole_Type.__name__ = "Integer32"
_UbiSCURedundancyRole_Object = MibTableColumn
ubiSCURedundancyRole = _UbiSCURedundancyRole_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 7, 1, 1, 1),
    _UbiSCURedundancyRole_Type()
)
ubiSCURedundancyRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSCURedundancyRole.setStatus("current")


class _UbiSCUPosition_Type(Integer32):
    """Custom type ubiSCUPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("left", 1),
          ("right", 2))
    )


_UbiSCUPosition_Type.__name__ = "Integer32"
_UbiSCUPosition_Object = MibTableColumn
ubiSCUPosition = _UbiSCUPosition_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 7, 1, 1, 2),
    _UbiSCUPosition_Type()
)
ubiSCUPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSCUPosition.setStatus("current")


class _UbiSCUMngLinkStatus_Type(Integer32):
    """Custom type ubiSCUMngLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_UbiSCUMngLinkStatus_Type.__name__ = "Integer32"
_UbiSCUMngLinkStatus_Object = MibTableColumn
ubiSCUMngLinkStatus = _UbiSCUMngLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 7, 1, 1, 3),
    _UbiSCUMngLinkStatus_Type()
)
ubiSCUMngLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSCUMngLinkStatus.setStatus("current")
_UbiSCUIpAddress_Type = IpAddress
_UbiSCUIpAddress_Object = MibTableColumn
ubiSCUIpAddress = _UbiSCUIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 7, 1, 1, 4),
    _UbiSCUIpAddress_Type()
)
ubiSCUIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSCUIpAddress.setStatus("current")


class _UbiSCUPeerEquipStatus_Type(Integer32):
    """Custom type ubiSCUPeerEquipStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unequip", 0),
          ("equip", 1))
    )


_UbiSCUPeerEquipStatus_Type.__name__ = "Integer32"
_UbiSCUPeerEquipStatus_Object = MibTableColumn
ubiSCUPeerEquipStatus = _UbiSCUPeerEquipStatus_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 7, 1, 1, 5),
    _UbiSCUPeerEquipStatus_Type()
)
ubiSCUPeerEquipStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSCUPeerEquipStatus.setStatus("current")


class _UbiSysRedundancyReload_Type(Integer32):
    """Custom type ubiSysRedundancyReload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reload_peer", 1),
          ("reload_shelf", 2))
    )


_UbiSysRedundancyReload_Type.__name__ = "Integer32"
_UbiSysRedundancyReload_Object = MibScalar
ubiSysRedundancyReload = _UbiSysRedundancyReload_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 7, 2),
    _UbiSysRedundancyReload_Type()
)
ubiSysRedundancyReload.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ubiSysRedundancyReload.setStatus("current")
_UbiSysRedundancyPeerImage_Type = DisplayString
_UbiSysRedundancyPeerImage_Object = MibScalar
ubiSysRedundancyPeerImage = _UbiSysRedundancyPeerImage_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 7, 3),
    _UbiSysRedundancyPeerImage_Type()
)
ubiSysRedundancyPeerImage.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ubiSysRedundancyPeerImage.setStatus("current")
_UbiSysBarCode_ObjectIdentity = ObjectIdentity
ubiSysBarCode = _UbiSysBarCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8)
)
_UbiSysBarcodeSystem_ObjectIdentity = ObjectIdentity
ubiSysBarcodeSystem = _UbiSysBarcodeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 1)
)
_UbiSysBarcodeSystemString_Type = DisplayString
_UbiSysBarcodeSystemString_Object = MibScalar
ubiSysBarcodeSystemString = _UbiSysBarcodeSystemString_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 1, 1),
    _UbiSysBarcodeSystemString_Type()
)
ubiSysBarcodeSystemString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodeSystemString.setStatus("current")
_UbiSysBarcodePowerTable_Object = MibTable
ubiSysBarcodePowerTable = _UbiSysBarcodePowerTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    ubiSysBarcodePowerTable.setStatus("current")
_UbiSysBarcodePowerEntry_Object = MibTableRow
ubiSysBarcodePowerEntry = _UbiSysBarcodePowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 2, 1)
)
ubiSysBarcodePowerEntry.setIndexNames(
    (0, "UBQS-SYSTEM-MIB", "ubiSysBarcodePowerIndex"),
)
if mibBuilder.loadTexts:
    ubiSysBarcodePowerEntry.setStatus("current")
_UbiSysBarcodePowerIndex_Type = Integer32
_UbiSysBarcodePowerIndex_Object = MibTableColumn
ubiSysBarcodePowerIndex = _UbiSysBarcodePowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 2, 1, 1),
    _UbiSysBarcodePowerIndex_Type()
)
ubiSysBarcodePowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodePowerIndex.setStatus("current")
_UbiSysBarcodePowerString_Type = DisplayString
_UbiSysBarcodePowerString_Object = MibTableColumn
ubiSysBarcodePowerString = _UbiSysBarcodePowerString_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 2, 1, 2),
    _UbiSysBarcodePowerString_Type()
)
ubiSysBarcodePowerString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodePowerString.setStatus("current")
_UbiSysBarcodeFanTable_Object = MibTable
ubiSysBarcodeFanTable = _UbiSysBarcodeFanTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    ubiSysBarcodeFanTable.setStatus("current")
_UbiSysBarcodeFanEntry_Object = MibTableRow
ubiSysBarcodeFanEntry = _UbiSysBarcodeFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 3, 1)
)
ubiSysBarcodeFanEntry.setIndexNames(
    (0, "UBQS-SYSTEM-MIB", "ubiSysBarcodeFanIndex"),
)
if mibBuilder.loadTexts:
    ubiSysBarcodeFanEntry.setStatus("current")
_UbiSysBarcodeFanIndex_Type = Integer32
_UbiSysBarcodeFanIndex_Object = MibTableColumn
ubiSysBarcodeFanIndex = _UbiSysBarcodeFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 3, 1, 1),
    _UbiSysBarcodeFanIndex_Type()
)
ubiSysBarcodeFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodeFanIndex.setStatus("current")
_UbiSysBarcodeFanString_Type = DisplayString
_UbiSysBarcodeFanString_Object = MibTableColumn
ubiSysBarcodeFanString = _UbiSysBarcodeFanString_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 3, 1, 2),
    _UbiSysBarcodeFanString_Type()
)
ubiSysBarcodeFanString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodeFanString.setStatus("current")
_UbiSysBarcodeUplinkTable_Object = MibTable
ubiSysBarcodeUplinkTable = _UbiSysBarcodeUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 4)
)
if mibBuilder.loadTexts:
    ubiSysBarcodeUplinkTable.setStatus("current")
_UbiSysBarcodeUplinkEntry_Object = MibTableRow
ubiSysBarcodeUplinkEntry = _UbiSysBarcodeUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 4, 1)
)
ubiSysBarcodeUplinkEntry.setIndexNames(
    (0, "UBQS-SYSTEM-MIB", "ubiSysBarcodeUplinkIndex"),
)
if mibBuilder.loadTexts:
    ubiSysBarcodeUplinkEntry.setStatus("current")
_UbiSysBarcodeUplinkIndex_Type = Integer32
_UbiSysBarcodeUplinkIndex_Object = MibTableColumn
ubiSysBarcodeUplinkIndex = _UbiSysBarcodeUplinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 4, 1, 1),
    _UbiSysBarcodeUplinkIndex_Type()
)
ubiSysBarcodeUplinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodeUplinkIndex.setStatus("current")
_UbiSysBarcodeUplinkString_Type = DisplayString
_UbiSysBarcodeUplinkString_Object = MibTableColumn
ubiSysBarcodeUplinkString = _UbiSysBarcodeUplinkString_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 4, 1, 2),
    _UbiSysBarcodeUplinkString_Type()
)
ubiSysBarcodeUplinkString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodeUplinkString.setStatus("current")
_UbiSysBarcodeSlotTable_Object = MibTable
ubiSysBarcodeSlotTable = _UbiSysBarcodeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    ubiSysBarcodeSlotTable.setStatus("current")
_UbiSysBarcodeSlotEntry_Object = MibTableRow
ubiSysBarcodeSlotEntry = _UbiSysBarcodeSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 5, 1)
)
ubiSysBarcodeSlotEntry.setIndexNames(
    (0, "UBQS-SYSTEM-MIB", "ubiSysBarcodeSlotIndex"),
)
if mibBuilder.loadTexts:
    ubiSysBarcodeSlotEntry.setStatus("current")
_UbiSysBarcodeSlotIndex_Type = Integer32
_UbiSysBarcodeSlotIndex_Object = MibTableColumn
ubiSysBarcodeSlotIndex = _UbiSysBarcodeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 5, 1, 1),
    _UbiSysBarcodeSlotIndex_Type()
)
ubiSysBarcodeSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodeSlotIndex.setStatus("current")
_UbiSysBarcodeSlotString_Type = DisplayString
_UbiSysBarcodeSlotString_Object = MibTableColumn
ubiSysBarcodeSlotString = _UbiSysBarcodeSlotString_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 5, 1, 2),
    _UbiSysBarcodeSlotString_Type()
)
ubiSysBarcodeSlotString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodeSlotString.setStatus("current")
_UbiSysBarcodeScuTable_Object = MibTable
ubiSysBarcodeScuTable = _UbiSysBarcodeScuTable_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 6)
)
if mibBuilder.loadTexts:
    ubiSysBarcodeScuTable.setStatus("current")
_UbiSysBarcodeScuEntry_Object = MibTableRow
ubiSysBarcodeScuEntry = _UbiSysBarcodeScuEntry_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 6, 1)
)
ubiSysBarcodeScuEntry.setIndexNames(
    (0, "UBQS-SYSTEM-MIB", "ubiSysBarcodeScuIndex"),
)
if mibBuilder.loadTexts:
    ubiSysBarcodeScuEntry.setStatus("current")
_UbiSysBarcodeScuIndex_Type = Integer32
_UbiSysBarcodeScuIndex_Object = MibTableColumn
ubiSysBarcodeScuIndex = _UbiSysBarcodeScuIndex_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 6, 1, 1),
    _UbiSysBarcodeScuIndex_Type()
)
ubiSysBarcodeScuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodeScuIndex.setStatus("current")
_UbiSysBarcodeScuString_Type = DisplayString
_UbiSysBarcodeScuString_Object = MibTableColumn
ubiSysBarcodeScuString = _UbiSysBarcodeScuString_Object(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 1, 8, 6, 1, 2),
    _UbiSysBarcodeScuString_Type()
)
ubiSysBarcodeScuString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubiSysBarcodeScuString.setStatus("current")
_UbiSystemMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ubiSystemMIBNotificationPrefix = _UbiSystemMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 2)
)
_UbiSystemMIBConformance_ObjectIdentity = ObjectIdentity
ubiSystemMIBConformance = _UbiSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 3)
)
_UbiSysMIBCompliances_ObjectIdentity = ObjectIdentity
ubiSysMIBCompliances = _UbiSysMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 3, 1)
)
_UbiSysMIBGroups_ObjectIdentity = ObjectIdentity
ubiSysMIBGroups = _UbiSysMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 3, 2)
)

# Managed Objects groups

ubiSysInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 3, 2, 1)
)
ubiSysInfoMIBGroup.setObjects(
      *(("UBQS-SYSTEM-MIB", "ubiSystemModel"),
        ("UBQS-SYSTEM-MIB", "ubiSystemSerialNumber"),
        ("UBQS-SYSTEM-MIB", "ubiHwVersion"),
        ("UBQS-SYSTEM-MIB", "ubiSwVersion"),
        ("UBQS-SYSTEM-MIB", "ubiReleaseDate"),
        ("UBQS-SYSTEM-MIB", "ubiSerialNumber"),
        ("UBQS-SYSTEM-MIB", "ubiSysPhysAddress"),
        ("UBQS-SYSTEM-MIB", "ubiSysClock"),
        ("UBQS-SYSTEM-MIB", "ubiSysTimeZoneName"),
        ("UBQS-SYSTEM-MIB", "ubiSysTimeZoneOffset"))
)
if mibBuilder.loadTexts:
    ubiSysInfoMIBGroup.setStatus("current")

ubiSysRscMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 3, 2, 2)
)
ubiSysRscMIBGroup.setObjects(
      *(("UBQS-SYSTEM-MIB", "ubiCpuFiveSec"),
        ("UBQS-SYSTEM-MIB", "ubiCpuOneMin"),
        ("UBQS-SYSTEM-MIB", "ubiCpuFiveMin"),
        ("UBQS-SYSTEM-MIB", "ubiCpuRisingThreshold"),
        ("UBQS-SYSTEM-MIB", "ubiCpuFallingThreshold"),
        ("UBQS-SYSTEM-MIB", "ubiCpuLoadTimePeriod"),
        ("UBQS-SYSTEM-MIB", "ubiMemoryAlloc"),
        ("UBQS-SYSTEM-MIB", "ubiMemoryFree"),
        ("UBQS-SYSTEM-MIB", "ubiMemoryTotal"),
        ("UBQS-SYSTEM-MIB", "ubiMemoryFreePercentage"),
        ("UBQS-SYSTEM-MIB", "ubiMemoryThreshold"))
)
if mibBuilder.loadTexts:
    ubiSysRscMIBGroup.setStatus("current")

ubiSysMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 3, 2, 3)
)
ubiSysMiscGroup.setObjects(
    ("UBQS-SYSTEM-MIB", "ubiLedTestTrigger")
)
if mibBuilder.loadTexts:
    ubiSysMiscGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ubiSysMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7800, 100, 1, 3, 1, 1)
)
ubiSysMIBCompliance.setObjects(
      *(("UBQS-SYSTEM-MIB", "ubiSysInfoMIBGroup"),
        ("UBQS-SYSTEM-MIB", "ubiSysRscMIBGroup"),
        ("UBQS-SYSTEM-MIB", "ubiSysBannerGroup"),
        ("UBQS-SYSTEM-MIB", "ubiSysInfoMIBGroup"),
        ("UBQS-SYSTEM-MIB", "ubiSysRscMIBGroup"),
        ("UBQS-SYSTEM-MIB", "ubiSysBannerGroup"))
)
if mibBuilder.loadTexts:
    ubiSysMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBQS-SYSTEM-MIB",
    **{"ubiSystemMIB": ubiSystemMIB,
       "ubiSystemMIBObjects": ubiSystemMIBObjects,
       "ubiSysReset": ubiSysReset,
       "ubiSysInfo": ubiSysInfo,
       "ubiSysModel": ubiSysModel,
       "ubiHwVersion": ubiHwVersion,
       "ubiSwVersion": ubiSwVersion,
       "ubiReleaseDate": ubiReleaseDate,
       "ubiSerialNumber": ubiSerialNumber,
       "ubiSysPhysAddress": ubiSysPhysAddress,
       "ubiSysClock": ubiSysClock,
       "ubiSysTimeZone": ubiSysTimeZone,
       "ubiSysTimeZoneName": ubiSysTimeZoneName,
       "ubiSysTimeZoneOffset": ubiSysTimeZoneOffset,
       "ubiSysBanner": ubiSysBanner,
       "ubiSysBannerLogin": ubiSysBannerLogin,
       "ubiSysBannerMotd": ubiSysBannerMotd,
       "ubiShelfPhysAddress": ubiShelfPhysAddress,
       "ubiBspVersion": ubiBspVersion,
       "ubiSysResetReason": ubiSysResetReason,
       "ubiSysLedTest": ubiSysLedTest,
       "ubiLedTestTimeout": ubiLedTestTimeout,
       "ubiLedTestTrigger": ubiLedTestTrigger,
       "ubiLedTestSlotId": ubiLedTestSlotId,
       "ubiSysRedundancy": ubiSysRedundancy,
       "ubiSysRedundancyInfoTable": ubiSysRedundancyInfoTable,
       "ubiSysRedundancyInfoEntry": ubiSysRedundancyInfoEntry,
       "ubiSCURedundancyRole": ubiSCURedundancyRole,
       "ubiSCUPosition": ubiSCUPosition,
       "ubiSCUMngLinkStatus": ubiSCUMngLinkStatus,
       "ubiSCUIpAddress": ubiSCUIpAddress,
       "ubiSCUPeerEquipStatus": ubiSCUPeerEquipStatus,
       "ubiSysRedundancyReload": ubiSysRedundancyReload,
       "ubiSysRedundancyPeerImage": ubiSysRedundancyPeerImage,
       "ubiSysBarCode": ubiSysBarCode,
       "ubiSysBarcodeSystem": ubiSysBarcodeSystem,
       "ubiSysBarcodeSystemString": ubiSysBarcodeSystemString,
       "ubiSysBarcodePowerTable": ubiSysBarcodePowerTable,
       "ubiSysBarcodePowerEntry": ubiSysBarcodePowerEntry,
       "ubiSysBarcodePowerIndex": ubiSysBarcodePowerIndex,
       "ubiSysBarcodePowerString": ubiSysBarcodePowerString,
       "ubiSysBarcodeFanTable": ubiSysBarcodeFanTable,
       "ubiSysBarcodeFanEntry": ubiSysBarcodeFanEntry,
       "ubiSysBarcodeFanIndex": ubiSysBarcodeFanIndex,
       "ubiSysBarcodeFanString": ubiSysBarcodeFanString,
       "ubiSysBarcodeUplinkTable": ubiSysBarcodeUplinkTable,
       "ubiSysBarcodeUplinkEntry": ubiSysBarcodeUplinkEntry,
       "ubiSysBarcodeUplinkIndex": ubiSysBarcodeUplinkIndex,
       "ubiSysBarcodeUplinkString": ubiSysBarcodeUplinkString,
       "ubiSysBarcodeSlotTable": ubiSysBarcodeSlotTable,
       "ubiSysBarcodeSlotEntry": ubiSysBarcodeSlotEntry,
       "ubiSysBarcodeSlotIndex": ubiSysBarcodeSlotIndex,
       "ubiSysBarcodeSlotString": ubiSysBarcodeSlotString,
       "ubiSysBarcodeScuTable": ubiSysBarcodeScuTable,
       "ubiSysBarcodeScuEntry": ubiSysBarcodeScuEntry,
       "ubiSysBarcodeScuIndex": ubiSysBarcodeScuIndex,
       "ubiSysBarcodeScuString": ubiSysBarcodeScuString,
       "ubiSystemMIBNotificationPrefix": ubiSystemMIBNotificationPrefix,
       "ubiSystemMIBConformance": ubiSystemMIBConformance,
       "ubiSysMIBCompliances": ubiSysMIBCompliances,
       "ubiSysMIBCompliance": ubiSysMIBCompliance,
       "ubiSysMIBGroups": ubiSysMIBGroups,
       "ubiSysInfoMIBGroup": ubiSysInfoMIBGroup,
       "ubiSysRscMIBGroup": ubiSysRscMIBGroup,
       "ubiSysMiscGroup": ubiSysMiscGroup}
)
