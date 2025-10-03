# SNMP MIB module (DRAGONWAVE-HCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dragonwave\DRAGONWAVE-HCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:26 2025
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

(horizonEquipmentOutTrapsCounter,) = mibBuilder.importSymbols(
    "HORIZON-EQUIPMENT-LOG-MIB",
    "horizonEquipmentOutTrapsCounter")

(horizon,) = mibBuilder.importSymbols(
    "HORIZON-MIB",
    "horizon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hzCpModIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1000)
)
if mibBuilder.loadTexts:
    hzCpModIdentity.setRevisions(
        ("2013-01-17 11:09",
         "2014-03-28 10:28",
         "2014-11-24 17:12",
         "2015-12-10 17:12")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HorizonCompactPlus_ObjectIdentity = ObjectIdentity
horizonCompactPlus = _HorizonCompactPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5)
)
_HzCpSystem_ObjectIdentity = ObjectIdentity
hzCpSystem = _HzCpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1)
)
_HzCpSysGeneral_ObjectIdentity = ObjectIdentity
hzCpSysGeneral = _HzCpSysGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 1)
)


class _HzCpResetSystem_Type(Integer32):
    """Custom type hzCpResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HzCpResetSystem_Type.__name__ = "Integer32"
_HzCpResetSystem_Object = MibScalar
hzCpResetSystem = _HzCpResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 1, 1),
    _HzCpResetSystem_Type()
)
hzCpResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpResetSystem.setStatus("current")


class _HzCpSaveMIB_Type(Integer32):
    """Custom type hzCpSaveMIB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_HzCpSaveMIB_Type.__name__ = "Integer32"
_HzCpSaveMIB_Object = MibScalar
hzCpSaveMIB = _HzCpSaveMIB_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 1, 2),
    _HzCpSaveMIB_Type()
)
hzCpSaveMIB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSaveMIB.setStatus("current")


class _HzCpOperStatus_Type(Integer32):
    """Custom type hzCpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_HzCpOperStatus_Type.__name__ = "Integer32"
_HzCpOperStatus_Object = MibScalar
hzCpOperStatus = _HzCpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 1, 3),
    _HzCpOperStatus_Type()
)
hzCpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpOperStatus.setStatus("current")
_HzCpSysSpeed_ObjectIdentity = ObjectIdentity
hzCpSysSpeed = _HzCpSysSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2)
)


class _HzCpSystemCurrentSpeed_Type(Integer32):
    """Custom type hzCpSystemCurrentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HzCpSystemCurrentSpeed_Type.__name__ = "Integer32"
_HzCpSystemCurrentSpeed_Object = MibScalar
hzCpSystemCurrentSpeed = _HzCpSystemCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2, 1),
    _HzCpSystemCurrentSpeed_Type()
)
hzCpSystemCurrentSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSystemCurrentSpeed.setStatus("current")


class _HzCpSystemLicensedSpeed_Type(Integer32):
    """Custom type hzCpSystemLicensedSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HzCpSystemLicensedSpeed_Type.__name__ = "Integer32"
_HzCpSystemLicensedSpeed_Object = MibScalar
hzCpSystemLicensedSpeed = _HzCpSystemLicensedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2, 2),
    _HzCpSystemLicensedSpeed_Type()
)
hzCpSystemLicensedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSystemLicensedSpeed.setStatus("current")
_HzCpSysUpgradeSpeed_ObjectIdentity = ObjectIdentity
hzCpSysUpgradeSpeed = _HzCpSysUpgradeSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2, 3)
)
_HzCpLicensedSpeedUpgradeSpeedAndKey_Type = DisplayString
_HzCpLicensedSpeedUpgradeSpeedAndKey_Object = MibScalar
hzCpLicensedSpeedUpgradeSpeedAndKey = _HzCpLicensedSpeedUpgradeSpeedAndKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2, 3, 1),
    _HzCpLicensedSpeedUpgradeSpeedAndKey_Type()
)
hzCpLicensedSpeedUpgradeSpeedAndKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpLicensedSpeedUpgradeSpeedAndKey.setStatus("current")
_HzCpLicensedSpeedCount_Type = Integer32
_HzCpLicensedSpeedCount_Object = MibScalar
hzCpLicensedSpeedCount = _HzCpLicensedSpeedCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2, 3, 2),
    _HzCpLicensedSpeedCount_Type()
)
hzCpLicensedSpeedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpLicensedSpeedCount.setStatus("current")
_HzCpSysDowngradeSpeed_ObjectIdentity = ObjectIdentity
hzCpSysDowngradeSpeed = _HzCpSysDowngradeSpeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2, 4)
)
_HzCpLicensedSpeedDowngradeSpeed_Type = Integer32
_HzCpLicensedSpeedDowngradeSpeed_Object = MibScalar
hzCpLicensedSpeedDowngradeSpeed = _HzCpLicensedSpeedDowngradeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2, 4, 1),
    _HzCpLicensedSpeedDowngradeSpeed_Type()
)
hzCpLicensedSpeedDowngradeSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpLicensedSpeedDowngradeSpeed.setStatus("current")
_HzCpLicensedSpeedCountUsedForKey_Type = Integer32
_HzCpLicensedSpeedCountUsedForKey_Object = MibScalar
hzCpLicensedSpeedCountUsedForKey = _HzCpLicensedSpeedCountUsedForKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2, 4, 2),
    _HzCpLicensedSpeedCountUsedForKey_Type()
)
hzCpLicensedSpeedCountUsedForKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpLicensedSpeedCountUsedForKey.setStatus("current")
_HzCpLicensedSpeedConfirmationKey_Type = DisplayString
_HzCpLicensedSpeedConfirmationKey_Object = MibScalar
hzCpLicensedSpeedConfirmationKey = _HzCpLicensedSpeedConfirmationKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2, 4, 3),
    _HzCpLicensedSpeedConfirmationKey_Type()
)
hzCpLicensedSpeedConfirmationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpLicensedSpeedConfirmationKey.setStatus("current")
_HzCpSysDowngradeSpeedDecrement_Type = Integer32
_HzCpSysDowngradeSpeedDecrement_Object = MibScalar
hzCpSysDowngradeSpeedDecrement = _HzCpSysDowngradeSpeedDecrement_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 2, 4, 4),
    _HzCpSysDowngradeSpeedDecrement_Type()
)
hzCpSysDowngradeSpeedDecrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSysDowngradeSpeedDecrement.setStatus("current")
_HzCpInventory_ObjectIdentity = ObjectIdentity
hzCpInventory = _HzCpInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3)
)
_HzCpHwInventory_ObjectIdentity = ObjectIdentity
hzCpHwInventory = _HzCpHwInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1)
)
_HzCpFrequencyFilePartNumber_Type = DisplayString
_HzCpFrequencyFilePartNumber_Object = MibScalar
hzCpFrequencyFilePartNumber = _HzCpFrequencyFilePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 1),
    _HzCpFrequencyFilePartNumber_Type()
)
hzCpFrequencyFilePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpFrequencyFilePartNumber.setStatus("current")
_HzCpUnitSerialNo_Type = DisplayString
_HzCpUnitSerialNo_Object = MibScalar
hzCpUnitSerialNo = _HzCpUnitSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 2),
    _HzCpUnitSerialNo_Type()
)
hzCpUnitSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpUnitSerialNo.setStatus("current")
_HzCpUnitAssemblyNo_Type = DisplayString
_HzCpUnitAssemblyNo_Object = MibScalar
hzCpUnitAssemblyNo = _HzCpUnitAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 3),
    _HzCpUnitAssemblyNo_Type()
)
hzCpUnitAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpUnitAssemblyNo.setStatus("current")
_HzCpModemSerialNo_Type = DisplayString
_HzCpModemSerialNo_Object = MibScalar
hzCpModemSerialNo = _HzCpModemSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 4),
    _HzCpModemSerialNo_Type()
)
hzCpModemSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemSerialNo.setStatus("current")
_HzCpModemAssemblyNo_Type = DisplayString
_HzCpModemAssemblyNo_Object = MibScalar
hzCpModemAssemblyNo = _HzCpModemAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 5),
    _HzCpModemAssemblyNo_Type()
)
hzCpModemAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemAssemblyNo.setStatus("current")
_HzCpPsuSerialNo_Type = DisplayString
_HzCpPsuSerialNo_Object = MibScalar
hzCpPsuSerialNo = _HzCpPsuSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 6),
    _HzCpPsuSerialNo_Type()
)
hzCpPsuSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPsuSerialNo.setStatus("current")
_HzCpPsuAssemblyNo_Type = DisplayString
_HzCpPsuAssemblyNo_Object = MibScalar
hzCpPsuAssemblyNo = _HzCpPsuAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 7),
    _HzCpPsuAssemblyNo_Type()
)
hzCpPsuAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPsuAssemblyNo.setStatus("current")
_HzCpRfSerialNo_Type = DisplayString
_HzCpRfSerialNo_Object = MibScalar
hzCpRfSerialNo = _HzCpRfSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 8),
    _HzCpRfSerialNo_Type()
)
hzCpRfSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRfSerialNo.setStatus("current")
_HzCpRfAssemblyNo_Type = DisplayString
_HzCpRfAssemblyNo_Object = MibScalar
hzCpRfAssemblyNo = _HzCpRfAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 9),
    _HzCpRfAssemblyNo_Type()
)
hzCpRfAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRfAssemblyNo.setStatus("current")
_HzCpDiplexerSerialNo_Type = DisplayString
_HzCpDiplexerSerialNo_Object = MibScalar
hzCpDiplexerSerialNo = _HzCpDiplexerSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 10),
    _HzCpDiplexerSerialNo_Type()
)
hzCpDiplexerSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpDiplexerSerialNo.setStatus("current")
_HzCpDiplexerAssemblyNo_Type = DisplayString
_HzCpDiplexerAssemblyNo_Object = MibScalar
hzCpDiplexerAssemblyNo = _HzCpDiplexerAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 11),
    _HzCpDiplexerAssemblyNo_Type()
)
hzCpDiplexerAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpDiplexerAssemblyNo.setStatus("current")
_HzCpSystemCleiNo_Type = DisplayString
_HzCpSystemCleiNo_Object = MibScalar
hzCpSystemCleiNo = _HzCpSystemCleiNo_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 1, 12),
    _HzCpSystemCleiNo_Type()
)
hzCpSystemCleiNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSystemCleiNo.setStatus("current")
_HzCpSwInventory_ObjectIdentity = ObjectIdentity
hzCpSwInventory = _HzCpSwInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 2)
)
_HzCpSwInventoryTable_Object = MibTable
hzCpSwInventoryTable = _HzCpSwInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hzCpSwInventoryTable.setStatus("current")
_HzCpSwInventoryEntry_Object = MibTableRow
hzCpSwInventoryEntry = _HzCpSwInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 2, 1, 1)
)
hzCpSwInventoryEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSwInvBank"),
)
if mibBuilder.loadTexts:
    hzCpSwInventoryEntry.setStatus("current")


class _HzCpSwInvBank_Type(Integer32):
    """Custom type hzCpSwInvBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bank-A", 1),
          ("bank-B", 2))
    )


_HzCpSwInvBank_Type.__name__ = "Integer32"
_HzCpSwInvBank_Object = MibTableColumn
hzCpSwInvBank = _HzCpSwInvBank_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 2, 1, 1, 1),
    _HzCpSwInvBank_Type()
)
hzCpSwInvBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSwInvBank.setStatus("current")


class _HzCpSwInvStatus_Type(Integer32):
    """Custom type hzCpSwInvStatus based on Integer32"""
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


_HzCpSwInvStatus_Type.__name__ = "Integer32"
_HzCpSwInvStatus_Object = MibTableColumn
hzCpSwInvStatus = _HzCpSwInvStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 2, 1, 1, 2),
    _HzCpSwInvStatus_Type()
)
hzCpSwInvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSwInvStatus.setStatus("current")
_HzCpSwInvOmniRelease_Type = DisplayString
_HzCpSwInvOmniRelease_Object = MibTableColumn
hzCpSwInvOmniRelease = _HzCpSwInvOmniRelease_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 2, 1, 1, 3),
    _HzCpSwInvOmniRelease_Type()
)
hzCpSwInvOmniRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSwInvOmniRelease.setStatus("current")
_HzCpSwInvFrequencyFileVersion_Type = DisplayString
_HzCpSwInvFrequencyFileVersion_Object = MibTableColumn
hzCpSwInvFrequencyFileVersion = _HzCpSwInvFrequencyFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 2, 1, 1, 4),
    _HzCpSwInvFrequencyFileVersion_Type()
)
hzCpSwInvFrequencyFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSwInvFrequencyFileVersion.setStatus("current")
_HzCpSwInvMibVersion_Type = DisplayString
_HzCpSwInvMibVersion_Object = MibTableColumn
hzCpSwInvMibVersion = _HzCpSwInvMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 2, 1, 1, 5),
    _HzCpSwInvMibVersion_Type()
)
hzCpSwInvMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSwInvMibVersion.setStatus("current")
_HzCpSwInvBootloaderVersion_Type = DisplayString
_HzCpSwInvBootloaderVersion_Object = MibTableColumn
hzCpSwInvBootloaderVersion = _HzCpSwInvBootloaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 3, 2, 1, 1, 6),
    _HzCpSwInvBootloaderVersion_Type()
)
hzCpSwInvBootloaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSwInvBootloaderVersion.setStatus("current")
_HzCpPeerSysInfo_ObjectIdentity = ObjectIdentity
hzCpPeerSysInfo = _HzCpPeerSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 4)
)
_HzCpPeerMacAddress_Type = DisplayString
_HzCpPeerMacAddress_Object = MibScalar
hzCpPeerMacAddress = _HzCpPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 4, 1),
    _HzCpPeerMacAddress_Type()
)
hzCpPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerMacAddress.setStatus("current")
_HzCpPeerIpAddress_Type = IpAddress
_HzCpPeerIpAddress_Object = MibScalar
hzCpPeerIpAddress = _HzCpPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 4, 2),
    _HzCpPeerIpAddress_Type()
)
hzCpPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerIpAddress.setStatus("current")
_HzCpPeerSubnetMask_Type = IpAddress
_HzCpPeerSubnetMask_Object = MibScalar
hzCpPeerSubnetMask = _HzCpPeerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 4, 3),
    _HzCpPeerSubnetMask_Type()
)
hzCpPeerSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerSubnetMask.setStatus("current")
_HzCpPeerDefaultGateway_Type = IpAddress
_HzCpPeerDefaultGateway_Object = MibScalar
hzCpPeerDefaultGateway = _HzCpPeerDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 4, 4),
    _HzCpPeerDefaultGateway_Type()
)
hzCpPeerDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerDefaultGateway.setStatus("current")
_HzCpPeerIpv6Prefix_Type = Integer32
_HzCpPeerIpv6Prefix_Object = MibScalar
hzCpPeerIpv6Prefix = _HzCpPeerIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 4, 5),
    _HzCpPeerIpv6Prefix_Type()
)
hzCpPeerIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerIpv6Prefix.setStatus("current")
_HzCpPeerIpv6Domain_Type = InetAddressType
_HzCpPeerIpv6Domain_Object = MibScalar
hzCpPeerIpv6Domain = _HzCpPeerIpv6Domain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 4, 6),
    _HzCpPeerIpv6Domain_Type()
)
hzCpPeerIpv6Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerIpv6Domain.setStatus("current")
_HzCpPeerIpv6Address_Type = InetAddress
_HzCpPeerIpv6Address_Object = MibScalar
hzCpPeerIpv6Address = _HzCpPeerIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 4, 7),
    _HzCpPeerIpv6Address_Type()
)
hzCpPeerIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerIpv6Address.setStatus("current")
_HzCpPeerIpv6GatewayDomain_Type = InetAddressType
_HzCpPeerIpv6GatewayDomain_Object = MibScalar
hzCpPeerIpv6GatewayDomain = _HzCpPeerIpv6GatewayDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 4, 8),
    _HzCpPeerIpv6GatewayDomain_Type()
)
hzCpPeerIpv6GatewayDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerIpv6GatewayDomain.setStatus("current")
_HzCpPeerIpv6GatewayAddress_Type = InetAddress
_HzCpPeerIpv6GatewayAddress_Object = MibScalar
hzCpPeerIpv6GatewayAddress = _HzCpPeerIpv6GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 4, 9),
    _HzCpPeerIpv6GatewayAddress_Type()
)
hzCpPeerIpv6GatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerIpv6GatewayAddress.setStatus("current")
_HzCpSysRedundancy_ObjectIdentity = ObjectIdentity
hzCpSysRedundancy = _HzCpSysRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5)
)


class _HzCpRedundancyMode_Type(Integer32):
    """Custom type hzCpRedundancyMode based on Integer32"""
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
        *(("off", 1),
          ("primary-hsb", 2),
          ("secondary-hsb", 3),
          ("primary-x2", 4),
          ("secondary-x2", 5))
    )


_HzCpRedundancyMode_Type.__name__ = "Integer32"
_HzCpRedundancyMode_Object = MibScalar
hzCpRedundancyMode = _HzCpRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 1),
    _HzCpRedundancyMode_Type()
)
hzCpRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyMode.setStatus("current")


class _HzCpRedundancySwitchMode_Type(Integer32):
    """Custom type hzCpRedundancySwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("force-active", 2),
          ("force-standby", 3))
    )


_HzCpRedundancySwitchMode_Type.__name__ = "Integer32"
_HzCpRedundancySwitchMode_Object = MibScalar
hzCpRedundancySwitchMode = _HzCpRedundancySwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 2),
    _HzCpRedundancySwitchMode_Type()
)
hzCpRedundancySwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancySwitchMode.setStatus("current")


class _HzCpRedundancyStandbyEnetState_Type(Integer32):
    """Custom type hzCpRedundancyStandbyEnetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("pulse", 3))
    )


_HzCpRedundancyStandbyEnetState_Type.__name__ = "Integer32"
_HzCpRedundancyStandbyEnetState_Object = MibScalar
hzCpRedundancyStandbyEnetState = _HzCpRedundancyStandbyEnetState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 3),
    _HzCpRedundancyStandbyEnetState_Type()
)
hzCpRedundancyStandbyEnetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyStandbyEnetState.setStatus("current")


class _HzCpRedundancyStateSwitch_Type(Integer32):
    """Custom type hzCpRedundancyStateSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_HzCpRedundancyStateSwitch_Type.__name__ = "Integer32"
_HzCpRedundancyStateSwitch_Object = MibScalar
hzCpRedundancyStateSwitch = _HzCpRedundancyStateSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 4),
    _HzCpRedundancyStateSwitch_Type()
)
hzCpRedundancyStateSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyStateSwitch.setStatus("current")


class _HzCpRedundancyMgmtSource_Type(Integer32):
    """Custom type hzCpRedundancyMgmtSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local-node", 1),
          ("active-node", 2),
          ("standby-node", 3))
    )


_HzCpRedundancyMgmtSource_Type.__name__ = "Integer32"
_HzCpRedundancyMgmtSource_Object = MibScalar
hzCpRedundancyMgmtSource = _HzCpRedundancyMgmtSource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 5),
    _HzCpRedundancyMgmtSource_Type()
)
hzCpRedundancyMgmtSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyMgmtSource.setStatus("current")
_HzCpRedundancyLinkSwitchParameters_ObjectIdentity = ObjectIdentity
hzCpRedundancyLinkSwitchParameters = _HzCpRedundancyLinkSwitchParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 6)
)
_HzCpRedundancyPrimaryTimeInActiveState_Type = Unsigned32
_HzCpRedundancyPrimaryTimeInActiveState_Object = MibScalar
hzCpRedundancyPrimaryTimeInActiveState = _HzCpRedundancyPrimaryTimeInActiveState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 6, 1),
    _HzCpRedundancyPrimaryTimeInActiveState_Type()
)
hzCpRedundancyPrimaryTimeInActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyPrimaryTimeInActiveState.setStatus("current")
_HzCpRedundancyPrimarySwitchErrorThreshold_Type = Unsigned32
_HzCpRedundancyPrimarySwitchErrorThreshold_Object = MibScalar
hzCpRedundancyPrimarySwitchErrorThreshold = _HzCpRedundancyPrimarySwitchErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 6, 2),
    _HzCpRedundancyPrimarySwitchErrorThreshold_Type()
)
hzCpRedundancyPrimarySwitchErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyPrimarySwitchErrorThreshold.setStatus("current")
_HzCpRedundancySecondaryTimeInActiveState_Type = Unsigned32
_HzCpRedundancySecondaryTimeInActiveState_Object = MibScalar
hzCpRedundancySecondaryTimeInActiveState = _HzCpRedundancySecondaryTimeInActiveState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 6, 3),
    _HzCpRedundancySecondaryTimeInActiveState_Type()
)
hzCpRedundancySecondaryTimeInActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancySecondaryTimeInActiveState.setStatus("current")
_HzCpRedundancySecondarySwitchErrorThreshold_Type = Unsigned32
_HzCpRedundancySecondarySwitchErrorThreshold_Object = MibScalar
hzCpRedundancySecondarySwitchErrorThreshold = _HzCpRedundancySecondarySwitchErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 6, 4),
    _HzCpRedundancySecondarySwitchErrorThreshold_Type()
)
hzCpRedundancySecondarySwitchErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancySecondarySwitchErrorThreshold.setStatus("current")
_HzCpRedundancyLinkMonitorParameters_ObjectIdentity = ObjectIdentity
hzCpRedundancyLinkMonitorParameters = _HzCpRedundancyLinkMonitorParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 7)
)
_HzCpRedundancyFaultPeriod_Type = Unsigned32
_HzCpRedundancyFaultPeriod_Object = MibScalar
hzCpRedundancyFaultPeriod = _HzCpRedundancyFaultPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 7, 1),
    _HzCpRedundancyFaultPeriod_Type()
)
hzCpRedundancyFaultPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyFaultPeriod.setStatus("current")
_HzCpRedundancyFaultThreshold_Type = Unsigned32
_HzCpRedundancyFaultThreshold_Object = MibScalar
hzCpRedundancyFaultThreshold = _HzCpRedundancyFaultThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 7, 2),
    _HzCpRedundancyFaultThreshold_Type()
)
hzCpRedundancyFaultThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyFaultThreshold.setStatus("current")
_HzCpPartnerSysInfo_ObjectIdentity = ObjectIdentity
hzCpPartnerSysInfo = _HzCpPartnerSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 8)
)
_HzCpPartnerMacAddress_Type = DisplayString
_HzCpPartnerMacAddress_Object = MibScalar
hzCpPartnerMacAddress = _HzCpPartnerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 8, 1),
    _HzCpPartnerMacAddress_Type()
)
hzCpPartnerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPartnerMacAddress.setStatus("current")
_HzCpPartnerIpAddress_Type = IpAddress
_HzCpPartnerIpAddress_Object = MibScalar
hzCpPartnerIpAddress = _HzCpPartnerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 8, 2),
    _HzCpPartnerIpAddress_Type()
)
hzCpPartnerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPartnerIpAddress.setStatus("current")
_HzCpPartnerSubnetMask_Type = IpAddress
_HzCpPartnerSubnetMask_Object = MibScalar
hzCpPartnerSubnetMask = _HzCpPartnerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 8, 3),
    _HzCpPartnerSubnetMask_Type()
)
hzCpPartnerSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPartnerSubnetMask.setStatus("current")
_HzCpPartnerDefaultGateway_Type = IpAddress
_HzCpPartnerDefaultGateway_Object = MibScalar
hzCpPartnerDefaultGateway = _HzCpPartnerDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 8, 4),
    _HzCpPartnerDefaultGateway_Type()
)
hzCpPartnerDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPartnerDefaultGateway.setStatus("current")
_HzCpPartnerIpv6Prefix_Type = Integer32
_HzCpPartnerIpv6Prefix_Object = MibScalar
hzCpPartnerIpv6Prefix = _HzCpPartnerIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 8, 5),
    _HzCpPartnerIpv6Prefix_Type()
)
hzCpPartnerIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPartnerIpv6Prefix.setStatus("current")
_HzCpPartnerIpv6Domain_Type = InetAddressType
_HzCpPartnerIpv6Domain_Object = MibScalar
hzCpPartnerIpv6Domain = _HzCpPartnerIpv6Domain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 8, 6),
    _HzCpPartnerIpv6Domain_Type()
)
hzCpPartnerIpv6Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPartnerIpv6Domain.setStatus("current")
_HzCpPartnerIpv6Address_Type = InetAddress
_HzCpPartnerIpv6Address_Object = MibScalar
hzCpPartnerIpv6Address = _HzCpPartnerIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 8, 7),
    _HzCpPartnerIpv6Address_Type()
)
hzCpPartnerIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPartnerIpv6Address.setStatus("current")
_HzCpPartnerIpv6GatewayDomain_Type = InetAddressType
_HzCpPartnerIpv6GatewayDomain_Object = MibScalar
hzCpPartnerIpv6GatewayDomain = _HzCpPartnerIpv6GatewayDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 8, 8),
    _HzCpPartnerIpv6GatewayDomain_Type()
)
hzCpPartnerIpv6GatewayDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPartnerIpv6GatewayDomain.setStatus("current")
_HzCpPartnerIpv6GatewayAddress_Type = InetAddress
_HzCpPartnerIpv6GatewayAddress_Object = MibScalar
hzCpPartnerIpv6GatewayAddress = _HzCpPartnerIpv6GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 8, 9),
    _HzCpPartnerIpv6GatewayAddress_Type()
)
hzCpPartnerIpv6GatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPartnerIpv6GatewayAddress.setStatus("current")
_HzCpPeerPartnerSysInfo_ObjectIdentity = ObjectIdentity
hzCpPeerPartnerSysInfo = _HzCpPeerPartnerSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 9)
)
_HzCpPeerPartnerMacAddress_Type = DisplayString
_HzCpPeerPartnerMacAddress_Object = MibScalar
hzCpPeerPartnerMacAddress = _HzCpPeerPartnerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 9, 1),
    _HzCpPeerPartnerMacAddress_Type()
)
hzCpPeerPartnerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerPartnerMacAddress.setStatus("current")
_HzCpPeerPartnerIpAddress_Type = IpAddress
_HzCpPeerPartnerIpAddress_Object = MibScalar
hzCpPeerPartnerIpAddress = _HzCpPeerPartnerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 9, 2),
    _HzCpPeerPartnerIpAddress_Type()
)
hzCpPeerPartnerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerPartnerIpAddress.setStatus("current")
_HzCpPeerPartnerSubnetMask_Type = IpAddress
_HzCpPeerPartnerSubnetMask_Object = MibScalar
hzCpPeerPartnerSubnetMask = _HzCpPeerPartnerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 9, 3),
    _HzCpPeerPartnerSubnetMask_Type()
)
hzCpPeerPartnerSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerPartnerSubnetMask.setStatus("current")
_HzCpPeerPartnerDefaultGateway_Type = IpAddress
_HzCpPeerPartnerDefaultGateway_Object = MibScalar
hzCpPeerPartnerDefaultGateway = _HzCpPeerPartnerDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 9, 4),
    _HzCpPeerPartnerDefaultGateway_Type()
)
hzCpPeerPartnerDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerPartnerDefaultGateway.setStatus("current")
_HzCpPeerPartnerIpv6Prefix_Type = Integer32
_HzCpPeerPartnerIpv6Prefix_Object = MibScalar
hzCpPeerPartnerIpv6Prefix = _HzCpPeerPartnerIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 9, 5),
    _HzCpPeerPartnerIpv6Prefix_Type()
)
hzCpPeerPartnerIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerPartnerIpv6Prefix.setStatus("current")
_HzCpPeerPartnerIpv6Domain_Type = InetAddressType
_HzCpPeerPartnerIpv6Domain_Object = MibScalar
hzCpPeerPartnerIpv6Domain = _HzCpPeerPartnerIpv6Domain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 9, 6),
    _HzCpPeerPartnerIpv6Domain_Type()
)
hzCpPeerPartnerIpv6Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerPartnerIpv6Domain.setStatus("current")
_HzCpPeerPartnerIpv6Address_Type = InetAddress
_HzCpPeerPartnerIpv6Address_Object = MibScalar
hzCpPeerPartnerIpv6Address = _HzCpPeerPartnerIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 9, 7),
    _HzCpPeerPartnerIpv6Address_Type()
)
hzCpPeerPartnerIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerPartnerIpv6Address.setStatus("current")
_HzCpPeerPartnerIpv6GatewayDomain_Type = InetAddressType
_HzCpPeerPartnerIpv6GatewayDomain_Object = MibScalar
hzCpPeerPartnerIpv6GatewayDomain = _HzCpPeerPartnerIpv6GatewayDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 9, 8),
    _HzCpPeerPartnerIpv6GatewayDomain_Type()
)
hzCpPeerPartnerIpv6GatewayDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerPartnerIpv6GatewayDomain.setStatus("current")
_HzCpPeerPartnerIpv6GatewayAddress_Type = InetAddress
_HzCpPeerPartnerIpv6GatewayAddress_Object = MibScalar
hzCpPeerPartnerIpv6GatewayAddress = _HzCpPeerPartnerIpv6GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 9, 9),
    _HzCpPeerPartnerIpv6GatewayAddress_Type()
)
hzCpPeerPartnerIpv6GatewayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerPartnerIpv6GatewayAddress.setStatus("current")
_HzCpPartnerCommunication_ObjectIdentity = ObjectIdentity
hzCpPartnerCommunication = _HzCpPartnerCommunication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 10)
)


class _HzCpPartnerAutoDiscovery_Type(Integer32):
    """Custom type hzCpPartnerAutoDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpPartnerAutoDiscovery_Type.__name__ = "Integer32"
_HzCpPartnerAutoDiscovery_Object = MibScalar
hzCpPartnerAutoDiscovery = _HzCpPartnerAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 10, 1),
    _HzCpPartnerAutoDiscovery_Type()
)
hzCpPartnerAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPartnerAutoDiscovery.setStatus("current")
_HzCpPartnerMacAddressOverride_Type = DisplayString
_HzCpPartnerMacAddressOverride_Object = MibScalar
hzCpPartnerMacAddressOverride = _HzCpPartnerMacAddressOverride_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 10, 2),
    _HzCpPartnerMacAddressOverride_Type()
)
hzCpPartnerMacAddressOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPartnerMacAddressOverride.setStatus("current")


class _HzCpPartnerVlanTagging_Type(Integer32):
    """Custom type hzCpPartnerVlanTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpPartnerVlanTagging_Type.__name__ = "Integer32"
_HzCpPartnerVlanTagging_Object = MibScalar
hzCpPartnerVlanTagging = _HzCpPartnerVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 10, 3),
    _HzCpPartnerVlanTagging_Type()
)
hzCpPartnerVlanTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPartnerVlanTagging.setStatus("current")
_HzCpPartnerVlanTagId_Type = Integer32
_HzCpPartnerVlanTagId_Object = MibScalar
hzCpPartnerVlanTagId = _HzCpPartnerVlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 10, 4),
    _HzCpPartnerVlanTagId_Type()
)
hzCpPartnerVlanTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPartnerVlanTagId.setStatus("current")
_HzCpPartnerVlanTagPriority_Type = Integer32
_HzCpPartnerVlanTagPriority_Object = MibScalar
hzCpPartnerVlanTagPriority = _HzCpPartnerVlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 10, 5),
    _HzCpPartnerVlanTagPriority_Type()
)
hzCpPartnerVlanTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPartnerVlanTagPriority.setStatus("current")
_HzCpRedundancyStatus_ObjectIdentity = ObjectIdentity
hzCpRedundancyStatus = _HzCpRedundancyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 11)
)
_HzCpRedundancyUserTrafficStatus_Type = DisplayString
_HzCpRedundancyUserTrafficStatus_Object = MibScalar
hzCpRedundancyUserTrafficStatus = _HzCpRedundancyUserTrafficStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 11, 1),
    _HzCpRedundancyUserTrafficStatus_Type()
)
hzCpRedundancyUserTrafficStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRedundancyUserTrafficStatus.setStatus("current")
_HzCpRedundancyWirelessLinkStatus_Type = DisplayString
_HzCpRedundancyWirelessLinkStatus_Object = MibScalar
hzCpRedundancyWirelessLinkStatus = _HzCpRedundancyWirelessLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 11, 2),
    _HzCpRedundancyWirelessLinkStatus_Type()
)
hzCpRedundancyWirelessLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRedundancyWirelessLinkStatus.setStatus("current")
_HzCpRedundancyEnetCrossLinkStatus_Type = DisplayString
_HzCpRedundancyEnetCrossLinkStatus_Object = MibScalar
hzCpRedundancyEnetCrossLinkStatus = _HzCpRedundancyEnetCrossLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 11, 3),
    _HzCpRedundancyEnetCrossLinkStatus_Type()
)
hzCpRedundancyEnetCrossLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRedundancyEnetCrossLinkStatus.setStatus("current")
_HzCpRedundancyPortGroupStatus_Type = DisplayString
_HzCpRedundancyPortGroupStatus_Object = MibScalar
hzCpRedundancyPortGroupStatus = _HzCpRedundancyPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 5, 11, 4),
    _HzCpRedundancyPortGroupStatus_Type()
)
hzCpRedundancyPortGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRedundancyPortGroupStatus.setStatus("current")
_HzCpSysDiagnostics_ObjectIdentity = ObjectIdentity
hzCpSysDiagnostics = _HzCpSysDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6)
)
_HzCpLoopback_ObjectIdentity = ObjectIdentity
hzCpLoopback = _HzCpLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 1)
)


class _HzCpLoopbackType_Type(Integer32):
    """Custom type hzCpLoopbackType based on Integer32"""
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
        *(("off", 1),
          ("radioNonNetwork", 2),
          ("radioNetwork", 3),
          ("networkNearEnd", 4),
          ("networkFarEnd", 5))
    )


_HzCpLoopbackType_Type.__name__ = "Integer32"
_HzCpLoopbackType_Object = MibScalar
hzCpLoopbackType = _HzCpLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 1, 1),
    _HzCpLoopbackType_Type()
)
hzCpLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpLoopbackType.setStatus("current")
_HzCpLoopbackTimeout_Type = Integer32
_HzCpLoopbackTimeout_Object = MibScalar
hzCpLoopbackTimeout = _HzCpLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 1, 2),
    _HzCpLoopbackTimeout_Type()
)
hzCpLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpLoopbackTimeout.setStatus("current")
_HzCpLoopbackNetworkMac_Type = DisplayString
_HzCpLoopbackNetworkMac_Object = MibScalar
hzCpLoopbackNetworkMac = _HzCpLoopbackNetworkMac_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 1, 3),
    _HzCpLoopbackNetworkMac_Type()
)
hzCpLoopbackNetworkMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpLoopbackNetworkMac.setStatus("current")
_HzCpLoopbackNetworkQueue_Type = Integer32
_HzCpLoopbackNetworkQueue_Object = MibScalar
hzCpLoopbackNetworkQueue = _HzCpLoopbackNetworkQueue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 1, 4),
    _HzCpLoopbackNetworkQueue_Type()
)
hzCpLoopbackNetworkQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpLoopbackNetworkQueue.setStatus("current")


class _HzCpLoopbackNetworkPort_Type(Integer32):
    """Custom type hzCpLoopbackNetworkPort based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4))
    )


_HzCpLoopbackNetworkPort_Type.__name__ = "Integer32"
_HzCpLoopbackNetworkPort_Object = MibScalar
hzCpLoopbackNetworkPort = _HzCpLoopbackNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 1, 5),
    _HzCpLoopbackNetworkPort_Type()
)
hzCpLoopbackNetworkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpLoopbackNetworkPort.setStatus("current")


class _HzCpLoopbackStart_Type(Integer32):
    """Custom type hzCpLoopbackStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_HzCpLoopbackStart_Type.__name__ = "Integer32"
_HzCpLoopbackStart_Object = MibScalar
hzCpLoopbackStart = _HzCpLoopbackStart_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 1, 6),
    _HzCpLoopbackStart_Type()
)
hzCpLoopbackStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpLoopbackStart.setStatus("current")


class _HzCpLoopbackStop_Type(Integer32):
    """Custom type hzCpLoopbackStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("stop", 1)
    )


_HzCpLoopbackStop_Type.__name__ = "Integer32"
_HzCpLoopbackStop_Object = MibScalar
hzCpLoopbackStop = _HzCpLoopbackStop_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 1, 7),
    _HzCpLoopbackStop_Type()
)
hzCpLoopbackStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpLoopbackStop.setStatus("current")
_HzCpHitlessAamDiagnostics_ObjectIdentity = ObjectIdentity
hzCpHitlessAamDiagnostics = _HzCpHitlessAamDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 2)
)
_HzCpHitlessAamModemTable_Object = MibTable
hzCpHitlessAamModemTable = _HzCpHitlessAamModemTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hzCpHitlessAamModemTable.setStatus("current")
_HzCpHitlessAamModemEntry_Object = MibTableRow
hzCpHitlessAamModemEntry = _HzCpHitlessAamModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 2, 1, 1)
)
hzCpHitlessAamModemEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpHitlessAamModemIndex"),
)
if mibBuilder.loadTexts:
    hzCpHitlessAamModemEntry.setStatus("current")


class _HzCpHitlessAamModemIndex_Type(Integer32):
    """Custom type hzCpHitlessAamModemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("modem-1", 1)
    )


_HzCpHitlessAamModemIndex_Type.__name__ = "Integer32"
_HzCpHitlessAamModemIndex_Object = MibTableColumn
hzCpHitlessAamModemIndex = _HzCpHitlessAamModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 2, 1, 1, 1),
    _HzCpHitlessAamModemIndex_Type()
)
hzCpHitlessAamModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpHitlessAamModemIndex.setStatus("current")


class _HzCpHitlessAamModemDiagnose_Type(Integer32):
    """Custom type hzCpHitlessAamModemDiagnose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_HzCpHitlessAamModemDiagnose_Type.__name__ = "Integer32"
_HzCpHitlessAamModemDiagnose_Object = MibTableColumn
hzCpHitlessAamModemDiagnose = _HzCpHitlessAamModemDiagnose_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 2, 1, 1, 2),
    _HzCpHitlessAamModemDiagnose_Type()
)
hzCpHitlessAamModemDiagnose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHitlessAamModemDiagnose.setStatus("current")
_HzCpHitlessAamModemDiagnosticResult_Type = DisplayString
_HzCpHitlessAamModemDiagnosticResult_Object = MibTableColumn
hzCpHitlessAamModemDiagnosticResult = _HzCpHitlessAamModemDiagnosticResult_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 2, 1, 1, 3),
    _HzCpHitlessAamModemDiagnosticResult_Type()
)
hzCpHitlessAamModemDiagnosticResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpHitlessAamModemDiagnosticResult.setStatus("current")
_HzCpCodeCheckCount_Type = Integer32
_HzCpCodeCheckCount_Object = MibScalar
hzCpCodeCheckCount = _HzCpCodeCheckCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 6, 3),
    _HzCpCodeCheckCount_Type()
)
hzCpCodeCheckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpCodeCheckCount.setStatus("current")
_HzCpSysLicensedFeatureGroups_ObjectIdentity = ObjectIdentity
hzCpSysLicensedFeatureGroups = _HzCpSysLicensedFeatureGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7)
)
_HzCpSysUpgradeFeatureGroupsTable_Object = MibTable
hzCpSysUpgradeFeatureGroupsTable = _HzCpSysUpgradeFeatureGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hzCpSysUpgradeFeatureGroupsTable.setStatus("current")
_HzCpSysUpgradeFeatureGroupsEntry_Object = MibTableRow
hzCpSysUpgradeFeatureGroupsEntry = _HzCpSysUpgradeFeatureGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 1, 1)
)
hzCpSysUpgradeFeatureGroupsEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpUpgradeLicensedFeatureIndex"),
)
if mibBuilder.loadTexts:
    hzCpSysUpgradeFeatureGroupsEntry.setStatus("current")


class _HzCpUpgradeLicensedFeatureIndex_Type(Integer32):
    """Custom type hzCpUpgradeLicensedFeatureIndex based on Integer32"""
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
        *(("rls", 1),
          ("eoamEcfmLldp", 2),
          ("hitlessAam", 3),
          ("bac", 4),
          ("encryption", 5))
    )


_HzCpUpgradeLicensedFeatureIndex_Type.__name__ = "Integer32"
_HzCpUpgradeLicensedFeatureIndex_Object = MibTableColumn
hzCpUpgradeLicensedFeatureIndex = _HzCpUpgradeLicensedFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 1, 1, 1),
    _HzCpUpgradeLicensedFeatureIndex_Type()
)
hzCpUpgradeLicensedFeatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpUpgradeLicensedFeatureIndex.setStatus("current")
_HzCpUpgradeLicensedFeatureKey_Type = DisplayString
_HzCpUpgradeLicensedFeatureKey_Object = MibTableColumn
hzCpUpgradeLicensedFeatureKey = _HzCpUpgradeLicensedFeatureKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 1, 1, 2),
    _HzCpUpgradeLicensedFeatureKey_Type()
)
hzCpUpgradeLicensedFeatureKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpUpgradeLicensedFeatureKey.setStatus("current")
_HzCpUpgradeLicensedFeatureCount_Type = Integer32
_HzCpUpgradeLicensedFeatureCount_Object = MibTableColumn
hzCpUpgradeLicensedFeatureCount = _HzCpUpgradeLicensedFeatureCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 1, 1, 3),
    _HzCpUpgradeLicensedFeatureCount_Type()
)
hzCpUpgradeLicensedFeatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpUpgradeLicensedFeatureCount.setStatus("current")
_HzCpSysDowngradeFeatureGroupsTable_Object = MibTable
hzCpSysDowngradeFeatureGroupsTable = _HzCpSysDowngradeFeatureGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hzCpSysDowngradeFeatureGroupsTable.setStatus("current")
_HzCpSysDowngradeFeatureGroupsEntry_Object = MibTableRow
hzCpSysDowngradeFeatureGroupsEntry = _HzCpSysDowngradeFeatureGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 2, 1)
)
hzCpSysDowngradeFeatureGroupsEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpDowngradeLicensedFeatureIndex"),
)
if mibBuilder.loadTexts:
    hzCpSysDowngradeFeatureGroupsEntry.setStatus("current")


class _HzCpDowngradeLicensedFeatureIndex_Type(Integer32):
    """Custom type hzCpDowngradeLicensedFeatureIndex based on Integer32"""
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
        *(("rls", 1),
          ("eoamEcfmLldp", 2),
          ("hitlessAam", 3),
          ("bac", 4),
          ("encryption", 5))
    )


_HzCpDowngradeLicensedFeatureIndex_Type.__name__ = "Integer32"
_HzCpDowngradeLicensedFeatureIndex_Object = MibTableColumn
hzCpDowngradeLicensedFeatureIndex = _HzCpDowngradeLicensedFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 2, 1, 1),
    _HzCpDowngradeLicensedFeatureIndex_Type()
)
hzCpDowngradeLicensedFeatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpDowngradeLicensedFeatureIndex.setStatus("current")


class _HzCpDowngradeLicensedFeature_Type(Integer32):
    """Custom type hzCpDowngradeLicensedFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("downgrade", 1)
    )


_HzCpDowngradeLicensedFeature_Type.__name__ = "Integer32"
_HzCpDowngradeLicensedFeature_Object = MibTableColumn
hzCpDowngradeLicensedFeature = _HzCpDowngradeLicensedFeature_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 2, 1, 2),
    _HzCpDowngradeLicensedFeature_Type()
)
hzCpDowngradeLicensedFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpDowngradeLicensedFeature.setStatus("current")
_HzCpDowngradeLicensedFeatureCount_Type = Integer32
_HzCpDowngradeLicensedFeatureCount_Object = MibTableColumn
hzCpDowngradeLicensedFeatureCount = _HzCpDowngradeLicensedFeatureCount_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 2, 1, 3),
    _HzCpDowngradeLicensedFeatureCount_Type()
)
hzCpDowngradeLicensedFeatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpDowngradeLicensedFeatureCount.setStatus("current")
_HzCpDowngradeLicensedFeatureKey_Type = DisplayString
_HzCpDowngradeLicensedFeatureKey_Object = MibTableColumn
hzCpDowngradeLicensedFeatureKey = _HzCpDowngradeLicensedFeatureKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 2, 1, 4),
    _HzCpDowngradeLicensedFeatureKey_Type()
)
hzCpDowngradeLicensedFeatureKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpDowngradeLicensedFeatureKey.setStatus("current")
_HzCpSysLicensedFeatureGroupsTable_Object = MibTable
hzCpSysLicensedFeatureGroupsTable = _HzCpSysLicensedFeatureGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 3)
)
if mibBuilder.loadTexts:
    hzCpSysLicensedFeatureGroupsTable.setStatus("current")
_HzCpSysLicensedFeatureGroupsEntry_Object = MibTableRow
hzCpSysLicensedFeatureGroupsEntry = _HzCpSysLicensedFeatureGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 3, 1)
)
hzCpSysLicensedFeatureGroupsEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSysLicensedFeatureGroupIndex"),
)
if mibBuilder.loadTexts:
    hzCpSysLicensedFeatureGroupsEntry.setStatus("current")


class _HzCpSysLicensedFeatureGroupIndex_Type(Integer32):
    """Custom type hzCpSysLicensedFeatureGroupIndex based on Integer32"""
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
        *(("rls", 1),
          ("eoamEcfmLldp", 2),
          ("hitlessAam", 3),
          ("bac", 4),
          ("encryption", 5))
    )


_HzCpSysLicensedFeatureGroupIndex_Type.__name__ = "Integer32"
_HzCpSysLicensedFeatureGroupIndex_Object = MibTableColumn
hzCpSysLicensedFeatureGroupIndex = _HzCpSysLicensedFeatureGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 3, 1, 1),
    _HzCpSysLicensedFeatureGroupIndex_Type()
)
hzCpSysLicensedFeatureGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSysLicensedFeatureGroupIndex.setStatus("current")
_HzCpSysLicensedFeatureGroup_Type = DisplayString
_HzCpSysLicensedFeatureGroup_Object = MibTableColumn
hzCpSysLicensedFeatureGroup = _HzCpSysLicensedFeatureGroup_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 3, 1, 2),
    _HzCpSysLicensedFeatureGroup_Type()
)
hzCpSysLicensedFeatureGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSysLicensedFeatureGroup.setStatus("current")


class _HzCpSysLicensedFeatureGroupStatus_Type(Integer32):
    """Custom type hzCpSysLicensedFeatureGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlicensed", 1),
          ("licensed", 2))
    )


_HzCpSysLicensedFeatureGroupStatus_Type.__name__ = "Integer32"
_HzCpSysLicensedFeatureGroupStatus_Object = MibTableColumn
hzCpSysLicensedFeatureGroupStatus = _HzCpSysLicensedFeatureGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 7, 3, 1, 3),
    _HzCpSysLicensedFeatureGroupStatus_Type()
)
hzCpSysLicensedFeatureGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSysLicensedFeatureGroupStatus.setStatus("current")
_HzCpPeerAuthentication_ObjectIdentity = ObjectIdentity
hzCpPeerAuthentication = _HzCpPeerAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 8)
)


class _HzCpPeerAuthenticationUniqueKey_Type(DisplayString):
    """Custom type hzCpPeerAuthenticationUniqueKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_HzCpPeerAuthenticationUniqueKey_Type.__name__ = "DisplayString"
_HzCpPeerAuthenticationUniqueKey_Object = MibScalar
hzCpPeerAuthenticationUniqueKey = _HzCpPeerAuthenticationUniqueKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 8, 1),
    _HzCpPeerAuthenticationUniqueKey_Type()
)
hzCpPeerAuthenticationUniqueKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPeerAuthenticationUniqueKey.setStatus("current")


class _HzCpPeerAuthenticationMode_Type(Integer32):
    """Custom type hzCpPeerAuthenticationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("unique", 2),
          ("group", 3))
    )


_HzCpPeerAuthenticationMode_Type.__name__ = "Integer32"
_HzCpPeerAuthenticationMode_Object = MibScalar
hzCpPeerAuthenticationMode = _HzCpPeerAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 8, 2),
    _HzCpPeerAuthenticationMode_Type()
)
hzCpPeerAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPeerAuthenticationMode.setStatus("current")


class _HzCpPeerAuthenticationFailureAction_Type(Integer32):
    """Custom type hzCpPeerAuthenticationFailureAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blockTraffic", 1),
          ("passTraffic", 2))
    )


_HzCpPeerAuthenticationFailureAction_Type.__name__ = "Integer32"
_HzCpPeerAuthenticationFailureAction_Object = MibScalar
hzCpPeerAuthenticationFailureAction = _HzCpPeerAuthenticationFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 8, 3),
    _HzCpPeerAuthenticationFailureAction_Type()
)
hzCpPeerAuthenticationFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPeerAuthenticationFailureAction.setStatus("current")


class _HzCpPeerAuthenticationStatus_Type(Integer32):
    """Custom type hzCpPeerAuthenticationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAuthenticated", 1),
          ("authenticated", 2),
          ("explicitAuthenticationFailure", 3))
    )


_HzCpPeerAuthenticationStatus_Type.__name__ = "Integer32"
_HzCpPeerAuthenticationStatus_Object = MibScalar
hzCpPeerAuthenticationStatus = _HzCpPeerAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 8, 4),
    _HzCpPeerAuthenticationStatus_Type()
)
hzCpPeerAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpPeerAuthenticationStatus.setStatus("current")


class _HzCpPeerAuthenticationGroupKey_Type(DisplayString):
    """Custom type hzCpPeerAuthenticationGroupKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_HzCpPeerAuthenticationGroupKey_Type.__name__ = "DisplayString"
_HzCpPeerAuthenticationGroupKey_Object = MibScalar
hzCpPeerAuthenticationGroupKey = _HzCpPeerAuthenticationGroupKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 8, 5),
    _HzCpPeerAuthenticationGroupKey_Type()
)
hzCpPeerAuthenticationGroupKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPeerAuthenticationGroupKey.setStatus("current")
_HzCpCalendar_ObjectIdentity = ObjectIdentity
hzCpCalendar = _HzCpCalendar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 9)
)
_HzCpDate_Type = DisplayString
_HzCpDate_Object = MibScalar
hzCpDate = _HzCpDate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 9, 1),
    _HzCpDate_Type()
)
hzCpDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpDate.setStatus("current")
_HzCpTime_Type = DisplayString
_HzCpTime_Object = MibScalar
hzCpTime = _HzCpTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 9, 2),
    _HzCpTime_Type()
)
hzCpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpTime.setStatus("current")
_HzCpDateAndTimeForLastTimeChange_Type = DateAndTime
_HzCpDateAndTimeForLastTimeChange_Object = MibScalar
hzCpDateAndTimeForLastTimeChange = _HzCpDateAndTimeForLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 9, 3),
    _HzCpDateAndTimeForLastTimeChange_Type()
)
hzCpDateAndTimeForLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpDateAndTimeForLastTimeChange.setStatus("current")
_HzCpLastTimeChange_Type = Integer32
_HzCpLastTimeChange_Object = MibScalar
hzCpLastTimeChange = _HzCpLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 9, 4),
    _HzCpLastTimeChange_Type()
)
hzCpLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpLastTimeChange.setStatus("current")
_HzCpCumulativeTimeChange_Type = Integer32
_HzCpCumulativeTimeChange_Object = MibScalar
hzCpCumulativeTimeChange = _HzCpCumulativeTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 9, 5),
    _HzCpCumulativeTimeChange_Type()
)
hzCpCumulativeTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpCumulativeTimeChange.setStatus("current")
_HzCpSntp_ObjectIdentity = ObjectIdentity
hzCpSntp = _HzCpSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10)
)


class _HzCpSntpEnable_Type(Integer32):
    """Custom type hzCpSntpEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpSntpEnable_Type.__name__ = "Integer32"
_HzCpSntpEnable_Object = MibScalar
hzCpSntpEnable = _HzCpSntpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 1),
    _HzCpSntpEnable_Type()
)
hzCpSntpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSntpEnable.setStatus("current")


class _HzCpSntpOffset_Type(Integer32):
    """Custom type hzCpSntpOffset based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 140),
    )


_HzCpSntpOffset_Type.__name__ = "Integer32"
_HzCpSntpOffset_Object = MibScalar
hzCpSntpOffset = _HzCpSntpOffset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 2),
    _HzCpSntpOffset_Type()
)
hzCpSntpOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSntpOffset.setStatus("current")
_HzCpSntpServerDepTable_Object = MibTable
hzCpSntpServerDepTable = _HzCpSntpServerDepTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 3)
)
if mibBuilder.loadTexts:
    hzCpSntpServerDepTable.setStatus("deprecated")
_HzCpSntpServerDepEntry_Object = MibTableRow
hzCpSntpServerDepEntry = _HzCpSntpServerDepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 3, 1)
)
hzCpSntpServerDepEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSntpServerIpAddressDep"),
)
if mibBuilder.loadTexts:
    hzCpSntpServerDepEntry.setStatus("deprecated")
_HzCpSntpServerIndexDep_Type = Integer32
_HzCpSntpServerIndexDep_Object = MibTableColumn
hzCpSntpServerIndexDep = _HzCpSntpServerIndexDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 3, 1, 1),
    _HzCpSntpServerIndexDep_Type()
)
hzCpSntpServerIndexDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSntpServerIndexDep.setStatus("deprecated")
_HzCpSntpServerIpAddressDep_Type = IpAddress
_HzCpSntpServerIpAddressDep_Object = MibTableColumn
hzCpSntpServerIpAddressDep = _HzCpSntpServerIpAddressDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 3, 1, 2),
    _HzCpSntpServerIpAddressDep_Type()
)
hzCpSntpServerIpAddressDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSntpServerIpAddressDep.setStatus("deprecated")


class _HzCpSntpServerStatusDep_Type(Integer32):
    """Custom type hzCpSntpServerStatusDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("failed", 2))
    )


_HzCpSntpServerStatusDep_Type.__name__ = "Integer32"
_HzCpSntpServerStatusDep_Object = MibTableColumn
hzCpSntpServerStatusDep = _HzCpSntpServerStatusDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 3, 1, 3),
    _HzCpSntpServerStatusDep_Type()
)
hzCpSntpServerStatusDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSntpServerStatusDep.setStatus("deprecated")
_HzCpSntpServerStratumDep_Type = Integer32
_HzCpSntpServerStratumDep_Object = MibTableColumn
hzCpSntpServerStratumDep = _HzCpSntpServerStratumDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 3, 1, 4),
    _HzCpSntpServerStratumDep_Type()
)
hzCpSntpServerStratumDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSntpServerStratumDep.setStatus("deprecated")
_HzCpSntpServerTable_Object = MibTable
hzCpSntpServerTable = _HzCpSntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 4)
)
if mibBuilder.loadTexts:
    hzCpSntpServerTable.setStatus("current")
_HzCpSntpServerEntry_Object = MibTableRow
hzCpSntpServerEntry = _HzCpSntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 4, 1)
)
hzCpSntpServerEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSntpServerIndex"),
)
if mibBuilder.loadTexts:
    hzCpSntpServerEntry.setStatus("current")
_HzCpSntpServerIndex_Type = Integer32
_HzCpSntpServerIndex_Object = MibTableColumn
hzCpSntpServerIndex = _HzCpSntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 4, 1, 1),
    _HzCpSntpServerIndex_Type()
)
hzCpSntpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSntpServerIndex.setStatus("current")
_HzCpSntpServerDomain_Type = InetAddressType
_HzCpSntpServerDomain_Object = MibTableColumn
hzCpSntpServerDomain = _HzCpSntpServerDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 4, 1, 2),
    _HzCpSntpServerDomain_Type()
)
hzCpSntpServerDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSntpServerDomain.setStatus("current")
_HzCpSntpServerAddress_Type = InetAddress
_HzCpSntpServerAddress_Object = MibTableColumn
hzCpSntpServerAddress = _HzCpSntpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 4, 1, 3),
    _HzCpSntpServerAddress_Type()
)
hzCpSntpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSntpServerAddress.setStatus("current")


class _HzCpSntpServerStatus_Type(Integer32):
    """Custom type hzCpSntpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("failed", 2))
    )


_HzCpSntpServerStatus_Type.__name__ = "Integer32"
_HzCpSntpServerStatus_Object = MibTableColumn
hzCpSntpServerStatus = _HzCpSntpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 4, 1, 4),
    _HzCpSntpServerStatus_Type()
)
hzCpSntpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSntpServerStatus.setStatus("current")
_HzCpSntpServerStratum_Type = Integer32
_HzCpSntpServerStratum_Object = MibTableColumn
hzCpSntpServerStratum = _HzCpSntpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 4, 1, 5),
    _HzCpSntpServerStratum_Type()
)
hzCpSntpServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSntpServerStratum.setStatus("current")


class _HzCpSntpRestoreDefault_Type(Integer32):
    """Custom type hzCpSntpRestoreDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restore", 1)
    )


_HzCpSntpRestoreDefault_Type.__name__ = "Integer32"
_HzCpSntpRestoreDefault_Object = MibScalar
hzCpSntpRestoreDefault = _HzCpSntpRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 10, 5),
    _HzCpSntpRestoreDefault_Type()
)
hzCpSntpRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSntpRestoreDefault.setStatus("current")
_HzCpSyncE_ObjectIdentity = ObjectIdentity
hzCpSyncE = _HzCpSyncE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 11)
)


class _HzCpSyncEState_Type(Integer32):
    """Custom type hzCpSyncEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("manual", 2),
          ("auto", 3))
    )


_HzCpSyncEState_Type.__name__ = "Integer32"
_HzCpSyncEState_Object = MibScalar
hzCpSyncEState = _HzCpSyncEState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 11, 1),
    _HzCpSyncEState_Type()
)
hzCpSyncEState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSyncEState.setStatus("current")


class _HzCpSyncEPrimarySource_Type(Integer32):
    """Custom type hzCpSyncEPrimarySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("wp1", 5),
          ("free-run", 6))
    )


_HzCpSyncEPrimarySource_Type.__name__ = "Integer32"
_HzCpSyncEPrimarySource_Object = MibScalar
hzCpSyncEPrimarySource = _HzCpSyncEPrimarySource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 11, 2),
    _HzCpSyncEPrimarySource_Type()
)
hzCpSyncEPrimarySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSyncEPrimarySource.setStatus("current")


class _HzCpSyncESecondarySource_Type(Integer32):
    """Custom type hzCpSyncESecondarySource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("wp1", 5),
          ("free-run", 6))
    )


_HzCpSyncESecondarySource_Type.__name__ = "Integer32"
_HzCpSyncESecondarySource_Object = MibScalar
hzCpSyncESecondarySource = _HzCpSyncESecondarySource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 11, 3),
    _HzCpSyncESecondarySource_Type()
)
hzCpSyncESecondarySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSyncESecondarySource.setStatus("current")
_HzCpSyncEMemberPorts_Type = DisplayString
_HzCpSyncEMemberPorts_Object = MibScalar
hzCpSyncEMemberPorts = _HzCpSyncEMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 11, 4),
    _HzCpSyncEMemberPorts_Type()
)
hzCpSyncEMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSyncEMemberPorts.setStatus("current")
_HzCpSyncEForcedHoldover_Type = DisplayString
_HzCpSyncEForcedHoldover_Object = MibScalar
hzCpSyncEForcedHoldover = _HzCpSyncEForcedHoldover_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 11, 5),
    _HzCpSyncEForcedHoldover_Type()
)
hzCpSyncEForcedHoldover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSyncEForcedHoldover.setStatus("current")
_HzCpSyncERevertive_Type = DisplayString
_HzCpSyncERevertive_Object = MibScalar
hzCpSyncERevertive = _HzCpSyncERevertive_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 11, 6),
    _HzCpSyncERevertive_Type()
)
hzCpSyncERevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSyncERevertive.setStatus("current")


class _HzCpSyncEClockSource_Type(Integer32):
    """Custom type hzCpSyncEClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("wp1", 5),
          ("free-run", 6))
    )


_HzCpSyncEClockSource_Type.__name__ = "Integer32"
_HzCpSyncEClockSource_Object = MibScalar
hzCpSyncEClockSource = _HzCpSyncEClockSource_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 11, 7),
    _HzCpSyncEClockSource_Type()
)
hzCpSyncEClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSyncEClockSource.setStatus("current")
_HzCpSyncEAcquisitionStatus_Type = DisplayString
_HzCpSyncEAcquisitionStatus_Object = MibScalar
hzCpSyncEAcquisitionStatus = _HzCpSyncEAcquisitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 11, 8),
    _HzCpSyncEAcquisitionStatus_Type()
)
hzCpSyncEAcquisitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSyncEAcquisitionStatus.setStatus("current")


class _HzCpSyncEWanderFilter_Type(Integer32):
    """Custom type hzCpSyncEWanderFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("option1", 1),
          ("option2", 2))
    )


_HzCpSyncEWanderFilter_Type.__name__ = "Integer32"
_HzCpSyncEWanderFilter_Object = MibScalar
hzCpSyncEWanderFilter = _HzCpSyncEWanderFilter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 11, 9),
    _HzCpSyncEWanderFilter_Type()
)
hzCpSyncEWanderFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSyncEWanderFilter.setStatus("current")
_HzCpBac_ObjectIdentity = ObjectIdentity
hzCpBac = _HzCpBac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 12)
)
_HzCpBacRecordAvgPeriod_Type = Integer32
_HzCpBacRecordAvgPeriod_Object = MibScalar
hzCpBacRecordAvgPeriod = _HzCpBacRecordAvgPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 12, 1),
    _HzCpBacRecordAvgPeriod_Type()
)
hzCpBacRecordAvgPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBacRecordAvgPeriod.setStatus("current")
_HzCpBacTable_Object = MibTable
hzCpBacTable = _HzCpBacTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 12, 2)
)
if mibBuilder.loadTexts:
    hzCpBacTable.setStatus("current")
_HzCpBacEntry_Object = MibTableRow
hzCpBacEntry = _HzCpBacEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 12, 2, 1)
)
hzCpBacEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpBacQIndex"),
)
if mibBuilder.loadTexts:
    hzCpBacEntry.setStatus("current")


class _HzCpBacQIndex_Type(Integer32):
    """Custom type hzCpBacQIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_HzCpBacQIndex_Type.__name__ = "Integer32"
_HzCpBacQIndex_Object = MibTableColumn
hzCpBacQIndex = _HzCpBacQIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 12, 2, 1, 1),
    _HzCpBacQIndex_Type()
)
hzCpBacQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpBacQIndex.setStatus("current")


class _HzCpBacQEnable_Type(Integer32):
    """Custom type hzCpBacQEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpBacQEnable_Type.__name__ = "Integer32"
_HzCpBacQEnable_Object = MibTableColumn
hzCpBacQEnable = _HzCpBacQEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 12, 2, 1, 2),
    _HzCpBacQEnable_Type()
)
hzCpBacQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBacQEnable.setStatus("current")
_HzCpBacQBlockSize_Type = Integer32
_HzCpBacQBlockSize_Object = MibTableColumn
hzCpBacQBlockSize = _HzCpBacQBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 12, 2, 1, 3),
    _HzCpBacQBlockSize_Type()
)
hzCpBacQBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBacQBlockSize.setStatus("current")


class _HzCpBacRecordLogging_Type(Integer32):
    """Custom type hzCpBacRecordLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpBacRecordLogging_Type.__name__ = "Integer32"
_HzCpBacRecordLogging_Object = MibTableColumn
hzCpBacRecordLogging = _HzCpBacRecordLogging_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 12, 2, 1, 4),
    _HzCpBacRecordLogging_Type()
)
hzCpBacRecordLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBacRecordLogging.setStatus("current")
_HzCpBacUncompressedRatio_Type = DisplayString
_HzCpBacUncompressedRatio_Object = MibTableColumn
hzCpBacUncompressedRatio = _HzCpBacUncompressedRatio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 12, 2, 1, 5),
    _HzCpBacUncompressedRatio_Type()
)
hzCpBacUncompressedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpBacUncompressedRatio.setStatus("current")
_HzCpBacGain_Type = DisplayString
_HzCpBacGain_Object = MibTableColumn
hzCpBacGain = _HzCpBacGain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 12, 2, 1, 6),
    _HzCpBacGain_Type()
)
hzCpBacGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpBacGain.setStatus("current")
_HzCpEcfmVsm_ObjectIdentity = ObjectIdentity
hzCpEcfmVsm = _HzCpEcfmVsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13)
)
_HzCpBandwidthVsm_ObjectIdentity = ObjectIdentity
hzCpBandwidthVsm = _HzCpBandwidthVsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13, 1)
)
_HzCpBwVsmVendorOui_Type = DisplayString
_HzCpBwVsmVendorOui_Object = MibScalar
hzCpBwVsmVendorOui = _HzCpBwVsmVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13, 1, 1),
    _HzCpBwVsmVendorOui_Type()
)
hzCpBwVsmVendorOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwVsmVendorOui.setStatus("current")
_HzCpBwVsmMdLevel_Type = Integer32
_HzCpBwVsmMdLevel_Object = MibScalar
hzCpBwVsmMdLevel = _HzCpBwVsmMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13, 1, 2),
    _HzCpBwVsmMdLevel_Type()
)
hzCpBwVsmMdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwVsmMdLevel.setStatus("current")
_HzCpBwVsmWaitTime_Type = Integer32
_HzCpBwVsmWaitTime_Object = MibScalar
hzCpBwVsmWaitTime = _HzCpBwVsmWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13, 1, 3),
    _HzCpBwVsmWaitTime_Type()
)
hzCpBwVsmWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwVsmWaitTime.setStatus("current")


class _HzCpBwVsmPeriod_Type(Integer32):
    """Custom type hzCpBwVsmPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one-sec", 1),
          ("ten-sec", 2),
          ("one-min", 3))
    )


_HzCpBwVsmPeriod_Type.__name__ = "Integer32"
_HzCpBwVsmPeriod_Object = MibScalar
hzCpBwVsmPeriod = _HzCpBwVsmPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13, 1, 4),
    _HzCpBwVsmPeriod_Type()
)
hzCpBwVsmPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwVsmPeriod.setStatus("current")


class _HzCpBwVsmVlanTag_Type(Integer32):
    """Custom type hzCpBwVsmVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HzCpBwVsmVlanTag_Type.__name__ = "Integer32"
_HzCpBwVsmVlanTag_Object = MibScalar
hzCpBwVsmVlanTag = _HzCpBwVsmVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13, 1, 5),
    _HzCpBwVsmVlanTag_Type()
)
hzCpBwVsmVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwVsmVlanTag.setStatus("current")
_HzCpBwVsmVlanId_Type = Integer32
_HzCpBwVsmVlanId_Object = MibScalar
hzCpBwVsmVlanId = _HzCpBwVsmVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13, 1, 6),
    _HzCpBwVsmVlanId_Type()
)
hzCpBwVsmVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwVsmVlanId.setStatus("current")
_HzCpBwVsmVlanPriority_Type = Integer32
_HzCpBwVsmVlanPriority_Object = MibScalar
hzCpBwVsmVlanPriority = _HzCpBwVsmVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13, 1, 7),
    _HzCpBwVsmVlanPriority_Type()
)
hzCpBwVsmVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwVsmVlanPriority.setStatus("current")
_HzCpBwVsmPortList_Type = DisplayString
_HzCpBwVsmPortList_Object = MibScalar
hzCpBwVsmPortList = _HzCpBwVsmPortList_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13, 1, 8),
    _HzCpBwVsmPortList_Type()
)
hzCpBwVsmPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwVsmPortList.setStatus("current")


class _HzCpBwVsmState_Type(Integer32):
    """Custom type hzCpBwVsmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HzCpBwVsmState_Type.__name__ = "Integer32"
_HzCpBwVsmState_Object = MibScalar
hzCpBwVsmState = _HzCpBwVsmState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 13, 1, 9),
    _HzCpBwVsmState_Type()
)
hzCpBwVsmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwVsmState.setStatus("current")
_HzCpPM_ObjectIdentity = ObjectIdentity
hzCpPM = _HzCpPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14)
)
_HzCpPmRspiThresholdTable_Object = MibTable
hzCpPmRspiThresholdTable = _HzCpPmRspiThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 1)
)
if mibBuilder.loadTexts:
    hzCpPmRspiThresholdTable.setStatus("current")
_HzCpPmRspiThresholdEntry_Object = MibTableRow
hzCpPmRspiThresholdEntry = _HzCpPmRspiThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 1, 1)
)
hzCpPmRspiThresholdEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpPmRspiThrIndex"),
)
if mibBuilder.loadTexts:
    hzCpPmRspiThresholdEntry.setStatus("current")
_HzCpPmRspiThrIndex_Type = Integer32
_HzCpPmRspiThrIndex_Object = MibTableColumn
hzCpPmRspiThrIndex = _HzCpPmRspiThrIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 1, 1, 1),
    _HzCpPmRspiThrIndex_Type()
)
hzCpPmRspiThrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hzCpPmRspiThrIndex.setStatus("current")
_HzCpPmRLT1_Type = Integer32
_HzCpPmRLT1_Object = MibTableColumn
hzCpPmRLT1 = _HzCpPmRLT1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 1, 1, 2),
    _HzCpPmRLT1_Type()
)
hzCpPmRLT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPmRLT1.setStatus("current")
_HzCpPmRLT2_Type = Integer32
_HzCpPmRLT2_Object = MibTableColumn
hzCpPmRLT2 = _HzCpPmRLT2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 1, 1, 3),
    _HzCpPmRLT2_Type()
)
hzCpPmRLT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPmRLT2.setStatus("current")
_HzCpPmRLT3_Type = Integer32
_HzCpPmRLT3_Object = MibTableColumn
hzCpPmRLT3 = _HzCpPmRLT3_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 1, 1, 4),
    _HzCpPmRLT3_Type()
)
hzCpPmRLT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPmRLT3.setStatus("current")
_HzCpPmRLT4_Type = Integer32
_HzCpPmRLT4_Object = MibTableColumn
hzCpPmRLT4 = _HzCpPmRLT4_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 1, 1, 5),
    _HzCpPmRLT4_Type()
)
hzCpPmRLT4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPmRLT4.setStatus("current")
_HzCpPmTLT1_Type = Integer32
_HzCpPmTLT1_Object = MibTableColumn
hzCpPmTLT1 = _HzCpPmTLT1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 1, 1, 6),
    _HzCpPmTLT1_Type()
)
hzCpPmTLT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPmTLT1.setStatus("current")
_HzCpPmTLT2_Type = Integer32
_HzCpPmTLT2_Object = MibTableColumn
hzCpPmTLT2 = _HzCpPmTLT2_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 1, 1, 7),
    _HzCpPmTLT2_Type()
)
hzCpPmTLT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPmTLT2.setStatus("current")
_HzCpPmRspiThrRowStatus_Type = RowStatus
_HzCpPmRspiThrRowStatus_Object = MibTableColumn
hzCpPmRspiThrRowStatus = _HzCpPmRspiThrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 1, 1, 8),
    _HzCpPmRspiThrRowStatus_Type()
)
hzCpPmRspiThrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPmRspiThrRowStatus.setStatus("current")
_HzCpPmAdvThresholdTable_Object = MibTable
hzCpPmAdvThresholdTable = _HzCpPmAdvThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 2)
)
if mibBuilder.loadTexts:
    hzCpPmAdvThresholdTable.setStatus("current")
_HzCpPmAdvThresholdEntry_Object = MibTableRow
hzCpPmAdvThresholdEntry = _HzCpPmAdvThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 2, 1)
)
hzCpPmAdvThresholdEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpPmAdvThrIndex"),
)
if mibBuilder.loadTexts:
    hzCpPmAdvThresholdEntry.setStatus("current")
_HzCpPmAdvThrIndex_Type = Integer32
_HzCpPmAdvThrIndex_Object = MibTableColumn
hzCpPmAdvThrIndex = _HzCpPmAdvThrIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 2, 1, 1),
    _HzCpPmAdvThrIndex_Type()
)
hzCpPmAdvThrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hzCpPmAdvThrIndex.setStatus("current")
_HzCpPmAdvTxHitsT1_Type = Integer32
_HzCpPmAdvTxHitsT1_Object = MibTableColumn
hzCpPmAdvTxHitsT1 = _HzCpPmAdvTxHitsT1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 2, 1, 2),
    _HzCpPmAdvTxHitsT1_Type()
)
hzCpPmAdvTxHitsT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPmAdvTxHitsT1.setStatus("current")
_HzCpPmAdvRxHitsT1_Type = Integer32
_HzCpPmAdvRxHitsT1_Object = MibTableColumn
hzCpPmAdvRxHitsT1 = _HzCpPmAdvRxHitsT1_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 2, 1, 3),
    _HzCpPmAdvRxHitsT1_Type()
)
hzCpPmAdvRxHitsT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPmAdvRxHitsT1.setStatus("current")
_HzCpPmAdvRowStatus_Type = RowStatus
_HzCpPmAdvRowStatus_Object = MibTableColumn
hzCpPmAdvRowStatus = _HzCpPmAdvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 1, 14, 2, 1, 4),
    _HzCpPmAdvRowStatus_Type()
)
hzCpPmAdvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPmAdvRowStatus.setStatus("current")
_HzCpManagement_ObjectIdentity = ObjectIdentity
hzCpManagement = _HzCpManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2)
)
_HzCpMacAddress_Type = DisplayString
_HzCpMacAddress_Object = MibScalar
hzCpMacAddress = _HzCpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 1),
    _HzCpMacAddress_Type()
)
hzCpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpMacAddress.setStatus("current")


class _HzCpTelnetAccessMode_Type(Integer32):
    """Custom type hzCpTelnetAccessMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpTelnetAccessMode_Type.__name__ = "Integer32"
_HzCpTelnetAccessMode_Object = MibScalar
hzCpTelnetAccessMode = _HzCpTelnetAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 2),
    _HzCpTelnetAccessMode_Type()
)
hzCpTelnetAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpTelnetAccessMode.setStatus("current")


class _HzCpSshAccessMode_Type(Integer32):
    """Custom type hzCpSshAccessMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpSshAccessMode_Type.__name__ = "Integer32"
_HzCpSshAccessMode_Object = MibScalar
hzCpSshAccessMode = _HzCpSshAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 3),
    _HzCpSshAccessMode_Type()
)
hzCpSshAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSshAccessMode.setStatus("current")
_HzCpNetworkManagementInterface_ObjectIdentity = ObjectIdentity
hzCpNetworkManagementInterface = _HzCpNetworkManagementInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4)
)
_HzCpNetMgmtInterfaceVlan_ObjectIdentity = ObjectIdentity
hzCpNetMgmtInterfaceVlan = _HzCpNetMgmtInterfaceVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 1)
)
_HzCpNetMgmtPortList_Type = DisplayString
_HzCpNetMgmtPortList_Object = MibScalar
hzCpNetMgmtPortList = _HzCpNetMgmtPortList_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 1, 1),
    _HzCpNetMgmtPortList_Type()
)
hzCpNetMgmtPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpNetMgmtPortList.setStatus("current")


class _HzCpNetMgmtVlanTagId_Type(Integer32):
    """Custom type hzCpNetMgmtVlanTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_HzCpNetMgmtVlanTagId_Type.__name__ = "Integer32"
_HzCpNetMgmtVlanTagId_Object = MibScalar
hzCpNetMgmtVlanTagId = _HzCpNetMgmtVlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 1, 2),
    _HzCpNetMgmtVlanTagId_Type()
)
hzCpNetMgmtVlanTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpNetMgmtVlanTagId.setStatus("current")


class _HzCpNetMgmtVlanTagPriority_Type(Integer32):
    """Custom type hzCpNetMgmtVlanTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HzCpNetMgmtVlanTagPriority_Type.__name__ = "Integer32"
_HzCpNetMgmtVlanTagPriority_Object = MibScalar
hzCpNetMgmtVlanTagPriority = _HzCpNetMgmtVlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 1, 3),
    _HzCpNetMgmtVlanTagPriority_Type()
)
hzCpNetMgmtVlanTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpNetMgmtVlanTagPriority.setStatus("current")


class _HzCpNetMgmtVlanTagging_Type(Integer32):
    """Custom type hzCpNetMgmtVlanTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HzCpNetMgmtVlanTagging_Type.__name__ = "Integer32"
_HzCpNetMgmtVlanTagging_Object = MibScalar
hzCpNetMgmtVlanTagging = _HzCpNetMgmtVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 1, 4),
    _HzCpNetMgmtVlanTagging_Type()
)
hzCpNetMgmtVlanTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpNetMgmtVlanTagging.setStatus("current")
_HzCpNetMgmtDscpPriority_Type = Integer32
_HzCpNetMgmtDscpPriority_Object = MibScalar
hzCpNetMgmtDscpPriority = _HzCpNetMgmtDscpPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 1, 5),
    _HzCpNetMgmtDscpPriority_Type()
)
hzCpNetMgmtDscpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpNetMgmtDscpPriority.setStatus("current")
_HzCpNetMgmtIpv4_ObjectIdentity = ObjectIdentity
hzCpNetMgmtIpv4 = _HzCpNetMgmtIpv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 2)
)
_HzCpIpAddress_Type = IpAddress
_HzCpIpAddress_Object = MibScalar
hzCpIpAddress = _HzCpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 2, 1),
    _HzCpIpAddress_Type()
)
hzCpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpIpAddress.setStatus("current")
_HzCpSubnetMask_Type = IpAddress
_HzCpSubnetMask_Object = MibScalar
hzCpSubnetMask = _HzCpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 2, 2),
    _HzCpSubnetMask_Type()
)
hzCpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSubnetMask.setStatus("current")
_HzCpDefaultGateway_Type = IpAddress
_HzCpDefaultGateway_Object = MibScalar
hzCpDefaultGateway = _HzCpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 2, 3),
    _HzCpDefaultGateway_Type()
)
hzCpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpDefaultGateway.setStatus("current")
_HzCpNetMgmttIpv6_ObjectIdentity = ObjectIdentity
hzCpNetMgmttIpv6 = _HzCpNetMgmttIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 3)
)
_HzCpIpv6Domain_Type = InetAddressType
_HzCpIpv6Domain_Object = MibScalar
hzCpIpv6Domain = _HzCpIpv6Domain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 3, 1),
    _HzCpIpv6Domain_Type()
)
hzCpIpv6Domain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpIpv6Domain.setStatus("current")
_HzCpIpv6Address_Type = InetAddress
_HzCpIpv6Address_Object = MibScalar
hzCpIpv6Address = _HzCpIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 3, 2),
    _HzCpIpv6Address_Type()
)
hzCpIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpIpv6Address.setStatus("current")
_HzCpIpv6Prefix_Type = Integer32
_HzCpIpv6Prefix_Object = MibScalar
hzCpIpv6Prefix = _HzCpIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 3, 3),
    _HzCpIpv6Prefix_Type()
)
hzCpIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpIpv6Prefix.setStatus("current")
_HzCpIpv6GatewayDomain_Type = InetAddressType
_HzCpIpv6GatewayDomain_Object = MibScalar
hzCpIpv6GatewayDomain = _HzCpIpv6GatewayDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 3, 4),
    _HzCpIpv6GatewayDomain_Type()
)
hzCpIpv6GatewayDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpIpv6GatewayDomain.setStatus("current")
_HzCpIpv6GatewayAddress_Type = InetAddress
_HzCpIpv6GatewayAddress_Object = MibScalar
hzCpIpv6GatewayAddress = _HzCpIpv6GatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 3, 5),
    _HzCpIpv6GatewayAddress_Type()
)
hzCpIpv6GatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpIpv6GatewayAddress.setStatus("current")
_HzCpIpv6LinkLocalDomain_Type = InetAddressType
_HzCpIpv6LinkLocalDomain_Object = MibScalar
hzCpIpv6LinkLocalDomain = _HzCpIpv6LinkLocalDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 3, 6),
    _HzCpIpv6LinkLocalDomain_Type()
)
hzCpIpv6LinkLocalDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpIpv6LinkLocalDomain.setStatus("current")
_HzCpIpv6LinkLocalAddress_Type = InetAddress
_HzCpIpv6LinkLocalAddress_Object = MibScalar
hzCpIpv6LinkLocalAddress = _HzCpIpv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 3, 7),
    _HzCpIpv6LinkLocalAddress_Type()
)
hzCpIpv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpIpv6LinkLocalAddress.setStatus("current")


class _HzCpNetMgmtApplyToSystem_Type(Integer32):
    """Custom type hzCpNetMgmtApplyToSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("apply", 1)
    )


_HzCpNetMgmtApplyToSystem_Type.__name__ = "Integer32"
_HzCpNetMgmtApplyToSystem_Object = MibScalar
hzCpNetMgmtApplyToSystem = _HzCpNetMgmtApplyToSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 4, 4),
    _HzCpNetMgmtApplyToSystem_Type()
)
hzCpNetMgmtApplyToSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpNetMgmtApplyToSystem.setStatus("current")
_HzCpSnmp_ObjectIdentity = ObjectIdentity
hzCpSnmp = _HzCpSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5)
)


class _HzCpSnmpUserAccess_Type(Integer32):
    """Custom type hzCpSnmpUserAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("explicitManagers", 1),
          ("any", 2))
    )


_HzCpSnmpUserAccess_Type.__name__ = "Integer32"
_HzCpSnmpUserAccess_Object = MibScalar
hzCpSnmpUserAccess = _HzCpSnmpUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 1),
    _HzCpSnmpUserAccess_Type()
)
hzCpSnmpUserAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpUserAccess.setStatus("current")


class _HzCpSnmpManagerAnyCommunityName_Type(DisplayString):
    """Custom type hzCpSnmpManagerAnyCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpSnmpManagerAnyCommunityName_Type.__name__ = "DisplayString"
_HzCpSnmpManagerAnyCommunityName_Object = MibScalar
hzCpSnmpManagerAnyCommunityName = _HzCpSnmpManagerAnyCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 2),
    _HzCpSnmpManagerAnyCommunityName_Type()
)
hzCpSnmpManagerAnyCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpManagerAnyCommunityName.setStatus("current")


class _HzCpSnmpSetRequests_Type(Integer32):
    """Custom type hzCpSnmpSetRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpSnmpSetRequests_Type.__name__ = "Integer32"
_HzCpSnmpSetRequests_Object = MibScalar
hzCpSnmpSetRequests = _HzCpSnmpSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 3),
    _HzCpSnmpSetRequests_Type()
)
hzCpSnmpSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpSetRequests.setStatus("current")
_HzCpSnmpManagersDepTable_Object = MibTable
hzCpSnmpManagersDepTable = _HzCpSnmpManagersDepTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 4)
)
if mibBuilder.loadTexts:
    hzCpSnmpManagersDepTable.setStatus("deprecated")
_HzCpSnmpManagersDepEntry_Object = MibTableRow
hzCpSnmpManagersDepEntry = _HzCpSnmpManagersDepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 4, 1)
)
hzCpSnmpManagersDepEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSnmpManagersIndexDep"),
)
if mibBuilder.loadTexts:
    hzCpSnmpManagersDepEntry.setStatus("deprecated")
_HzCpSnmpManagersIndexDep_Type = Integer32
_HzCpSnmpManagersIndexDep_Object = MibTableColumn
hzCpSnmpManagersIndexDep = _HzCpSnmpManagersIndexDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 4, 1, 1),
    _HzCpSnmpManagersIndexDep_Type()
)
hzCpSnmpManagersIndexDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpManagersIndexDep.setStatus("deprecated")
_HzCpSnmpManagerIpAddressDep_Type = IpAddress
_HzCpSnmpManagerIpAddressDep_Object = MibTableColumn
hzCpSnmpManagerIpAddressDep = _HzCpSnmpManagerIpAddressDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 4, 1, 2),
    _HzCpSnmpManagerIpAddressDep_Type()
)
hzCpSnmpManagerIpAddressDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpManagerIpAddressDep.setStatus("deprecated")


class _HzCpSnmpManagerCommunityNameDep_Type(DisplayString):
    """Custom type hzCpSnmpManagerCommunityNameDep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzCpSnmpManagerCommunityNameDep_Type.__name__ = "DisplayString"
_HzCpSnmpManagerCommunityNameDep_Object = MibTableColumn
hzCpSnmpManagerCommunityNameDep = _HzCpSnmpManagerCommunityNameDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 4, 1, 3),
    _HzCpSnmpManagerCommunityNameDep_Type()
)
hzCpSnmpManagerCommunityNameDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpManagerCommunityNameDep.setStatus("deprecated")


class _HzCpSnmpManagerActivatedDep_Type(Integer32):
    """Custom type hzCpSnmpManagerActivatedDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzCpSnmpManagerActivatedDep_Type.__name__ = "Integer32"
_HzCpSnmpManagerActivatedDep_Object = MibTableColumn
hzCpSnmpManagerActivatedDep = _HzCpSnmpManagerActivatedDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 4, 1, 4),
    _HzCpSnmpManagerActivatedDep_Type()
)
hzCpSnmpManagerActivatedDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpManagerActivatedDep.setStatus("deprecated")
_HzCpSnmpV3ManagersTable_Object = MibTable
hzCpSnmpV3ManagersTable = _HzCpSnmpV3ManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 5)
)
if mibBuilder.loadTexts:
    hzCpSnmpV3ManagersTable.setStatus("current")
_HzCpSnmpV3ManagersEntry_Object = MibTableRow
hzCpSnmpV3ManagersEntry = _HzCpSnmpV3ManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 5, 1)
)
hzCpSnmpV3ManagersEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSnmpV3ManagersIndex"),
)
if mibBuilder.loadTexts:
    hzCpSnmpV3ManagersEntry.setStatus("current")
_HzCpSnmpV3ManagersIndex_Type = Integer32
_HzCpSnmpV3ManagersIndex_Object = MibTableColumn
hzCpSnmpV3ManagersIndex = _HzCpSnmpV3ManagersIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 5, 1, 1),
    _HzCpSnmpV3ManagersIndex_Type()
)
hzCpSnmpV3ManagersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpV3ManagersIndex.setStatus("current")


class _HzCpSnmpV3ManagerUserName_Type(DisplayString):
    """Custom type hzCpSnmpV3ManagerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpSnmpV3ManagerUserName_Type.__name__ = "DisplayString"
_HzCpSnmpV3ManagerUserName_Object = MibTableColumn
hzCpSnmpV3ManagerUserName = _HzCpSnmpV3ManagerUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 5, 1, 2),
    _HzCpSnmpV3ManagerUserName_Type()
)
hzCpSnmpV3ManagerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3ManagerUserName.setStatus("current")


class _HzCpSnmpV3ManagerAuthProtocol_Type(Integer32):
    """Custom type hzCpSnmpV3ManagerAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("md5", 2),
          ("sha", 3))
    )


_HzCpSnmpV3ManagerAuthProtocol_Type.__name__ = "Integer32"
_HzCpSnmpV3ManagerAuthProtocol_Object = MibTableColumn
hzCpSnmpV3ManagerAuthProtocol = _HzCpSnmpV3ManagerAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 5, 1, 3),
    _HzCpSnmpV3ManagerAuthProtocol_Type()
)
hzCpSnmpV3ManagerAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3ManagerAuthProtocol.setStatus("current")


class _HzCpSnmpV3ManagerAuthPassword_Type(DisplayString):
    """Custom type hzCpSnmpV3ManagerAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpSnmpV3ManagerAuthPassword_Type.__name__ = "DisplayString"
_HzCpSnmpV3ManagerAuthPassword_Object = MibTableColumn
hzCpSnmpV3ManagerAuthPassword = _HzCpSnmpV3ManagerAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 5, 1, 4),
    _HzCpSnmpV3ManagerAuthPassword_Type()
)
hzCpSnmpV3ManagerAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3ManagerAuthPassword.setStatus("current")


class _HzCpSnmpV3ManagerPrivProtocol_Type(Integer32):
    """Custom type hzCpSnmpV3ManagerPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPriv", 1),
          ("des", 2))
    )


_HzCpSnmpV3ManagerPrivProtocol_Type.__name__ = "Integer32"
_HzCpSnmpV3ManagerPrivProtocol_Object = MibTableColumn
hzCpSnmpV3ManagerPrivProtocol = _HzCpSnmpV3ManagerPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 5, 1, 5),
    _HzCpSnmpV3ManagerPrivProtocol_Type()
)
hzCpSnmpV3ManagerPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3ManagerPrivProtocol.setStatus("current")


class _HzCpSnmpV3ManagerPrivPassword_Type(DisplayString):
    """Custom type hzCpSnmpV3ManagerPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpSnmpV3ManagerPrivPassword_Type.__name__ = "DisplayString"
_HzCpSnmpV3ManagerPrivPassword_Object = MibTableColumn
hzCpSnmpV3ManagerPrivPassword = _HzCpSnmpV3ManagerPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 5, 1, 6),
    _HzCpSnmpV3ManagerPrivPassword_Type()
)
hzCpSnmpV3ManagerPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3ManagerPrivPassword.setStatus("current")


class _HzCpSnmpV3ManagerActivated_Type(Integer32):
    """Custom type hzCpSnmpV3ManagerActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzCpSnmpV3ManagerActivated_Type.__name__ = "Integer32"
_HzCpSnmpV3ManagerActivated_Object = MibTableColumn
hzCpSnmpV3ManagerActivated = _HzCpSnmpV3ManagerActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 5, 1, 7),
    _HzCpSnmpV3ManagerActivated_Type()
)
hzCpSnmpV3ManagerActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3ManagerActivated.setStatus("current")


class _HzCpSnmpAccessMode_Type(Integer32):
    """Custom type hzCpSnmpAccessMode based on Integer32"""
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
        *(("off", 1),
          ("v1", 2),
          ("v2c", 3),
          ("v3", 4))
    )


_HzCpSnmpAccessMode_Type.__name__ = "Integer32"
_HzCpSnmpAccessMode_Object = MibScalar
hzCpSnmpAccessMode = _HzCpSnmpAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 6),
    _HzCpSnmpAccessMode_Type()
)
hzCpSnmpAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpAccessMode.setStatus("current")
_HzCpSnmpManagersTable_Object = MibTable
hzCpSnmpManagersTable = _HzCpSnmpManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 7)
)
if mibBuilder.loadTexts:
    hzCpSnmpManagersTable.setStatus("current")
_HzCpSnmpManagersEntry_Object = MibTableRow
hzCpSnmpManagersEntry = _HzCpSnmpManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 7, 1)
)
hzCpSnmpManagersEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSnmpManagersIndex"),
)
if mibBuilder.loadTexts:
    hzCpSnmpManagersEntry.setStatus("current")
_HzCpSnmpManagersIndex_Type = Integer32
_HzCpSnmpManagersIndex_Object = MibTableColumn
hzCpSnmpManagersIndex = _HzCpSnmpManagersIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 7, 1, 1),
    _HzCpSnmpManagersIndex_Type()
)
hzCpSnmpManagersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpManagersIndex.setStatus("current")
_HzCpSnmpManagerDomain_Type = InetAddressType
_HzCpSnmpManagerDomain_Object = MibTableColumn
hzCpSnmpManagerDomain = _HzCpSnmpManagerDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 7, 1, 2),
    _HzCpSnmpManagerDomain_Type()
)
hzCpSnmpManagerDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpManagerDomain.setStatus("current")
_HzCpSnmpManagerAddress_Type = InetAddress
_HzCpSnmpManagerAddress_Object = MibTableColumn
hzCpSnmpManagerAddress = _HzCpSnmpManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 7, 1, 3),
    _HzCpSnmpManagerAddress_Type()
)
hzCpSnmpManagerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpManagerAddress.setStatus("current")


class _HzCpSnmpManagerCommunityName_Type(DisplayString):
    """Custom type hzCpSnmpManagerCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpSnmpManagerCommunityName_Type.__name__ = "DisplayString"
_HzCpSnmpManagerCommunityName_Object = MibTableColumn
hzCpSnmpManagerCommunityName = _HzCpSnmpManagerCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 7, 1, 4),
    _HzCpSnmpManagerCommunityName_Type()
)
hzCpSnmpManagerCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpManagerCommunityName.setStatus("current")
_HzCpSnmpManagersPrefixLength_Type = InetAddressPrefixLength
_HzCpSnmpManagersPrefixLength_Object = MibTableColumn
hzCpSnmpManagersPrefixLength = _HzCpSnmpManagersPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 7, 1, 5),
    _HzCpSnmpManagersPrefixLength_Type()
)
hzCpSnmpManagersPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpManagersPrefixLength.setStatus("current")


class _HzCpSnmpManagerActivated_Type(Integer32):
    """Custom type hzCpSnmpManagerActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzCpSnmpManagerActivated_Type.__name__ = "Integer32"
_HzCpSnmpManagerActivated_Object = MibTableColumn
hzCpSnmpManagerActivated = _HzCpSnmpManagerActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 5, 7, 1, 32),
    _HzCpSnmpManagerActivated_Type()
)
hzCpSnmpManagerActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpManagerActivated.setStatus("current")
_HzCpTrapConfig_ObjectIdentity = ObjectIdentity
hzCpTrapConfig = _HzCpTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6)
)
_HzCpSnmpTrapHostDepTable_Object = MibTable
hzCpSnmpTrapHostDepTable = _HzCpSnmpTrapHostDepTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 1)
)
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostDepTable.setStatus("deprecated")
_HzCpSnmpTrapHostDepEntry_Object = MibTableRow
hzCpSnmpTrapHostDepEntry = _HzCpSnmpTrapHostDepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 1, 1)
)
hzCpSnmpTrapHostDepEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSnmpTrapHostIndexDep"),
)
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostDepEntry.setStatus("deprecated")
_HzCpSnmpTrapHostIndexDep_Type = Integer32
_HzCpSnmpTrapHostIndexDep_Object = MibTableColumn
hzCpSnmpTrapHostIndexDep = _HzCpSnmpTrapHostIndexDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 1, 1, 1),
    _HzCpSnmpTrapHostIndexDep_Type()
)
hzCpSnmpTrapHostIndexDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostIndexDep.setStatus("deprecated")
_HzCpSnmpTrapHostIpAddressDep_Type = IpAddress
_HzCpSnmpTrapHostIpAddressDep_Object = MibTableColumn
hzCpSnmpTrapHostIpAddressDep = _HzCpSnmpTrapHostIpAddressDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 1, 1, 2),
    _HzCpSnmpTrapHostIpAddressDep_Type()
)
hzCpSnmpTrapHostIpAddressDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostIpAddressDep.setStatus("deprecated")


class _HzCpSnmpTrapHostCommunityNameDep_Type(DisplayString):
    """Custom type hzCpSnmpTrapHostCommunityNameDep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzCpSnmpTrapHostCommunityNameDep_Type.__name__ = "DisplayString"
_HzCpSnmpTrapHostCommunityNameDep_Object = MibTableColumn
hzCpSnmpTrapHostCommunityNameDep = _HzCpSnmpTrapHostCommunityNameDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 1, 1, 3),
    _HzCpSnmpTrapHostCommunityNameDep_Type()
)
hzCpSnmpTrapHostCommunityNameDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostCommunityNameDep.setStatus("deprecated")


class _HzCpSnmpTrapHostActivatedDep_Type(Integer32):
    """Custom type hzCpSnmpTrapHostActivatedDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzCpSnmpTrapHostActivatedDep_Type.__name__ = "Integer32"
_HzCpSnmpTrapHostActivatedDep_Object = MibTableColumn
hzCpSnmpTrapHostActivatedDep = _HzCpSnmpTrapHostActivatedDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 1, 1, 4),
    _HzCpSnmpTrapHostActivatedDep_Type()
)
hzCpSnmpTrapHostActivatedDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostActivatedDep.setStatus("deprecated")
_HzCpSnmpV3TrapHostsDepTable_Object = MibTable
hzCpSnmpV3TrapHostsDepTable = _HzCpSnmpV3TrapHostsDepTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 2)
)
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostsDepTable.setStatus("deprecated")
_HzCpSnmpV3TrapHostsDepEntry_Object = MibTableRow
hzCpSnmpV3TrapHostsDepEntry = _HzCpSnmpV3TrapHostsDepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 2, 1)
)
hzCpSnmpV3TrapHostsDepEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSnmpV3TrapHostsIndexDep"),
)
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostsDepEntry.setStatus("deprecated")


class _HzCpSnmpV3TrapHostsIndexDep_Type(Integer32):
    """Custom type hzCpSnmpV3TrapHostsIndexDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HzCpSnmpV3TrapHostsIndexDep_Type.__name__ = "Integer32"
_HzCpSnmpV3TrapHostsIndexDep_Object = MibTableColumn
hzCpSnmpV3TrapHostsIndexDep = _HzCpSnmpV3TrapHostsIndexDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 2, 1, 1),
    _HzCpSnmpV3TrapHostsIndexDep_Type()
)
hzCpSnmpV3TrapHostsIndexDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostsIndexDep.setStatus("deprecated")
_HzCpSnmpV3TrapHostIpAddressDep_Type = IpAddress
_HzCpSnmpV3TrapHostIpAddressDep_Object = MibTableColumn
hzCpSnmpV3TrapHostIpAddressDep = _HzCpSnmpV3TrapHostIpAddressDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 2, 1, 2),
    _HzCpSnmpV3TrapHostIpAddressDep_Type()
)
hzCpSnmpV3TrapHostIpAddressDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostIpAddressDep.setStatus("deprecated")


class _HzCpSnmpV3TrapHostUserNameDep_Type(DisplayString):
    """Custom type hzCpSnmpV3TrapHostUserNameDep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzCpSnmpV3TrapHostUserNameDep_Type.__name__ = "DisplayString"
_HzCpSnmpV3TrapHostUserNameDep_Object = MibTableColumn
hzCpSnmpV3TrapHostUserNameDep = _HzCpSnmpV3TrapHostUserNameDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 2, 1, 3),
    _HzCpSnmpV3TrapHostUserNameDep_Type()
)
hzCpSnmpV3TrapHostUserNameDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostUserNameDep.setStatus("deprecated")


class _HzCpSnmpV3TrapHostAuthProtocolDep_Type(Integer32):
    """Custom type hzCpSnmpV3TrapHostAuthProtocolDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("md5", 2),
          ("sha", 3))
    )


_HzCpSnmpV3TrapHostAuthProtocolDep_Type.__name__ = "Integer32"
_HzCpSnmpV3TrapHostAuthProtocolDep_Object = MibTableColumn
hzCpSnmpV3TrapHostAuthProtocolDep = _HzCpSnmpV3TrapHostAuthProtocolDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 2, 1, 4),
    _HzCpSnmpV3TrapHostAuthProtocolDep_Type()
)
hzCpSnmpV3TrapHostAuthProtocolDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostAuthProtocolDep.setStatus("deprecated")


class _HzCpSnmpV3TrapHostAuthPasswordDep_Type(DisplayString):
    """Custom type hzCpSnmpV3TrapHostAuthPasswordDep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzCpSnmpV3TrapHostAuthPasswordDep_Type.__name__ = "DisplayString"
_HzCpSnmpV3TrapHostAuthPasswordDep_Object = MibTableColumn
hzCpSnmpV3TrapHostAuthPasswordDep = _HzCpSnmpV3TrapHostAuthPasswordDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 2, 1, 5),
    _HzCpSnmpV3TrapHostAuthPasswordDep_Type()
)
hzCpSnmpV3TrapHostAuthPasswordDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostAuthPasswordDep.setStatus("deprecated")


class _HzCpSnmpV3TrapHostPrivProtocolDep_Type(Integer32):
    """Custom type hzCpSnmpV3TrapHostPrivProtocolDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPriv", 1),
          ("des", 2))
    )


_HzCpSnmpV3TrapHostPrivProtocolDep_Type.__name__ = "Integer32"
_HzCpSnmpV3TrapHostPrivProtocolDep_Object = MibTableColumn
hzCpSnmpV3TrapHostPrivProtocolDep = _HzCpSnmpV3TrapHostPrivProtocolDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 2, 1, 6),
    _HzCpSnmpV3TrapHostPrivProtocolDep_Type()
)
hzCpSnmpV3TrapHostPrivProtocolDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostPrivProtocolDep.setStatus("deprecated")


class _HzCpSnmpV3TrapHostPrivPasswordDep_Type(DisplayString):
    """Custom type hzCpSnmpV3TrapHostPrivPasswordDep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzCpSnmpV3TrapHostPrivPasswordDep_Type.__name__ = "DisplayString"
_HzCpSnmpV3TrapHostPrivPasswordDep_Object = MibTableColumn
hzCpSnmpV3TrapHostPrivPasswordDep = _HzCpSnmpV3TrapHostPrivPasswordDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 2, 1, 7),
    _HzCpSnmpV3TrapHostPrivPasswordDep_Type()
)
hzCpSnmpV3TrapHostPrivPasswordDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostPrivPasswordDep.setStatus("deprecated")


class _HzCpSnmpV3TrapHostActivatedDep_Type(Integer32):
    """Custom type hzCpSnmpV3TrapHostActivatedDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzCpSnmpV3TrapHostActivatedDep_Type.__name__ = "Integer32"
_HzCpSnmpV3TrapHostActivatedDep_Object = MibTableColumn
hzCpSnmpV3TrapHostActivatedDep = _HzCpSnmpV3TrapHostActivatedDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 2, 1, 8),
    _HzCpSnmpV3TrapHostActivatedDep_Type()
)
hzCpSnmpV3TrapHostActivatedDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostActivatedDep.setStatus("deprecated")
_HzCpTrapEnable_ObjectIdentity = ObjectIdentity
hzCpTrapEnable = _HzCpTrapEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3)
)


class _HzCpColdStartTrap_Type(Integer32):
    """Custom type hzCpColdStartTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpColdStartTrap_Type.__name__ = "Integer32"
_HzCpColdStartTrap_Object = MibScalar
hzCpColdStartTrap = _HzCpColdStartTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 1),
    _HzCpColdStartTrap_Type()
)
hzCpColdStartTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpColdStartTrap.setStatus("current")


class _HzCpLinkDownTrap_Type(Integer32):
    """Custom type hzCpLinkDownTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpLinkDownTrap_Type.__name__ = "Integer32"
_HzCpLinkDownTrap_Object = MibScalar
hzCpLinkDownTrap = _HzCpLinkDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 2),
    _HzCpLinkDownTrap_Type()
)
hzCpLinkDownTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpLinkDownTrap.setStatus("current")


class _HzCpPeerAuthenticationFailureTrap_Type(Integer32):
    """Custom type hzCpPeerAuthenticationFailureTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpPeerAuthenticationFailureTrap_Type.__name__ = "Integer32"
_HzCpPeerAuthenticationFailureTrap_Object = MibScalar
hzCpPeerAuthenticationFailureTrap = _HzCpPeerAuthenticationFailureTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 3),
    _HzCpPeerAuthenticationFailureTrap_Type()
)
hzCpPeerAuthenticationFailureTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPeerAuthenticationFailureTrap.setStatus("current")


class _HzCpHitlessAamConfigMismatchTrap_Type(Integer32):
    """Custom type hzCpHitlessAamConfigMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpHitlessAamConfigMismatchTrap_Type.__name__ = "Integer32"
_HzCpHitlessAamConfigMismatchTrap_Object = MibScalar
hzCpHitlessAamConfigMismatchTrap = _HzCpHitlessAamConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 4),
    _HzCpHitlessAamConfigMismatchTrap_Type()
)
hzCpHitlessAamConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHitlessAamConfigMismatchTrap.setStatus("current")


class _HzCpHitlessAamModulationLoweredTrap_Type(Integer32):
    """Custom type hzCpHitlessAamModulationLoweredTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpHitlessAamModulationLoweredTrap_Type.__name__ = "Integer32"
_HzCpHitlessAamModulationLoweredTrap_Object = MibScalar
hzCpHitlessAamModulationLoweredTrap = _HzCpHitlessAamModulationLoweredTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 5),
    _HzCpHitlessAamModulationLoweredTrap_Type()
)
hzCpHitlessAamModulationLoweredTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHitlessAamModulationLoweredTrap.setStatus("current")


class _HzCpHitlessAamModulationChangedEventTrap_Type(Integer32):
    """Custom type hzCpHitlessAamModulationChangedEventTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpHitlessAamModulationChangedEventTrap_Type.__name__ = "Integer32"
_HzCpHitlessAamModulationChangedEventTrap_Object = MibScalar
hzCpHitlessAamModulationChangedEventTrap = _HzCpHitlessAamModulationChangedEventTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 6),
    _HzCpHitlessAamModulationChangedEventTrap_Type()
)
hzCpHitlessAamModulationChangedEventTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHitlessAamModulationChangedEventTrap.setStatus("current")


class _HzCpAtpcConfigMismatchTrap_Type(Integer32):
    """Custom type hzCpAtpcConfigMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpAtpcConfigMismatchTrap_Type.__name__ = "Integer32"
_HzCpAtpcConfigMismatchTrap_Object = MibScalar
hzCpAtpcConfigMismatchTrap = _HzCpAtpcConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 7),
    _HzCpAtpcConfigMismatchTrap_Type()
)
hzCpAtpcConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpAtpcConfigMismatchTrap.setStatus("current")


class _HzCpAtpcAutoDisabledTrap_Type(Integer32):
    """Custom type hzCpAtpcAutoDisabledTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpAtpcAutoDisabledTrap_Type.__name__ = "Integer32"
_HzCpAtpcAutoDisabledTrap_Object = MibScalar
hzCpAtpcAutoDisabledTrap = _HzCpAtpcAutoDisabledTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 8),
    _HzCpAtpcAutoDisabledTrap_Type()
)
hzCpAtpcAutoDisabledTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpAtpcAutoDisabledTrap.setStatus("current")


class _HzCpNoSntpServersReachableTrap_Type(Integer32):
    """Custom type hzCpNoSntpServersReachableTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpNoSntpServersReachableTrap_Type.__name__ = "Integer32"
_HzCpNoSntpServersReachableTrap_Object = MibScalar
hzCpNoSntpServersReachableTrap = _HzCpNoSntpServersReachableTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 9),
    _HzCpNoSntpServersReachableTrap_Type()
)
hzCpNoSntpServersReachableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpNoSntpServersReachableTrap.setStatus("current")


class _HzCpFrequencyFileInvalidTrap_Type(Integer32):
    """Custom type hzCpFrequencyFileInvalidTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpFrequencyFileInvalidTrap_Type.__name__ = "Integer32"
_HzCpFrequencyFileInvalidTrap_Object = MibScalar
hzCpFrequencyFileInvalidTrap = _HzCpFrequencyFileInvalidTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 10),
    _HzCpFrequencyFileInvalidTrap_Type()
)
hzCpFrequencyFileInvalidTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpFrequencyFileInvalidTrap.setStatus("current")


class _HzCpAggregateDroppedFramesThresholdTrap_Type(Integer32):
    """Custom type hzCpAggregateDroppedFramesThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpAggregateDroppedFramesThresholdTrap_Type.__name__ = "Integer32"
_HzCpAggregateDroppedFramesThresholdTrap_Object = MibScalar
hzCpAggregateDroppedFramesThresholdTrap = _HzCpAggregateDroppedFramesThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 11),
    _HzCpAggregateDroppedFramesThresholdTrap_Type()
)
hzCpAggregateDroppedFramesThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpAggregateDroppedFramesThresholdTrap.setStatus("current")


class _HzCpQueueDroppedFramesThresholdTrap_Type(Integer32):
    """Custom type hzCpQueueDroppedFramesThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpQueueDroppedFramesThresholdTrap_Type.__name__ = "Integer32"
_HzCpQueueDroppedFramesThresholdTrap_Object = MibScalar
hzCpQueueDroppedFramesThresholdTrap = _HzCpQueueDroppedFramesThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 12),
    _HzCpQueueDroppedFramesThresholdTrap_Type()
)
hzCpQueueDroppedFramesThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpQueueDroppedFramesThresholdTrap.setStatus("current")


class _HzCpBwUtilizationThresholdTrap_Type(Integer32):
    """Custom type hzCpBwUtilizationThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpBwUtilizationThresholdTrap_Type.__name__ = "Integer32"
_HzCpBwUtilizationThresholdTrap_Object = MibScalar
hzCpBwUtilizationThresholdTrap = _HzCpBwUtilizationThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 13),
    _HzCpBwUtilizationThresholdTrap_Type()
)
hzCpBwUtilizationThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwUtilizationThresholdTrap.setStatus("current")


class _HzCpQueueDepthThresholdTrap_Type(Integer32):
    """Custom type hzCpQueueDepthThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpQueueDepthThresholdTrap_Type.__name__ = "Integer32"
_HzCpQueueDepthThresholdTrap_Object = MibScalar
hzCpQueueDepthThresholdTrap = _HzCpQueueDepthThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 14),
    _HzCpQueueDepthThresholdTrap_Type()
)
hzCpQueueDepthThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpQueueDepthThresholdTrap.setStatus("current")


class _HzCpRlsConfigMismatchTrap_Type(Integer32):
    """Custom type hzCpRlsConfigMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRlsConfigMismatchTrap_Type.__name__ = "Integer32"
_HzCpRlsConfigMismatchTrap_Object = MibScalar
hzCpRlsConfigMismatchTrap = _HzCpRlsConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 15),
    _HzCpRlsConfigMismatchTrap_Type()
)
hzCpRlsConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsConfigMismatchTrap.setStatus("current")


class _HzCpRlsShutdownActivatedTrap_Type(Integer32):
    """Custom type hzCpRlsShutdownActivatedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRlsShutdownActivatedTrap_Type.__name__ = "Integer32"
_HzCpRlsShutdownActivatedTrap_Object = MibScalar
hzCpRlsShutdownActivatedTrap = _HzCpRlsShutdownActivatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 16),
    _HzCpRlsShutdownActivatedTrap_Type()
)
hzCpRlsShutdownActivatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsShutdownActivatedTrap.setStatus("current")


class _HzCpRlsQueueBasedShutdownActivatedTrap_Type(Integer32):
    """Custom type hzCpRlsQueueBasedShutdownActivatedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRlsQueueBasedShutdownActivatedTrap_Type.__name__ = "Integer32"
_HzCpRlsQueueBasedShutdownActivatedTrap_Object = MibScalar
hzCpRlsQueueBasedShutdownActivatedTrap = _HzCpRlsQueueBasedShutdownActivatedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 17),
    _HzCpRlsQueueBasedShutdownActivatedTrap_Type()
)
hzCpRlsQueueBasedShutdownActivatedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsQueueBasedShutdownActivatedTrap.setStatus("current")


class _HzCpModemRxLossOfSignalLockTrap_Type(Integer32):
    """Custom type hzCpModemRxLossOfSignalLockTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpModemRxLossOfSignalLockTrap_Type.__name__ = "Integer32"
_HzCpModemRxLossOfSignalLockTrap_Object = MibScalar
hzCpModemRxLossOfSignalLockTrap = _HzCpModemRxLossOfSignalLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 18),
    _HzCpModemRxLossOfSignalLockTrap_Type()
)
hzCpModemRxLossOfSignalLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpModemRxLossOfSignalLockTrap.setStatus("current")


class _HzCpModemSnrBelowThresholdTrap_Type(Integer32):
    """Custom type hzCpModemSnrBelowThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpModemSnrBelowThresholdTrap_Type.__name__ = "Integer32"
_HzCpModemSnrBelowThresholdTrap_Object = MibScalar
hzCpModemSnrBelowThresholdTrap = _HzCpModemSnrBelowThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 19),
    _HzCpModemSnrBelowThresholdTrap_Type()
)
hzCpModemSnrBelowThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpModemSnrBelowThresholdTrap.setStatus("current")


class _HzCpModemEqualizerStressThresholdTrap_Type(Integer32):
    """Custom type hzCpModemEqualizerStressThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpModemEqualizerStressThresholdTrap_Type.__name__ = "Integer32"
_HzCpModemEqualizerStressThresholdTrap_Object = MibScalar
hzCpModemEqualizerStressThresholdTrap = _HzCpModemEqualizerStressThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 20),
    _HzCpModemEqualizerStressThresholdTrap_Type()
)
hzCpModemEqualizerStressThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpModemEqualizerStressThresholdTrap.setStatus("current")


class _HzCpRslBelowThresholdTrap_Type(Integer32):
    """Custom type hzCpRslBelowThresholdTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRslBelowThresholdTrap_Type.__name__ = "Integer32"
_HzCpRslBelowThresholdTrap_Object = MibScalar
hzCpRslBelowThresholdTrap = _HzCpRslBelowThresholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 21),
    _HzCpRslBelowThresholdTrap_Type()
)
hzCpRslBelowThresholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRslBelowThresholdTrap.setStatus("current")


class _HzCpRadioSynthLostLockTrap_Type(Integer32):
    """Custom type hzCpRadioSynthLostLockTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRadioSynthLostLockTrap_Type.__name__ = "Integer32"
_HzCpRadioSynthLostLockTrap_Object = MibScalar
hzCpRadioSynthLostLockTrap = _HzCpRadioSynthLostLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 22),
    _HzCpRadioSynthLostLockTrap_Type()
)
hzCpRadioSynthLostLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadioSynthLostLockTrap.setStatus("current")


class _HzCpRadioCalTableNotAvailableTrap_Type(Integer32):
    """Custom type hzCpRadioCalTableNotAvailableTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRadioCalTableNotAvailableTrap_Type.__name__ = "Integer32"
_HzCpRadioCalTableNotAvailableTrap_Object = MibScalar
hzCpRadioCalTableNotAvailableTrap = _HzCpRadioCalTableNotAvailableTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 23),
    _HzCpRadioCalTableNotAvailableTrap_Type()
)
hzCpRadioCalTableNotAvailableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadioCalTableNotAvailableTrap.setStatus("current")


class _HzCpRadioDrainCurrentOutOfLimitTrap_Type(Integer32):
    """Custom type hzCpRadioDrainCurrentOutOfLimitTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRadioDrainCurrentOutOfLimitTrap_Type.__name__ = "Integer32"
_HzCpRadioDrainCurrentOutOfLimitTrap_Object = MibScalar
hzCpRadioDrainCurrentOutOfLimitTrap = _HzCpRadioDrainCurrentOutOfLimitTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 24),
    _HzCpRadioDrainCurrentOutOfLimitTrap_Type()
)
hzCpRadioDrainCurrentOutOfLimitTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadioDrainCurrentOutOfLimitTrap.setStatus("current")


class _HzCpRadioPowerAmplifierTrap_Type(Integer32):
    """Custom type hzCpRadioPowerAmplifierTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRadioPowerAmplifierTrap_Type.__name__ = "Integer32"
_HzCpRadioPowerAmplifierTrap_Object = MibScalar
hzCpRadioPowerAmplifierTrap = _HzCpRadioPowerAmplifierTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 25),
    _HzCpRadioPowerAmplifierTrap_Type()
)
hzCpRadioPowerAmplifierTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadioPowerAmplifierTrap.setStatus("current")


class _HzCpTemperatureOutOfLimitTrap_Type(Integer32):
    """Custom type hzCpTemperatureOutOfLimitTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpTemperatureOutOfLimitTrap_Type.__name__ = "Integer32"
_HzCpTemperatureOutOfLimitTrap_Object = MibScalar
hzCpTemperatureOutOfLimitTrap = _HzCpTemperatureOutOfLimitTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 26),
    _HzCpTemperatureOutOfLimitTrap_Type()
)
hzCpTemperatureOutOfLimitTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpTemperatureOutOfLimitTrap.setStatus("current")


class _HzCpRedundancyConfigMismatchTrap_Type(Integer32):
    """Custom type hzCpRedundancyConfigMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRedundancyConfigMismatchTrap_Type.__name__ = "Integer32"
_HzCpRedundancyConfigMismatchTrap_Object = MibScalar
hzCpRedundancyConfigMismatchTrap = _HzCpRedundancyConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 27),
    _HzCpRedundancyConfigMismatchTrap_Type()
)
hzCpRedundancyConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyConfigMismatchTrap.setStatus("current")


class _HzCpRedundancyActiveOnSecondaryTrap_Type(Integer32):
    """Custom type hzCpRedundancyActiveOnSecondaryTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRedundancyActiveOnSecondaryTrap_Type.__name__ = "Integer32"
_HzCpRedundancyActiveOnSecondaryTrap_Object = MibScalar
hzCpRedundancyActiveOnSecondaryTrap = _HzCpRedundancyActiveOnSecondaryTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 28),
    _HzCpRedundancyActiveOnSecondaryTrap_Type()
)
hzCpRedundancyActiveOnSecondaryTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyActiveOnSecondaryTrap.setStatus("current")


class _HzCpRedundancyOperatingInForcedSwitchTrap_Type(Integer32):
    """Custom type hzCpRedundancyOperatingInForcedSwitchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRedundancyOperatingInForcedSwitchTrap_Type.__name__ = "Integer32"
_HzCpRedundancyOperatingInForcedSwitchTrap_Object = MibScalar
hzCpRedundancyOperatingInForcedSwitchTrap = _HzCpRedundancyOperatingInForcedSwitchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 29),
    _HzCpRedundancyOperatingInForcedSwitchTrap_Type()
)
hzCpRedundancyOperatingInForcedSwitchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyOperatingInForcedSwitchTrap.setStatus("current")


class _HzCpRedundancyEnetCrossLinkTrap_Type(Integer32):
    """Custom type hzCpRedundancyEnetCrossLinkTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRedundancyEnetCrossLinkTrap_Type.__name__ = "Integer32"
_HzCpRedundancyEnetCrossLinkTrap_Object = MibScalar
hzCpRedundancyEnetCrossLinkTrap = _HzCpRedundancyEnetCrossLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 30),
    _HzCpRedundancyEnetCrossLinkTrap_Type()
)
hzCpRedundancyEnetCrossLinkTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyEnetCrossLinkTrap.setStatus("current")


class _HzCpRedundancyActiveUsingPartnerWLinkTrap_Type(Integer32):
    """Custom type hzCpRedundancyActiveUsingPartnerWLinkTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRedundancyActiveUsingPartnerWLinkTrap_Type.__name__ = "Integer32"
_HzCpRedundancyActiveUsingPartnerWLinkTrap_Object = MibScalar
hzCpRedundancyActiveUsingPartnerWLinkTrap = _HzCpRedundancyActiveUsingPartnerWLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 31),
    _HzCpRedundancyActiveUsingPartnerWLinkTrap_Type()
)
hzCpRedundancyActiveUsingPartnerWLinkTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyActiveUsingPartnerWLinkTrap.setStatus("current")


class _HzCpRedundancyStandbyWLinkInUseTrap_Type(Integer32):
    """Custom type hzCpRedundancyStandbyWLinkInUseTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRedundancyStandbyWLinkInUseTrap_Type.__name__ = "Integer32"
_HzCpRedundancyStandbyWLinkInUseTrap_Object = MibScalar
hzCpRedundancyStandbyWLinkInUseTrap = _HzCpRedundancyStandbyWLinkInUseTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 32),
    _HzCpRedundancyStandbyWLinkInUseTrap_Type()
)
hzCpRedundancyStandbyWLinkInUseTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyStandbyWLinkInUseTrap.setStatus("current")


class _HzCpRedundancyStandbyOnPrimaryTrap_Type(Integer32):
    """Custom type hzCpRedundancyStandbyOnPrimaryTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRedundancyStandbyOnPrimaryTrap_Type.__name__ = "Integer32"
_HzCpRedundancyStandbyOnPrimaryTrap_Object = MibScalar
hzCpRedundancyStandbyOnPrimaryTrap = _HzCpRedundancyStandbyOnPrimaryTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 33),
    _HzCpRedundancyStandbyOnPrimaryTrap_Type()
)
hzCpRedundancyStandbyOnPrimaryTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRedundancyStandbyOnPrimaryTrap.setStatus("current")


class _HzCpX2DeliveringHalfCapacityTrap_Type(Integer32):
    """Custom type hzCpX2DeliveringHalfCapacityTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpX2DeliveringHalfCapacityTrap_Type.__name__ = "Integer32"
_HzCpX2DeliveringHalfCapacityTrap_Object = MibScalar
hzCpX2DeliveringHalfCapacityTrap = _HzCpX2DeliveringHalfCapacityTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 34),
    _HzCpX2DeliveringHalfCapacityTrap_Type()
)
hzCpX2DeliveringHalfCapacityTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpX2DeliveringHalfCapacityTrap.setStatus("current")


class _HzCpBncCableSignalNotDetectedTrap_Type(Integer32):
    """Custom type hzCpBncCableSignalNotDetectedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpBncCableSignalNotDetectedTrap_Type.__name__ = "Integer32"
_HzCpBncCableSignalNotDetectedTrap_Object = MibScalar
hzCpBncCableSignalNotDetectedTrap = _HzCpBncCableSignalNotDetectedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 35),
    _HzCpBncCableSignalNotDetectedTrap_Type()
)
hzCpBncCableSignalNotDetectedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBncCableSignalNotDetectedTrap.setStatus("current")


class _HzCpEthernetSpeedReducedTrap_Type(Integer32):
    """Custom type hzCpEthernetSpeedReducedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpEthernetSpeedReducedTrap_Type.__name__ = "Integer32"
_HzCpEthernetSpeedReducedTrap_Object = MibScalar
hzCpEthernetSpeedReducedTrap = _HzCpEthernetSpeedReducedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 36),
    _HzCpEthernetSpeedReducedTrap_Type()
)
hzCpEthernetSpeedReducedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEthernetSpeedReducedTrap.setStatus("current")


class _HzCpSynceLostLockTrap_Type(Integer32):
    """Custom type hzCpSynceLostLockTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpSynceLostLockTrap_Type.__name__ = "Integer32"
_HzCpSynceLostLockTrap_Object = MibScalar
hzCpSynceLostLockTrap = _HzCpSynceLostLockTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 37),
    _HzCpSynceLostLockTrap_Type()
)
hzCpSynceLostLockTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSynceLostLockTrap.setStatus("current")


class _HzCpSynceSecondarySourceInUseTrap_Type(Integer32):
    """Custom type hzCpSynceSecondarySourceInUseTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpSynceSecondarySourceInUseTrap_Type.__name__ = "Integer32"
_HzCpSynceSecondarySourceInUseTrap_Object = MibScalar
hzCpSynceSecondarySourceInUseTrap = _HzCpSynceSecondarySourceInUseTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 38),
    _HzCpSynceSecondarySourceInUseTrap_Type()
)
hzCpSynceSecondarySourceInUseTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSynceSecondarySourceInUseTrap.setStatus("current")


class _HzCpUserSessionTrap_Type(Integer32):
    """Custom type hzCpUserSessionTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpUserSessionTrap_Type.__name__ = "Integer32"
_HzCpUserSessionTrap_Object = MibScalar
hzCpUserSessionTrap = _HzCpUserSessionTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 39),
    _HzCpUserSessionTrap_Type()
)
hzCpUserSessionTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpUserSessionTrap.setStatus("current")


class _HzCpInvalidSystemConfigTrap_Type(Integer32):
    """Custom type hzCpInvalidSystemConfigTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpInvalidSystemConfigTrap_Type.__name__ = "Integer32"
_HzCpInvalidSystemConfigTrap_Object = MibScalar
hzCpInvalidSystemConfigTrap = _HzCpInvalidSystemConfigTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 40),
    _HzCpInvalidSystemConfigTrap_Type()
)
hzCpInvalidSystemConfigTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpInvalidSystemConfigTrap.setStatus("current")


class _HzCpMibChangeNotSavedTrap_Type(Integer32):
    """Custom type hzCpMibChangeNotSavedTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpMibChangeNotSavedTrap_Type.__name__ = "Integer32"
_HzCpMibChangeNotSavedTrap_Object = MibScalar
hzCpMibChangeNotSavedTrap = _HzCpMibChangeNotSavedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 41),
    _HzCpMibChangeNotSavedTrap_Type()
)
hzCpMibChangeNotSavedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpMibChangeNotSavedTrap.setStatus("current")


class _HzCpTransmitterLossOfSyncTrap_Type(Integer32):
    """Custom type hzCpTransmitterLossOfSyncTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpTransmitterLossOfSyncTrap_Type.__name__ = "Integer32"
_HzCpTransmitterLossOfSyncTrap_Object = MibScalar
hzCpTransmitterLossOfSyncTrap = _HzCpTransmitterLossOfSyncTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 42),
    _HzCpTransmitterLossOfSyncTrap_Type()
)
hzCpTransmitterLossOfSyncTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpTransmitterLossOfSyncTrap.setStatus("current")


class _HzCpRadioLinearityCalErrorTrap_Type(Integer32):
    """Custom type hzCpRadioLinearityCalErrorTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRadioLinearityCalErrorTrap_Type.__name__ = "Integer32"
_HzCpRadioLinearityCalErrorTrap_Object = MibScalar
hzCpRadioLinearityCalErrorTrap = _HzCpRadioLinearityCalErrorTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 43),
    _HzCpRadioLinearityCalErrorTrap_Type()
)
hzCpRadioLinearityCalErrorTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadioLinearityCalErrorTrap.setStatus("current")


class _HzCpSynceConfigMismatchTrap_Type(Integer32):
    """Custom type hzCpSynceConfigMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpSynceConfigMismatchTrap_Type.__name__ = "Integer32"
_HzCpSynceConfigMismatchTrap_Object = MibScalar
hzCpSynceConfigMismatchTrap = _HzCpSynceConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 44),
    _HzCpSynceConfigMismatchTrap_Type()
)
hzCpSynceConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSynceConfigMismatchTrap.setStatus("current")


class _HzCpCryptoPowerUpTestsFailedTrap_Type(Integer32):
    """Custom type hzCpCryptoPowerUpTestsFailedTrap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpCryptoPowerUpTestsFailedTrap_Type.__name__ = "Integer32"
_HzCpCryptoPowerUpTestsFailedTrap_Object = MibScalar
hzCpCryptoPowerUpTestsFailedTrap = _HzCpCryptoPowerUpTestsFailedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 45),
    _HzCpCryptoPowerUpTestsFailedTrap_Type()
)
hzCpCryptoPowerUpTestsFailedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCryptoPowerUpTestsFailedTrap.setStatus("current")


class _HzCpCryptoConfigMismatchTrap_Type(Integer32):
    """Custom type hzCpCryptoConfigMismatchTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpCryptoConfigMismatchTrap_Type.__name__ = "Integer32"
_HzCpCryptoConfigMismatchTrap_Object = MibScalar
hzCpCryptoConfigMismatchTrap = _HzCpCryptoConfigMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 46),
    _HzCpCryptoConfigMismatchTrap_Type()
)
hzCpCryptoConfigMismatchTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCryptoConfigMismatchTrap.setStatus("current")


class _HzCpSystemTimeChangeTrap_Type(Integer32):
    """Custom type hzCpSystemTimeChangeTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpSystemTimeChangeTrap_Type.__name__ = "Integer32"
_HzCpSystemTimeChangeTrap_Object = MibScalar
hzCpSystemTimeChangeTrap = _HzCpSystemTimeChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 47),
    _HzCpSystemTimeChangeTrap_Type()
)
hzCpSystemTimeChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSystemTimeChangeTrap.setStatus("current")


class _HzCpCodeCheckTrap_Type(Integer32):
    """Custom type hzCpCodeCheckTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpCodeCheckTrap_Type.__name__ = "Integer32"
_HzCpCodeCheckTrap_Object = MibScalar
hzCpCodeCheckTrap = _HzCpCodeCheckTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 48),
    _HzCpCodeCheckTrap_Type()
)
hzCpCodeCheckTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCodeCheckTrap.setStatus("current")


class _HzCpConfigChangedTrap_Type(Integer32):
    """Custom type hzCpConfigChangedTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpConfigChangedTrap_Type.__name__ = "Integer32"
_HzCpConfigChangedTrap_Object = MibScalar
hzCpConfigChangedTrap = _HzCpConfigChangedTrap_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 3, 49),
    _HzCpConfigChangedTrap_Type()
)
hzCpConfigChangedTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpConfigChangedTrap.setStatus("current")
_HzCpSnmpTrapHostTable_Object = MibTable
hzCpSnmpTrapHostTable = _HzCpSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 4)
)
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostTable.setStatus("current")
_HzCpSnmpTrapHostEntry_Object = MibTableRow
hzCpSnmpTrapHostEntry = _HzCpSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 4, 1)
)
hzCpSnmpTrapHostEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSnmpTrapHostIndex"),
)
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostEntry.setStatus("current")
_HzCpSnmpTrapHostIndex_Type = Integer32
_HzCpSnmpTrapHostIndex_Object = MibTableColumn
hzCpSnmpTrapHostIndex = _HzCpSnmpTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 4, 1, 1),
    _HzCpSnmpTrapHostIndex_Type()
)
hzCpSnmpTrapHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostIndex.setStatus("current")
_HzCpSnmpTrapHostDomain_Type = InetAddressType
_HzCpSnmpTrapHostDomain_Object = MibTableColumn
hzCpSnmpTrapHostDomain = _HzCpSnmpTrapHostDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 4, 1, 2),
    _HzCpSnmpTrapHostDomain_Type()
)
hzCpSnmpTrapHostDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostDomain.setStatus("current")
_HzCpSnmpTrapHostAddress_Type = InetAddress
_HzCpSnmpTrapHostAddress_Object = MibTableColumn
hzCpSnmpTrapHostAddress = _HzCpSnmpTrapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 4, 1, 3),
    _HzCpSnmpTrapHostAddress_Type()
)
hzCpSnmpTrapHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostAddress.setStatus("current")


class _HzCpSnmpTrapHostCommunityName_Type(DisplayString):
    """Custom type hzCpSnmpTrapHostCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpSnmpTrapHostCommunityName_Type.__name__ = "DisplayString"
_HzCpSnmpTrapHostCommunityName_Object = MibTableColumn
hzCpSnmpTrapHostCommunityName = _HzCpSnmpTrapHostCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 4, 1, 4),
    _HzCpSnmpTrapHostCommunityName_Type()
)
hzCpSnmpTrapHostCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostCommunityName.setStatus("current")


class _HzCpSnmpTrapHostActivated_Type(Integer32):
    """Custom type hzCpSnmpTrapHostActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzCpSnmpTrapHostActivated_Type.__name__ = "Integer32"
_HzCpSnmpTrapHostActivated_Object = MibTableColumn
hzCpSnmpTrapHostActivated = _HzCpSnmpTrapHostActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 4, 1, 32),
    _HzCpSnmpTrapHostActivated_Type()
)
hzCpSnmpTrapHostActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpTrapHostActivated.setStatus("current")
_HzCpSnmpV3TrapHostsTable_Object = MibTable
hzCpSnmpV3TrapHostsTable = _HzCpSnmpV3TrapHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5)
)
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostsTable.setStatus("current")
_HzCpSnmpV3TrapHostsEntry_Object = MibTableRow
hzCpSnmpV3TrapHostsEntry = _HzCpSnmpV3TrapHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5, 1)
)
hzCpSnmpV3TrapHostsEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSnmpV3TrapHostsIndex"),
)
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostsEntry.setStatus("current")


class _HzCpSnmpV3TrapHostsIndex_Type(Integer32):
    """Custom type hzCpSnmpV3TrapHostsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HzCpSnmpV3TrapHostsIndex_Type.__name__ = "Integer32"
_HzCpSnmpV3TrapHostsIndex_Object = MibTableColumn
hzCpSnmpV3TrapHostsIndex = _HzCpSnmpV3TrapHostsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5, 1, 1),
    _HzCpSnmpV3TrapHostsIndex_Type()
)
hzCpSnmpV3TrapHostsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostsIndex.setStatus("current")
_HzCpSnmpV3TrapHostDomain_Type = InetAddressType
_HzCpSnmpV3TrapHostDomain_Object = MibTableColumn
hzCpSnmpV3TrapHostDomain = _HzCpSnmpV3TrapHostDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5, 1, 2),
    _HzCpSnmpV3TrapHostDomain_Type()
)
hzCpSnmpV3TrapHostDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostDomain.setStatus("current")
_HzCpSnmpV3TrapHostAddress_Type = InetAddress
_HzCpSnmpV3TrapHostAddress_Object = MibTableColumn
hzCpSnmpV3TrapHostAddress = _HzCpSnmpV3TrapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5, 1, 3),
    _HzCpSnmpV3TrapHostAddress_Type()
)
hzCpSnmpV3TrapHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostAddress.setStatus("current")


class _HzCpSnmpV3TrapHostUserName_Type(DisplayString):
    """Custom type hzCpSnmpV3TrapHostUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpSnmpV3TrapHostUserName_Type.__name__ = "DisplayString"
_HzCpSnmpV3TrapHostUserName_Object = MibTableColumn
hzCpSnmpV3TrapHostUserName = _HzCpSnmpV3TrapHostUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5, 1, 4),
    _HzCpSnmpV3TrapHostUserName_Type()
)
hzCpSnmpV3TrapHostUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostUserName.setStatus("current")


class _HzCpSnmpV3TrapHostAuthProtocol_Type(Integer32):
    """Custom type hzCpSnmpV3TrapHostAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuth", 1),
          ("md5", 2),
          ("sha", 3))
    )


_HzCpSnmpV3TrapHostAuthProtocol_Type.__name__ = "Integer32"
_HzCpSnmpV3TrapHostAuthProtocol_Object = MibTableColumn
hzCpSnmpV3TrapHostAuthProtocol = _HzCpSnmpV3TrapHostAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5, 1, 5),
    _HzCpSnmpV3TrapHostAuthProtocol_Type()
)
hzCpSnmpV3TrapHostAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostAuthProtocol.setStatus("current")


class _HzCpSnmpV3TrapHostAuthPassword_Type(DisplayString):
    """Custom type hzCpSnmpV3TrapHostAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpSnmpV3TrapHostAuthPassword_Type.__name__ = "DisplayString"
_HzCpSnmpV3TrapHostAuthPassword_Object = MibTableColumn
hzCpSnmpV3TrapHostAuthPassword = _HzCpSnmpV3TrapHostAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5, 1, 6),
    _HzCpSnmpV3TrapHostAuthPassword_Type()
)
hzCpSnmpV3TrapHostAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostAuthPassword.setStatus("current")


class _HzCpSnmpV3TrapHostPrivProtocol_Type(Integer32):
    """Custom type hzCpSnmpV3TrapHostPrivProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPriv", 1),
          ("des", 2))
    )


_HzCpSnmpV3TrapHostPrivProtocol_Type.__name__ = "Integer32"
_HzCpSnmpV3TrapHostPrivProtocol_Object = MibTableColumn
hzCpSnmpV3TrapHostPrivProtocol = _HzCpSnmpV3TrapHostPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5, 1, 7),
    _HzCpSnmpV3TrapHostPrivProtocol_Type()
)
hzCpSnmpV3TrapHostPrivProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostPrivProtocol.setStatus("current")


class _HzCpSnmpV3TrapHostPrivPassword_Type(DisplayString):
    """Custom type hzCpSnmpV3TrapHostPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpSnmpV3TrapHostPrivPassword_Type.__name__ = "DisplayString"
_HzCpSnmpV3TrapHostPrivPassword_Object = MibTableColumn
hzCpSnmpV3TrapHostPrivPassword = _HzCpSnmpV3TrapHostPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5, 1, 8),
    _HzCpSnmpV3TrapHostPrivPassword_Type()
)
hzCpSnmpV3TrapHostPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostPrivPassword.setStatus("current")


class _HzCpSnmpV3TrapHostActivated_Type(Integer32):
    """Custom type hzCpSnmpV3TrapHostActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("active", 2))
    )


_HzCpSnmpV3TrapHostActivated_Type.__name__ = "Integer32"
_HzCpSnmpV3TrapHostActivated_Object = MibTableColumn
hzCpSnmpV3TrapHostActivated = _HzCpSnmpV3TrapHostActivated_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 6, 5, 1, 32),
    _HzCpSnmpV3TrapHostActivated_Type()
)
hzCpSnmpV3TrapHostActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSnmpV3TrapHostActivated.setStatus("current")
_HzCpRadius_ObjectIdentity = ObjectIdentity
hzCpRadius = _HzCpRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7)
)


class _HzCpRadiusSuperUserAuthentication_Type(Integer32):
    """Custom type hzCpRadiusSuperUserAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpRadiusSuperUserAuthentication_Type.__name__ = "Integer32"
_HzCpRadiusSuperUserAuthentication_Object = MibScalar
hzCpRadiusSuperUserAuthentication = _HzCpRadiusSuperUserAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 1),
    _HzCpRadiusSuperUserAuthentication_Type()
)
hzCpRadiusSuperUserAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadiusSuperUserAuthentication.setStatus("current")
_HzCpRadiusServerTimeOut_Type = Integer32
_HzCpRadiusServerTimeOut_Object = MibScalar
hzCpRadiusServerTimeOut = _HzCpRadiusServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 2),
    _HzCpRadiusServerTimeOut_Type()
)
hzCpRadiusServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadiusServerTimeOut.setStatus("current")
_HzCpRadiusServerDeadTime_Type = Integer32
_HzCpRadiusServerDeadTime_Object = MibScalar
hzCpRadiusServerDeadTime = _HzCpRadiusServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 3),
    _HzCpRadiusServerDeadTime_Type()
)
hzCpRadiusServerDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadiusServerDeadTime.setStatus("current")
_HzCpRadiusServerReTransmit_Type = Integer32
_HzCpRadiusServerReTransmit_Object = MibScalar
hzCpRadiusServerReTransmit = _HzCpRadiusServerReTransmit_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 4),
    _HzCpRadiusServerReTransmit_Type()
)
hzCpRadiusServerReTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadiusServerReTransmit.setStatus("current")
_HzCpRadiusServerDepTable_Object = MibTable
hzCpRadiusServerDepTable = _HzCpRadiusServerDepTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 5)
)
if mibBuilder.loadTexts:
    hzCpRadiusServerDepTable.setStatus("deprecated")
_HzCpRadiusServerDepEntry_Object = MibTableRow
hzCpRadiusServerDepEntry = _HzCpRadiusServerDepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 5, 1)
)
hzCpRadiusServerDepEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpRadiusServerIndexDep"),
)
if mibBuilder.loadTexts:
    hzCpRadiusServerDepEntry.setStatus("deprecated")
_HzCpRadiusServerIndexDep_Type = Integer32
_HzCpRadiusServerIndexDep_Object = MibTableColumn
hzCpRadiusServerIndexDep = _HzCpRadiusServerIndexDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 5, 1, 1),
    _HzCpRadiusServerIndexDep_Type()
)
hzCpRadiusServerIndexDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadiusServerIndexDep.setStatus("deprecated")
_HzCpRadiusCfgdHostIpAddressDep_Type = IpAddress
_HzCpRadiusCfgdHostIpAddressDep_Object = MibTableColumn
hzCpRadiusCfgdHostIpAddressDep = _HzCpRadiusCfgdHostIpAddressDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 5, 1, 2),
    _HzCpRadiusCfgdHostIpAddressDep_Type()
)
hzCpRadiusCfgdHostIpAddressDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadiusCfgdHostIpAddressDep.setStatus("deprecated")
_HzCpRadiusCfgdHostKeyDep_Type = DisplayString
_HzCpRadiusCfgdHostKeyDep_Object = MibTableColumn
hzCpRadiusCfgdHostKeyDep = _HzCpRadiusCfgdHostKeyDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 5, 1, 3),
    _HzCpRadiusCfgdHostKeyDep_Type()
)
hzCpRadiusCfgdHostKeyDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadiusCfgdHostKeyDep.setStatus("deprecated")
_HzCpRadiusServerTable_Object = MibTable
hzCpRadiusServerTable = _HzCpRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 6)
)
if mibBuilder.loadTexts:
    hzCpRadiusServerTable.setStatus("current")
_HzCpRadiusServerEntry_Object = MibTableRow
hzCpRadiusServerEntry = _HzCpRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 6, 1)
)
hzCpRadiusServerEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    hzCpRadiusServerEntry.setStatus("current")
_HzCpRadiusServerIndex_Type = Integer32
_HzCpRadiusServerIndex_Object = MibTableColumn
hzCpRadiusServerIndex = _HzCpRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 6, 1, 1),
    _HzCpRadiusServerIndex_Type()
)
hzCpRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadiusServerIndex.setStatus("current")
_HzCpRadiusCfgdHostDomain_Type = InetAddressType
_HzCpRadiusCfgdHostDomain_Object = MibTableColumn
hzCpRadiusCfgdHostDomain = _HzCpRadiusCfgdHostDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 6, 1, 2),
    _HzCpRadiusCfgdHostDomain_Type()
)
hzCpRadiusCfgdHostDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadiusCfgdHostDomain.setStatus("current")
_HzCpRadiusCfgdHostAddress_Type = InetAddress
_HzCpRadiusCfgdHostAddress_Object = MibTableColumn
hzCpRadiusCfgdHostAddress = _HzCpRadiusCfgdHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 6, 1, 3),
    _HzCpRadiusCfgdHostAddress_Type()
)
hzCpRadiusCfgdHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadiusCfgdHostAddress.setStatus("current")


class _HzCpRadiusCfgdHostKey_Type(DisplayString):
    """Custom type hzCpRadiusCfgdHostKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpRadiusCfgdHostKey_Type.__name__ = "DisplayString"
_HzCpRadiusCfgdHostKey_Object = MibTableColumn
hzCpRadiusCfgdHostKey = _HzCpRadiusCfgdHostKey_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 7, 6, 1, 4),
    _HzCpRadiusCfgdHostKey_Type()
)
hzCpRadiusCfgdHostKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadiusCfgdHostKey.setStatus("current")
_HzCpManagementSessions_ObjectIdentity = ObjectIdentity
hzCpManagementSessions = _HzCpManagementSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 8)
)
_HzCpUserSessionUserTable_Object = MibTable
hzCpUserSessionUserTable = _HzCpUserSessionUserTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 8, 1)
)
if mibBuilder.loadTexts:
    hzCpUserSessionUserTable.setStatus("current")
_HzCpUserSessionUserEntry_Object = MibTableRow
hzCpUserSessionUserEntry = _HzCpUserSessionUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 8, 1, 1)
)
hzCpUserSessionUserEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpUserSessionUserIndex"),
)
if mibBuilder.loadTexts:
    hzCpUserSessionUserEntry.setStatus("current")


class _HzCpUserSessionUserIndex_Type(Integer32):
    """Custom type hzCpUserSessionUserIndex based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("user1", 1),
          ("user2", 2),
          ("user3", 3),
          ("user4", 4),
          ("user5", 5),
          ("user6", 6),
          ("user7", 7),
          ("user8", 8),
          ("user9", 9),
          ("user10", 10),
          ("user11", 11),
          ("user12", 12),
          ("user13", 13),
          ("user14", 14),
          ("user15", 15),
          ("user16", 16),
          ("user17", 17),
          ("user18", 18),
          ("user19", 19),
          ("user20", 20))
    )


_HzCpUserSessionUserIndex_Type.__name__ = "Integer32"
_HzCpUserSessionUserIndex_Object = MibTableColumn
hzCpUserSessionUserIndex = _HzCpUserSessionUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 8, 1, 1, 1),
    _HzCpUserSessionUserIndex_Type()
)
hzCpUserSessionUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpUserSessionUserIndex.setStatus("current")


class _HzCpUserSessionUserName_Type(DisplayString):
    """Custom type hzCpUserSessionUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpUserSessionUserName_Type.__name__ = "DisplayString"
_HzCpUserSessionUserName_Object = MibTableColumn
hzCpUserSessionUserName = _HzCpUserSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 8, 1, 1, 2),
    _HzCpUserSessionUserName_Type()
)
hzCpUserSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpUserSessionUserName.setStatus("current")
_HzCpUserSessionUserConnectionType_Type = DisplayString
_HzCpUserSessionUserConnectionType_Object = MibTableColumn
hzCpUserSessionUserConnectionType = _HzCpUserSessionUserConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 8, 1, 1, 3),
    _HzCpUserSessionUserConnectionType_Type()
)
hzCpUserSessionUserConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpUserSessionUserConnectionType.setStatus("current")


class _HzCpUserSessionUserState_Type(Integer32):
    """Custom type hzCpUserSessionUserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informationNotAvailable", 1),
          ("sessionTerminated", 2),
          ("sessionInProgress", 3))
    )


_HzCpUserSessionUserState_Type.__name__ = "Integer32"
_HzCpUserSessionUserState_Object = MibTableColumn
hzCpUserSessionUserState = _HzCpUserSessionUserState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 8, 1, 1, 4),
    _HzCpUserSessionUserState_Type()
)
hzCpUserSessionUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpUserSessionUserState.setStatus("current")
_HzCpHttp_ObjectIdentity = ObjectIdentity
hzCpHttp = _HzCpHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 9)
)


class _HzCpHttpEnable_Type(Integer32):
    """Custom type hzCpHttpEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpHttpEnable_Type.__name__ = "Integer32"
_HzCpHttpEnable_Object = MibScalar
hzCpHttpEnable = _HzCpHttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 9, 1),
    _HzCpHttpEnable_Type()
)
hzCpHttpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHttpEnable.setStatus("current")
_HzCpHttpSecure_ObjectIdentity = ObjectIdentity
hzCpHttpSecure = _HzCpHttpSecure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 9, 2)
)


class _HzCpHttpSecureCertificateStatus_Type(DisplayString):
    """Custom type hzCpHttpSecureCertificateStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HzCpHttpSecureCertificateStatus_Type.__name__ = "DisplayString"
_HzCpHttpSecureCertificateStatus_Object = MibScalar
hzCpHttpSecureCertificateStatus = _HzCpHttpSecureCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 9, 2, 1),
    _HzCpHttpSecureCertificateStatus_Type()
)
hzCpHttpSecureCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpHttpSecureCertificateStatus.setStatus("current")


class _HzCpHttpSecureAccessForAdminUsers_Type(Integer32):
    """Custom type hzCpHttpSecureAccessForAdminUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpHttpSecureAccessForAdminUsers_Type.__name__ = "Integer32"
_HzCpHttpSecureAccessForAdminUsers_Object = MibScalar
hzCpHttpSecureAccessForAdminUsers = _HzCpHttpSecureAccessForAdminUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 9, 2, 2),
    _HzCpHttpSecureAccessForAdminUsers_Type()
)
hzCpHttpSecureAccessForAdminUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHttpSecureAccessForAdminUsers.setStatus("current")


class _HzCpHttpSecureAccessForNocUsers_Type(Integer32):
    """Custom type hzCpHttpSecureAccessForNocUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpHttpSecureAccessForNocUsers_Type.__name__ = "Integer32"
_HzCpHttpSecureAccessForNocUsers_Object = MibScalar
hzCpHttpSecureAccessForNocUsers = _HzCpHttpSecureAccessForNocUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 9, 2, 3),
    _HzCpHttpSecureAccessForNocUsers_Type()
)
hzCpHttpSecureAccessForNocUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHttpSecureAccessForNocUsers.setStatus("current")


class _HzCpHttpSecureAccessForSuperUsers_Type(Integer32):
    """Custom type hzCpHttpSecureAccessForSuperUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpHttpSecureAccessForSuperUsers_Type.__name__ = "Integer32"
_HzCpHttpSecureAccessForSuperUsers_Object = MibScalar
hzCpHttpSecureAccessForSuperUsers = _HzCpHttpSecureAccessForSuperUsers_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 2, 9, 2, 4),
    _HzCpHttpSecureAccessForSuperUsers_Type()
)
hzCpHttpSecureAccessForSuperUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHttpSecureAccessForSuperUsers.setStatus("current")
_HzCpNetworkInterface_ObjectIdentity = ObjectIdentity
hzCpNetworkInterface = _HzCpNetworkInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3)
)
_HzCpEnetPort_ObjectIdentity = ObjectIdentity
hzCpEnetPort = _HzCpEnetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1)
)
_HzCpEnetPortConfigTable_Object = MibTable
hzCpEnetPortConfigTable = _HzCpEnetPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hzCpEnetPortConfigTable.setStatus("current")
_HzCpEnetPortConfigEntry_Object = MibTableRow
hzCpEnetPortConfigEntry = _HzCpEnetPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1)
)
hzCpEnetPortConfigEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpEnetPortIndex"),
)
if mibBuilder.loadTexts:
    hzCpEnetPortConfigEntry.setStatus("current")


class _HzCpEnetPortIndex_Type(Integer32):
    """Custom type hzCpEnetPortIndex based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4))
    )


_HzCpEnetPortIndex_Type.__name__ = "Integer32"
_HzCpEnetPortIndex_Object = MibTableColumn
hzCpEnetPortIndex = _HzCpEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 1),
    _HzCpEnetPortIndex_Type()
)
hzCpEnetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortIndex.setStatus("current")
_HzCpEnetPortName_Type = DisplayString
_HzCpEnetPortName_Object = MibTableColumn
hzCpEnetPortName = _HzCpEnetPortName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 2),
    _HzCpEnetPortName_Type()
)
hzCpEnetPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortName.setStatus("current")


class _HzCpEnetPortAutoNegotiation_Type(Integer32):
    """Custom type hzCpEnetPortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HzCpEnetPortAutoNegotiation_Type.__name__ = "Integer32"
_HzCpEnetPortAutoNegotiation_Object = MibTableColumn
hzCpEnetPortAutoNegotiation = _HzCpEnetPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 3),
    _HzCpEnetPortAutoNegotiation_Type()
)
hzCpEnetPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPortAutoNegotiation.setStatus("current")


class _HzCpEnetPortSpeed_Type(Integer32):
    """Custom type hzCpEnetPortSpeed based on Integer32"""
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
        *(("x10M", 1),
          ("x100M", 2),
          ("x1000M", 3),
          ("auto", 4))
    )


_HzCpEnetPortSpeed_Type.__name__ = "Integer32"
_HzCpEnetPortSpeed_Object = MibTableColumn
hzCpEnetPortSpeed = _HzCpEnetPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 4),
    _HzCpEnetPortSpeed_Type()
)
hzCpEnetPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPortSpeed.setStatus("current")


class _HzCpEnetPortDuplex_Type(Integer32):
    """Custom type hzCpEnetPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("auto", 3))
    )


_HzCpEnetPortDuplex_Type.__name__ = "Integer32"
_HzCpEnetPortDuplex_Object = MibTableColumn
hzCpEnetPortDuplex = _HzCpEnetPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 5),
    _HzCpEnetPortDuplex_Type()
)
hzCpEnetPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortDuplex.setStatus("current")


class _HzCpEnetPortMedia_Type(Integer32):
    """Custom type hzCpEnetPortMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2),
          ("auto", 3))
    )


_HzCpEnetPortMedia_Type.__name__ = "Integer32"
_HzCpEnetPortMedia_Object = MibTableColumn
hzCpEnetPortMedia = _HzCpEnetPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 6),
    _HzCpEnetPortMedia_Type()
)
hzCpEnetPortMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPortMedia.setStatus("current")


class _HzCpEnetPortAdminState_Type(Integer32):
    """Custom type hzCpEnetPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HzCpEnetPortAdminState_Type.__name__ = "Integer32"
_HzCpEnetPortAdminState_Object = MibTableColumn
hzCpEnetPortAdminState = _HzCpEnetPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 7),
    _HzCpEnetPortAdminState_Type()
)
hzCpEnetPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPortAdminState.setStatus("current")


class _HzCpEnetPortPauseFrame_Type(Integer32):
    """Custom type hzCpEnetPortPauseFrame based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_HzCpEnetPortPauseFrame_Type.__name__ = "Integer32"
_HzCpEnetPortPauseFrame_Object = MibTableColumn
hzCpEnetPortPauseFrame = _HzCpEnetPortPauseFrame_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 8),
    _HzCpEnetPortPauseFrame_Type()
)
hzCpEnetPortPauseFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPortPauseFrame.setStatus("current")


class _HzCpEnetPortMaxFrameSize_Type(Integer32):
    """Custom type hzCpEnetPortMaxFrameSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1600, 9600),
    )


_HzCpEnetPortMaxFrameSize_Type.__name__ = "Integer32"
_HzCpEnetPortMaxFrameSize_Object = MibTableColumn
hzCpEnetPortMaxFrameSize = _HzCpEnetPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 9),
    _HzCpEnetPortMaxFrameSize_Type()
)
hzCpEnetPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPortMaxFrameSize.setStatus("current")


class _HzCpEnetPortOpticalTransceiverState_Type(Integer32):
    """Custom type hzCpEnetPortOpticalTransceiverState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpEnetPortOpticalTransceiverState_Type.__name__ = "Integer32"
_HzCpEnetPortOpticalTransceiverState_Object = MibTableColumn
hzCpEnetPortOpticalTransceiverState = _HzCpEnetPortOpticalTransceiverState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 10),
    _HzCpEnetPortOpticalTransceiverState_Type()
)
hzCpEnetPortOpticalTransceiverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPortOpticalTransceiverState.setStatus("current")


class _HzCpEnetPortState_Type(Integer32):
    """Custom type hzCpEnetPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HzCpEnetPortState_Type.__name__ = "Integer32"
_HzCpEnetPortState_Object = MibTableColumn
hzCpEnetPortState = _HzCpEnetPortState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 11),
    _HzCpEnetPortState_Type()
)
hzCpEnetPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPortState.setStatus("current")


class _HzCpEnetPayloadState_Type(Integer32):
    """Custom type hzCpEnetPayloadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HzCpEnetPayloadState_Type.__name__ = "Integer32"
_HzCpEnetPayloadState_Object = MibTableColumn
hzCpEnetPayloadState = _HzCpEnetPayloadState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 1, 1, 12),
    _HzCpEnetPayloadState_Type()
)
hzCpEnetPayloadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPayloadState.setStatus("current")
_HzCpEnetPortStatusTable_Object = MibTable
hzCpEnetPortStatusTable = _HzCpEnetPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hzCpEnetPortStatusTable.setStatus("current")
_HzCpEnetPortStatusEntry_Object = MibTableRow
hzCpEnetPortStatusEntry = _HzCpEnetPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 2, 1)
)
hzCpEnetPortStatusEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpEnetPortStatusIndex"),
)
if mibBuilder.loadTexts:
    hzCpEnetPortStatusEntry.setStatus("current")


class _HzCpEnetPortStatusIndex_Type(Integer32):
    """Custom type hzCpEnetPortStatusIndex based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4))
    )


_HzCpEnetPortStatusIndex_Type.__name__ = "Integer32"
_HzCpEnetPortStatusIndex_Object = MibTableColumn
hzCpEnetPortStatusIndex = _HzCpEnetPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 2, 1, 1),
    _HzCpEnetPortStatusIndex_Type()
)
hzCpEnetPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortStatusIndex.setStatus("current")


class _HzCpEnetPortLinkStatus_Type(Integer32):
    """Custom type hzCpEnetPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("invalid", 3))
    )


_HzCpEnetPortLinkStatus_Type.__name__ = "Integer32"
_HzCpEnetPortLinkStatus_Object = MibTableColumn
hzCpEnetPortLinkStatus = _HzCpEnetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 2, 1, 2),
    _HzCpEnetPortLinkStatus_Type()
)
hzCpEnetPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortLinkStatus.setStatus("current")


class _HzCpEnetPortAutoNegotiationStatus_Type(Integer32):
    """Custom type hzCpEnetPortAutoNegotiationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("invalid", 3))
    )


_HzCpEnetPortAutoNegotiationStatus_Type.__name__ = "Integer32"
_HzCpEnetPortAutoNegotiationStatus_Object = MibTableColumn
hzCpEnetPortAutoNegotiationStatus = _HzCpEnetPortAutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 2, 1, 3),
    _HzCpEnetPortAutoNegotiationStatus_Type()
)
hzCpEnetPortAutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortAutoNegotiationStatus.setStatus("current")


class _HzCpEnetPortSpeedStatus_Type(Integer32):
    """Custom type hzCpEnetPortSpeedStatus based on Integer32"""
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
        *(("x10M", 1),
          ("x100M", 2),
          ("x1000M", 3),
          ("auto", 4),
          ("invalid", 5))
    )


_HzCpEnetPortSpeedStatus_Type.__name__ = "Integer32"
_HzCpEnetPortSpeedStatus_Object = MibTableColumn
hzCpEnetPortSpeedStatus = _HzCpEnetPortSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 2, 1, 4),
    _HzCpEnetPortSpeedStatus_Type()
)
hzCpEnetPortSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortSpeedStatus.setStatus("current")


class _HzCpEnetPortDuplexStatus_Type(Integer32):
    """Custom type hzCpEnetPortDuplexStatus based on Integer32"""
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
        *(("full", 1),
          ("half", 2),
          ("auto", 3),
          ("invalid", 4))
    )


_HzCpEnetPortDuplexStatus_Type.__name__ = "Integer32"
_HzCpEnetPortDuplexStatus_Object = MibTableColumn
hzCpEnetPortDuplexStatus = _HzCpEnetPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 2, 1, 5),
    _HzCpEnetPortDuplexStatus_Type()
)
hzCpEnetPortDuplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortDuplexStatus.setStatus("current")


class _HzCpEnetPortMediaStatus_Type(Integer32):
    """Custom type hzCpEnetPortMediaStatus based on Integer32"""
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
        *(("copper", 1),
          ("fiber", 2),
          ("auto", 3),
          ("invalid", 4))
    )


_HzCpEnetPortMediaStatus_Type.__name__ = "Integer32"
_HzCpEnetPortMediaStatus_Object = MibTableColumn
hzCpEnetPortMediaStatus = _HzCpEnetPortMediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 2, 1, 6),
    _HzCpEnetPortMediaStatus_Type()
)
hzCpEnetPortMediaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortMediaStatus.setStatus("current")
_HzCpEnetPortStatsTable_Object = MibTable
hzCpEnetPortStatsTable = _HzCpEnetPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hzCpEnetPortStatsTable.setStatus("current")
_HzCpEnetPortStatsEntry_Object = MibTableRow
hzCpEnetPortStatsEntry = _HzCpEnetPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 3, 1)
)
hzCpEnetPortStatsEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpEnetPortStatsIndex"),
)
if mibBuilder.loadTexts:
    hzCpEnetPortStatsEntry.setStatus("current")


class _HzCpEnetPortStatsIndex_Type(Integer32):
    """Custom type hzCpEnetPortStatsIndex based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4))
    )


_HzCpEnetPortStatsIndex_Type.__name__ = "Integer32"
_HzCpEnetPortStatsIndex_Object = MibTableColumn
hzCpEnetPortStatsIndex = _HzCpEnetPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 3, 1, 1),
    _HzCpEnetPortStatsIndex_Type()
)
hzCpEnetPortStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortStatsIndex.setStatus("current")
_HzCpEnetPortTxFrames_Type = Counter64
_HzCpEnetPortTxFrames_Object = MibTableColumn
hzCpEnetPortTxFrames = _HzCpEnetPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 3, 1, 2),
    _HzCpEnetPortTxFrames_Type()
)
hzCpEnetPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortTxFrames.setStatus("current")
_HzCpEnetPortTxBytes_Type = Counter64
_HzCpEnetPortTxBytes_Object = MibTableColumn
hzCpEnetPortTxBytes = _HzCpEnetPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 3, 1, 3),
    _HzCpEnetPortTxBytes_Type()
)
hzCpEnetPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortTxBytes.setStatus("current")
_HzCpEnetPortRxFramesOk_Type = Counter64
_HzCpEnetPortRxFramesOk_Object = MibTableColumn
hzCpEnetPortRxFramesOk = _HzCpEnetPortRxFramesOk_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 3, 1, 4),
    _HzCpEnetPortRxFramesOk_Type()
)
hzCpEnetPortRxFramesOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortRxFramesOk.setStatus("current")
_HzCpEnetPortRxBytesOk_Type = Counter64
_HzCpEnetPortRxBytesOk_Object = MibTableColumn
hzCpEnetPortRxBytesOk = _HzCpEnetPortRxBytesOk_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 3, 1, 5),
    _HzCpEnetPortRxBytesOk_Type()
)
hzCpEnetPortRxBytesOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortRxBytesOk.setStatus("current")
_HzCpEnetPortRxFramesLengthErrors_Type = Counter64
_HzCpEnetPortRxFramesLengthErrors_Object = MibTableColumn
hzCpEnetPortRxFramesLengthErrors = _HzCpEnetPortRxFramesLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 3, 1, 6),
    _HzCpEnetPortRxFramesLengthErrors_Type()
)
hzCpEnetPortRxFramesLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortRxFramesLengthErrors.setStatus("current")
_HzCpEnetPortRxFramesCrcErrors_Type = Counter64
_HzCpEnetPortRxFramesCrcErrors_Object = MibTableColumn
hzCpEnetPortRxFramesCrcErrors = _HzCpEnetPortRxFramesCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 3, 1, 7),
    _HzCpEnetPortRxFramesCrcErrors_Type()
)
hzCpEnetPortRxFramesCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortRxFramesCrcErrors.setStatus("current")
_HzCpEnetPortRxDiscarded_Type = Counter64
_HzCpEnetPortRxDiscarded_Object = MibTableColumn
hzCpEnetPortRxDiscarded = _HzCpEnetPortRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 3, 1, 8),
    _HzCpEnetPortRxDiscarded_Type()
)
hzCpEnetPortRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortRxDiscarded.setStatus("current")
_HzCpEnetAggregatedStats_ObjectIdentity = ObjectIdentity
hzCpEnetAggregatedStats = _HzCpEnetAggregatedStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4)
)
_HzCpEnetAggTxFrames_Type = Counter64
_HzCpEnetAggTxFrames_Object = MibScalar
hzCpEnetAggTxFrames = _HzCpEnetAggTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 1),
    _HzCpEnetAggTxFrames_Type()
)
hzCpEnetAggTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggTxFrames.setStatus("current")
_HzCpEnetAggTxBytes_Type = Counter64
_HzCpEnetAggTxBytes_Object = MibScalar
hzCpEnetAggTxBytes = _HzCpEnetAggTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 2),
    _HzCpEnetAggTxBytes_Type()
)
hzCpEnetAggTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggTxBytes.setStatus("current")
_HzCpEnetAggRxFramesOK_Type = Counter64
_HzCpEnetAggRxFramesOK_Object = MibScalar
hzCpEnetAggRxFramesOK = _HzCpEnetAggRxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 3),
    _HzCpEnetAggRxFramesOK_Type()
)
hzCpEnetAggRxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggRxFramesOK.setStatus("current")
_HzCpEnetAggRxBytesOK_Type = Counter64
_HzCpEnetAggRxBytesOK_Object = MibScalar
hzCpEnetAggRxBytesOK = _HzCpEnetAggRxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 4),
    _HzCpEnetAggRxBytesOK_Type()
)
hzCpEnetAggRxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggRxBytesOK.setStatus("current")
_HzCpEnetAggRxFramesLengthError_Type = Counter64
_HzCpEnetAggRxFramesLengthError_Object = MibScalar
hzCpEnetAggRxFramesLengthError = _HzCpEnetAggRxFramesLengthError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 5),
    _HzCpEnetAggRxFramesLengthError_Type()
)
hzCpEnetAggRxFramesLengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggRxFramesLengthError.setStatus("current")
_HzCpEnetAggPortRxFramesCrcError_Type = Counter64
_HzCpEnetAggPortRxFramesCrcError_Object = MibScalar
hzCpEnetAggPortRxFramesCrcError = _HzCpEnetAggPortRxFramesCrcError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 6),
    _HzCpEnetAggPortRxFramesCrcError_Type()
)
hzCpEnetAggPortRxFramesCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggPortRxFramesCrcError.setStatus("current")
_HzCpEnetAggPortRxFramesDrops_Type = Counter64
_HzCpEnetAggPortRxFramesDrops_Object = MibScalar
hzCpEnetAggPortRxFramesDrops = _HzCpEnetAggPortRxFramesDrops_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 7),
    _HzCpEnetAggPortRxFramesDrops_Type()
)
hzCpEnetAggPortRxFramesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggPortRxFramesDrops.setStatus("current")
_HzCpEnetAggBWUtilization_Type = Integer32
_HzCpEnetAggBWUtilization_Object = MibScalar
hzCpEnetAggBWUtilization = _HzCpEnetAggBWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 8),
    _HzCpEnetAggBWUtilization_Type()
)
hzCpEnetAggBWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggBWUtilization.setStatus("current")
_HzCpEnetAggIngressDataRate_Type = Integer32
_HzCpEnetAggIngressDataRate_Object = MibScalar
hzCpEnetAggIngressDataRate = _HzCpEnetAggIngressDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 9),
    _HzCpEnetAggIngressDataRate_Type()
)
hzCpEnetAggIngressDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggIngressDataRate.setStatus("current")
_HzCpEnetAggEgressDataRate_Type = Integer32
_HzCpEnetAggEgressDataRate_Object = MibScalar
hzCpEnetAggEgressDataRate = _HzCpEnetAggEgressDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 10),
    _HzCpEnetAggEgressDataRate_Type()
)
hzCpEnetAggEgressDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggEgressDataRate.setStatus("current")
_HzCpEnetAggFramesInQueueTable_Object = MibTable
hzCpEnetAggFramesInQueueTable = _HzCpEnetAggFramesInQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 11)
)
if mibBuilder.loadTexts:
    hzCpEnetAggFramesInQueueTable.setStatus("current")
_HzCpEnetAggFramesInQueueEntry_Object = MibTableRow
hzCpEnetAggFramesInQueueEntry = _HzCpEnetAggFramesInQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 11, 1)
)
hzCpEnetAggFramesInQueueEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpEnetAggFramesInQueueIndex"),
)
if mibBuilder.loadTexts:
    hzCpEnetAggFramesInQueueEntry.setStatus("current")


class _HzCpEnetAggFramesInQueueIndex_Type(Integer32):
    """Custom type hzCpEnetAggFramesInQueueIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_HzCpEnetAggFramesInQueueIndex_Type.__name__ = "Integer32"
_HzCpEnetAggFramesInQueueIndex_Object = MibTableColumn
hzCpEnetAggFramesInQueueIndex = _HzCpEnetAggFramesInQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 11, 1, 1),
    _HzCpEnetAggFramesInQueueIndex_Type()
)
hzCpEnetAggFramesInQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggFramesInQueueIndex.setStatus("current")
_HzCpEnetAggFramesInQueue_Type = Counter64
_HzCpEnetAggFramesInQueue_Object = MibTableColumn
hzCpEnetAggFramesInQueue = _HzCpEnetAggFramesInQueue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 11, 1, 2),
    _HzCpEnetAggFramesInQueue_Type()
)
hzCpEnetAggFramesInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggFramesInQueue.setStatus("current")
_HzCpEnetAggFramesInQueueDiscarded_Type = Counter64
_HzCpEnetAggFramesInQueueDiscarded_Object = MibTableColumn
hzCpEnetAggFramesInQueueDiscarded = _HzCpEnetAggFramesInQueueDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 4, 11, 1, 3),
    _HzCpEnetAggFramesInQueueDiscarded_Type()
)
hzCpEnetAggFramesInQueueDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggFramesInQueueDiscarded.setStatus("current")
_HzCpEnetPortLcStatsTable_Object = MibTable
hzCpEnetPortLcStatsTable = _HzCpEnetPortLcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 5)
)
if mibBuilder.loadTexts:
    hzCpEnetPortLcStatsTable.setStatus("current")
_HzCpEnetPortLcStatsEntry_Object = MibTableRow
hzCpEnetPortLcStatsEntry = _HzCpEnetPortLcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 5, 1)
)
hzCpEnetPortLcStatsEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpEnetPortLcStatsIndex"),
)
if mibBuilder.loadTexts:
    hzCpEnetPortLcStatsEntry.setStatus("current")


class _HzCpEnetPortLcStatsIndex_Type(Integer32):
    """Custom type hzCpEnetPortLcStatsIndex based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4))
    )


_HzCpEnetPortLcStatsIndex_Type.__name__ = "Integer32"
_HzCpEnetPortLcStatsIndex_Object = MibTableColumn
hzCpEnetPortLcStatsIndex = _HzCpEnetPortLcStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 5, 1, 1),
    _HzCpEnetPortLcStatsIndex_Type()
)
hzCpEnetPortLcStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortLcStatsIndex.setStatus("current")
_HzCpEnetPortLcTxFrames_Type = Counter32
_HzCpEnetPortLcTxFrames_Object = MibTableColumn
hzCpEnetPortLcTxFrames = _HzCpEnetPortLcTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 5, 1, 2),
    _HzCpEnetPortLcTxFrames_Type()
)
hzCpEnetPortLcTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortLcTxFrames.setStatus("current")
_HzCpEnetPortLcTxBytes_Type = Counter32
_HzCpEnetPortLcTxBytes_Object = MibTableColumn
hzCpEnetPortLcTxBytes = _HzCpEnetPortLcTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 5, 1, 3),
    _HzCpEnetPortLcTxBytes_Type()
)
hzCpEnetPortLcTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortLcTxBytes.setStatus("current")
_HzCpEnetPortLcRxFramesOk_Type = Counter32
_HzCpEnetPortLcRxFramesOk_Object = MibTableColumn
hzCpEnetPortLcRxFramesOk = _HzCpEnetPortLcRxFramesOk_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 5, 1, 4),
    _HzCpEnetPortLcRxFramesOk_Type()
)
hzCpEnetPortLcRxFramesOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortLcRxFramesOk.setStatus("current")
_HzCpEnetPortLcRxBytesOk_Type = Counter32
_HzCpEnetPortLcRxBytesOk_Object = MibTableColumn
hzCpEnetPortLcRxBytesOk = _HzCpEnetPortLcRxBytesOk_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 5, 1, 5),
    _HzCpEnetPortLcRxBytesOk_Type()
)
hzCpEnetPortLcRxBytesOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortLcRxBytesOk.setStatus("current")
_HzCpEnetPortLcRxFramesLengthErrors_Type = Counter32
_HzCpEnetPortLcRxFramesLengthErrors_Object = MibTableColumn
hzCpEnetPortLcRxFramesLengthErrors = _HzCpEnetPortLcRxFramesLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 5, 1, 6),
    _HzCpEnetPortLcRxFramesLengthErrors_Type()
)
hzCpEnetPortLcRxFramesLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortLcRxFramesLengthErrors.setStatus("current")
_HzCpEnetPortLcRxFramesCrcErrors_Type = Counter32
_HzCpEnetPortLcRxFramesCrcErrors_Object = MibTableColumn
hzCpEnetPortLcRxFramesCrcErrors = _HzCpEnetPortLcRxFramesCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 5, 1, 7),
    _HzCpEnetPortLcRxFramesCrcErrors_Type()
)
hzCpEnetPortLcRxFramesCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortLcRxFramesCrcErrors.setStatus("current")
_HzCpEnetPortLcRxDiscarded_Type = Counter32
_HzCpEnetPortLcRxDiscarded_Object = MibTableColumn
hzCpEnetPortLcRxDiscarded = _HzCpEnetPortLcRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 5, 1, 8),
    _HzCpEnetPortLcRxDiscarded_Type()
)
hzCpEnetPortLcRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortLcRxDiscarded.setStatus("current")
_HzCpEnetAggregatedLcStats_ObjectIdentity = ObjectIdentity
hzCpEnetAggregatedLcStats = _HzCpEnetAggregatedLcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6)
)
_HzCpEnetAggLcTxFrames_Type = Counter32
_HzCpEnetAggLcTxFrames_Object = MibScalar
hzCpEnetAggLcTxFrames = _HzCpEnetAggLcTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 1),
    _HzCpEnetAggLcTxFrames_Type()
)
hzCpEnetAggLcTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcTxFrames.setStatus("current")
_HzCpEnetAggLcTxBytes_Type = Counter32
_HzCpEnetAggLcTxBytes_Object = MibScalar
hzCpEnetAggLcTxBytes = _HzCpEnetAggLcTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 2),
    _HzCpEnetAggLcTxBytes_Type()
)
hzCpEnetAggLcTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcTxBytes.setStatus("current")
_HzCpEnetAggLcRxFramesOK_Type = Counter32
_HzCpEnetAggLcRxFramesOK_Object = MibScalar
hzCpEnetAggLcRxFramesOK = _HzCpEnetAggLcRxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 3),
    _HzCpEnetAggLcRxFramesOK_Type()
)
hzCpEnetAggLcRxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcRxFramesOK.setStatus("current")
_HzCpEnetAggLcRxBytesOK_Type = Counter32
_HzCpEnetAggLcRxBytesOK_Object = MibScalar
hzCpEnetAggLcRxBytesOK = _HzCpEnetAggLcRxBytesOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 4),
    _HzCpEnetAggLcRxBytesOK_Type()
)
hzCpEnetAggLcRxBytesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcRxBytesOK.setStatus("current")
_HzCpEnetAggLcRxFramesLengthError_Type = Counter32
_HzCpEnetAggLcRxFramesLengthError_Object = MibScalar
hzCpEnetAggLcRxFramesLengthError = _HzCpEnetAggLcRxFramesLengthError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 5),
    _HzCpEnetAggLcRxFramesLengthError_Type()
)
hzCpEnetAggLcRxFramesLengthError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcRxFramesLengthError.setStatus("current")
_HzCpEnetAggLcRxFramesCrcError_Type = Counter32
_HzCpEnetAggLcRxFramesCrcError_Object = MibScalar
hzCpEnetAggLcRxFramesCrcError = _HzCpEnetAggLcRxFramesCrcError_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 6),
    _HzCpEnetAggLcRxFramesCrcError_Type()
)
hzCpEnetAggLcRxFramesCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcRxFramesCrcError.setStatus("current")
_HzCpEnetAggLcRxFramesDrops_Type = Counter32
_HzCpEnetAggLcRxFramesDrops_Object = MibScalar
hzCpEnetAggLcRxFramesDrops = _HzCpEnetAggLcRxFramesDrops_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 7),
    _HzCpEnetAggLcRxFramesDrops_Type()
)
hzCpEnetAggLcRxFramesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcRxFramesDrops.setStatus("current")
_HzCpEnetAggLcBWUtilization_Type = Integer32
_HzCpEnetAggLcBWUtilization_Object = MibScalar
hzCpEnetAggLcBWUtilization = _HzCpEnetAggLcBWUtilization_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 8),
    _HzCpEnetAggLcBWUtilization_Type()
)
hzCpEnetAggLcBWUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcBWUtilization.setStatus("current")
_HzCpEnetAggLcIngressDataRate_Type = Integer32
_HzCpEnetAggLcIngressDataRate_Object = MibScalar
hzCpEnetAggLcIngressDataRate = _HzCpEnetAggLcIngressDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 9),
    _HzCpEnetAggLcIngressDataRate_Type()
)
hzCpEnetAggLcIngressDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcIngressDataRate.setStatus("current")
_HzCpEnetAggLcEgressDataRate_Type = Integer32
_HzCpEnetAggLcEgressDataRate_Object = MibScalar
hzCpEnetAggLcEgressDataRate = _HzCpEnetAggLcEgressDataRate_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 10),
    _HzCpEnetAggLcEgressDataRate_Type()
)
hzCpEnetAggLcEgressDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcEgressDataRate.setStatus("current")
_HzCpEnetAggLcFramesInQueueTable_Object = MibTable
hzCpEnetAggLcFramesInQueueTable = _HzCpEnetAggLcFramesInQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 11)
)
if mibBuilder.loadTexts:
    hzCpEnetAggLcFramesInQueueTable.setStatus("current")
_HzCpEnetAggLcFramesInQueueEntry_Object = MibTableRow
hzCpEnetAggLcFramesInQueueEntry = _HzCpEnetAggLcFramesInQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 11, 1)
)
hzCpEnetAggLcFramesInQueueEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpEnetAggLcFramesInQueueIndex"),
)
if mibBuilder.loadTexts:
    hzCpEnetAggLcFramesInQueueEntry.setStatus("current")


class _HzCpEnetAggLcFramesInQueueIndex_Type(Integer32):
    """Custom type hzCpEnetAggLcFramesInQueueIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_HzCpEnetAggLcFramesInQueueIndex_Type.__name__ = "Integer32"
_HzCpEnetAggLcFramesInQueueIndex_Object = MibTableColumn
hzCpEnetAggLcFramesInQueueIndex = _HzCpEnetAggLcFramesInQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 11, 1, 1),
    _HzCpEnetAggLcFramesInQueueIndex_Type()
)
hzCpEnetAggLcFramesInQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcFramesInQueueIndex.setStatus("current")
_HzCpEnetAggLcFramesInQueue_Type = Counter32
_HzCpEnetAggLcFramesInQueue_Object = MibTableColumn
hzCpEnetAggLcFramesInQueue = _HzCpEnetAggLcFramesInQueue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 11, 1, 2),
    _HzCpEnetAggLcFramesInQueue_Type()
)
hzCpEnetAggLcFramesInQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcFramesInQueue.setStatus("current")
_HzCpEnetAggLcFramesInQueueDiscarded_Type = Counter32
_HzCpEnetAggLcFramesInQueueDiscarded_Object = MibTableColumn
hzCpEnetAggLcFramesInQueueDiscarded = _HzCpEnetAggLcFramesInQueueDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 6, 11, 1, 3),
    _HzCpEnetAggLcFramesInQueueDiscarded_Type()
)
hzCpEnetAggLcFramesInQueueDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetAggLcFramesInQueueDiscarded.setStatus("current")
_HzCpEnetPortVlanTable_Object = MibTable
hzCpEnetPortVlanTable = _HzCpEnetPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 7)
)
if mibBuilder.loadTexts:
    hzCpEnetPortVlanTable.setStatus("current")
_HzCpEnetPortVlanEntry_Object = MibTableRow
hzCpEnetPortVlanEntry = _HzCpEnetPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 7, 1)
)
hzCpEnetPortVlanEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpEnetPortVlanIndex"),
)
if mibBuilder.loadTexts:
    hzCpEnetPortVlanEntry.setStatus("current")


class _HzCpEnetPortVlanIndex_Type(Integer32):
    """Custom type hzCpEnetPortVlanIndex based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4))
    )


_HzCpEnetPortVlanIndex_Type.__name__ = "Integer32"
_HzCpEnetPortVlanIndex_Object = MibTableColumn
hzCpEnetPortVlanIndex = _HzCpEnetPortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 7, 1, 1),
    _HzCpEnetPortVlanIndex_Type()
)
hzCpEnetPortVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpEnetPortVlanIndex.setStatus("current")
_HzCpEnetPortDefaultVlanId_Type = Integer32
_HzCpEnetPortDefaultVlanId_Object = MibTableColumn
hzCpEnetPortDefaultVlanId = _HzCpEnetPortDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 7, 1, 2),
    _HzCpEnetPortDefaultVlanId_Type()
)
hzCpEnetPortDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPortDefaultVlanId.setStatus("current")
_HzCpEnetPortDefaultVlanPriority_Type = Integer32
_HzCpEnetPortDefaultVlanPriority_Object = MibTableColumn
hzCpEnetPortDefaultVlanPriority = _HzCpEnetPortDefaultVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 3, 1, 7, 1, 3),
    _HzCpEnetPortDefaultVlanPriority_Type()
)
hzCpEnetPortDefaultVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEnetPortDefaultVlanPriority.setStatus("current")
_HzCpWirelessInterface_ObjectIdentity = ObjectIdentity
hzCpWirelessInterface = _HzCpWirelessInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4)
)
_HzCpWirelessInterfaceNames_ObjectIdentity = ObjectIdentity
hzCpWirelessInterfaceNames = _HzCpWirelessInterfaceNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 1)
)
_HzCpWirelessInterfaceNameTable_Object = MibTable
hzCpWirelessInterfaceNameTable = _HzCpWirelessInterfaceNameTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hzCpWirelessInterfaceNameTable.setStatus("current")
_HzCpWirelessInterfaceNameEntry_Object = MibTableRow
hzCpWirelessInterfaceNameEntry = _HzCpWirelessInterfaceNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 1, 1, 1)
)
hzCpWirelessInterfaceNameEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpWirelessInterfaceNameIndex"),
)
if mibBuilder.loadTexts:
    hzCpWirelessInterfaceNameEntry.setStatus("current")


class _HzCpWirelessInterfaceNameIndex_Type(Integer32):
    """Custom type hzCpWirelessInterfaceNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzCpWirelessInterfaceNameIndex_Type.__name__ = "Integer32"
_HzCpWirelessInterfaceNameIndex_Object = MibTableColumn
hzCpWirelessInterfaceNameIndex = _HzCpWirelessInterfaceNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 1, 1, 1, 1),
    _HzCpWirelessInterfaceNameIndex_Type()
)
hzCpWirelessInterfaceNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessInterfaceNameIndex.setStatus("current")
_HzCpWirelessInterfaceName_Type = DisplayString
_HzCpWirelessInterfaceName_Object = MibTableColumn
hzCpWirelessInterfaceName = _HzCpWirelessInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 1, 1, 1, 2),
    _HzCpWirelessInterfaceName_Type()
)
hzCpWirelessInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessInterfaceName.setStatus("current")
_HzCpWirelessInterfaceModems_ObjectIdentity = ObjectIdentity
hzCpWirelessInterfaceModems = _HzCpWirelessInterfaceModems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2)
)
_HzCpModemTable_Object = MibTable
hzCpModemTable = _HzCpModemTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hzCpModemTable.setStatus("current")
_HzCpModemEntry_Object = MibTableRow
hzCpModemEntry = _HzCpModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1)
)
hzCpModemEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
)
if mibBuilder.loadTexts:
    hzCpModemEntry.setStatus("current")


class _HzCpModemIndex_Type(Integer32):
    """Custom type hzCpModemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wireless-port-1", 1)
    )


_HzCpModemIndex_Type.__name__ = "Integer32"
_HzCpModemIndex_Object = MibTableColumn
hzCpModemIndex = _HzCpModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1, 1),
    _HzCpModemIndex_Type()
)
hzCpModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemIndex.setStatus("current")


class _HzCpModemOperStatus_Type(Integer32):
    """Custom type hzCpModemOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_HzCpModemOperStatus_Type.__name__ = "Integer32"
_HzCpModemOperStatus_Object = MibTableColumn
hzCpModemOperStatus = _HzCpModemOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1, 2),
    _HzCpModemOperStatus_Type()
)
hzCpModemOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemOperStatus.setStatus("current")
_HzCpModemChannelizedRSL_Type = Integer32
_HzCpModemChannelizedRSL_Object = MibTableColumn
hzCpModemChannelizedRSL = _HzCpModemChannelizedRSL_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1, 3),
    _HzCpModemChannelizedRSL_Type()
)
hzCpModemChannelizedRSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemChannelizedRSL.setStatus("current")
_HzCpModemChannelizedRSLUnsignedInt_Type = Integer32
_HzCpModemChannelizedRSLUnsignedInt_Object = MibTableColumn
hzCpModemChannelizedRSLUnsignedInt = _HzCpModemChannelizedRSLUnsignedInt_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1, 4),
    _HzCpModemChannelizedRSLUnsignedInt_Type()
)
hzCpModemChannelizedRSLUnsignedInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemChannelizedRSLUnsignedInt.setStatus("current")


class _HzCpModemModulationType_Type(Integer32):
    """Custom type hzCpModemModulationType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("qpsk", 1),
          ("qam16", 2),
          ("qam32", 3),
          ("qam64", 4),
          ("qam128", 5),
          ("qam256", 6),
          ("qam512", 7),
          ("qam1024", 8),
          ("qam2048", 9))
    )


_HzCpModemModulationType_Type.__name__ = "Integer32"
_HzCpModemModulationType_Object = MibTableColumn
hzCpModemModulationType = _HzCpModemModulationType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1, 5),
    _HzCpModemModulationType_Type()
)
hzCpModemModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemModulationType.setStatus("current")
_HzCpModemRxSpeed_Type = Integer32
_HzCpModemRxSpeed_Object = MibTableColumn
hzCpModemRxSpeed = _HzCpModemRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1, 6),
    _HzCpModemRxSpeed_Type()
)
hzCpModemRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemRxSpeed.setStatus("current")
_HzCpModemTxSpeed_Type = Integer32
_HzCpModemTxSpeed_Object = MibTableColumn
hzCpModemTxSpeed = _HzCpModemTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1, 7),
    _HzCpModemTxSpeed_Type()
)
hzCpModemTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemTxSpeed.setStatus("current")
_HzCpModemSNR_Type = Integer32
_HzCpModemSNR_Object = MibTableColumn
hzCpModemSNR = _HzCpModemSNR_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1, 8),
    _HzCpModemSNR_Type()
)
hzCpModemSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemSNR.setStatus("current")
_HzCpModemEbToNoiseRatio_Type = Integer32
_HzCpModemEbToNoiseRatio_Object = MibTableColumn
hzCpModemEbToNoiseRatio = _HzCpModemEbToNoiseRatio_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1, 9),
    _HzCpModemEbToNoiseRatio_Type()
)
hzCpModemEbToNoiseRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemEbToNoiseRatio.setStatus("current")
_HzCpModemEqualizerStress_Type = Integer32
_HzCpModemEqualizerStress_Object = MibTableColumn
hzCpModemEqualizerStress = _HzCpModemEqualizerStress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 1, 1, 10),
    _HzCpModemEqualizerStress_Type()
)
hzCpModemEqualizerStress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpModemEqualizerStress.setStatus("current")
_HzCpWirelessPortStatsTable_Object = MibTable
hzCpWirelessPortStatsTable = _HzCpWirelessPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hzCpWirelessPortStatsTable.setStatus("current")
_HzCpWirelessPortStatsEntry_Object = MibTableRow
hzCpWirelessPortStatsEntry = _HzCpWirelessPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 2, 1)
)
hzCpWirelessPortStatsEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpWirelessPortStatsIndex"),
)
if mibBuilder.loadTexts:
    hzCpWirelessPortStatsEntry.setStatus("current")


class _HzCpWirelessPortStatsIndex_Type(Integer32):
    """Custom type hzCpWirelessPortStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzCpWirelessPortStatsIndex_Type.__name__ = "Integer32"
_HzCpWirelessPortStatsIndex_Object = MibTableColumn
hzCpWirelessPortStatsIndex = _HzCpWirelessPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 2, 1, 1),
    _HzCpWirelessPortStatsIndex_Type()
)
hzCpWirelessPortStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessPortStatsIndex.setStatus("current")
_HzCpWirelessPortTxBlocks_Type = Counter64
_HzCpWirelessPortTxBlocks_Object = MibTableColumn
hzCpWirelessPortTxBlocks = _HzCpWirelessPortTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 2, 1, 2),
    _HzCpWirelessPortTxBlocks_Type()
)
hzCpWirelessPortTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessPortTxBlocks.setStatus("current")
_HzCpWirelessPortRxBlocksOKs_Type = Counter64
_HzCpWirelessPortRxBlocksOKs_Object = MibTableColumn
hzCpWirelessPortRxBlocksOKs = _HzCpWirelessPortRxBlocksOKs_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 2, 1, 3),
    _HzCpWirelessPortRxBlocksOKs_Type()
)
hzCpWirelessPortRxBlocksOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessPortRxBlocksOKs.setStatus("current")
_HzCpWirelessPortRxBlocksErrors_Type = Counter64
_HzCpWirelessPortRxBlocksErrors_Object = MibTableColumn
hzCpWirelessPortRxBlocksErrors = _HzCpWirelessPortRxBlocksErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 2, 1, 4),
    _HzCpWirelessPortRxBlocksErrors_Type()
)
hzCpWirelessPortRxBlocksErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessPortRxBlocksErrors.setStatus("current")
_HzCpWirelessAggregateStats_ObjectIdentity = ObjectIdentity
hzCpWirelessAggregateStats = _HzCpWirelessAggregateStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 3)
)
_HzCpWirelessAggTxFrames_Type = Counter64
_HzCpWirelessAggTxFrames_Object = MibScalar
hzCpWirelessAggTxFrames = _HzCpWirelessAggTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 3, 1),
    _HzCpWirelessAggTxFrames_Type()
)
hzCpWirelessAggTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessAggTxFrames.setStatus("current")
_HzCpWirelessAggRxFramesOK_Type = Counter64
_HzCpWirelessAggRxFramesOK_Object = MibScalar
hzCpWirelessAggRxFramesOK = _HzCpWirelessAggRxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 3, 2),
    _HzCpWirelessAggRxFramesOK_Type()
)
hzCpWirelessAggRxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessAggRxFramesOK.setStatus("current")
_HzCpWirelessAggRxFramesErrors_Type = Counter64
_HzCpWirelessAggRxFramesErrors_Object = MibScalar
hzCpWirelessAggRxFramesErrors = _HzCpWirelessAggRxFramesErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 3, 3),
    _HzCpWirelessAggRxFramesErrors_Type()
)
hzCpWirelessAggRxFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessAggRxFramesErrors.setStatus("current")
_HzCpWirelessAggRxFramesDiscards_Type = Counter64
_HzCpWirelessAggRxFramesDiscards_Object = MibScalar
hzCpWirelessAggRxFramesDiscards = _HzCpWirelessAggRxFramesDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 3, 4),
    _HzCpWirelessAggRxFramesDiscards_Type()
)
hzCpWirelessAggRxFramesDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessAggRxFramesDiscards.setStatus("current")
_HzCpWirelessPortLcStatsTable_Object = MibTable
hzCpWirelessPortLcStatsTable = _HzCpWirelessPortLcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 4)
)
if mibBuilder.loadTexts:
    hzCpWirelessPortLcStatsTable.setStatus("current")
_HzCpWirelessPortLcStatsEntry_Object = MibTableRow
hzCpWirelessPortLcStatsEntry = _HzCpWirelessPortLcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 4, 1)
)
hzCpWirelessPortLcStatsEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpWirelessPortLcStatsIndex"),
)
if mibBuilder.loadTexts:
    hzCpWirelessPortLcStatsEntry.setStatus("current")


class _HzCpWirelessPortLcStatsIndex_Type(Integer32):
    """Custom type hzCpWirelessPortLcStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wireless-port-1", 1),
          ("wireless-port-2", 2))
    )


_HzCpWirelessPortLcStatsIndex_Type.__name__ = "Integer32"
_HzCpWirelessPortLcStatsIndex_Object = MibTableColumn
hzCpWirelessPortLcStatsIndex = _HzCpWirelessPortLcStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 4, 1, 1),
    _HzCpWirelessPortLcStatsIndex_Type()
)
hzCpWirelessPortLcStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessPortLcStatsIndex.setStatus("current")
_HzCpWirelessPortLcTxBlocks_Type = Counter32
_HzCpWirelessPortLcTxBlocks_Object = MibTableColumn
hzCpWirelessPortLcTxBlocks = _HzCpWirelessPortLcTxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 4, 1, 2),
    _HzCpWirelessPortLcTxBlocks_Type()
)
hzCpWirelessPortLcTxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessPortLcTxBlocks.setStatus("current")
_HzCpWirelessPortLcRxBlocksOKs_Type = Counter32
_HzCpWirelessPortLcRxBlocksOKs_Object = MibTableColumn
hzCpWirelessPortLcRxBlocksOKs = _HzCpWirelessPortLcRxBlocksOKs_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 4, 1, 3),
    _HzCpWirelessPortLcRxBlocksOKs_Type()
)
hzCpWirelessPortLcRxBlocksOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessPortLcRxBlocksOKs.setStatus("current")
_HzCpWirelessPortLcRxBlocksErrors_Type = Counter32
_HzCpWirelessPortLcRxBlocksErrors_Object = MibTableColumn
hzCpWirelessPortLcRxBlocksErrors = _HzCpWirelessPortLcRxBlocksErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 4, 1, 4),
    _HzCpWirelessPortLcRxBlocksErrors_Type()
)
hzCpWirelessPortLcRxBlocksErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessPortLcRxBlocksErrors.setStatus("current")
_HzCpWirelessAggregateLcStats_ObjectIdentity = ObjectIdentity
hzCpWirelessAggregateLcStats = _HzCpWirelessAggregateLcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 5)
)
_HzCpWirelessAggLcTxFrames_Type = Counter32
_HzCpWirelessAggLcTxFrames_Object = MibScalar
hzCpWirelessAggLcTxFrames = _HzCpWirelessAggLcTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 5, 1),
    _HzCpWirelessAggLcTxFrames_Type()
)
hzCpWirelessAggLcTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessAggLcTxFrames.setStatus("current")
_HzCpWirelessAggLcRxFramesOK_Type = Counter32
_HzCpWirelessAggLcRxFramesOK_Object = MibScalar
hzCpWirelessAggLcRxFramesOK = _HzCpWirelessAggLcRxFramesOK_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 5, 2),
    _HzCpWirelessAggLcRxFramesOK_Type()
)
hzCpWirelessAggLcRxFramesOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessAggLcRxFramesOK.setStatus("current")
_HzCpWirelessAggLcRxFramesErrors_Type = Counter32
_HzCpWirelessAggLcRxFramesErrors_Object = MibScalar
hzCpWirelessAggLcRxFramesErrors = _HzCpWirelessAggLcRxFramesErrors_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 5, 3),
    _HzCpWirelessAggLcRxFramesErrors_Type()
)
hzCpWirelessAggLcRxFramesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessAggLcRxFramesErrors.setStatus("current")
_HzCpWirelessAggLcRxFramesDiscards_Type = Counter32
_HzCpWirelessAggLcRxFramesDiscards_Object = MibScalar
hzCpWirelessAggLcRxFramesDiscards = _HzCpWirelessAggLcRxFramesDiscards_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 2, 5, 4),
    _HzCpWirelessAggLcRxFramesDiscards_Type()
)
hzCpWirelessAggLcRxFramesDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessAggLcRxFramesDiscards.setStatus("current")
_HzCpWirelessInterfaceRadios_ObjectIdentity = ObjectIdentity
hzCpWirelessInterfaceRadios = _HzCpWirelessInterfaceRadios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4)
)
_HzCpRadioTable_Object = MibTable
hzCpRadioTable = _HzCpRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1)
)
if mibBuilder.loadTexts:
    hzCpRadioTable.setStatus("current")
_HzCpRadioEntry_Object = MibTableRow
hzCpRadioEntry = _HzCpRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1)
)
hzCpRadioEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
)
if mibBuilder.loadTexts:
    hzCpRadioEntry.setStatus("current")


class _HzCpRadioIndex_Type(Integer32):
    """Custom type hzCpRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wireless-port-1", 1)
    )


_HzCpRadioIndex_Type.__name__ = "Integer32"
_HzCpRadioIndex_Object = MibTableColumn
hzCpRadioIndex = _HzCpRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 1),
    _HzCpRadioIndex_Type()
)
hzCpRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadioIndex.setStatus("current")
_HzCpRadioDescription_Type = DisplayString
_HzCpRadioDescription_Object = MibTableColumn
hzCpRadioDescription = _HzCpRadioDescription_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 2),
    _HzCpRadioDescription_Type()
)
hzCpRadioDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadioDescription.setStatus("current")


class _HzCpRadioOperStatus_Type(Integer32):
    """Custom type hzCpRadioOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_HzCpRadioOperStatus_Type.__name__ = "Integer32"
_HzCpRadioOperStatus_Object = MibTableColumn
hzCpRadioOperStatus = _HzCpRadioOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 3),
    _HzCpRadioOperStatus_Type()
)
hzCpRadioOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadioOperStatus.setStatus("current")
_HzCpRadioTxGain_Type = Integer32
_HzCpRadioTxGain_Object = MibTableColumn
hzCpRadioTxGain = _HzCpRadioTxGain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 4),
    _HzCpRadioTxGain_Type()
)
hzCpRadioTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadioTxGain.setStatus("current")
_HzCpRadioRxGain_Type = Integer32
_HzCpRadioRxGain_Object = MibTableColumn
hzCpRadioRxGain = _HzCpRadioRxGain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 5),
    _HzCpRadioRxGain_Type()
)
hzCpRadioRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadioRxGain.setStatus("current")
_HzCpRadioReset_Type = Integer32
_HzCpRadioReset_Object = MibTableColumn
hzCpRadioReset = _HzCpRadioReset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 6),
    _HzCpRadioReset_Type()
)
hzCpRadioReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadioReset.setStatus("current")


class _HzCpRadioTransmitPowerdBm_Type(Integer32):
    """Custom type hzCpRadioTransmitPowerdBm based on Integer32"""
    defaultValue = 0


_HzCpRadioTransmitPowerdBm_Type.__name__ = "Integer32"
_HzCpRadioTransmitPowerdBm_Object = MibTableColumn
hzCpRadioTransmitPowerdBm = _HzCpRadioTransmitPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 7),
    _HzCpRadioTransmitPowerdBm_Type()
)
hzCpRadioTransmitPowerdBm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadioTransmitPowerdBm.setStatus("current")


class _HzCpRadioPowerOption_Type(Integer32):
    """Custom type hzCpRadioPowerOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("highPower", 2))
    )


_HzCpRadioPowerOption_Type.__name__ = "Integer32"
_HzCpRadioPowerOption_Object = MibTableColumn
hzCpRadioPowerOption = _HzCpRadioPowerOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 8),
    _HzCpRadioPowerOption_Type()
)
hzCpRadioPowerOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadioPowerOption.setStatus("current")


class _HzCpRadioTxState_Type(Integer32):
    """Custom type hzCpRadioTxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpRadioTxState_Type.__name__ = "Integer32"
_HzCpRadioTxState_Object = MibTableColumn
hzCpRadioTxState = _HzCpRadioTxState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 9),
    _HzCpRadioTxState_Type()
)
hzCpRadioTxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadioTxState.setStatus("current")


class _HzCpRadioActualTxState_Type(Integer32):
    """Custom type hzCpRadioActualTxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpRadioActualTxState_Type.__name__ = "Integer32"
_HzCpRadioActualTxState_Object = MibTableColumn
hzCpRadioActualTxState = _HzCpRadioActualTxState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 10),
    _HzCpRadioActualTxState_Type()
)
hzCpRadioActualTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadioActualTxState.setStatus("current")
_HzCpRadioTemperature_Type = Integer32
_HzCpRadioTemperature_Object = MibTableColumn
hzCpRadioTemperature = _HzCpRadioTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 11),
    _HzCpRadioTemperature_Type()
)
hzCpRadioTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadioTemperature.setStatus("current")
_HzCpRadioMaxTransmitPowerdBm_Type = Integer32
_HzCpRadioMaxTransmitPowerdBm_Object = MibTableColumn
hzCpRadioMaxTransmitPowerdBm = _HzCpRadioMaxTransmitPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 12),
    _HzCpRadioMaxTransmitPowerdBm_Type()
)
hzCpRadioMaxTransmitPowerdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadioMaxTransmitPowerdBm.setStatus("current")
_HzCpRadioActualTransmitPowerdBm_Type = Integer32
_HzCpRadioActualTransmitPowerdBm_Object = MibTableColumn
hzCpRadioActualTransmitPowerdBm = _HzCpRadioActualTransmitPowerdBm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 4, 1, 1, 13),
    _HzCpRadioActualTransmitPowerdBm_Type()
)
hzCpRadioActualTransmitPowerdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadioActualTransmitPowerdBm.setStatus("current")
_HzCpWirelessInterfaceRadioFrequencies_ObjectIdentity = ObjectIdentity
hzCpWirelessInterfaceRadioFrequencies = _HzCpWirelessInterfaceRadioFrequencies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5)
)
_HzCpWirelessInterfaceRadio1Frequencies_ObjectIdentity = ObjectIdentity
hzCpWirelessInterfaceRadio1Frequencies = _HzCpWirelessInterfaceRadio1Frequencies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1)
)


class _HzCpRadio1FreqGroupSelected_Type(Integer32):
    """Custom type hzCpRadio1FreqGroupSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("txLow", 1),
          ("txHigh", 2),
          ("none", 3))
    )


_HzCpRadio1FreqGroupSelected_Type.__name__ = "Integer32"
_HzCpRadio1FreqGroupSelected_Object = MibScalar
hzCpRadio1FreqGroupSelected = _HzCpRadio1FreqGroupSelected_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 1),
    _HzCpRadio1FreqGroupSelected_Type()
)
hzCpRadio1FreqGroupSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1FreqGroupSelected.setStatus("current")
_HzCpRadio1BandTable_Object = MibTable
hzCpRadio1BandTable = _HzCpRadio1BandTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hzCpRadio1BandTable.setStatus("current")
_HzCpRadio1BandEntry_Object = MibTableRow
hzCpRadio1BandEntry = _HzCpRadio1BandEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 2, 1)
)
hzCpRadio1BandEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpRadio1BandIndex"),
)
if mibBuilder.loadTexts:
    hzCpRadio1BandEntry.setStatus("current")
_HzCpRadio1BandIndex_Type = Integer32
_HzCpRadio1BandIndex_Object = MibTableColumn
hzCpRadio1BandIndex = _HzCpRadio1BandIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 2, 1, 1),
    _HzCpRadio1BandIndex_Type()
)
hzCpRadio1BandIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1BandIndex.setStatus("current")
_HzCpRadio1BandId_Type = Integer32
_HzCpRadio1BandId_Object = MibTableColumn
hzCpRadio1BandId = _HzCpRadio1BandId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 2, 1, 2),
    _HzCpRadio1BandId_Type()
)
hzCpRadio1BandId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1BandId.setStatus("current")
_HzCpRadio1BandName_Type = DisplayString
_HzCpRadio1BandName_Object = MibTableColumn
hzCpRadio1BandName = _HzCpRadio1BandName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 2, 1, 3),
    _HzCpRadio1BandName_Type()
)
hzCpRadio1BandName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1BandName.setStatus("current")


class _HzCpRadio1BandProgrammed_Type(Integer32):
    """Custom type hzCpRadio1BandProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzCpRadio1BandProgrammed_Type.__name__ = "Integer32"
_HzCpRadio1BandProgrammed_Object = MibTableColumn
hzCpRadio1BandProgrammed = _HzCpRadio1BandProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 2, 1, 4),
    _HzCpRadio1BandProgrammed_Type()
)
hzCpRadio1BandProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadio1BandProgrammed.setStatus("current")
_HzCpRadio1FreqTable_Object = MibTable
hzCpRadio1FreqTable = _HzCpRadio1FreqTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hzCpRadio1FreqTable.setStatus("current")
_HzCpRadio1FreqEntry_Object = MibTableRow
hzCpRadio1FreqEntry = _HzCpRadio1FreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 3, 1)
)
hzCpRadio1FreqEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpRadio1FreqIndex"),
)
if mibBuilder.loadTexts:
    hzCpRadio1FreqEntry.setStatus("current")
_HzCpRadio1FreqIndex_Type = Integer32
_HzCpRadio1FreqIndex_Object = MibTableColumn
hzCpRadio1FreqIndex = _HzCpRadio1FreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 3, 1, 1),
    _HzCpRadio1FreqIndex_Type()
)
hzCpRadio1FreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1FreqIndex.setStatus("current")
_HzCpRadio1FreqChannelIndex_Type = DisplayString
_HzCpRadio1FreqChannelIndex_Object = MibTableColumn
hzCpRadio1FreqChannelIndex = _HzCpRadio1FreqChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 3, 1, 2),
    _HzCpRadio1FreqChannelIndex_Type()
)
hzCpRadio1FreqChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1FreqChannelIndex.setStatus("current")
_HzCpRadio1FreqTransmitRfFrequency_Type = Integer32
_HzCpRadio1FreqTransmitRfFrequency_Object = MibTableColumn
hzCpRadio1FreqTransmitRfFrequency = _HzCpRadio1FreqTransmitRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 3, 1, 3),
    _HzCpRadio1FreqTransmitRfFrequency_Type()
)
hzCpRadio1FreqTransmitRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1FreqTransmitRfFrequency.setStatus("current")
_HzCpRadio1FreqReceiveRfFrequency_Type = Integer32
_HzCpRadio1FreqReceiveRfFrequency_Object = MibTableColumn
hzCpRadio1FreqReceiveRfFrequency = _HzCpRadio1FreqReceiveRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 3, 1, 4),
    _HzCpRadio1FreqReceiveRfFrequency_Type()
)
hzCpRadio1FreqReceiveRfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1FreqReceiveRfFrequency.setStatus("current")


class _HzCpRadio1FreqProgrammed_Type(Integer32):
    """Custom type hzCpRadio1FreqProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzCpRadio1FreqProgrammed_Type.__name__ = "Integer32"
_HzCpRadio1FreqProgrammed_Object = MibTableColumn
hzCpRadio1FreqProgrammed = _HzCpRadio1FreqProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 3, 1, 5),
    _HzCpRadio1FreqProgrammed_Type()
)
hzCpRadio1FreqProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRadio1FreqProgrammed.setStatus("current")
_HzCpRadio1ProgrammedFrequency_ObjectIdentity = ObjectIdentity
hzCpRadio1ProgrammedFrequency = _HzCpRadio1ProgrammedFrequency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 4)
)
_HzCpRadio1ProgrammedFrequencyChannel_Type = DisplayString
_HzCpRadio1ProgrammedFrequencyChannel_Object = MibScalar
hzCpRadio1ProgrammedFrequencyChannel = _HzCpRadio1ProgrammedFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 4, 1),
    _HzCpRadio1ProgrammedFrequencyChannel_Type()
)
hzCpRadio1ProgrammedFrequencyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1ProgrammedFrequencyChannel.setStatus("current")
_HzCpRadio1ProgrammedFrequencyTxRf_Type = Integer32
_HzCpRadio1ProgrammedFrequencyTxRf_Object = MibScalar
hzCpRadio1ProgrammedFrequencyTxRf = _HzCpRadio1ProgrammedFrequencyTxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 4, 2),
    _HzCpRadio1ProgrammedFrequencyTxRf_Type()
)
hzCpRadio1ProgrammedFrequencyTxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1ProgrammedFrequencyTxRf.setStatus("current")
_HzCpRadio1ProgrammedFrequencyRxRf_Type = Integer32
_HzCpRadio1ProgrammedFrequencyRxRf_Object = MibScalar
hzCpRadio1ProgrammedFrequencyRxRf = _HzCpRadio1ProgrammedFrequencyRxRf_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 1, 4, 3),
    _HzCpRadio1ProgrammedFrequencyRxRf_Type()
)
hzCpRadio1ProgrammedFrequencyRxRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRadio1ProgrammedFrequencyRxRf.setStatus("current")
_HzCpSystemModeTable_Object = MibTable
hzCpSystemModeTable = _HzCpSystemModeTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 2)
)
if mibBuilder.loadTexts:
    hzCpSystemModeTable.setStatus("current")
_HzCpSystemModeEntry_Object = MibTableRow
hzCpSystemModeEntry = _HzCpSystemModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 2, 1)
)
hzCpSystemModeEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpSystemModeIndex"),
)
if mibBuilder.loadTexts:
    hzCpSystemModeEntry.setStatus("current")
_HzCpSystemModeIndex_Type = Integer32
_HzCpSystemModeIndex_Object = MibTableColumn
hzCpSystemModeIndex = _HzCpSystemModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 2, 1, 1),
    _HzCpSystemModeIndex_Type()
)
hzCpSystemModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSystemModeIndex.setStatus("current")
_HzCpSystemModeId_Type = Integer32
_HzCpSystemModeId_Object = MibTableColumn
hzCpSystemModeId = _HzCpSystemModeId_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 2, 1, 2),
    _HzCpSystemModeId_Type()
)
hzCpSystemModeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSystemModeId.setStatus("current")
_HzCpSystemModeName_Type = DisplayString
_HzCpSystemModeName_Object = MibTableColumn
hzCpSystemModeName = _HzCpSystemModeName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 2, 1, 3),
    _HzCpSystemModeName_Type()
)
hzCpSystemModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSystemModeName.setStatus("current")


class _HzCpSystemModeProgrammed_Type(Integer32):
    """Custom type hzCpSystemModeProgrammed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_HzCpSystemModeProgrammed_Type.__name__ = "Integer32"
_HzCpSystemModeProgrammed_Object = MibTableColumn
hzCpSystemModeProgrammed = _HzCpSystemModeProgrammed_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 2, 1, 4),
    _HzCpSystemModeProgrammed_Type()
)
hzCpSystemModeProgrammed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSystemModeProgrammed.setStatus("current")


class _HzCpApplyFrequencyChangesToSystem_Type(Integer32):
    """Custom type hzCpApplyFrequencyChangesToSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("apply", 1)
    )


_HzCpApplyFrequencyChangesToSystem_Type.__name__ = "Integer32"
_HzCpApplyFrequencyChangesToSystem_Object = MibScalar
hzCpApplyFrequencyChangesToSystem = _HzCpApplyFrequencyChangesToSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 5, 3),
    _HzCpApplyFrequencyChangesToSystem_Type()
)
hzCpApplyFrequencyChangesToSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpApplyFrequencyChangesToSystem.setStatus("current")
_HzCpWirelessInterfaceAntenna_ObjectIdentity = ObjectIdentity
hzCpWirelessInterfaceAntenna = _HzCpWirelessInterfaceAntenna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 6)
)
_HzCpAntennaDiameter_Type = Integer32
_HzCpAntennaDiameter_Object = MibScalar
hzCpAntennaDiameter = _HzCpAntennaDiameter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 6, 1),
    _HzCpAntennaDiameter_Type()
)
hzCpAntennaDiameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpAntennaDiameter.setStatus("current")


class _HzCpAntennaTilt_Type(Integer32):
    """Custom type hzCpAntennaTilt based on Integer32"""
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
        *(("unknown", 1),
          ("vertical", 2),
          ("horizontal", 3),
          ("flat", 4))
    )


_HzCpAntennaTilt_Type.__name__ = "Integer32"
_HzCpAntennaTilt_Object = MibScalar
hzCpAntennaTilt = _HzCpAntennaTilt_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 4, 6, 2),
    _HzCpAntennaTilt_Type()
)
hzCpAntennaTilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpAntennaTilt.setStatus("current")
_HzCpAlarms_ObjectIdentity = ObjectIdentity
hzCpAlarms = _HzCpAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5)
)
_HzCpThresholdAlarmConfig_ObjectIdentity = ObjectIdentity
hzCpThresholdAlarmConfig = _HzCpThresholdAlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1)
)
_HzCpAggregatedThresholdAlarm_ObjectIdentity = ObjectIdentity
hzCpAggregatedThresholdAlarm = _HzCpAggregatedThresholdAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 1)
)


class _HzCpDroppedFramesThresholdParams_Type(DisplayString):
    """Custom type hzCpDroppedFramesThresholdParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzCpDroppedFramesThresholdParams_Type.__name__ = "DisplayString"
_HzCpDroppedFramesThresholdParams_Object = MibScalar
hzCpDroppedFramesThresholdParams = _HzCpDroppedFramesThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 1, 1),
    _HzCpDroppedFramesThresholdParams_Type()
)
hzCpDroppedFramesThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpDroppedFramesThresholdParams.setStatus("current")


class _HzCpBwUtilizationThresholdParams_Type(DisplayString):
    """Custom type hzCpBwUtilizationThresholdParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzCpBwUtilizationThresholdParams_Type.__name__ = "DisplayString"
_HzCpBwUtilizationThresholdParams_Object = MibScalar
hzCpBwUtilizationThresholdParams = _HzCpBwUtilizationThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 1, 2),
    _HzCpBwUtilizationThresholdParams_Type()
)
hzCpBwUtilizationThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpBwUtilizationThresholdParams.setStatus("current")
_HzCpQBasedThresholdAlarm_ObjectIdentity = ObjectIdentity
hzCpQBasedThresholdAlarm = _HzCpQBasedThresholdAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 2)
)
_HzCpQBasedThresholdAlarmTable_Object = MibTable
hzCpQBasedThresholdAlarmTable = _HzCpQBasedThresholdAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hzCpQBasedThresholdAlarmTable.setStatus("current")
_HzCpQBasedThresholdAlarmEntry_Object = MibTableRow
hzCpQBasedThresholdAlarmEntry = _HzCpQBasedThresholdAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 2, 1, 1)
)
hzCpQBasedThresholdAlarmEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpQBasedThresholdIndex"),
)
if mibBuilder.loadTexts:
    hzCpQBasedThresholdAlarmEntry.setStatus("current")


class _HzCpQBasedThresholdIndex_Type(Integer32):
    """Custom type hzCpQBasedThresholdIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_HzCpQBasedThresholdIndex_Type.__name__ = "Integer32"
_HzCpQBasedThresholdIndex_Object = MibTableColumn
hzCpQBasedThresholdIndex = _HzCpQBasedThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 2, 1, 1, 1),
    _HzCpQBasedThresholdIndex_Type()
)
hzCpQBasedThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpQBasedThresholdIndex.setStatus("current")
_HzCpQBasedDepthThresholdParams_Type = DisplayString
_HzCpQBasedDepthThresholdParams_Object = MibTableColumn
hzCpQBasedDepthThresholdParams = _HzCpQBasedDepthThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 2, 1, 1, 2),
    _HzCpQBasedDepthThresholdParams_Type()
)
hzCpQBasedDepthThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpQBasedDepthThresholdParams.setStatus("current")
_HzCpQBasedDroppedFramesThresholdParams_Type = DisplayString
_HzCpQBasedDroppedFramesThresholdParams_Object = MibTableColumn
hzCpQBasedDroppedFramesThresholdParams = _HzCpQBasedDroppedFramesThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 2, 1, 1, 3),
    _HzCpQBasedDroppedFramesThresholdParams_Type()
)
hzCpQBasedDroppedFramesThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpQBasedDroppedFramesThresholdParams.setStatus("current")
_HzCpWirelessInterfaceThresholdAlarmTable_Object = MibTable
hzCpWirelessInterfaceThresholdAlarmTable = _HzCpWirelessInterfaceThresholdAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hzCpWirelessInterfaceThresholdAlarmTable.setStatus("current")
_HzCpWirelessInterfaceThresholdAlarmEntry_Object = MibTableRow
hzCpWirelessInterfaceThresholdAlarmEntry = _HzCpWirelessInterfaceThresholdAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 3, 1)
)
hzCpWirelessInterfaceThresholdAlarmEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpWirelessInterfaceThresholdAlarmIndex"),
)
if mibBuilder.loadTexts:
    hzCpWirelessInterfaceThresholdAlarmEntry.setStatus("current")


class _HzCpWirelessInterfaceThresholdAlarmIndex_Type(Integer32):
    """Custom type hzCpWirelessInterfaceThresholdAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wireless-port-1", 1)
    )


_HzCpWirelessInterfaceThresholdAlarmIndex_Type.__name__ = "Integer32"
_HzCpWirelessInterfaceThresholdAlarmIndex_Object = MibTableColumn
hzCpWirelessInterfaceThresholdAlarmIndex = _HzCpWirelessInterfaceThresholdAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 3, 1, 1),
    _HzCpWirelessInterfaceThresholdAlarmIndex_Type()
)
hzCpWirelessInterfaceThresholdAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessInterfaceThresholdAlarmIndex.setStatus("current")


class _HzCpWirelessInterfaceRslThresholdParams_Type(DisplayString):
    """Custom type hzCpWirelessInterfaceRslThresholdParams based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzCpWirelessInterfaceRslThresholdParams_Type.__name__ = "DisplayString"
_HzCpWirelessInterfaceRslThresholdParams_Object = MibTableColumn
hzCpWirelessInterfaceRslThresholdParams = _HzCpWirelessInterfaceRslThresholdParams_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 3, 1, 2),
    _HzCpWirelessInterfaceRslThresholdParams_Type()
)
hzCpWirelessInterfaceRslThresholdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpWirelessInterfaceRslThresholdParams.setStatus("current")


class _HzCpWirelessInterfaceSnrThreshold_Type(DisplayString):
    """Custom type hzCpWirelessInterfaceSnrThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzCpWirelessInterfaceSnrThreshold_Type.__name__ = "DisplayString"
_HzCpWirelessInterfaceSnrThreshold_Object = MibTableColumn
hzCpWirelessInterfaceSnrThreshold = _HzCpWirelessInterfaceSnrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 1, 3, 1, 3),
    _HzCpWirelessInterfaceSnrThreshold_Type()
)
hzCpWirelessInterfaceSnrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpWirelessInterfaceSnrThreshold.setStatus("current")
_HzCpAlarmConfigTable_Object = MibTable
hzCpAlarmConfigTable = _HzCpAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 2)
)
if mibBuilder.loadTexts:
    hzCpAlarmConfigTable.setStatus("current")
_HzCpAlarmConfigEntry_Object = MibTableRow
hzCpAlarmConfigEntry = _HzCpAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 2, 1)
)
hzCpAlarmConfigEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigIndex"),
    (0, "DRAGONWAVE-HCP-MIB", "hzCpAlarmInstanceIndex"),
)
if mibBuilder.loadTexts:
    hzCpAlarmConfigEntry.setStatus("current")


class _HzCpAlarmConfigIndex_Type(Integer32):
    """Custom type hzCpAlarmConfigIndex based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 1),
          ("peerAuthenticationFailure", 2),
          ("haamConfigMismatch", 3),
          ("haamOnLowModulation", 4),
          ("atpcConfigMismatch", 5),
          ("atpcAutoDisabled", 6),
          ("sntpUnreachable", 7),
          ("freqFileInvalid", 8),
          ("aggregateDroppedFramesThreshold", 9),
          ("queueDroppedFramesThreshold", 10),
          ("bwUtilizationThreshold", 11),
          ("queueDepthThreshold", 12),
          ("rlsConfigMismatch", 13),
          ("rlsShutdownActivated", 14),
          ("rlsQBasedShutdown", 15),
          ("modemRxLossOfSignal", 16),
          ("modemSnrBelowThreshold", 17),
          ("modemEqStressAboveThreshold", 18),
          ("rslBelowThershold", 19),
          ("radioSynthLostLock", 20),
          ("radioCalTableUnavailable", 21),
          ("radioCurrentOutOfLimits", 22),
          ("radioPowerAmp", 23),
          ("tempOutOfLimits", 24),
          ("redundancyConfigMismatch", 25),
          ("redundancyActiveOnSecondary", 26),
          ("redundancyOperatingInForcedSwitch", 27),
          ("redundancyEnetCrossLinkActive", 28),
          ("redundancyActiveUsingPartnerWLink", 29),
          ("redundancyStandbyWLinkInUse", 30),
          ("redundancyStandbyOnPrimary", 31),
          ("x2DeliveringHalfCapacity", 32),
          ("bncSignalNotDetected", 33),
          ("ethernetSpeedReduced", 34),
          ("synceLostLock", 35),
          ("synceSecondarySourceInUse", 36),
          ("invalidSysConfig", 37),
          ("mibChangeNotSaved", 38),
          ("transmitterLossOfSync", 39),
          ("radioLinearityCalError", 40),
          ("synceConfigMismatch", 41),
          ("cryptoPowerUpTestsFailed", 42),
          ("cyptoConfigMismatch", 43))
    )


_HzCpAlarmConfigIndex_Type.__name__ = "Integer32"
_HzCpAlarmConfigIndex_Object = MibTableColumn
hzCpAlarmConfigIndex = _HzCpAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 2, 1, 1),
    _HzCpAlarmConfigIndex_Type()
)
hzCpAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpAlarmConfigIndex.setStatus("current")
_HzCpAlarmInstanceIndex_Type = Unsigned32
_HzCpAlarmInstanceIndex_Object = MibTableColumn
hzCpAlarmInstanceIndex = _HzCpAlarmInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 2, 1, 2),
    _HzCpAlarmInstanceIndex_Type()
)
hzCpAlarmInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpAlarmInstanceIndex.setStatus("current")


class _HzCpAlarmConfigSeverity_Type(Integer32):
    """Custom type hzCpAlarmConfigSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("minor", 1),
          ("major", 2),
          ("critical", 3))
    )


_HzCpAlarmConfigSeverity_Type.__name__ = "Integer32"
_HzCpAlarmConfigSeverity_Object = MibTableColumn
hzCpAlarmConfigSeverity = _HzCpAlarmConfigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 2, 1, 3),
    _HzCpAlarmConfigSeverity_Type()
)
hzCpAlarmConfigSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpAlarmConfigSeverity.setStatus("current")


class _HzCpAlarmConfigState_Type(Integer32):
    """Custom type hzCpAlarmConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HzCpAlarmConfigState_Type.__name__ = "Integer32"
_HzCpAlarmConfigState_Object = MibTableColumn
hzCpAlarmConfigState = _HzCpAlarmConfigState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 2, 1, 4),
    _HzCpAlarmConfigState_Type()
)
hzCpAlarmConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpAlarmConfigState.setStatus("current")
_HzCpAlarmStatusTable_Object = MibTable
hzCpAlarmStatusTable = _HzCpAlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 3)
)
if mibBuilder.loadTexts:
    hzCpAlarmStatusTable.setStatus("current")
_HzCpAlarmStatusEntry_Object = MibTableRow
hzCpAlarmStatusEntry = _HzCpAlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 3, 1)
)
hzCpAlarmStatusEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpAlarmStatusIndex"),
    (0, "DRAGONWAVE-HCP-MIB", "hzCpAlarmStatusInstanceIndex"),
)
if mibBuilder.loadTexts:
    hzCpAlarmStatusEntry.setStatus("current")


class _HzCpAlarmStatusIndex_Type(Integer32):
    """Custom type hzCpAlarmStatusIndex based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 1),
          ("peerAuthenticationFailure", 2),
          ("haamConfigMismatch", 3),
          ("haamOnLowModulation", 4),
          ("atpcConfigMismatch", 5),
          ("atpcAutoDisabled", 6),
          ("sntpUnreachable", 7),
          ("freqFileInvalid", 8),
          ("aggregateDroppedFramesThreshold", 9),
          ("queueDroppedFramesThreshold", 10),
          ("bwUtilizationThreshold", 11),
          ("queueDepthThreshold", 12),
          ("rlsConfigMismatch", 13),
          ("rlsShutdownActivated", 14),
          ("rlsQBasedShutdown", 15),
          ("modemRxLossOfSignal", 16),
          ("modemSnrBelowThreshold", 17),
          ("modemEqStressAboveThreshold", 18),
          ("rslBelowThershold", 19),
          ("radioSynthLostLock", 20),
          ("radioCalTableUnavailable", 21),
          ("radioCurrentOutOfLimits", 22),
          ("radioPowerAmp", 23),
          ("tempOutOfLimits", 24),
          ("redundancyConfigMismatch", 25),
          ("redundancyActiveOnSecondary", 26),
          ("redundancyOperatingInForcedSwitch", 27),
          ("redundancyEnetCrossLinkActive", 28),
          ("redundancyActiveUsingPartnerWLink", 29),
          ("redundancyStandbyWLinkInUse", 30),
          ("redundancyStandbyOnPrimary", 31),
          ("x2DeliveringHalfCapacity", 32),
          ("bncSignalNotDetected", 33),
          ("ethernetSpeedReduced", 34),
          ("synceLostLock", 35),
          ("synceSecondarySourceInUse", 36),
          ("invalidSysConfig", 37),
          ("mibChangeNotSaved", 38),
          ("transmitterLossOfSync", 39),
          ("radioLinearityCalError", 40),
          ("synceConfigMismatch", 41),
          ("cryptoPowerUpTestsFailed", 42),
          ("cryptoConfigMismatch", 43))
    )


_HzCpAlarmStatusIndex_Type.__name__ = "Integer32"
_HzCpAlarmStatusIndex_Object = MibTableColumn
hzCpAlarmStatusIndex = _HzCpAlarmStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 3, 1, 1),
    _HzCpAlarmStatusIndex_Type()
)
hzCpAlarmStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpAlarmStatusIndex.setStatus("current")
_HzCpAlarmStatusInstanceIndex_Type = Unsigned32
_HzCpAlarmStatusInstanceIndex_Object = MibTableColumn
hzCpAlarmStatusInstanceIndex = _HzCpAlarmStatusInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 3, 1, 2),
    _HzCpAlarmStatusInstanceIndex_Type()
)
hzCpAlarmStatusInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpAlarmStatusInstanceIndex.setStatus("current")


class _HzCpAlarmStatus_Type(Integer32):
    """Custom type hzCpAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpAlarmStatus_Type.__name__ = "Integer32"
_HzCpAlarmStatus_Object = MibTableColumn
hzCpAlarmStatus = _HzCpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 3, 1, 3),
    _HzCpAlarmStatus_Type()
)
hzCpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpAlarmStatus.setStatus("current")
_HzCpAlarmRaisedDateAndTime_Type = DateAndTime
_HzCpAlarmRaisedDateAndTime_Object = MibTableColumn
hzCpAlarmRaisedDateAndTime = _HzCpAlarmRaisedDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 3, 1, 4),
    _HzCpAlarmRaisedDateAndTime_Type()
)
hzCpAlarmRaisedDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpAlarmRaisedDateAndTime.setStatus("current")
_HzCpAlarmClearedDateAndTime_Type = DateAndTime
_HzCpAlarmClearedDateAndTime_Object = MibTableColumn
hzCpAlarmClearedDateAndTime = _HzCpAlarmClearedDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 5, 3, 1, 5),
    _HzCpAlarmClearedDateAndTime_Type()
)
hzCpAlarmClearedDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpAlarmClearedDateAndTime.setStatus("current")
_HzCpQos_ObjectIdentity = ObjectIdentity
hzCpQos = _HzCpQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6)
)


class _HzCpQosEnable_Type(Integer32):
    """Custom type hzCpQosEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpQosEnable_Type.__name__ = "Integer32"
_HzCpQosEnable_Object = MibScalar
hzCpQosEnable = _HzCpQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 1),
    _HzCpQosEnable_Type()
)
hzCpQosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpQosEnable.setStatus("current")


class _HzCpCosType_Type(Integer32):
    """Custom type hzCpCosType based on Integer32"""
    defaultValue = 1

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
        *(("cosVlan", 1),
          ("cosQinQiTag", 2),
          ("cosQinQoTag", 3),
          ("cosDscp", 4),
          ("cosMplsExp", 5))
    )


_HzCpCosType_Type.__name__ = "Integer32"
_HzCpCosType_Object = MibScalar
hzCpCosType = _HzCpCosType_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 2),
    _HzCpCosType_Type()
)
hzCpCosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosType.setStatus("current")
_HzCpCosQinQiTag_Type = DisplayString
_HzCpCosQinQiTag_Object = MibScalar
hzCpCosQinQiTag = _HzCpCosQinQiTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 3),
    _HzCpCosQinQiTag_Type()
)
hzCpCosQinQiTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosQinQiTag.setStatus("current")
_HzCpCosQinQoTag_Type = DisplayString
_HzCpCosQinQoTag_Object = MibScalar
hzCpCosQinQoTag = _HzCpCosQinQoTag_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 4),
    _HzCpCosQinQoTag_Type()
)
hzCpCosQinQoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosQinQoTag.setStatus("current")


class _HzCpCosExpediteQueue_Type(Integer32):
    """Custom type hzCpCosExpediteQueue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpCosExpediteQueue_Type.__name__ = "Integer32"
_HzCpCosExpediteQueue_Object = MibScalar
hzCpCosExpediteQueue = _HzCpCosExpediteQueue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 5),
    _HzCpCosExpediteQueue_Type()
)
hzCpCosExpediteQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosExpediteQueue.setStatus("current")


class _HzCpCosQueueCIR_Type(DisplayString):
    """Custom type hzCpCosQueueCIR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpCosQueueCIR_Type.__name__ = "DisplayString"
_HzCpCosQueueCIR_Object = MibScalar
hzCpCosQueueCIR = _HzCpCosQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 6),
    _HzCpCosQueueCIR_Type()
)
hzCpCosQueueCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosQueueCIR.setStatus("current")


class _HzCpCosQueueCBS_Type(DisplayString):
    """Custom type hzCpCosQueueCBS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpCosQueueCBS_Type.__name__ = "DisplayString"
_HzCpCosQueueCBS_Object = MibScalar
hzCpCosQueueCBS = _HzCpCosQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 7),
    _HzCpCosQueueCBS_Type()
)
hzCpCosQueueCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosQueueCBS.setStatus("current")


class _HzCpQosPolicy_Type(Integer32):
    """Custom type hzCpQosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict-priority", 1),
          ("wfq", 2))
    )


_HzCpQosPolicy_Type.__name__ = "Integer32"
_HzCpQosPolicy_Object = MibScalar
hzCpQosPolicy = _HzCpQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 8),
    _HzCpQosPolicy_Type()
)
hzCpQosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpQosPolicy.setStatus("current")


class _HzCpCosWfqWeight_Type(DisplayString):
    """Custom type hzCpCosWfqWeight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HzCpCosWfqWeight_Type.__name__ = "DisplayString"
_HzCpCosWfqWeight_Object = MibScalar
hzCpCosWfqWeight = _HzCpCosWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 9),
    _HzCpCosWfqWeight_Type()
)
hzCpCosWfqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosWfqWeight.setStatus("current")
_HzCpCosNumPriorityQueues_Type = Integer32
_HzCpCosNumPriorityQueues_Object = MibScalar
hzCpCosNumPriorityQueues = _HzCpCosNumPriorityQueues_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 10),
    _HzCpCosNumPriorityQueues_Type()
)
hzCpCosNumPriorityQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosNumPriorityQueues.setStatus("current")


class _HzCpCosCutThroughQueue_Type(Integer32):
    """Custom type hzCpCosCutThroughQueue based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("q1", 2),
          ("q2", 3),
          ("q3", 4),
          ("q4", 5),
          ("q5", 6),
          ("q6", 7),
          ("q7", 8),
          ("q8", 9))
    )


_HzCpCosCutThroughQueue_Type.__name__ = "Integer32"
_HzCpCosCutThroughQueue_Object = MibScalar
hzCpCosCutThroughQueue = _HzCpCosCutThroughQueue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 11),
    _HzCpCosCutThroughQueue_Type()
)
hzCpCosCutThroughQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosCutThroughQueue.setStatus("current")
_HzCpQosPortConfigTable_Object = MibTable
hzCpQosPortConfigTable = _HzCpQosPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 12)
)
if mibBuilder.loadTexts:
    hzCpQosPortConfigTable.setStatus("current")
_HzCpQosPortConfigEntry_Object = MibTableRow
hzCpQosPortConfigEntry = _HzCpQosPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 12, 1)
)
hzCpQosPortConfigEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpCosPortIndex"),
)
if mibBuilder.loadTexts:
    hzCpQosPortConfigEntry.setStatus("current")


class _HzCpCosPortIndex_Type(Integer32):
    """Custom type hzCpCosPortIndex based on Integer32"""
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
        *(("enet-port-1", 1),
          ("enet-port-2", 2),
          ("enet-port-3", 3),
          ("enet-port-4", 4))
    )


_HzCpCosPortIndex_Type.__name__ = "Integer32"
_HzCpCosPortIndex_Object = MibTableColumn
hzCpCosPortIndex = _HzCpCosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 12, 1, 1),
    _HzCpCosPortIndex_Type()
)
hzCpCosPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpCosPortIndex.setStatus("current")
_HzCpCosQueueMapping_Type = DisplayString
_HzCpCosQueueMapping_Object = MibTableColumn
hzCpCosQueueMapping = _HzCpCosQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 12, 1, 2),
    _HzCpCosQueueMapping_Type()
)
hzCpCosQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosQueueMapping.setStatus("current")


class _HzCpCosDefaultValue_Type(Integer32):
    """Custom type hzCpCosDefaultValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HzCpCosDefaultValue_Type.__name__ = "Integer32"
_HzCpCosDefaultValue_Object = MibTableColumn
hzCpCosDefaultValue = _HzCpCosDefaultValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 12, 1, 3),
    _HzCpCosDefaultValue_Type()
)
hzCpCosDefaultValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosDefaultValue.setStatus("current")
_HzCpCosUserFlowDepTable_Object = MibTable
hzCpCosUserFlowDepTable = _HzCpCosUserFlowDepTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 13)
)
if mibBuilder.loadTexts:
    hzCpCosUserFlowDepTable.setStatus("deprecated")
_HzCpCosUserFlowDepEntry_Object = MibTableRow
hzCpCosUserFlowDepEntry = _HzCpCosUserFlowDepEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 13, 1)
)
hzCpCosUserFlowDepEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpCosUserFlowIndexDep"),
)
if mibBuilder.loadTexts:
    hzCpCosUserFlowDepEntry.setStatus("deprecated")


class _HzCpCosUserFlowIndexDep_Type(Integer32):
    """Custom type hzCpCosUserFlowIndexDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flow1", 1),
          ("flow2", 2),
          ("flow3", 3))
    )


_HzCpCosUserFlowIndexDep_Type.__name__ = "Integer32"
_HzCpCosUserFlowIndexDep_Object = MibTableColumn
hzCpCosUserFlowIndexDep = _HzCpCosUserFlowIndexDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 13, 1, 1),
    _HzCpCosUserFlowIndexDep_Type()
)
hzCpCosUserFlowIndexDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpCosUserFlowIndexDep.setStatus("deprecated")
_HzCpCosUserFlowStateDep_Type = DisplayString
_HzCpCosUserFlowStateDep_Object = MibTableColumn
hzCpCosUserFlowStateDep = _HzCpCosUserFlowStateDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 13, 1, 2),
    _HzCpCosUserFlowStateDep_Type()
)
hzCpCosUserFlowStateDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpCosUserFlowStateDep.setStatus("deprecated")
_HzCpCosUserClassTable_Object = MibTable
hzCpCosUserClassTable = _HzCpCosUserClassTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 14)
)
if mibBuilder.loadTexts:
    hzCpCosUserClassTable.setStatus("current")
_HzCpCosUserClassEntry_Object = MibTableRow
hzCpCosUserClassEntry = _HzCpCosUserClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 14, 1)
)
hzCpCosUserClassEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpCosUserClassIndex"),
)
if mibBuilder.loadTexts:
    hzCpCosUserClassEntry.setStatus("current")


class _HzCpCosUserClassIndex_Type(Integer32):
    """Custom type hzCpCosUserClassIndex based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("c1", 1),
          ("c2", 2),
          ("c3", 3),
          ("c4", 4),
          ("c5", 5),
          ("c6", 6),
          ("c7", 7),
          ("c8", 8),
          ("c9", 9),
          ("c10", 10),
          ("c11", 11),
          ("c12", 12),
          ("c13", 13))
    )


_HzCpCosUserClassIndex_Type.__name__ = "Integer32"
_HzCpCosUserClassIndex_Object = MibTableColumn
hzCpCosUserClassIndex = _HzCpCosUserClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 14, 1, 1),
    _HzCpCosUserClassIndex_Type()
)
hzCpCosUserClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpCosUserClassIndex.setStatus("current")
_HzCpCosUserClassOffset_Type = Integer32
_HzCpCosUserClassOffset_Object = MibTableColumn
hzCpCosUserClassOffset = _HzCpCosUserClassOffset_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 14, 1, 2),
    _HzCpCosUserClassOffset_Type()
)
hzCpCosUserClassOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserClassOffset.setStatus("current")
_HzCpCosUserClassValue_Type = DisplayString
_HzCpCosUserClassValue_Object = MibTableColumn
hzCpCosUserClassValue = _HzCpCosUserClassValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 14, 1, 3),
    _HzCpCosUserClassValue_Type()
)
hzCpCosUserClassValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserClassValue.setStatus("current")
_HzCpCosUserClassMask_Type = DisplayString
_HzCpCosUserClassMask_Object = MibTableColumn
hzCpCosUserClassMask = _HzCpCosUserClassMask_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 14, 1, 4),
    _HzCpCosUserClassMask_Type()
)
hzCpCosUserClassMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserClassMask.setStatus("current")
_HzCpCosUserFlowFilterTable_Object = MibTable
hzCpCosUserFlowFilterTable = _HzCpCosUserFlowFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 15)
)
if mibBuilder.loadTexts:
    hzCpCosUserFlowFilterTable.setStatus("current")
_HzCpCosUserFlowFilterEntry_Object = MibTableRow
hzCpCosUserFlowFilterEntry = _HzCpCosUserFlowFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 15, 1)
)
hzCpCosUserFlowFilterEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpCosUserFlowFilterIndex"),
)
if mibBuilder.loadTexts:
    hzCpCosUserFlowFilterEntry.setStatus("current")


class _HzCpCosUserFlowFilterIndex_Type(Integer32):
    """Custom type hzCpCosUserFlowFilterIndex based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("flow1", 1),
          ("flow2", 2),
          ("flow3", 3),
          ("flow4", 4),
          ("flow5", 5),
          ("flow6", 6),
          ("flow7", 7),
          ("flow8", 8),
          ("flow9", 9),
          ("flow10", 10),
          ("flow11", 11),
          ("flow12", 12),
          ("flow13", 13))
    )


_HzCpCosUserFlowFilterIndex_Type.__name__ = "Integer32"
_HzCpCosUserFlowFilterIndex_Object = MibTableColumn
hzCpCosUserFlowFilterIndex = _HzCpCosUserFlowFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 15, 1, 1),
    _HzCpCosUserFlowFilterIndex_Type()
)
hzCpCosUserFlowFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpCosUserFlowFilterIndex.setStatus("current")
_HzCpCosUserFlowFilter_Type = DisplayString
_HzCpCosUserFlowFilter_Object = MibTableColumn
hzCpCosUserFlowFilter = _HzCpCosUserFlowFilter_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 15, 1, 2),
    _HzCpCosUserFlowFilter_Type()
)
hzCpCosUserFlowFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserFlowFilter.setStatus("current")
_HzCpCosUserFlowMappingTable_Object = MibTable
hzCpCosUserFlowMappingTable = _HzCpCosUserFlowMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16)
)
if mibBuilder.loadTexts:
    hzCpCosUserFlowMappingTable.setStatus("current")
_HzCpCosUserFlowMappingEntry_Object = MibTableRow
hzCpCosUserFlowMappingEntry = _HzCpCosUserFlowMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1)
)
hzCpCosUserFlowMappingEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpCosUserFlowMappingIndex"),
)
if mibBuilder.loadTexts:
    hzCpCosUserFlowMappingEntry.setStatus("current")


class _HzCpCosUserFlowMappingIndex_Type(Integer32):
    """Custom type hzCpCosUserFlowMappingIndex based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("flow1", 1),
          ("flow2", 2),
          ("flow3", 3),
          ("flow4", 4),
          ("flow5", 5),
          ("flow6", 6),
          ("flow7", 7),
          ("flow8", 8),
          ("flow9", 9),
          ("flow10", 10),
          ("flow11", 11),
          ("flow12", 12),
          ("flow13", 13))
    )


_HzCpCosUserFlowMappingIndex_Type.__name__ = "Integer32"
_HzCpCosUserFlowMappingIndex_Object = MibTableColumn
hzCpCosUserFlowMappingIndex = _HzCpCosUserFlowMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1, 1),
    _HzCpCosUserFlowMappingIndex_Type()
)
hzCpCosUserFlowMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpCosUserFlowMappingIndex.setStatus("current")


class _HzCpCosUserFlowEnable_Type(Integer32):
    """Custom type hzCpCosUserFlowEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HzCpCosUserFlowEnable_Type.__name__ = "Integer32"
_HzCpCosUserFlowEnable_Object = MibTableColumn
hzCpCosUserFlowEnable = _HzCpCosUserFlowEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1, 2),
    _HzCpCosUserFlowEnable_Type()
)
hzCpCosUserFlowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserFlowEnable.setStatus("current")


class _HzCpCosUserFlowP1Queue_Type(Integer32):
    """Custom type hzCpCosUserFlowP1Queue based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_HzCpCosUserFlowP1Queue_Type.__name__ = "Integer32"
_HzCpCosUserFlowP1Queue_Object = MibTableColumn
hzCpCosUserFlowP1Queue = _HzCpCosUserFlowP1Queue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1, 3),
    _HzCpCosUserFlowP1Queue_Type()
)
hzCpCosUserFlowP1Queue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserFlowP1Queue.setStatus("current")


class _HzCpCosUserFlowP1TargetPort_Type(Integer32):
    """Custom type hzCpCosUserFlowP1TargetPort based on Integer32"""
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
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4))
    )


_HzCpCosUserFlowP1TargetPort_Type.__name__ = "Integer32"
_HzCpCosUserFlowP1TargetPort_Object = MibTableColumn
hzCpCosUserFlowP1TargetPort = _HzCpCosUserFlowP1TargetPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1, 4),
    _HzCpCosUserFlowP1TargetPort_Type()
)
hzCpCosUserFlowP1TargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserFlowP1TargetPort.setStatus("current")


class _HzCpCosUserFlowP2Queue_Type(Integer32):
    """Custom type hzCpCosUserFlowP2Queue based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_HzCpCosUserFlowP2Queue_Type.__name__ = "Integer32"
_HzCpCosUserFlowP2Queue_Object = MibTableColumn
hzCpCosUserFlowP2Queue = _HzCpCosUserFlowP2Queue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1, 5),
    _HzCpCosUserFlowP2Queue_Type()
)
hzCpCosUserFlowP2Queue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserFlowP2Queue.setStatus("current")


class _HzCpCosUserFlowP2TargetPort_Type(Integer32):
    """Custom type hzCpCosUserFlowP2TargetPort based on Integer32"""
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
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4))
    )


_HzCpCosUserFlowP2TargetPort_Type.__name__ = "Integer32"
_HzCpCosUserFlowP2TargetPort_Object = MibTableColumn
hzCpCosUserFlowP2TargetPort = _HzCpCosUserFlowP2TargetPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1, 6),
    _HzCpCosUserFlowP2TargetPort_Type()
)
hzCpCosUserFlowP2TargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserFlowP2TargetPort.setStatus("current")


class _HzCpCosUserFlowP3Queue_Type(Integer32):
    """Custom type hzCpCosUserFlowP3Queue based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_HzCpCosUserFlowP3Queue_Type.__name__ = "Integer32"
_HzCpCosUserFlowP3Queue_Object = MibTableColumn
hzCpCosUserFlowP3Queue = _HzCpCosUserFlowP3Queue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1, 7),
    _HzCpCosUserFlowP3Queue_Type()
)
hzCpCosUserFlowP3Queue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserFlowP3Queue.setStatus("current")


class _HzCpCosUserFlowP3TargetPort_Type(Integer32):
    """Custom type hzCpCosUserFlowP3TargetPort based on Integer32"""
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
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4))
    )


_HzCpCosUserFlowP3TargetPort_Type.__name__ = "Integer32"
_HzCpCosUserFlowP3TargetPort_Object = MibTableColumn
hzCpCosUserFlowP3TargetPort = _HzCpCosUserFlowP3TargetPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1, 8),
    _HzCpCosUserFlowP3TargetPort_Type()
)
hzCpCosUserFlowP3TargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserFlowP3TargetPort.setStatus("current")


class _HzCpCosUserFlowP4Queue_Type(Integer32):
    """Custom type hzCpCosUserFlowP4Queue based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_HzCpCosUserFlowP4Queue_Type.__name__ = "Integer32"
_HzCpCosUserFlowP4Queue_Object = MibTableColumn
hzCpCosUserFlowP4Queue = _HzCpCosUserFlowP4Queue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1, 9),
    _HzCpCosUserFlowP4Queue_Type()
)
hzCpCosUserFlowP4Queue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserFlowP4Queue.setStatus("current")


class _HzCpCosUserFlowP4TargetPort_Type(Integer32):
    """Custom type hzCpCosUserFlowP4TargetPort based on Integer32"""
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
        *(("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4))
    )


_HzCpCosUserFlowP4TargetPort_Type.__name__ = "Integer32"
_HzCpCosUserFlowP4TargetPort_Object = MibTableColumn
hzCpCosUserFlowP4TargetPort = _HzCpCosUserFlowP4TargetPort_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 6, 16, 1, 10),
    _HzCpCosUserFlowP4TargetPort_Type()
)
hzCpCosUserFlowP4TargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpCosUserFlowP4TargetPort.setStatus("current")
_HzCpRapidLinkShutdown_ObjectIdentity = ObjectIdentity
hzCpRapidLinkShutdown = _HzCpRapidLinkShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7)
)


class _HzCpRlsMode_Type(Integer32):
    """Custom type hzCpRlsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("basic", 2),
          ("advanced", 3))
    )


_HzCpRlsMode_Type.__name__ = "Integer32"
_HzCpRlsMode_Object = MibScalar
hzCpRlsMode = _HzCpRlsMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 1),
    _HzCpRlsMode_Type()
)
hzCpRlsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsMode.setStatus("current")


class _HzCpRlsLinkControl_Type(Integer32):
    """Custom type hzCpRlsLinkControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_HzCpRlsLinkControl_Type.__name__ = "Integer32"
_HzCpRlsLinkControl_Object = MibScalar
hzCpRlsLinkControl = _HzCpRlsLinkControl_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 2),
    _HzCpRlsLinkControl_Type()
)
hzCpRlsLinkControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsLinkControl.setStatus("current")


class _HzCpApplyRlsMonitorParametersToSystem_Type(Integer32):
    """Custom type hzCpApplyRlsMonitorParametersToSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("apply", 1)
    )


_HzCpApplyRlsMonitorParametersToSystem_Type.__name__ = "Integer32"
_HzCpApplyRlsMonitorParametersToSystem_Object = MibScalar
hzCpApplyRlsMonitorParametersToSystem = _HzCpApplyRlsMonitorParametersToSystem_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 3),
    _HzCpApplyRlsMonitorParametersToSystem_Type()
)
hzCpApplyRlsMonitorParametersToSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpApplyRlsMonitorParametersToSystem.setStatus("current")


class _HzCpRlsLinkEnable_Type(Integer32):
    """Custom type hzCpRlsLinkEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpRlsLinkEnable_Type.__name__ = "Integer32"
_HzCpRlsLinkEnable_Object = MibScalar
hzCpRlsLinkEnable = _HzCpRlsLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 4),
    _HzCpRlsLinkEnable_Type()
)
hzCpRlsLinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsLinkEnable.setStatus("current")
_HzCpRlsPortGroup_Type = DisplayString
_HzCpRlsPortGroup_Object = MibScalar
hzCpRlsPortGroup = _HzCpRlsPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 5),
    _HzCpRlsPortGroup_Type()
)
hzCpRlsPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsPortGroup.setStatus("current")


class _HzCpRlsShutdownPolicy_Type(Integer32):
    """Custom type hzCpRlsShutdownPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-down", 1),
          ("eoam-msg", 2))
    )


_HzCpRlsShutdownPolicy_Type.__name__ = "Integer32"
_HzCpRlsShutdownPolicy_Object = MibScalar
hzCpRlsShutdownPolicy = _HzCpRlsShutdownPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 6),
    _HzCpRlsShutdownPolicy_Type()
)
hzCpRlsShutdownPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsShutdownPolicy.setStatus("current")
_HzCpRlsSoftFaultMonitorTable_Object = MibTable
hzCpRlsSoftFaultMonitorTable = _HzCpRlsSoftFaultMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 7)
)
if mibBuilder.loadTexts:
    hzCpRlsSoftFaultMonitorTable.setStatus("current")
_HzCpRlsSoftFaultMonitorEntry_Object = MibTableRow
hzCpRlsSoftFaultMonitorEntry = _HzCpRlsSoftFaultMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 7, 1)
)
hzCpRlsSoftFaultMonitorEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpRlsSoftFaultMonitorIndex"),
)
if mibBuilder.loadTexts:
    hzCpRlsSoftFaultMonitorEntry.setStatus("current")


class _HzCpRlsSoftFaultMonitorIndex_Type(Integer32):
    """Custom type hzCpRlsSoftFaultMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wireless-port-1", 1)
    )


_HzCpRlsSoftFaultMonitorIndex_Type.__name__ = "Integer32"
_HzCpRlsSoftFaultMonitorIndex_Object = MibTableColumn
hzCpRlsSoftFaultMonitorIndex = _HzCpRlsSoftFaultMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 7, 1, 1),
    _HzCpRlsSoftFaultMonitorIndex_Type()
)
hzCpRlsSoftFaultMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsSoftFaultMonitorIndex.setStatus("current")
_HzCpRlsEstablishErredFrameThreshold_Type = Integer32
_HzCpRlsEstablishErredFrameThreshold_Object = MibTableColumn
hzCpRlsEstablishErredFrameThreshold = _HzCpRlsEstablishErredFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 7, 1, 2),
    _HzCpRlsEstablishErredFrameThreshold_Type()
)
hzCpRlsEstablishErredFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsEstablishErredFrameThreshold.setStatus("current")
_HzCpRlsShutdownErredFrameThreshold_Type = Integer32
_HzCpRlsShutdownErredFrameThreshold_Object = MibTableColumn
hzCpRlsShutdownErredFrameThreshold = _HzCpRlsShutdownErredFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 7, 1, 3),
    _HzCpRlsShutdownErredFrameThreshold_Type()
)
hzCpRlsShutdownErredFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsShutdownErredFrameThreshold.setStatus("current")
_HzCpRlsEstablishNumberOfSamples_Type = Integer32
_HzCpRlsEstablishNumberOfSamples_Object = MibTableColumn
hzCpRlsEstablishNumberOfSamples = _HzCpRlsEstablishNumberOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 7, 1, 4),
    _HzCpRlsEstablishNumberOfSamples_Type()
)
hzCpRlsEstablishNumberOfSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsEstablishNumberOfSamples.setStatus("current")
_HzCpRlsShutdownNumberOfSamples_Type = Integer32
_HzCpRlsShutdownNumberOfSamples_Object = MibTableColumn
hzCpRlsShutdownNumberOfSamples = _HzCpRlsShutdownNumberOfSamples_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 7, 1, 5),
    _HzCpRlsShutdownNumberOfSamples_Type()
)
hzCpRlsShutdownNumberOfSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsShutdownNumberOfSamples.setStatus("current")
_HzCpRlsEstablishSamplePeriod_Type = Integer32
_HzCpRlsEstablishSamplePeriod_Object = MibTableColumn
hzCpRlsEstablishSamplePeriod = _HzCpRlsEstablishSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 7, 1, 6),
    _HzCpRlsEstablishSamplePeriod_Type()
)
hzCpRlsEstablishSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsEstablishSamplePeriod.setStatus("current")
_HzCpRlsShutdownSamplePeriod_Type = Integer32
_HzCpRlsShutdownSamplePeriod_Object = MibTableColumn
hzCpRlsShutdownSamplePeriod = _HzCpRlsShutdownSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 7, 1, 7),
    _HzCpRlsShutdownSamplePeriod_Type()
)
hzCpRlsShutdownSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsShutdownSamplePeriod.setStatus("current")
_HzCpRlsQuickShutdownSamplePeriod_Type = Integer32
_HzCpRlsQuickShutdownSamplePeriod_Object = MibTableColumn
hzCpRlsQuickShutdownSamplePeriod = _HzCpRlsQuickShutdownSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 7, 1, 8),
    _HzCpRlsQuickShutdownSamplePeriod_Type()
)
hzCpRlsQuickShutdownSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsQuickShutdownSamplePeriod.setStatus("current")
_HzCpRlsHardFaultMonitorTable_Object = MibTable
hzCpRlsHardFaultMonitorTable = _HzCpRlsHardFaultMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 8)
)
if mibBuilder.loadTexts:
    hzCpRlsHardFaultMonitorTable.setStatus("current")
_HzCpRlsHardFaultMonitorEntry_Object = MibTableRow
hzCpRlsHardFaultMonitorEntry = _HzCpRlsHardFaultMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 8, 1)
)
hzCpRlsHardFaultMonitorEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpRlsHardFaultMonitorIndex"),
)
if mibBuilder.loadTexts:
    hzCpRlsHardFaultMonitorEntry.setStatus("current")


class _HzCpRlsHardFaultMonitorIndex_Type(Integer32):
    """Custom type hzCpRlsHardFaultMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wireless-port-1", 1)
    )


_HzCpRlsHardFaultMonitorIndex_Type.__name__ = "Integer32"
_HzCpRlsHardFaultMonitorIndex_Object = MibTableColumn
hzCpRlsHardFaultMonitorIndex = _HzCpRlsHardFaultMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 8, 1, 1),
    _HzCpRlsHardFaultMonitorIndex_Type()
)
hzCpRlsHardFaultMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsHardFaultMonitorIndex.setStatus("current")
_HzCpRlsHardFaultSamplePeriod_Type = Integer32
_HzCpRlsHardFaultSamplePeriod_Object = MibTableColumn
hzCpRlsHardFaultSamplePeriod = _HzCpRlsHardFaultSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 8, 1, 2),
    _HzCpRlsHardFaultSamplePeriod_Type()
)
hzCpRlsHardFaultSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsHardFaultSamplePeriod.setStatus("current")
_HzCpRlsHardFaultThreshold_Type = Integer32
_HzCpRlsHardFaultThreshold_Object = MibTableColumn
hzCpRlsHardFaultThreshold = _HzCpRlsHardFaultThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 8, 1, 3),
    _HzCpRlsHardFaultThreshold_Type()
)
hzCpRlsHardFaultThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsHardFaultThreshold.setStatus("current")
_HzCpRlsReceiveSignalLevelMonitorTable_Object = MibTable
hzCpRlsReceiveSignalLevelMonitorTable = _HzCpRlsReceiveSignalLevelMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 9)
)
if mibBuilder.loadTexts:
    hzCpRlsReceiveSignalLevelMonitorTable.setStatus("current")
_HzCpRlsReceiveSignalLevelMonitorEntry_Object = MibTableRow
hzCpRlsReceiveSignalLevelMonitorEntry = _HzCpRlsReceiveSignalLevelMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 9, 1)
)
hzCpRlsReceiveSignalLevelMonitorEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpRlsReceiveSignalLevelMonitorIndex"),
)
if mibBuilder.loadTexts:
    hzCpRlsReceiveSignalLevelMonitorEntry.setStatus("current")


class _HzCpRlsReceiveSignalLevelMonitorIndex_Type(Integer32):
    """Custom type hzCpRlsReceiveSignalLevelMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wireless-port-1", 1)
    )


_HzCpRlsReceiveSignalLevelMonitorIndex_Type.__name__ = "Integer32"
_HzCpRlsReceiveSignalLevelMonitorIndex_Object = MibTableColumn
hzCpRlsReceiveSignalLevelMonitorIndex = _HzCpRlsReceiveSignalLevelMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 9, 1, 1),
    _HzCpRlsReceiveSignalLevelMonitorIndex_Type()
)
hzCpRlsReceiveSignalLevelMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsReceiveSignalLevelMonitorIndex.setStatus("current")
_HzCpRlsMakeRslMonitorRslValue_Type = DisplayString
_HzCpRlsMakeRslMonitorRslValue_Object = MibTableColumn
hzCpRlsMakeRslMonitorRslValue = _HzCpRlsMakeRslMonitorRslValue_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 9, 1, 2),
    _HzCpRlsMakeRslMonitorRslValue_Type()
)
hzCpRlsMakeRslMonitorRslValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsMakeRslMonitorRslValue.setStatus("current")
_HzCpRlsMakeRslMonitorPeriod_Type = Integer32
_HzCpRlsMakeRslMonitorPeriod_Object = MibTableColumn
hzCpRlsMakeRslMonitorPeriod = _HzCpRlsMakeRslMonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 9, 1, 3),
    _HzCpRlsMakeRslMonitorPeriod_Type()
)
hzCpRlsMakeRslMonitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpRlsMakeRslMonitorPeriod.setStatus("current")
_HzCpRlsStatusTable_Object = MibTable
hzCpRlsStatusTable = _HzCpRlsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    hzCpRlsStatusTable.setStatus("current")
_HzCpRlsStatusEntry_Object = MibTableRow
hzCpRlsStatusEntry = _HzCpRlsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1)
)
hzCpRlsStatusEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpRlsStatusIndex"),
)
if mibBuilder.loadTexts:
    hzCpRlsStatusEntry.setStatus("current")


class _HzCpRlsStatusIndex_Type(Integer32):
    """Custom type hzCpRlsStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wireless-port-1", 1)
    )


_HzCpRlsStatusIndex_Type.__name__ = "Integer32"
_HzCpRlsStatusIndex_Object = MibTableColumn
hzCpRlsStatusIndex = _HzCpRlsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 1),
    _HzCpRlsStatusIndex_Type()
)
hzCpRlsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsStatusIndex.setStatus("current")
_HzCpRlsOption_Type = DisplayString
_HzCpRlsOption_Object = MibTableColumn
hzCpRlsOption = _HzCpRlsOption_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 2),
    _HzCpRlsOption_Type()
)
hzCpRlsOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsOption.setStatus("current")
_HzCpRlsState_Type = DisplayString
_HzCpRlsState_Object = MibTableColumn
hzCpRlsState = _HzCpRlsState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 3),
    _HzCpRlsState_Type()
)
hzCpRlsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsState.setStatus("current")
_HzCpRlsMismatchState_Type = DisplayString
_HzCpRlsMismatchState_Object = MibTableColumn
hzCpRlsMismatchState = _HzCpRlsMismatchState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 4),
    _HzCpRlsMismatchState_Type()
)
hzCpRlsMismatchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsMismatchState.setStatus("current")
_HzCpRlsDegradeMonitorState_Type = DisplayString
_HzCpRlsDegradeMonitorState_Object = MibTableColumn
hzCpRlsDegradeMonitorState = _HzCpRlsDegradeMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 5),
    _HzCpRlsDegradeMonitorState_Type()
)
hzCpRlsDegradeMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsDegradeMonitorState.setStatus("current")
_HzCpRlsHardFaultMonitorState_Type = DisplayString
_HzCpRlsHardFaultMonitorState_Object = MibTableColumn
hzCpRlsHardFaultMonitorState = _HzCpRlsHardFaultMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 6),
    _HzCpRlsHardFaultMonitorState_Type()
)
hzCpRlsHardFaultMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsHardFaultMonitorState.setStatus("current")
_HzCpRlsMakeRslThresholdState_Type = DisplayString
_HzCpRlsMakeRslThresholdState_Object = MibTableColumn
hzCpRlsMakeRslThresholdState = _HzCpRlsMakeRslThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 7),
    _HzCpRlsMakeRslThresholdState_Type()
)
hzCpRlsMakeRslThresholdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsMakeRslThresholdState.setStatus("current")
_HzCpRlsPeerRslState_Type = DisplayString
_HzCpRlsPeerRslState_Object = MibTableColumn
hzCpRlsPeerRslState = _HzCpRlsPeerRslState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 8),
    _HzCpRlsPeerRslState_Type()
)
hzCpRlsPeerRslState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsPeerRslState.setStatus("current")
_HzCpRlsRadioInterfaceState_Type = DisplayString
_HzCpRlsRadioInterfaceState_Object = MibTableColumn
hzCpRlsRadioInterfaceState = _HzCpRlsRadioInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 9),
    _HzCpRlsRadioInterfaceState_Type()
)
hzCpRlsRadioInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsRadioInterfaceState.setStatus("current")
_HzCpRlsNetworkInterfaceState_Type = DisplayString
_HzCpRlsNetworkInterfaceState_Object = MibTableColumn
hzCpRlsNetworkInterfaceState = _HzCpRlsNetworkInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 10),
    _HzCpRlsNetworkInterfaceState_Type()
)
hzCpRlsNetworkInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsNetworkInterfaceState.setStatus("current")
_HzCpRlsUserConfiguredEstablishFer_Type = DisplayString
_HzCpRlsUserConfiguredEstablishFer_Object = MibTableColumn
hzCpRlsUserConfiguredEstablishFer = _HzCpRlsUserConfiguredEstablishFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 11),
    _HzCpRlsUserConfiguredEstablishFer_Type()
)
hzCpRlsUserConfiguredEstablishFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsUserConfiguredEstablishFer.setStatus("current")
_HzCpRlsMinimumAchievableEstablishFer_Type = DisplayString
_HzCpRlsMinimumAchievableEstablishFer_Object = MibTableColumn
hzCpRlsMinimumAchievableEstablishFer = _HzCpRlsMinimumAchievableEstablishFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 12),
    _HzCpRlsMinimumAchievableEstablishFer_Type()
)
hzCpRlsMinimumAchievableEstablishFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsMinimumAchievableEstablishFer.setStatus("current")
_HzCpRlsUserConfiguredShutdownFer_Type = DisplayString
_HzCpRlsUserConfiguredShutdownFer_Object = MibTableColumn
hzCpRlsUserConfiguredShutdownFer = _HzCpRlsUserConfiguredShutdownFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 13),
    _HzCpRlsUserConfiguredShutdownFer_Type()
)
hzCpRlsUserConfiguredShutdownFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsUserConfiguredShutdownFer.setStatus("current")
_HzCpRlsMinimumAchievableShutdownFer_Type = DisplayString
_HzCpRlsMinimumAchievableShutdownFer_Object = MibTableColumn
hzCpRlsMinimumAchievableShutdownFer = _HzCpRlsMinimumAchievableShutdownFer_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 14),
    _HzCpRlsMinimumAchievableShutdownFer_Type()
)
hzCpRlsMinimumAchievableShutdownFer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsMinimumAchievableShutdownFer.setStatus("current")
_HzCpRlsUserConfiguredEstablishMonitorTime_Type = Integer32
_HzCpRlsUserConfiguredEstablishMonitorTime_Object = MibTableColumn
hzCpRlsUserConfiguredEstablishMonitorTime = _HzCpRlsUserConfiguredEstablishMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 15),
    _HzCpRlsUserConfiguredEstablishMonitorTime_Type()
)
hzCpRlsUserConfiguredEstablishMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsUserConfiguredEstablishMonitorTime.setStatus("current")
_HzCpRlsActualEstablishMonitorTime_Type = Integer32
_HzCpRlsActualEstablishMonitorTime_Object = MibTableColumn
hzCpRlsActualEstablishMonitorTime = _HzCpRlsActualEstablishMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 16),
    _HzCpRlsActualEstablishMonitorTime_Type()
)
hzCpRlsActualEstablishMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsActualEstablishMonitorTime.setStatus("current")
_HzCpRlsUserConfiguredShutdownMonitorTime_Type = Integer32
_HzCpRlsUserConfiguredShutdownMonitorTime_Object = MibTableColumn
hzCpRlsUserConfiguredShutdownMonitorTime = _HzCpRlsUserConfiguredShutdownMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 17),
    _HzCpRlsUserConfiguredShutdownMonitorTime_Type()
)
hzCpRlsUserConfiguredShutdownMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsUserConfiguredShutdownMonitorTime.setStatus("current")
_HzCpRlsActualShutdownMonitorTime_Type = Integer32
_HzCpRlsActualShutdownMonitorTime_Object = MibTableColumn
hzCpRlsActualShutdownMonitorTime = _HzCpRlsActualShutdownMonitorTime_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 7, 10, 1, 18),
    _HzCpRlsActualShutdownMonitorTime_Type()
)
hzCpRlsActualShutdownMonitorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpRlsActualShutdownMonitorTime.setStatus("current")
_HzCpLogs_ObjectIdentity = ObjectIdentity
hzCpLogs = _HzCpLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 8)
)


class _HzCpEventLogEnable_Type(Integer32):
    """Custom type hzCpEventLogEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpEventLogEnable_Type.__name__ = "Integer32"
_HzCpEventLogEnable_Object = MibScalar
hzCpEventLogEnable = _HzCpEventLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 8, 1),
    _HzCpEventLogEnable_Type()
)
hzCpEventLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpEventLogEnable.setStatus("current")


class _HzCpPerfmLogEnable_Type(Integer32):
    """Custom type hzCpPerfmLogEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpPerfmLogEnable_Type.__name__ = "Integer32"
_HzCpPerfmLogEnable_Object = MibScalar
hzCpPerfmLogEnable = _HzCpPerfmLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 8, 2),
    _HzCpPerfmLogEnable_Type()
)
hzCpPerfmLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPerfmLogEnable.setStatus("current")


class _HzCpPerfmLogInterval_Type(DisplayString):
    """Custom type hzCpPerfmLogInterval based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HzCpPerfmLogInterval_Type.__name__ = "DisplayString"
_HzCpPerfmLogInterval_Object = MibScalar
hzCpPerfmLogInterval = _HzCpPerfmLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 8, 3),
    _HzCpPerfmLogInterval_Type()
)
hzCpPerfmLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpPerfmLogInterval.setStatus("current")
_HzCpSysLog_ObjectIdentity = ObjectIdentity
hzCpSysLog = _HzCpSysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 8, 4)
)


class _HzCpSysLogEnable_Type(Integer32):
    """Custom type hzCpSysLogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpSysLogEnable_Type.__name__ = "Integer32"
_HzCpSysLogEnable_Object = MibScalar
hzCpSysLogEnable = _HzCpSysLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 8, 4, 1),
    _HzCpSysLogEnable_Type()
)
hzCpSysLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSysLogEnable.setStatus("current")
_HzCpSysLogIpAddressDep_Type = IpAddress
_HzCpSysLogIpAddressDep_Object = MibScalar
hzCpSysLogIpAddressDep = _HzCpSysLogIpAddressDep_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 8, 4, 2),
    _HzCpSysLogIpAddressDep_Type()
)
hzCpSysLogIpAddressDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpSysLogIpAddressDep.setStatus("deprecated")
_HzCpSysLogHostDomain_Type = InetAddressType
_HzCpSysLogHostDomain_Object = MibScalar
hzCpSysLogHostDomain = _HzCpSysLogHostDomain_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 8, 4, 3),
    _HzCpSysLogHostDomain_Type()
)
hzCpSysLogHostDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSysLogHostDomain.setStatus("current")
_HzCpSysLogHostAddress_Type = InetAddress
_HzCpSysLogHostAddress_Object = MibScalar
hzCpSysLogHostAddress = _HzCpSysLogHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 8, 4, 4),
    _HzCpSysLogHostAddress_Type()
)
hzCpSysLogHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpSysLogHostAddress.setStatus("current")
_HzCpAtpc_ObjectIdentity = ObjectIdentity
hzCpAtpc = _HzCpAtpc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 9)
)


class _HzCpAtpcEnable_Type(Integer32):
    """Custom type hzCpAtpcEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpAtpcEnable_Type.__name__ = "Integer32"
_HzCpAtpcEnable_Object = MibScalar
hzCpAtpcEnable = _HzCpAtpcEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 9, 1),
    _HzCpAtpcEnable_Type()
)
hzCpAtpcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpAtpcEnable.setStatus("current")


class _HzCpAtpcStatus_Type(Integer32):
    """Custom type hzCpAtpcStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("disabledAuto", 2),
          ("running", 3),
          ("runningToggling", 4),
          ("suspended", 5),
          ("suspendedLostComm", 6),
          ("suspendedRadioDown", 7),
          ("suspendedRadioMuted", 8),
          ("suspendedRadioLoopback", 9))
    )


_HzCpAtpcStatus_Type.__name__ = "Integer32"
_HzCpAtpcStatus_Object = MibScalar
hzCpAtpcStatus = _HzCpAtpcStatus_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 9, 2),
    _HzCpAtpcStatus_Type()
)
hzCpAtpcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpAtpcStatus.setStatus("current")


class _HzCpAtpcCoordinatedPowerDbm_Type(Integer32):
    """Custom type hzCpAtpcCoordinatedPowerDbm based on Integer32"""
    defaultValue = 0


_HzCpAtpcCoordinatedPowerDbm_Type.__name__ = "Integer32"
_HzCpAtpcCoordinatedPowerDbm_Object = MibScalar
hzCpAtpcCoordinatedPowerDbm = _HzCpAtpcCoordinatedPowerDbm_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 9, 3),
    _HzCpAtpcCoordinatedPowerDbm_Type()
)
hzCpAtpcCoordinatedPowerDbm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpAtpcCoordinatedPowerDbm.setStatus("current")


class _HzCpAtpcCoordinatedPwrEnable_Type(Integer32):
    """Custom type hzCpAtpcCoordinatedPwrEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_HzCpAtpcCoordinatedPwrEnable_Type.__name__ = "Integer32"
_HzCpAtpcCoordinatedPwrEnable_Object = MibScalar
hzCpAtpcCoordinatedPwrEnable = _HzCpAtpcCoordinatedPwrEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 9, 4),
    _HzCpAtpcCoordinatedPwrEnable_Type()
)
hzCpAtpcCoordinatedPwrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpAtpcCoordinatedPwrEnable.setStatus("current")
_HzCpAtpcMinTxPower_Type = Integer32
_HzCpAtpcMinTxPower_Object = MibScalar
hzCpAtpcMinTxPower = _HzCpAtpcMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 9, 5),
    _HzCpAtpcMinTxPower_Type()
)
hzCpAtpcMinTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpAtpcMinTxPower.setStatus("current")
_HzCpAtpcMaxTxPower_Type = Integer32
_HzCpAtpcMaxTxPower_Object = MibScalar
hzCpAtpcMaxTxPower = _HzCpAtpcMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 9, 6),
    _HzCpAtpcMaxTxPower_Type()
)
hzCpAtpcMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpAtpcMaxTxPower.setStatus("current")
_HzCpHitlessAam_ObjectIdentity = ObjectIdentity
hzCpHitlessAam = _HzCpHitlessAam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10)
)


class _HzCpHitlessAamEnable_Type(Integer32):
    """Custom type hzCpHitlessAamEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpHitlessAamEnable_Type.__name__ = "Integer32"
_HzCpHitlessAamEnable_Object = MibScalar
hzCpHitlessAamEnable = _HzCpHitlessAamEnable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 1),
    _HzCpHitlessAamEnable_Type()
)
hzCpHitlessAamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHitlessAamEnable.setStatus("current")


class _HzCpHitlessAamManualMode_Type(Integer32):
    """Custom type hzCpHitlessAamManualMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpHitlessAamManualMode_Type.__name__ = "Integer32"
_HzCpHitlessAamManualMode_Object = MibScalar
hzCpHitlessAamManualMode = _HzCpHitlessAamManualMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 2),
    _HzCpHitlessAamManualMode_Type()
)
hzCpHitlessAamManualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHitlessAamManualMode.setStatus("current")
_HzCpHitlessAamWaitToRestore_Type = Integer32
_HzCpHitlessAamWaitToRestore_Object = MibScalar
hzCpHitlessAamWaitToRestore = _HzCpHitlessAamWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 3),
    _HzCpHitlessAamWaitToRestore_Type()
)
hzCpHitlessAamWaitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHitlessAamWaitToRestore.setStatus("current")


class _HzCpHitlessAamOrgSpecEoamMsg_Type(Integer32):
    """Custom type hzCpHitlessAamOrgSpecEoamMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_HzCpHitlessAamOrgSpecEoamMsg_Type.__name__ = "Integer32"
_HzCpHitlessAamOrgSpecEoamMsg_Object = MibScalar
hzCpHitlessAamOrgSpecEoamMsg = _HzCpHitlessAamOrgSpecEoamMsg_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 4),
    _HzCpHitlessAamOrgSpecEoamMsg_Type()
)
hzCpHitlessAamOrgSpecEoamMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHitlessAamOrgSpecEoamMsg.setStatus("current")
_HzCpHitlessAamTable_Object = MibTable
hzCpHitlessAamTable = _HzCpHitlessAamTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 5)
)
if mibBuilder.loadTexts:
    hzCpHitlessAamTable.setStatus("current")
_HzCpHitlessAamEntry_Object = MibTableRow
hzCpHitlessAamEntry = _HzCpHitlessAamEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 5, 1)
)
hzCpHitlessAamEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpWirelessPortIndex"),
)
if mibBuilder.loadTexts:
    hzCpHitlessAamEntry.setStatus("current")


class _HzCpWirelessPortIndex_Type(Integer32):
    """Custom type hzCpWirelessPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wireless-port-1", 1)
    )


_HzCpWirelessPortIndex_Type.__name__ = "Integer32"
_HzCpWirelessPortIndex_Object = MibTableColumn
hzCpWirelessPortIndex = _HzCpWirelessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 5, 1, 1),
    _HzCpWirelessPortIndex_Type()
)
hzCpWirelessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpWirelessPortIndex.setStatus("current")


class _HzCpHitlessAamCurrentMode_Type(DisplayString):
    """Custom type hzCpHitlessAamCurrentMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HzCpHitlessAamCurrentMode_Type.__name__ = "DisplayString"
_HzCpHitlessAamCurrentMode_Object = MibTableColumn
hzCpHitlessAamCurrentMode = _HzCpHitlessAamCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 5, 1, 2),
    _HzCpHitlessAamCurrentMode_Type()
)
hzCpHitlessAamCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpHitlessAamCurrentMode.setStatus("current")
_HzCpHitlessAamModeTable_Object = MibTable
hzCpHitlessAamModeTable = _HzCpHitlessAamModeTable_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 6)
)
if mibBuilder.loadTexts:
    hzCpHitlessAamModeTable.setStatus("current")
_HzCpHitlessAamModeEntry_Object = MibTableRow
hzCpHitlessAamModeEntry = _HzCpHitlessAamModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 6, 1)
)
hzCpHitlessAamModeEntry.setIndexNames(
    (0, "DRAGONWAVE-HCP-MIB", "hzCpHitlessAamModeIndex"),
)
if mibBuilder.loadTexts:
    hzCpHitlessAamModeEntry.setStatus("current")
_HzCpHitlessAamModeIndex_Type = Integer32
_HzCpHitlessAamModeIndex_Object = MibTableColumn
hzCpHitlessAamModeIndex = _HzCpHitlessAamModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 6, 1, 1),
    _HzCpHitlessAamModeIndex_Type()
)
hzCpHitlessAamModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpHitlessAamModeIndex.setStatus("current")
_HzCpHitlessAammModeName_Type = DisplayString
_HzCpHitlessAammModeName_Object = MibTableColumn
hzCpHitlessAammModeName = _HzCpHitlessAammModeName_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 6, 1, 2),
    _HzCpHitlessAammModeName_Type()
)
hzCpHitlessAammModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hzCpHitlessAammModeName.setStatus("current")


class _HzCpHitlessAamModeRange_Type(Integer32):
    """Custom type hzCpHitlessAamModeRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAllowed", 1),
          ("allowed", 2),
          ("max", 3))
    )


_HzCpHitlessAamModeRange_Type.__name__ = "Integer32"
_HzCpHitlessAamModeRange_Object = MibTableColumn
hzCpHitlessAamModeRange = _HzCpHitlessAamModeRange_Object(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 10, 6, 1, 3),
    _HzCpHitlessAamModeRange_Type()
)
hzCpHitlessAamModeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hzCpHitlessAamModeRange.setStatus("current")
_HzCpSnmpNotifications_ObjectIdentity = ObjectIdentity
hzCpSnmpNotifications = _HzCpSnmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11)
)

# Managed Objects groups


# Notification objects

hzCpLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 1)
)
hzCpLinkDown.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("IF-MIB", "ifIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpLinkDown.setStatus(
        "current"
    )

hzCpLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 2)
)
hzCpLinkUp.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("IF-MIB", "ifIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpLinkUp.setStatus(
        "current"
    )

hzCpPeerAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 3)
)
hzCpPeerAuthenticationFailure.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpPeerAuthenticationFailure.setStatus(
        "current"
    )

hzCpPeerAuthenticationFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 4)
)
hzCpPeerAuthenticationFailureCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpPeerAuthenticationFailureCleared.setStatus(
        "current"
    )

hzCpHitlessAamConfigMisMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 5)
)
hzCpHitlessAamConfigMisMatch.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpHitlessAamConfigMisMatch.setStatus(
        "current"
    )

hzCpHitlessAamConfigMisMatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 6)
)
hzCpHitlessAamConfigMisMatchCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpHitlessAamConfigMisMatchCleared.setStatus(
        "current"
    )

hzCpHitlessAamModulationLowered = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 7)
)
hzCpHitlessAamModulationLowered.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpHitlessAamModulationLowered.setStatus(
        "current"
    )

hzCpHitlessAamModulationLoweredCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 8)
)
hzCpHitlessAamModulationLoweredCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpHitlessAamModulationLoweredCleared.setStatus(
        "current"
    )

hzCpHitlessAamModulationChangedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 9)
)
hzCpHitlessAamModulationChangedEvent.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpHitlessAamModulationChangedEvent.setStatus(
        "current"
    )

hzCpAtpcConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 10)
)
hzCpAtpcConfigMismatch.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpAtpcConfigMismatch.setStatus(
        "current"
    )

hzCpAtpcConfigMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 11)
)
hzCpAtpcConfigMismatchCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpAtpcConfigMismatchCleared.setStatus(
        "current"
    )

hzCpAtpcAutoDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 12)
)
hzCpAtpcAutoDisabled.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpAtpcAutoDisabled.setStatus(
        "current"
    )

hzCpAtpcAutoDisabledCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 13)
)
hzCpAtpcAutoDisabledCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpAtpcAutoDisabledCleared.setStatus(
        "current"
    )

hzCpNoSntpServersReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 14)
)
hzCpNoSntpServersReachable.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpNoSntpServersReachable.setStatus(
        "current"
    )

hzCpNoSntpServersReachableCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 15)
)
hzCpNoSntpServersReachableCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpNoSntpServersReachableCleared.setStatus(
        "current"
    )

hzCpFrequencyFileInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 16)
)
hzCpFrequencyFileInvalid.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpFrequencyFileInvalid.setStatus(
        "current"
    )

hzCpAggregateDroppedFramesThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 17)
)
hzCpAggregateDroppedFramesThreshold.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpAggregateDroppedFramesThreshold.setStatus(
        "current"
    )

hzCpAggregateDroppedFramesThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 18)
)
hzCpAggregateDroppedFramesThresholdCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpAggregateDroppedFramesThresholdCleared.setStatus(
        "current"
    )

hzCpQueueDroppedFramesThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 19)
)
hzCpQueueDroppedFramesThreshold.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpQBasedThresholdIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpQueueDroppedFramesThreshold.setStatus(
        "current"
    )

hzCpQueueDroppedFramesThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 20)
)
hzCpQueueDroppedFramesThresholdCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpQBasedThresholdIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpQueueDroppedFramesThresholdCleared.setStatus(
        "current"
    )

hzCpBwUtilizationThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 21)
)
hzCpBwUtilizationThreshold.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpBwUtilizationThreshold.setStatus(
        "current"
    )

hzCpBwUtilizationThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 22)
)
hzCpBwUtilizationThresholdCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpBwUtilizationThresholdCleared.setStatus(
        "current"
    )

hzCpQueueDepthThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 23)
)
hzCpQueueDepthThreshold.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpQBasedThresholdIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpQueueDepthThreshold.setStatus(
        "current"
    )

hzCpQueueDepthThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 24)
)
hzCpQueueDepthThresholdCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpQBasedThresholdIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpQueueDepthThresholdCleared.setStatus(
        "current"
    )

hzCpRlsConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 25)
)
hzCpRlsConfigMismatch.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRlsConfigMismatch.setStatus(
        "current"
    )

hzCpRlsConfigMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 26)
)
hzCpRlsConfigMismatchCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRlsConfigMismatchCleared.setStatus(
        "current"
    )

hzCpRlsShutdownActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 27)
)
hzCpRlsShutdownActivated.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRlsShutdownActivated.setStatus(
        "current"
    )

hzCpRlsShutdownActivatedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 28)
)
hzCpRlsShutdownActivatedCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRlsShutdownActivatedCleared.setStatus(
        "current"
    )

hzCpRlsQueueBasedShutdownActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 29)
)
hzCpRlsQueueBasedShutdownActivated.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRlsQueueBasedShutdownActivated.setStatus(
        "current"
    )

hzCpRlsQueueBasedShutdownActivatedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 30)
)
hzCpRlsQueueBasedShutdownActivatedCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRlsQueueBasedShutdownActivatedCleared.setStatus(
        "current"
    )

hzCpModemRxLossOfSignalLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 31)
)
hzCpModemRxLossOfSignalLock.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpModemRxLossOfSignalLock.setStatus(
        "current"
    )

hzCpModemRxLossOfSignalLockCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 32)
)
hzCpModemRxLossOfSignalLockCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpModemRxLossOfSignalLockCleared.setStatus(
        "current"
    )

hzCpModemSnrBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 33)
)
hzCpModemSnrBelowThreshold.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpModemSnrBelowThreshold.setStatus(
        "current"
    )

hzCpModemSnrBelowThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 34)
)
hzCpModemSnrBelowThresholdCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpModemSnrBelowThresholdCleared.setStatus(
        "current"
    )

hzCpModemEqualizerStressThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 35)
)
hzCpModemEqualizerStressThreshold.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpModemEqualizerStressThreshold.setStatus(
        "current"
    )

hzCpModemEqualizerStressThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 36)
)
hzCpModemEqualizerStressThresholdCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpModemEqualizerStressThresholdCleared.setStatus(
        "current"
    )

hzCpRslBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 37)
)
hzCpRslBelowThreshold.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRslBelowThreshold.setStatus(
        "current"
    )

hzCpRslBelowThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 38)
)
hzCpRslBelowThresholdCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpModemIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRslBelowThresholdCleared.setStatus(
        "current"
    )

hzCpRadioSynthLostLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 39)
)
hzCpRadioSynthLostLock.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRadioSynthLostLock.setStatus(
        "current"
    )

hzCpRadioSynthLostLockCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 40)
)
hzCpRadioSynthLostLockCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRadioSynthLostLockCleared.setStatus(
        "current"
    )

hzCpRadioCalTableNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 41)
)
hzCpRadioCalTableNotAvailable.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRadioCalTableNotAvailable.setStatus(
        "current"
    )

hzCpRadioCalTableNotAvailableCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 42)
)
hzCpRadioCalTableNotAvailableCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRadioCalTableNotAvailableCleared.setStatus(
        "current"
    )

hzCpRadioDrainCurrentOutOfLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 43)
)
hzCpRadioDrainCurrentOutOfLimit.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRadioDrainCurrentOutOfLimit.setStatus(
        "current"
    )

hzCpRadioDrainCurrentOutOfLimitCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 44)
)
hzCpRadioDrainCurrentOutOfLimitCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRadioDrainCurrentOutOfLimitCleared.setStatus(
        "current"
    )

hzCpRadioPowerAmplifier = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 45)
)
hzCpRadioPowerAmplifier.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRadioPowerAmplifier.setStatus(
        "current"
    )

hzCpRadioPowerAmplifierCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 46)
)
hzCpRadioPowerAmplifierCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpRadioIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRadioPowerAmplifierCleared.setStatus(
        "current"
    )

hzCpTemperatureOutOfLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 47)
)
hzCpTemperatureOutOfLimit.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpTemperatureOutOfLimit.setStatus(
        "current"
    )

hzCpTemperatureOutOfLimitCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 48)
)
hzCpTemperatureOutOfLimitCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpTemperatureOutOfLimitCleared.setStatus(
        "current"
    )

hzCpRedundancyConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 49)
)
hzCpRedundancyConfigMismatch.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpAlarmInstanceIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyConfigMismatch.setStatus(
        "current"
    )

hzCpRedundancyConfigMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 50)
)
hzCpRedundancyConfigMismatchCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpAlarmInstanceIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyConfigMismatchCleared.setStatus(
        "current"
    )

hzCpRedundancyActiveOnSecondary = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 51)
)
hzCpRedundancyActiveOnSecondary.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyActiveOnSecondary.setStatus(
        "current"
    )

hzCpRedundancyActiveOnSecondaryCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 52)
)
hzCpRedundancyActiveOnSecondaryCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyActiveOnSecondaryCleared.setStatus(
        "current"
    )

hzCpRedundancyOperatingInForcedSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 53)
)
hzCpRedundancyOperatingInForcedSwitch.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyOperatingInForcedSwitch.setStatus(
        "current"
    )

hzCpRedundancyOperatingInForcedSwitchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 54)
)
hzCpRedundancyOperatingInForcedSwitchCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyOperatingInForcedSwitchCleared.setStatus(
        "current"
    )

hzCpRedundancyEnetCrossLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 55)
)
hzCpRedundancyEnetCrossLink.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyEnetCrossLink.setStatus(
        "current"
    )

hzCpRedundancyEnetCrossLinkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 56)
)
hzCpRedundancyEnetCrossLinkCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyEnetCrossLinkCleared.setStatus(
        "current"
    )

hzCpRedundancyActiveUsingPartnerWLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 57)
)
hzCpRedundancyActiveUsingPartnerWLink.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyActiveUsingPartnerWLink.setStatus(
        "current"
    )

hzCpRedundancyActiveUsingPartnerWLinkCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 58)
)
hzCpRedundancyActiveUsingPartnerWLinkCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyActiveUsingPartnerWLinkCleared.setStatus(
        "current"
    )

hzCpRedundancyStandbyWLinkInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 59)
)
hzCpRedundancyStandbyWLinkInUse.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyStandbyWLinkInUse.setStatus(
        "current"
    )

hzCpRedundancyStandbyWLinkInUseCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 60)
)
hzCpRedundancyStandbyWLinkInUseCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyStandbyWLinkInUseCleared.setStatus(
        "current"
    )

hzCpRedundancyStandbyOnPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 61)
)
hzCpRedundancyStandbyOnPrimary.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyStandbyOnPrimary.setStatus(
        "current"
    )

hzCpRedundancyStandbyOnPrimaryCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 62)
)
hzCpRedundancyStandbyOnPrimaryCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRedundancyStandbyOnPrimaryCleared.setStatus(
        "current"
    )

hzCpX2DeliveringHalfCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 63)
)
hzCpX2DeliveringHalfCapacity.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpX2DeliveringHalfCapacity.setStatus(
        "current"
    )

hzCpX2DeliveringHalfCapacityCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 64)
)
hzCpX2DeliveringHalfCapacityCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpX2DeliveringHalfCapacityCleared.setStatus(
        "current"
    )

hzCpBncCableSignalNotDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 65)
)
hzCpBncCableSignalNotDetected.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpBncCableSignalNotDetected.setStatus(
        "current"
    )

hzCpBncCableSignalNotDetectedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 66)
)
hzCpBncCableSignalNotDetectedCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpBncCableSignalNotDetectedCleared.setStatus(
        "current"
    )

hzCpEthernetSpeedReduced = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 67)
)
hzCpEthernetSpeedReduced.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("IF-MIB", "ifIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpEthernetSpeedReduced.setStatus(
        "current"
    )

hzCpEthernetSpeedReducedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 68)
)
hzCpEthernetSpeedReducedCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("IF-MIB", "ifIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpEthernetSpeedReducedCleared.setStatus(
        "current"
    )

hzCpSynceLostLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 69)
)
hzCpSynceLostLock.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpSynceLostLock.setStatus(
        "current"
    )

hzCpSynceLostLockCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 70)
)
hzCpSynceLostLockCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpSynceLostLockCleared.setStatus(
        "current"
    )

hzCpSynceSecondarySourceInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 71)
)
hzCpSynceSecondarySourceInUse.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpSynceSecondarySourceInUse.setStatus(
        "current"
    )

hzCpSynceSecondarySourceInUseCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 72)
)
hzCpSynceSecondarySourceInUseCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpSynceSecondarySourceInUseCleared.setStatus(
        "current"
    )

hzCpUserSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 73)
)
hzCpUserSession.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpUserSessionUserName"),
        ("DRAGONWAVE-HCP-MIB", "hzCpUserSessionUserConnectionType"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpUserSession.setStatus(
        "current"
    )

hzCpUserSessionCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 74)
)
hzCpUserSessionCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpUserSessionUserName"),
        ("DRAGONWAVE-HCP-MIB", "hzCpUserSessionUserConnectionType"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpUserSessionCleared.setStatus(
        "current"
    )

hzCpInvalidSystemConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 75)
)
hzCpInvalidSystemConfig.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpInvalidSystemConfig.setStatus(
        "current"
    )

hzCpInvalidSystemConfigCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 76)
)
hzCpInvalidSystemConfigCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpInvalidSystemConfigCleared.setStatus(
        "current"
    )

hzCpMibChangeNotSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 77)
)
hzCpMibChangeNotSaved.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpMibChangeNotSaved.setStatus(
        "current"
    )

hzCpMibChangeNotSavedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 78)
)
hzCpMibChangeNotSavedCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpMibChangeNotSavedCleared.setStatus(
        "current"
    )

hzCpTransmitterLossOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 79)
)
hzCpTransmitterLossOfSync.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpTransmitterLossOfSync.setStatus(
        "current"
    )

hzCpTransmitterLossOfSyncCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 80)
)
hzCpTransmitterLossOfSyncCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpTransmitterLossOfSyncCleared.setStatus(
        "current"
    )

hzCpRadioLinearityCalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 81)
)
hzCpRadioLinearityCalError.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRadioLinearityCalError.setStatus(
        "current"
    )

hzCpRadioLinearityCalErrorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 82)
)
hzCpRadioLinearityCalErrorCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpRadioLinearityCalErrorCleared.setStatus(
        "current"
    )

hzCpSynceConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 83)
)
hzCpSynceConfigMismatch.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpAlarmInstanceIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpSynceConfigMismatch.setStatus(
        "current"
    )

hzCpSynceConfigMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 84)
)
hzCpSynceConfigMismatchCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpAlarmInstanceIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpSynceConfigMismatchCleared.setStatus(
        "current"
    )

hzCpCryptoPowerUpTestsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 85)
)
hzCpCryptoPowerUpTestsFailed.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpCryptoPowerUpTestsFailed.setStatus(
        "current"
    )

hzCpCryptoConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 86)
)
hzCpCryptoConfigMismatch.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpAlarmInstanceIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpCryptoConfigMismatch.setStatus(
        "current"
    )

hzCpCryptoConfigMismatchCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 87)
)
hzCpCryptoConfigMismatchCleared.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpAlarmConfigSeverity"),
        ("DRAGONWAVE-HCP-MIB", "hzCpAlarmInstanceIndex"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpCryptoConfigMismatchCleared.setStatus(
        "current"
    )

hzCpSystemTimeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 88)
)
hzCpSystemTimeChange.setObjects(
      *(("DRAGONWAVE-HCP-MIB", "hzCpDateAndTimeForLastTimeChange"),
        ("DRAGONWAVE-HCP-MIB", "hzCpLastTimeChange"),
        ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter"))
)
if mibBuilder.loadTexts:
    hzCpSystemTimeChange.setStatus(
        "current"
    )

hzCpCodeCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 89)
)
hzCpCodeCheck.setObjects(
    ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter")
)
if mibBuilder.loadTexts:
    hzCpCodeCheck.setStatus(
        "current"
    )

hzCpConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 7262, 2, 5, 11, 90)
)
hzCpConfigChanged.setObjects(
    ("HORIZON-EQUIPMENT-LOG-MIB", "horizonEquipmentOutTrapsCounter")
)
if mibBuilder.loadTexts:
    hzCpConfigChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DRAGONWAVE-HCP-MIB",
    **{"horizonCompactPlus": horizonCompactPlus,
       "hzCpSystem": hzCpSystem,
       "hzCpSysGeneral": hzCpSysGeneral,
       "hzCpResetSystem": hzCpResetSystem,
       "hzCpSaveMIB": hzCpSaveMIB,
       "hzCpOperStatus": hzCpOperStatus,
       "hzCpSysSpeed": hzCpSysSpeed,
       "hzCpSystemCurrentSpeed": hzCpSystemCurrentSpeed,
       "hzCpSystemLicensedSpeed": hzCpSystemLicensedSpeed,
       "hzCpSysUpgradeSpeed": hzCpSysUpgradeSpeed,
       "hzCpLicensedSpeedUpgradeSpeedAndKey": hzCpLicensedSpeedUpgradeSpeedAndKey,
       "hzCpLicensedSpeedCount": hzCpLicensedSpeedCount,
       "hzCpSysDowngradeSpeed": hzCpSysDowngradeSpeed,
       "hzCpLicensedSpeedDowngradeSpeed": hzCpLicensedSpeedDowngradeSpeed,
       "hzCpLicensedSpeedCountUsedForKey": hzCpLicensedSpeedCountUsedForKey,
       "hzCpLicensedSpeedConfirmationKey": hzCpLicensedSpeedConfirmationKey,
       "hzCpSysDowngradeSpeedDecrement": hzCpSysDowngradeSpeedDecrement,
       "hzCpInventory": hzCpInventory,
       "hzCpHwInventory": hzCpHwInventory,
       "hzCpFrequencyFilePartNumber": hzCpFrequencyFilePartNumber,
       "hzCpUnitSerialNo": hzCpUnitSerialNo,
       "hzCpUnitAssemblyNo": hzCpUnitAssemblyNo,
       "hzCpModemSerialNo": hzCpModemSerialNo,
       "hzCpModemAssemblyNo": hzCpModemAssemblyNo,
       "hzCpPsuSerialNo": hzCpPsuSerialNo,
       "hzCpPsuAssemblyNo": hzCpPsuAssemblyNo,
       "hzCpRfSerialNo": hzCpRfSerialNo,
       "hzCpRfAssemblyNo": hzCpRfAssemblyNo,
       "hzCpDiplexerSerialNo": hzCpDiplexerSerialNo,
       "hzCpDiplexerAssemblyNo": hzCpDiplexerAssemblyNo,
       "hzCpSystemCleiNo": hzCpSystemCleiNo,
       "hzCpSwInventory": hzCpSwInventory,
       "hzCpSwInventoryTable": hzCpSwInventoryTable,
       "hzCpSwInventoryEntry": hzCpSwInventoryEntry,
       "hzCpSwInvBank": hzCpSwInvBank,
       "hzCpSwInvStatus": hzCpSwInvStatus,
       "hzCpSwInvOmniRelease": hzCpSwInvOmniRelease,
       "hzCpSwInvFrequencyFileVersion": hzCpSwInvFrequencyFileVersion,
       "hzCpSwInvMibVersion": hzCpSwInvMibVersion,
       "hzCpSwInvBootloaderVersion": hzCpSwInvBootloaderVersion,
       "hzCpPeerSysInfo": hzCpPeerSysInfo,
       "hzCpPeerMacAddress": hzCpPeerMacAddress,
       "hzCpPeerIpAddress": hzCpPeerIpAddress,
       "hzCpPeerSubnetMask": hzCpPeerSubnetMask,
       "hzCpPeerDefaultGateway": hzCpPeerDefaultGateway,
       "hzCpPeerIpv6Prefix": hzCpPeerIpv6Prefix,
       "hzCpPeerIpv6Domain": hzCpPeerIpv6Domain,
       "hzCpPeerIpv6Address": hzCpPeerIpv6Address,
       "hzCpPeerIpv6GatewayDomain": hzCpPeerIpv6GatewayDomain,
       "hzCpPeerIpv6GatewayAddress": hzCpPeerIpv6GatewayAddress,
       "hzCpSysRedundancy": hzCpSysRedundancy,
       "hzCpRedundancyMode": hzCpRedundancyMode,
       "hzCpRedundancySwitchMode": hzCpRedundancySwitchMode,
       "hzCpRedundancyStandbyEnetState": hzCpRedundancyStandbyEnetState,
       "hzCpRedundancyStateSwitch": hzCpRedundancyStateSwitch,
       "hzCpRedundancyMgmtSource": hzCpRedundancyMgmtSource,
       "hzCpRedundancyLinkSwitchParameters": hzCpRedundancyLinkSwitchParameters,
       "hzCpRedundancyPrimaryTimeInActiveState": hzCpRedundancyPrimaryTimeInActiveState,
       "hzCpRedundancyPrimarySwitchErrorThreshold": hzCpRedundancyPrimarySwitchErrorThreshold,
       "hzCpRedundancySecondaryTimeInActiveState": hzCpRedundancySecondaryTimeInActiveState,
       "hzCpRedundancySecondarySwitchErrorThreshold": hzCpRedundancySecondarySwitchErrorThreshold,
       "hzCpRedundancyLinkMonitorParameters": hzCpRedundancyLinkMonitorParameters,
       "hzCpRedundancyFaultPeriod": hzCpRedundancyFaultPeriod,
       "hzCpRedundancyFaultThreshold": hzCpRedundancyFaultThreshold,
       "hzCpPartnerSysInfo": hzCpPartnerSysInfo,
       "hzCpPartnerMacAddress": hzCpPartnerMacAddress,
       "hzCpPartnerIpAddress": hzCpPartnerIpAddress,
       "hzCpPartnerSubnetMask": hzCpPartnerSubnetMask,
       "hzCpPartnerDefaultGateway": hzCpPartnerDefaultGateway,
       "hzCpPartnerIpv6Prefix": hzCpPartnerIpv6Prefix,
       "hzCpPartnerIpv6Domain": hzCpPartnerIpv6Domain,
       "hzCpPartnerIpv6Address": hzCpPartnerIpv6Address,
       "hzCpPartnerIpv6GatewayDomain": hzCpPartnerIpv6GatewayDomain,
       "hzCpPartnerIpv6GatewayAddress": hzCpPartnerIpv6GatewayAddress,
       "hzCpPeerPartnerSysInfo": hzCpPeerPartnerSysInfo,
       "hzCpPeerPartnerMacAddress": hzCpPeerPartnerMacAddress,
       "hzCpPeerPartnerIpAddress": hzCpPeerPartnerIpAddress,
       "hzCpPeerPartnerSubnetMask": hzCpPeerPartnerSubnetMask,
       "hzCpPeerPartnerDefaultGateway": hzCpPeerPartnerDefaultGateway,
       "hzCpPeerPartnerIpv6Prefix": hzCpPeerPartnerIpv6Prefix,
       "hzCpPeerPartnerIpv6Domain": hzCpPeerPartnerIpv6Domain,
       "hzCpPeerPartnerIpv6Address": hzCpPeerPartnerIpv6Address,
       "hzCpPeerPartnerIpv6GatewayDomain": hzCpPeerPartnerIpv6GatewayDomain,
       "hzCpPeerPartnerIpv6GatewayAddress": hzCpPeerPartnerIpv6GatewayAddress,
       "hzCpPartnerCommunication": hzCpPartnerCommunication,
       "hzCpPartnerAutoDiscovery": hzCpPartnerAutoDiscovery,
       "hzCpPartnerMacAddressOverride": hzCpPartnerMacAddressOverride,
       "hzCpPartnerVlanTagging": hzCpPartnerVlanTagging,
       "hzCpPartnerVlanTagId": hzCpPartnerVlanTagId,
       "hzCpPartnerVlanTagPriority": hzCpPartnerVlanTagPriority,
       "hzCpRedundancyStatus": hzCpRedundancyStatus,
       "hzCpRedundancyUserTrafficStatus": hzCpRedundancyUserTrafficStatus,
       "hzCpRedundancyWirelessLinkStatus": hzCpRedundancyWirelessLinkStatus,
       "hzCpRedundancyEnetCrossLinkStatus": hzCpRedundancyEnetCrossLinkStatus,
       "hzCpRedundancyPortGroupStatus": hzCpRedundancyPortGroupStatus,
       "hzCpSysDiagnostics": hzCpSysDiagnostics,
       "hzCpLoopback": hzCpLoopback,
       "hzCpLoopbackType": hzCpLoopbackType,
       "hzCpLoopbackTimeout": hzCpLoopbackTimeout,
       "hzCpLoopbackNetworkMac": hzCpLoopbackNetworkMac,
       "hzCpLoopbackNetworkQueue": hzCpLoopbackNetworkQueue,
       "hzCpLoopbackNetworkPort": hzCpLoopbackNetworkPort,
       "hzCpLoopbackStart": hzCpLoopbackStart,
       "hzCpLoopbackStop": hzCpLoopbackStop,
       "hzCpHitlessAamDiagnostics": hzCpHitlessAamDiagnostics,
       "hzCpHitlessAamModemTable": hzCpHitlessAamModemTable,
       "hzCpHitlessAamModemEntry": hzCpHitlessAamModemEntry,
       "hzCpHitlessAamModemIndex": hzCpHitlessAamModemIndex,
       "hzCpHitlessAamModemDiagnose": hzCpHitlessAamModemDiagnose,
       "hzCpHitlessAamModemDiagnosticResult": hzCpHitlessAamModemDiagnosticResult,
       "hzCpCodeCheckCount": hzCpCodeCheckCount,
       "hzCpSysLicensedFeatureGroups": hzCpSysLicensedFeatureGroups,
       "hzCpSysUpgradeFeatureGroupsTable": hzCpSysUpgradeFeatureGroupsTable,
       "hzCpSysUpgradeFeatureGroupsEntry": hzCpSysUpgradeFeatureGroupsEntry,
       "hzCpUpgradeLicensedFeatureIndex": hzCpUpgradeLicensedFeatureIndex,
       "hzCpUpgradeLicensedFeatureKey": hzCpUpgradeLicensedFeatureKey,
       "hzCpUpgradeLicensedFeatureCount": hzCpUpgradeLicensedFeatureCount,
       "hzCpSysDowngradeFeatureGroupsTable": hzCpSysDowngradeFeatureGroupsTable,
       "hzCpSysDowngradeFeatureGroupsEntry": hzCpSysDowngradeFeatureGroupsEntry,
       "hzCpDowngradeLicensedFeatureIndex": hzCpDowngradeLicensedFeatureIndex,
       "hzCpDowngradeLicensedFeature": hzCpDowngradeLicensedFeature,
       "hzCpDowngradeLicensedFeatureCount": hzCpDowngradeLicensedFeatureCount,
       "hzCpDowngradeLicensedFeatureKey": hzCpDowngradeLicensedFeatureKey,
       "hzCpSysLicensedFeatureGroupsTable": hzCpSysLicensedFeatureGroupsTable,
       "hzCpSysLicensedFeatureGroupsEntry": hzCpSysLicensedFeatureGroupsEntry,
       "hzCpSysLicensedFeatureGroupIndex": hzCpSysLicensedFeatureGroupIndex,
       "hzCpSysLicensedFeatureGroup": hzCpSysLicensedFeatureGroup,
       "hzCpSysLicensedFeatureGroupStatus": hzCpSysLicensedFeatureGroupStatus,
       "hzCpPeerAuthentication": hzCpPeerAuthentication,
       "hzCpPeerAuthenticationUniqueKey": hzCpPeerAuthenticationUniqueKey,
       "hzCpPeerAuthenticationMode": hzCpPeerAuthenticationMode,
       "hzCpPeerAuthenticationFailureAction": hzCpPeerAuthenticationFailureAction,
       "hzCpPeerAuthenticationStatus": hzCpPeerAuthenticationStatus,
       "hzCpPeerAuthenticationGroupKey": hzCpPeerAuthenticationGroupKey,
       "hzCpCalendar": hzCpCalendar,
       "hzCpDate": hzCpDate,
       "hzCpTime": hzCpTime,
       "hzCpDateAndTimeForLastTimeChange": hzCpDateAndTimeForLastTimeChange,
       "hzCpLastTimeChange": hzCpLastTimeChange,
       "hzCpCumulativeTimeChange": hzCpCumulativeTimeChange,
       "hzCpSntp": hzCpSntp,
       "hzCpSntpEnable": hzCpSntpEnable,
       "hzCpSntpOffset": hzCpSntpOffset,
       "hzCpSntpServerDepTable": hzCpSntpServerDepTable,
       "hzCpSntpServerDepEntry": hzCpSntpServerDepEntry,
       "hzCpSntpServerIndexDep": hzCpSntpServerIndexDep,
       "hzCpSntpServerIpAddressDep": hzCpSntpServerIpAddressDep,
       "hzCpSntpServerStatusDep": hzCpSntpServerStatusDep,
       "hzCpSntpServerStratumDep": hzCpSntpServerStratumDep,
       "hzCpSntpServerTable": hzCpSntpServerTable,
       "hzCpSntpServerEntry": hzCpSntpServerEntry,
       "hzCpSntpServerIndex": hzCpSntpServerIndex,
       "hzCpSntpServerDomain": hzCpSntpServerDomain,
       "hzCpSntpServerAddress": hzCpSntpServerAddress,
       "hzCpSntpServerStatus": hzCpSntpServerStatus,
       "hzCpSntpServerStratum": hzCpSntpServerStratum,
       "hzCpSntpRestoreDefault": hzCpSntpRestoreDefault,
       "hzCpSyncE": hzCpSyncE,
       "hzCpSyncEState": hzCpSyncEState,
       "hzCpSyncEPrimarySource": hzCpSyncEPrimarySource,
       "hzCpSyncESecondarySource": hzCpSyncESecondarySource,
       "hzCpSyncEMemberPorts": hzCpSyncEMemberPorts,
       "hzCpSyncEForcedHoldover": hzCpSyncEForcedHoldover,
       "hzCpSyncERevertive": hzCpSyncERevertive,
       "hzCpSyncEClockSource": hzCpSyncEClockSource,
       "hzCpSyncEAcquisitionStatus": hzCpSyncEAcquisitionStatus,
       "hzCpSyncEWanderFilter": hzCpSyncEWanderFilter,
       "hzCpBac": hzCpBac,
       "hzCpBacRecordAvgPeriod": hzCpBacRecordAvgPeriod,
       "hzCpBacTable": hzCpBacTable,
       "hzCpBacEntry": hzCpBacEntry,
       "hzCpBacQIndex": hzCpBacQIndex,
       "hzCpBacQEnable": hzCpBacQEnable,
       "hzCpBacQBlockSize": hzCpBacQBlockSize,
       "hzCpBacRecordLogging": hzCpBacRecordLogging,
       "hzCpBacUncompressedRatio": hzCpBacUncompressedRatio,
       "hzCpBacGain": hzCpBacGain,
       "hzCpEcfmVsm": hzCpEcfmVsm,
       "hzCpBandwidthVsm": hzCpBandwidthVsm,
       "hzCpBwVsmVendorOui": hzCpBwVsmVendorOui,
       "hzCpBwVsmMdLevel": hzCpBwVsmMdLevel,
       "hzCpBwVsmWaitTime": hzCpBwVsmWaitTime,
       "hzCpBwVsmPeriod": hzCpBwVsmPeriod,
       "hzCpBwVsmVlanTag": hzCpBwVsmVlanTag,
       "hzCpBwVsmVlanId": hzCpBwVsmVlanId,
       "hzCpBwVsmVlanPriority": hzCpBwVsmVlanPriority,
       "hzCpBwVsmPortList": hzCpBwVsmPortList,
       "hzCpBwVsmState": hzCpBwVsmState,
       "hzCpPM": hzCpPM,
       "hzCpPmRspiThresholdTable": hzCpPmRspiThresholdTable,
       "hzCpPmRspiThresholdEntry": hzCpPmRspiThresholdEntry,
       "hzCpPmRspiThrIndex": hzCpPmRspiThrIndex,
       "hzCpPmRLT1": hzCpPmRLT1,
       "hzCpPmRLT2": hzCpPmRLT2,
       "hzCpPmRLT3": hzCpPmRLT3,
       "hzCpPmRLT4": hzCpPmRLT4,
       "hzCpPmTLT1": hzCpPmTLT1,
       "hzCpPmTLT2": hzCpPmTLT2,
       "hzCpPmRspiThrRowStatus": hzCpPmRspiThrRowStatus,
       "hzCpPmAdvThresholdTable": hzCpPmAdvThresholdTable,
       "hzCpPmAdvThresholdEntry": hzCpPmAdvThresholdEntry,
       "hzCpPmAdvThrIndex": hzCpPmAdvThrIndex,
       "hzCpPmAdvTxHitsT1": hzCpPmAdvTxHitsT1,
       "hzCpPmAdvRxHitsT1": hzCpPmAdvRxHitsT1,
       "hzCpPmAdvRowStatus": hzCpPmAdvRowStatus,
       "hzCpManagement": hzCpManagement,
       "hzCpMacAddress": hzCpMacAddress,
       "hzCpTelnetAccessMode": hzCpTelnetAccessMode,
       "hzCpSshAccessMode": hzCpSshAccessMode,
       "hzCpNetworkManagementInterface": hzCpNetworkManagementInterface,
       "hzCpNetMgmtInterfaceVlan": hzCpNetMgmtInterfaceVlan,
       "hzCpNetMgmtPortList": hzCpNetMgmtPortList,
       "hzCpNetMgmtVlanTagId": hzCpNetMgmtVlanTagId,
       "hzCpNetMgmtVlanTagPriority": hzCpNetMgmtVlanTagPriority,
       "hzCpNetMgmtVlanTagging": hzCpNetMgmtVlanTagging,
       "hzCpNetMgmtDscpPriority": hzCpNetMgmtDscpPriority,
       "hzCpNetMgmtIpv4": hzCpNetMgmtIpv4,
       "hzCpIpAddress": hzCpIpAddress,
       "hzCpSubnetMask": hzCpSubnetMask,
       "hzCpDefaultGateway": hzCpDefaultGateway,
       "hzCpNetMgmttIpv6": hzCpNetMgmttIpv6,
       "hzCpIpv6Domain": hzCpIpv6Domain,
       "hzCpIpv6Address": hzCpIpv6Address,
       "hzCpIpv6Prefix": hzCpIpv6Prefix,
       "hzCpIpv6GatewayDomain": hzCpIpv6GatewayDomain,
       "hzCpIpv6GatewayAddress": hzCpIpv6GatewayAddress,
       "hzCpIpv6LinkLocalDomain": hzCpIpv6LinkLocalDomain,
       "hzCpIpv6LinkLocalAddress": hzCpIpv6LinkLocalAddress,
       "hzCpNetMgmtApplyToSystem": hzCpNetMgmtApplyToSystem,
       "hzCpSnmp": hzCpSnmp,
       "hzCpSnmpUserAccess": hzCpSnmpUserAccess,
       "hzCpSnmpManagerAnyCommunityName": hzCpSnmpManagerAnyCommunityName,
       "hzCpSnmpSetRequests": hzCpSnmpSetRequests,
       "hzCpSnmpManagersDepTable": hzCpSnmpManagersDepTable,
       "hzCpSnmpManagersDepEntry": hzCpSnmpManagersDepEntry,
       "hzCpSnmpManagersIndexDep": hzCpSnmpManagersIndexDep,
       "hzCpSnmpManagerIpAddressDep": hzCpSnmpManagerIpAddressDep,
       "hzCpSnmpManagerCommunityNameDep": hzCpSnmpManagerCommunityNameDep,
       "hzCpSnmpManagerActivatedDep": hzCpSnmpManagerActivatedDep,
       "hzCpSnmpV3ManagersTable": hzCpSnmpV3ManagersTable,
       "hzCpSnmpV3ManagersEntry": hzCpSnmpV3ManagersEntry,
       "hzCpSnmpV3ManagersIndex": hzCpSnmpV3ManagersIndex,
       "hzCpSnmpV3ManagerUserName": hzCpSnmpV3ManagerUserName,
       "hzCpSnmpV3ManagerAuthProtocol": hzCpSnmpV3ManagerAuthProtocol,
       "hzCpSnmpV3ManagerAuthPassword": hzCpSnmpV3ManagerAuthPassword,
       "hzCpSnmpV3ManagerPrivProtocol": hzCpSnmpV3ManagerPrivProtocol,
       "hzCpSnmpV3ManagerPrivPassword": hzCpSnmpV3ManagerPrivPassword,
       "hzCpSnmpV3ManagerActivated": hzCpSnmpV3ManagerActivated,
       "hzCpSnmpAccessMode": hzCpSnmpAccessMode,
       "hzCpSnmpManagersTable": hzCpSnmpManagersTable,
       "hzCpSnmpManagersEntry": hzCpSnmpManagersEntry,
       "hzCpSnmpManagersIndex": hzCpSnmpManagersIndex,
       "hzCpSnmpManagerDomain": hzCpSnmpManagerDomain,
       "hzCpSnmpManagerAddress": hzCpSnmpManagerAddress,
       "hzCpSnmpManagerCommunityName": hzCpSnmpManagerCommunityName,
       "hzCpSnmpManagersPrefixLength": hzCpSnmpManagersPrefixLength,
       "hzCpSnmpManagerActivated": hzCpSnmpManagerActivated,
       "hzCpTrapConfig": hzCpTrapConfig,
       "hzCpSnmpTrapHostDepTable": hzCpSnmpTrapHostDepTable,
       "hzCpSnmpTrapHostDepEntry": hzCpSnmpTrapHostDepEntry,
       "hzCpSnmpTrapHostIndexDep": hzCpSnmpTrapHostIndexDep,
       "hzCpSnmpTrapHostIpAddressDep": hzCpSnmpTrapHostIpAddressDep,
       "hzCpSnmpTrapHostCommunityNameDep": hzCpSnmpTrapHostCommunityNameDep,
       "hzCpSnmpTrapHostActivatedDep": hzCpSnmpTrapHostActivatedDep,
       "hzCpSnmpV3TrapHostsDepTable": hzCpSnmpV3TrapHostsDepTable,
       "hzCpSnmpV3TrapHostsDepEntry": hzCpSnmpV3TrapHostsDepEntry,
       "hzCpSnmpV3TrapHostsIndexDep": hzCpSnmpV3TrapHostsIndexDep,
       "hzCpSnmpV3TrapHostIpAddressDep": hzCpSnmpV3TrapHostIpAddressDep,
       "hzCpSnmpV3TrapHostUserNameDep": hzCpSnmpV3TrapHostUserNameDep,
       "hzCpSnmpV3TrapHostAuthProtocolDep": hzCpSnmpV3TrapHostAuthProtocolDep,
       "hzCpSnmpV3TrapHostAuthPasswordDep": hzCpSnmpV3TrapHostAuthPasswordDep,
       "hzCpSnmpV3TrapHostPrivProtocolDep": hzCpSnmpV3TrapHostPrivProtocolDep,
       "hzCpSnmpV3TrapHostPrivPasswordDep": hzCpSnmpV3TrapHostPrivPasswordDep,
       "hzCpSnmpV3TrapHostActivatedDep": hzCpSnmpV3TrapHostActivatedDep,
       "hzCpTrapEnable": hzCpTrapEnable,
       "hzCpColdStartTrap": hzCpColdStartTrap,
       "hzCpLinkDownTrap": hzCpLinkDownTrap,
       "hzCpPeerAuthenticationFailureTrap": hzCpPeerAuthenticationFailureTrap,
       "hzCpHitlessAamConfigMismatchTrap": hzCpHitlessAamConfigMismatchTrap,
       "hzCpHitlessAamModulationLoweredTrap": hzCpHitlessAamModulationLoweredTrap,
       "hzCpHitlessAamModulationChangedEventTrap": hzCpHitlessAamModulationChangedEventTrap,
       "hzCpAtpcConfigMismatchTrap": hzCpAtpcConfigMismatchTrap,
       "hzCpAtpcAutoDisabledTrap": hzCpAtpcAutoDisabledTrap,
       "hzCpNoSntpServersReachableTrap": hzCpNoSntpServersReachableTrap,
       "hzCpFrequencyFileInvalidTrap": hzCpFrequencyFileInvalidTrap,
       "hzCpAggregateDroppedFramesThresholdTrap": hzCpAggregateDroppedFramesThresholdTrap,
       "hzCpQueueDroppedFramesThresholdTrap": hzCpQueueDroppedFramesThresholdTrap,
       "hzCpBwUtilizationThresholdTrap": hzCpBwUtilizationThresholdTrap,
       "hzCpQueueDepthThresholdTrap": hzCpQueueDepthThresholdTrap,
       "hzCpRlsConfigMismatchTrap": hzCpRlsConfigMismatchTrap,
       "hzCpRlsShutdownActivatedTrap": hzCpRlsShutdownActivatedTrap,
       "hzCpRlsQueueBasedShutdownActivatedTrap": hzCpRlsQueueBasedShutdownActivatedTrap,
       "hzCpModemRxLossOfSignalLockTrap": hzCpModemRxLossOfSignalLockTrap,
       "hzCpModemSnrBelowThresholdTrap": hzCpModemSnrBelowThresholdTrap,
       "hzCpModemEqualizerStressThresholdTrap": hzCpModemEqualizerStressThresholdTrap,
       "hzCpRslBelowThresholdTrap": hzCpRslBelowThresholdTrap,
       "hzCpRadioSynthLostLockTrap": hzCpRadioSynthLostLockTrap,
       "hzCpRadioCalTableNotAvailableTrap": hzCpRadioCalTableNotAvailableTrap,
       "hzCpRadioDrainCurrentOutOfLimitTrap": hzCpRadioDrainCurrentOutOfLimitTrap,
       "hzCpRadioPowerAmplifierTrap": hzCpRadioPowerAmplifierTrap,
       "hzCpTemperatureOutOfLimitTrap": hzCpTemperatureOutOfLimitTrap,
       "hzCpRedundancyConfigMismatchTrap": hzCpRedundancyConfigMismatchTrap,
       "hzCpRedundancyActiveOnSecondaryTrap": hzCpRedundancyActiveOnSecondaryTrap,
       "hzCpRedundancyOperatingInForcedSwitchTrap": hzCpRedundancyOperatingInForcedSwitchTrap,
       "hzCpRedundancyEnetCrossLinkTrap": hzCpRedundancyEnetCrossLinkTrap,
       "hzCpRedundancyActiveUsingPartnerWLinkTrap": hzCpRedundancyActiveUsingPartnerWLinkTrap,
       "hzCpRedundancyStandbyWLinkInUseTrap": hzCpRedundancyStandbyWLinkInUseTrap,
       "hzCpRedundancyStandbyOnPrimaryTrap": hzCpRedundancyStandbyOnPrimaryTrap,
       "hzCpX2DeliveringHalfCapacityTrap": hzCpX2DeliveringHalfCapacityTrap,
       "hzCpBncCableSignalNotDetectedTrap": hzCpBncCableSignalNotDetectedTrap,
       "hzCpEthernetSpeedReducedTrap": hzCpEthernetSpeedReducedTrap,
       "hzCpSynceLostLockTrap": hzCpSynceLostLockTrap,
       "hzCpSynceSecondarySourceInUseTrap": hzCpSynceSecondarySourceInUseTrap,
       "hzCpUserSessionTrap": hzCpUserSessionTrap,
       "hzCpInvalidSystemConfigTrap": hzCpInvalidSystemConfigTrap,
       "hzCpMibChangeNotSavedTrap": hzCpMibChangeNotSavedTrap,
       "hzCpTransmitterLossOfSyncTrap": hzCpTransmitterLossOfSyncTrap,
       "hzCpRadioLinearityCalErrorTrap": hzCpRadioLinearityCalErrorTrap,
       "hzCpSynceConfigMismatchTrap": hzCpSynceConfigMismatchTrap,
       "hzCpCryptoPowerUpTestsFailedTrap": hzCpCryptoPowerUpTestsFailedTrap,
       "hzCpCryptoConfigMismatchTrap": hzCpCryptoConfigMismatchTrap,
       "hzCpSystemTimeChangeTrap": hzCpSystemTimeChangeTrap,
       "hzCpCodeCheckTrap": hzCpCodeCheckTrap,
       "hzCpConfigChangedTrap": hzCpConfigChangedTrap,
       "hzCpSnmpTrapHostTable": hzCpSnmpTrapHostTable,
       "hzCpSnmpTrapHostEntry": hzCpSnmpTrapHostEntry,
       "hzCpSnmpTrapHostIndex": hzCpSnmpTrapHostIndex,
       "hzCpSnmpTrapHostDomain": hzCpSnmpTrapHostDomain,
       "hzCpSnmpTrapHostAddress": hzCpSnmpTrapHostAddress,
       "hzCpSnmpTrapHostCommunityName": hzCpSnmpTrapHostCommunityName,
       "hzCpSnmpTrapHostActivated": hzCpSnmpTrapHostActivated,
       "hzCpSnmpV3TrapHostsTable": hzCpSnmpV3TrapHostsTable,
       "hzCpSnmpV3TrapHostsEntry": hzCpSnmpV3TrapHostsEntry,
       "hzCpSnmpV3TrapHostsIndex": hzCpSnmpV3TrapHostsIndex,
       "hzCpSnmpV3TrapHostDomain": hzCpSnmpV3TrapHostDomain,
       "hzCpSnmpV3TrapHostAddress": hzCpSnmpV3TrapHostAddress,
       "hzCpSnmpV3TrapHostUserName": hzCpSnmpV3TrapHostUserName,
       "hzCpSnmpV3TrapHostAuthProtocol": hzCpSnmpV3TrapHostAuthProtocol,
       "hzCpSnmpV3TrapHostAuthPassword": hzCpSnmpV3TrapHostAuthPassword,
       "hzCpSnmpV3TrapHostPrivProtocol": hzCpSnmpV3TrapHostPrivProtocol,
       "hzCpSnmpV3TrapHostPrivPassword": hzCpSnmpV3TrapHostPrivPassword,
       "hzCpSnmpV3TrapHostActivated": hzCpSnmpV3TrapHostActivated,
       "hzCpRadius": hzCpRadius,
       "hzCpRadiusSuperUserAuthentication": hzCpRadiusSuperUserAuthentication,
       "hzCpRadiusServerTimeOut": hzCpRadiusServerTimeOut,
       "hzCpRadiusServerDeadTime": hzCpRadiusServerDeadTime,
       "hzCpRadiusServerReTransmit": hzCpRadiusServerReTransmit,
       "hzCpRadiusServerDepTable": hzCpRadiusServerDepTable,
       "hzCpRadiusServerDepEntry": hzCpRadiusServerDepEntry,
       "hzCpRadiusServerIndexDep": hzCpRadiusServerIndexDep,
       "hzCpRadiusCfgdHostIpAddressDep": hzCpRadiusCfgdHostIpAddressDep,
       "hzCpRadiusCfgdHostKeyDep": hzCpRadiusCfgdHostKeyDep,
       "hzCpRadiusServerTable": hzCpRadiusServerTable,
       "hzCpRadiusServerEntry": hzCpRadiusServerEntry,
       "hzCpRadiusServerIndex": hzCpRadiusServerIndex,
       "hzCpRadiusCfgdHostDomain": hzCpRadiusCfgdHostDomain,
       "hzCpRadiusCfgdHostAddress": hzCpRadiusCfgdHostAddress,
       "hzCpRadiusCfgdHostKey": hzCpRadiusCfgdHostKey,
       "hzCpManagementSessions": hzCpManagementSessions,
       "hzCpUserSessionUserTable": hzCpUserSessionUserTable,
       "hzCpUserSessionUserEntry": hzCpUserSessionUserEntry,
       "hzCpUserSessionUserIndex": hzCpUserSessionUserIndex,
       "hzCpUserSessionUserName": hzCpUserSessionUserName,
       "hzCpUserSessionUserConnectionType": hzCpUserSessionUserConnectionType,
       "hzCpUserSessionUserState": hzCpUserSessionUserState,
       "hzCpHttp": hzCpHttp,
       "hzCpHttpEnable": hzCpHttpEnable,
       "hzCpHttpSecure": hzCpHttpSecure,
       "hzCpHttpSecureCertificateStatus": hzCpHttpSecureCertificateStatus,
       "hzCpHttpSecureAccessForAdminUsers": hzCpHttpSecureAccessForAdminUsers,
       "hzCpHttpSecureAccessForNocUsers": hzCpHttpSecureAccessForNocUsers,
       "hzCpHttpSecureAccessForSuperUsers": hzCpHttpSecureAccessForSuperUsers,
       "hzCpNetworkInterface": hzCpNetworkInterface,
       "hzCpEnetPort": hzCpEnetPort,
       "hzCpEnetPortConfigTable": hzCpEnetPortConfigTable,
       "hzCpEnetPortConfigEntry": hzCpEnetPortConfigEntry,
       "hzCpEnetPortIndex": hzCpEnetPortIndex,
       "hzCpEnetPortName": hzCpEnetPortName,
       "hzCpEnetPortAutoNegotiation": hzCpEnetPortAutoNegotiation,
       "hzCpEnetPortSpeed": hzCpEnetPortSpeed,
       "hzCpEnetPortDuplex": hzCpEnetPortDuplex,
       "hzCpEnetPortMedia": hzCpEnetPortMedia,
       "hzCpEnetPortAdminState": hzCpEnetPortAdminState,
       "hzCpEnetPortPauseFrame": hzCpEnetPortPauseFrame,
       "hzCpEnetPortMaxFrameSize": hzCpEnetPortMaxFrameSize,
       "hzCpEnetPortOpticalTransceiverState": hzCpEnetPortOpticalTransceiverState,
       "hzCpEnetPortState": hzCpEnetPortState,
       "hzCpEnetPayloadState": hzCpEnetPayloadState,
       "hzCpEnetPortStatusTable": hzCpEnetPortStatusTable,
       "hzCpEnetPortStatusEntry": hzCpEnetPortStatusEntry,
       "hzCpEnetPortStatusIndex": hzCpEnetPortStatusIndex,
       "hzCpEnetPortLinkStatus": hzCpEnetPortLinkStatus,
       "hzCpEnetPortAutoNegotiationStatus": hzCpEnetPortAutoNegotiationStatus,
       "hzCpEnetPortSpeedStatus": hzCpEnetPortSpeedStatus,
       "hzCpEnetPortDuplexStatus": hzCpEnetPortDuplexStatus,
       "hzCpEnetPortMediaStatus": hzCpEnetPortMediaStatus,
       "hzCpEnetPortStatsTable": hzCpEnetPortStatsTable,
       "hzCpEnetPortStatsEntry": hzCpEnetPortStatsEntry,
       "hzCpEnetPortStatsIndex": hzCpEnetPortStatsIndex,
       "hzCpEnetPortTxFrames": hzCpEnetPortTxFrames,
       "hzCpEnetPortTxBytes": hzCpEnetPortTxBytes,
       "hzCpEnetPortRxFramesOk": hzCpEnetPortRxFramesOk,
       "hzCpEnetPortRxBytesOk": hzCpEnetPortRxBytesOk,
       "hzCpEnetPortRxFramesLengthErrors": hzCpEnetPortRxFramesLengthErrors,
       "hzCpEnetPortRxFramesCrcErrors": hzCpEnetPortRxFramesCrcErrors,
       "hzCpEnetPortRxDiscarded": hzCpEnetPortRxDiscarded,
       "hzCpEnetAggregatedStats": hzCpEnetAggregatedStats,
       "hzCpEnetAggTxFrames": hzCpEnetAggTxFrames,
       "hzCpEnetAggTxBytes": hzCpEnetAggTxBytes,
       "hzCpEnetAggRxFramesOK": hzCpEnetAggRxFramesOK,
       "hzCpEnetAggRxBytesOK": hzCpEnetAggRxBytesOK,
       "hzCpEnetAggRxFramesLengthError": hzCpEnetAggRxFramesLengthError,
       "hzCpEnetAggPortRxFramesCrcError": hzCpEnetAggPortRxFramesCrcError,
       "hzCpEnetAggPortRxFramesDrops": hzCpEnetAggPortRxFramesDrops,
       "hzCpEnetAggBWUtilization": hzCpEnetAggBWUtilization,
       "hzCpEnetAggIngressDataRate": hzCpEnetAggIngressDataRate,
       "hzCpEnetAggEgressDataRate": hzCpEnetAggEgressDataRate,
       "hzCpEnetAggFramesInQueueTable": hzCpEnetAggFramesInQueueTable,
       "hzCpEnetAggFramesInQueueEntry": hzCpEnetAggFramesInQueueEntry,
       "hzCpEnetAggFramesInQueueIndex": hzCpEnetAggFramesInQueueIndex,
       "hzCpEnetAggFramesInQueue": hzCpEnetAggFramesInQueue,
       "hzCpEnetAggFramesInQueueDiscarded": hzCpEnetAggFramesInQueueDiscarded,
       "hzCpEnetPortLcStatsTable": hzCpEnetPortLcStatsTable,
       "hzCpEnetPortLcStatsEntry": hzCpEnetPortLcStatsEntry,
       "hzCpEnetPortLcStatsIndex": hzCpEnetPortLcStatsIndex,
       "hzCpEnetPortLcTxFrames": hzCpEnetPortLcTxFrames,
       "hzCpEnetPortLcTxBytes": hzCpEnetPortLcTxBytes,
       "hzCpEnetPortLcRxFramesOk": hzCpEnetPortLcRxFramesOk,
       "hzCpEnetPortLcRxBytesOk": hzCpEnetPortLcRxBytesOk,
       "hzCpEnetPortLcRxFramesLengthErrors": hzCpEnetPortLcRxFramesLengthErrors,
       "hzCpEnetPortLcRxFramesCrcErrors": hzCpEnetPortLcRxFramesCrcErrors,
       "hzCpEnetPortLcRxDiscarded": hzCpEnetPortLcRxDiscarded,
       "hzCpEnetAggregatedLcStats": hzCpEnetAggregatedLcStats,
       "hzCpEnetAggLcTxFrames": hzCpEnetAggLcTxFrames,
       "hzCpEnetAggLcTxBytes": hzCpEnetAggLcTxBytes,
       "hzCpEnetAggLcRxFramesOK": hzCpEnetAggLcRxFramesOK,
       "hzCpEnetAggLcRxBytesOK": hzCpEnetAggLcRxBytesOK,
       "hzCpEnetAggLcRxFramesLengthError": hzCpEnetAggLcRxFramesLengthError,
       "hzCpEnetAggLcRxFramesCrcError": hzCpEnetAggLcRxFramesCrcError,
       "hzCpEnetAggLcRxFramesDrops": hzCpEnetAggLcRxFramesDrops,
       "hzCpEnetAggLcBWUtilization": hzCpEnetAggLcBWUtilization,
       "hzCpEnetAggLcIngressDataRate": hzCpEnetAggLcIngressDataRate,
       "hzCpEnetAggLcEgressDataRate": hzCpEnetAggLcEgressDataRate,
       "hzCpEnetAggLcFramesInQueueTable": hzCpEnetAggLcFramesInQueueTable,
       "hzCpEnetAggLcFramesInQueueEntry": hzCpEnetAggLcFramesInQueueEntry,
       "hzCpEnetAggLcFramesInQueueIndex": hzCpEnetAggLcFramesInQueueIndex,
       "hzCpEnetAggLcFramesInQueue": hzCpEnetAggLcFramesInQueue,
       "hzCpEnetAggLcFramesInQueueDiscarded": hzCpEnetAggLcFramesInQueueDiscarded,
       "hzCpEnetPortVlanTable": hzCpEnetPortVlanTable,
       "hzCpEnetPortVlanEntry": hzCpEnetPortVlanEntry,
       "hzCpEnetPortVlanIndex": hzCpEnetPortVlanIndex,
       "hzCpEnetPortDefaultVlanId": hzCpEnetPortDefaultVlanId,
       "hzCpEnetPortDefaultVlanPriority": hzCpEnetPortDefaultVlanPriority,
       "hzCpWirelessInterface": hzCpWirelessInterface,
       "hzCpWirelessInterfaceNames": hzCpWirelessInterfaceNames,
       "hzCpWirelessInterfaceNameTable": hzCpWirelessInterfaceNameTable,
       "hzCpWirelessInterfaceNameEntry": hzCpWirelessInterfaceNameEntry,
       "hzCpWirelessInterfaceNameIndex": hzCpWirelessInterfaceNameIndex,
       "hzCpWirelessInterfaceName": hzCpWirelessInterfaceName,
       "hzCpWirelessInterfaceModems": hzCpWirelessInterfaceModems,
       "hzCpModemTable": hzCpModemTable,
       "hzCpModemEntry": hzCpModemEntry,
       "hzCpModemIndex": hzCpModemIndex,
       "hzCpModemOperStatus": hzCpModemOperStatus,
       "hzCpModemChannelizedRSL": hzCpModemChannelizedRSL,
       "hzCpModemChannelizedRSLUnsignedInt": hzCpModemChannelizedRSLUnsignedInt,
       "hzCpModemModulationType": hzCpModemModulationType,
       "hzCpModemRxSpeed": hzCpModemRxSpeed,
       "hzCpModemTxSpeed": hzCpModemTxSpeed,
       "hzCpModemSNR": hzCpModemSNR,
       "hzCpModemEbToNoiseRatio": hzCpModemEbToNoiseRatio,
       "hzCpModemEqualizerStress": hzCpModemEqualizerStress,
       "hzCpWirelessPortStatsTable": hzCpWirelessPortStatsTable,
       "hzCpWirelessPortStatsEntry": hzCpWirelessPortStatsEntry,
       "hzCpWirelessPortStatsIndex": hzCpWirelessPortStatsIndex,
       "hzCpWirelessPortTxBlocks": hzCpWirelessPortTxBlocks,
       "hzCpWirelessPortRxBlocksOKs": hzCpWirelessPortRxBlocksOKs,
       "hzCpWirelessPortRxBlocksErrors": hzCpWirelessPortRxBlocksErrors,
       "hzCpWirelessAggregateStats": hzCpWirelessAggregateStats,
       "hzCpWirelessAggTxFrames": hzCpWirelessAggTxFrames,
       "hzCpWirelessAggRxFramesOK": hzCpWirelessAggRxFramesOK,
       "hzCpWirelessAggRxFramesErrors": hzCpWirelessAggRxFramesErrors,
       "hzCpWirelessAggRxFramesDiscards": hzCpWirelessAggRxFramesDiscards,
       "hzCpWirelessPortLcStatsTable": hzCpWirelessPortLcStatsTable,
       "hzCpWirelessPortLcStatsEntry": hzCpWirelessPortLcStatsEntry,
       "hzCpWirelessPortLcStatsIndex": hzCpWirelessPortLcStatsIndex,
       "hzCpWirelessPortLcTxBlocks": hzCpWirelessPortLcTxBlocks,
       "hzCpWirelessPortLcRxBlocksOKs": hzCpWirelessPortLcRxBlocksOKs,
       "hzCpWirelessPortLcRxBlocksErrors": hzCpWirelessPortLcRxBlocksErrors,
       "hzCpWirelessAggregateLcStats": hzCpWirelessAggregateLcStats,
       "hzCpWirelessAggLcTxFrames": hzCpWirelessAggLcTxFrames,
       "hzCpWirelessAggLcRxFramesOK": hzCpWirelessAggLcRxFramesOK,
       "hzCpWirelessAggLcRxFramesErrors": hzCpWirelessAggLcRxFramesErrors,
       "hzCpWirelessAggLcRxFramesDiscards": hzCpWirelessAggLcRxFramesDiscards,
       "hzCpWirelessInterfaceRadios": hzCpWirelessInterfaceRadios,
       "hzCpRadioTable": hzCpRadioTable,
       "hzCpRadioEntry": hzCpRadioEntry,
       "hzCpRadioIndex": hzCpRadioIndex,
       "hzCpRadioDescription": hzCpRadioDescription,
       "hzCpRadioOperStatus": hzCpRadioOperStatus,
       "hzCpRadioTxGain": hzCpRadioTxGain,
       "hzCpRadioRxGain": hzCpRadioRxGain,
       "hzCpRadioReset": hzCpRadioReset,
       "hzCpRadioTransmitPowerdBm": hzCpRadioTransmitPowerdBm,
       "hzCpRadioPowerOption": hzCpRadioPowerOption,
       "hzCpRadioTxState": hzCpRadioTxState,
       "hzCpRadioActualTxState": hzCpRadioActualTxState,
       "hzCpRadioTemperature": hzCpRadioTemperature,
       "hzCpRadioMaxTransmitPowerdBm": hzCpRadioMaxTransmitPowerdBm,
       "hzCpRadioActualTransmitPowerdBm": hzCpRadioActualTransmitPowerdBm,
       "hzCpWirelessInterfaceRadioFrequencies": hzCpWirelessInterfaceRadioFrequencies,
       "hzCpWirelessInterfaceRadio1Frequencies": hzCpWirelessInterfaceRadio1Frequencies,
       "hzCpRadio1FreqGroupSelected": hzCpRadio1FreqGroupSelected,
       "hzCpRadio1BandTable": hzCpRadio1BandTable,
       "hzCpRadio1BandEntry": hzCpRadio1BandEntry,
       "hzCpRadio1BandIndex": hzCpRadio1BandIndex,
       "hzCpRadio1BandId": hzCpRadio1BandId,
       "hzCpRadio1BandName": hzCpRadio1BandName,
       "hzCpRadio1BandProgrammed": hzCpRadio1BandProgrammed,
       "hzCpRadio1FreqTable": hzCpRadio1FreqTable,
       "hzCpRadio1FreqEntry": hzCpRadio1FreqEntry,
       "hzCpRadio1FreqIndex": hzCpRadio1FreqIndex,
       "hzCpRadio1FreqChannelIndex": hzCpRadio1FreqChannelIndex,
       "hzCpRadio1FreqTransmitRfFrequency": hzCpRadio1FreqTransmitRfFrequency,
       "hzCpRadio1FreqReceiveRfFrequency": hzCpRadio1FreqReceiveRfFrequency,
       "hzCpRadio1FreqProgrammed": hzCpRadio1FreqProgrammed,
       "hzCpRadio1ProgrammedFrequency": hzCpRadio1ProgrammedFrequency,
       "hzCpRadio1ProgrammedFrequencyChannel": hzCpRadio1ProgrammedFrequencyChannel,
       "hzCpRadio1ProgrammedFrequencyTxRf": hzCpRadio1ProgrammedFrequencyTxRf,
       "hzCpRadio1ProgrammedFrequencyRxRf": hzCpRadio1ProgrammedFrequencyRxRf,
       "hzCpSystemModeTable": hzCpSystemModeTable,
       "hzCpSystemModeEntry": hzCpSystemModeEntry,
       "hzCpSystemModeIndex": hzCpSystemModeIndex,
       "hzCpSystemModeId": hzCpSystemModeId,
       "hzCpSystemModeName": hzCpSystemModeName,
       "hzCpSystemModeProgrammed": hzCpSystemModeProgrammed,
       "hzCpApplyFrequencyChangesToSystem": hzCpApplyFrequencyChangesToSystem,
       "hzCpWirelessInterfaceAntenna": hzCpWirelessInterfaceAntenna,
       "hzCpAntennaDiameter": hzCpAntennaDiameter,
       "hzCpAntennaTilt": hzCpAntennaTilt,
       "hzCpAlarms": hzCpAlarms,
       "hzCpThresholdAlarmConfig": hzCpThresholdAlarmConfig,
       "hzCpAggregatedThresholdAlarm": hzCpAggregatedThresholdAlarm,
       "hzCpDroppedFramesThresholdParams": hzCpDroppedFramesThresholdParams,
       "hzCpBwUtilizationThresholdParams": hzCpBwUtilizationThresholdParams,
       "hzCpQBasedThresholdAlarm": hzCpQBasedThresholdAlarm,
       "hzCpQBasedThresholdAlarmTable": hzCpQBasedThresholdAlarmTable,
       "hzCpQBasedThresholdAlarmEntry": hzCpQBasedThresholdAlarmEntry,
       "hzCpQBasedThresholdIndex": hzCpQBasedThresholdIndex,
       "hzCpQBasedDepthThresholdParams": hzCpQBasedDepthThresholdParams,
       "hzCpQBasedDroppedFramesThresholdParams": hzCpQBasedDroppedFramesThresholdParams,
       "hzCpWirelessInterfaceThresholdAlarmTable": hzCpWirelessInterfaceThresholdAlarmTable,
       "hzCpWirelessInterfaceThresholdAlarmEntry": hzCpWirelessInterfaceThresholdAlarmEntry,
       "hzCpWirelessInterfaceThresholdAlarmIndex": hzCpWirelessInterfaceThresholdAlarmIndex,
       "hzCpWirelessInterfaceRslThresholdParams": hzCpWirelessInterfaceRslThresholdParams,
       "hzCpWirelessInterfaceSnrThreshold": hzCpWirelessInterfaceSnrThreshold,
       "hzCpAlarmConfigTable": hzCpAlarmConfigTable,
       "hzCpAlarmConfigEntry": hzCpAlarmConfigEntry,
       "hzCpAlarmConfigIndex": hzCpAlarmConfigIndex,
       "hzCpAlarmInstanceIndex": hzCpAlarmInstanceIndex,
       "hzCpAlarmConfigSeverity": hzCpAlarmConfigSeverity,
       "hzCpAlarmConfigState": hzCpAlarmConfigState,
       "hzCpAlarmStatusTable": hzCpAlarmStatusTable,
       "hzCpAlarmStatusEntry": hzCpAlarmStatusEntry,
       "hzCpAlarmStatusIndex": hzCpAlarmStatusIndex,
       "hzCpAlarmStatusInstanceIndex": hzCpAlarmStatusInstanceIndex,
       "hzCpAlarmStatus": hzCpAlarmStatus,
       "hzCpAlarmRaisedDateAndTime": hzCpAlarmRaisedDateAndTime,
       "hzCpAlarmClearedDateAndTime": hzCpAlarmClearedDateAndTime,
       "hzCpQos": hzCpQos,
       "hzCpQosEnable": hzCpQosEnable,
       "hzCpCosType": hzCpCosType,
       "hzCpCosQinQiTag": hzCpCosQinQiTag,
       "hzCpCosQinQoTag": hzCpCosQinQoTag,
       "hzCpCosExpediteQueue": hzCpCosExpediteQueue,
       "hzCpCosQueueCIR": hzCpCosQueueCIR,
       "hzCpCosQueueCBS": hzCpCosQueueCBS,
       "hzCpQosPolicy": hzCpQosPolicy,
       "hzCpCosWfqWeight": hzCpCosWfqWeight,
       "hzCpCosNumPriorityQueues": hzCpCosNumPriorityQueues,
       "hzCpCosCutThroughQueue": hzCpCosCutThroughQueue,
       "hzCpQosPortConfigTable": hzCpQosPortConfigTable,
       "hzCpQosPortConfigEntry": hzCpQosPortConfigEntry,
       "hzCpCosPortIndex": hzCpCosPortIndex,
       "hzCpCosQueueMapping": hzCpCosQueueMapping,
       "hzCpCosDefaultValue": hzCpCosDefaultValue,
       "hzCpCosUserFlowDepTable": hzCpCosUserFlowDepTable,
       "hzCpCosUserFlowDepEntry": hzCpCosUserFlowDepEntry,
       "hzCpCosUserFlowIndexDep": hzCpCosUserFlowIndexDep,
       "hzCpCosUserFlowStateDep": hzCpCosUserFlowStateDep,
       "hzCpCosUserClassTable": hzCpCosUserClassTable,
       "hzCpCosUserClassEntry": hzCpCosUserClassEntry,
       "hzCpCosUserClassIndex": hzCpCosUserClassIndex,
       "hzCpCosUserClassOffset": hzCpCosUserClassOffset,
       "hzCpCosUserClassValue": hzCpCosUserClassValue,
       "hzCpCosUserClassMask": hzCpCosUserClassMask,
       "hzCpCosUserFlowFilterTable": hzCpCosUserFlowFilterTable,
       "hzCpCosUserFlowFilterEntry": hzCpCosUserFlowFilterEntry,
       "hzCpCosUserFlowFilterIndex": hzCpCosUserFlowFilterIndex,
       "hzCpCosUserFlowFilter": hzCpCosUserFlowFilter,
       "hzCpCosUserFlowMappingTable": hzCpCosUserFlowMappingTable,
       "hzCpCosUserFlowMappingEntry": hzCpCosUserFlowMappingEntry,
       "hzCpCosUserFlowMappingIndex": hzCpCosUserFlowMappingIndex,
       "hzCpCosUserFlowEnable": hzCpCosUserFlowEnable,
       "hzCpCosUserFlowP1Queue": hzCpCosUserFlowP1Queue,
       "hzCpCosUserFlowP1TargetPort": hzCpCosUserFlowP1TargetPort,
       "hzCpCosUserFlowP2Queue": hzCpCosUserFlowP2Queue,
       "hzCpCosUserFlowP2TargetPort": hzCpCosUserFlowP2TargetPort,
       "hzCpCosUserFlowP3Queue": hzCpCosUserFlowP3Queue,
       "hzCpCosUserFlowP3TargetPort": hzCpCosUserFlowP3TargetPort,
       "hzCpCosUserFlowP4Queue": hzCpCosUserFlowP4Queue,
       "hzCpCosUserFlowP4TargetPort": hzCpCosUserFlowP4TargetPort,
       "hzCpRapidLinkShutdown": hzCpRapidLinkShutdown,
       "hzCpRlsMode": hzCpRlsMode,
       "hzCpRlsLinkControl": hzCpRlsLinkControl,
       "hzCpApplyRlsMonitorParametersToSystem": hzCpApplyRlsMonitorParametersToSystem,
       "hzCpRlsLinkEnable": hzCpRlsLinkEnable,
       "hzCpRlsPortGroup": hzCpRlsPortGroup,
       "hzCpRlsShutdownPolicy": hzCpRlsShutdownPolicy,
       "hzCpRlsSoftFaultMonitorTable": hzCpRlsSoftFaultMonitorTable,
       "hzCpRlsSoftFaultMonitorEntry": hzCpRlsSoftFaultMonitorEntry,
       "hzCpRlsSoftFaultMonitorIndex": hzCpRlsSoftFaultMonitorIndex,
       "hzCpRlsEstablishErredFrameThreshold": hzCpRlsEstablishErredFrameThreshold,
       "hzCpRlsShutdownErredFrameThreshold": hzCpRlsShutdownErredFrameThreshold,
       "hzCpRlsEstablishNumberOfSamples": hzCpRlsEstablishNumberOfSamples,
       "hzCpRlsShutdownNumberOfSamples": hzCpRlsShutdownNumberOfSamples,
       "hzCpRlsEstablishSamplePeriod": hzCpRlsEstablishSamplePeriod,
       "hzCpRlsShutdownSamplePeriod": hzCpRlsShutdownSamplePeriod,
       "hzCpRlsQuickShutdownSamplePeriod": hzCpRlsQuickShutdownSamplePeriod,
       "hzCpRlsHardFaultMonitorTable": hzCpRlsHardFaultMonitorTable,
       "hzCpRlsHardFaultMonitorEntry": hzCpRlsHardFaultMonitorEntry,
       "hzCpRlsHardFaultMonitorIndex": hzCpRlsHardFaultMonitorIndex,
       "hzCpRlsHardFaultSamplePeriod": hzCpRlsHardFaultSamplePeriod,
       "hzCpRlsHardFaultThreshold": hzCpRlsHardFaultThreshold,
       "hzCpRlsReceiveSignalLevelMonitorTable": hzCpRlsReceiveSignalLevelMonitorTable,
       "hzCpRlsReceiveSignalLevelMonitorEntry": hzCpRlsReceiveSignalLevelMonitorEntry,
       "hzCpRlsReceiveSignalLevelMonitorIndex": hzCpRlsReceiveSignalLevelMonitorIndex,
       "hzCpRlsMakeRslMonitorRslValue": hzCpRlsMakeRslMonitorRslValue,
       "hzCpRlsMakeRslMonitorPeriod": hzCpRlsMakeRslMonitorPeriod,
       "hzCpRlsStatusTable": hzCpRlsStatusTable,
       "hzCpRlsStatusEntry": hzCpRlsStatusEntry,
       "hzCpRlsStatusIndex": hzCpRlsStatusIndex,
       "hzCpRlsOption": hzCpRlsOption,
       "hzCpRlsState": hzCpRlsState,
       "hzCpRlsMismatchState": hzCpRlsMismatchState,
       "hzCpRlsDegradeMonitorState": hzCpRlsDegradeMonitorState,
       "hzCpRlsHardFaultMonitorState": hzCpRlsHardFaultMonitorState,
       "hzCpRlsMakeRslThresholdState": hzCpRlsMakeRslThresholdState,
       "hzCpRlsPeerRslState": hzCpRlsPeerRslState,
       "hzCpRlsRadioInterfaceState": hzCpRlsRadioInterfaceState,
       "hzCpRlsNetworkInterfaceState": hzCpRlsNetworkInterfaceState,
       "hzCpRlsUserConfiguredEstablishFer": hzCpRlsUserConfiguredEstablishFer,
       "hzCpRlsMinimumAchievableEstablishFer": hzCpRlsMinimumAchievableEstablishFer,
       "hzCpRlsUserConfiguredShutdownFer": hzCpRlsUserConfiguredShutdownFer,
       "hzCpRlsMinimumAchievableShutdownFer": hzCpRlsMinimumAchievableShutdownFer,
       "hzCpRlsUserConfiguredEstablishMonitorTime": hzCpRlsUserConfiguredEstablishMonitorTime,
       "hzCpRlsActualEstablishMonitorTime": hzCpRlsActualEstablishMonitorTime,
       "hzCpRlsUserConfiguredShutdownMonitorTime": hzCpRlsUserConfiguredShutdownMonitorTime,
       "hzCpRlsActualShutdownMonitorTime": hzCpRlsActualShutdownMonitorTime,
       "hzCpLogs": hzCpLogs,
       "hzCpEventLogEnable": hzCpEventLogEnable,
       "hzCpPerfmLogEnable": hzCpPerfmLogEnable,
       "hzCpPerfmLogInterval": hzCpPerfmLogInterval,
       "hzCpSysLog": hzCpSysLog,
       "hzCpSysLogEnable": hzCpSysLogEnable,
       "hzCpSysLogIpAddressDep": hzCpSysLogIpAddressDep,
       "hzCpSysLogHostDomain": hzCpSysLogHostDomain,
       "hzCpSysLogHostAddress": hzCpSysLogHostAddress,
       "hzCpAtpc": hzCpAtpc,
       "hzCpAtpcEnable": hzCpAtpcEnable,
       "hzCpAtpcStatus": hzCpAtpcStatus,
       "hzCpAtpcCoordinatedPowerDbm": hzCpAtpcCoordinatedPowerDbm,
       "hzCpAtpcCoordinatedPwrEnable": hzCpAtpcCoordinatedPwrEnable,
       "hzCpAtpcMinTxPower": hzCpAtpcMinTxPower,
       "hzCpAtpcMaxTxPower": hzCpAtpcMaxTxPower,
       "hzCpHitlessAam": hzCpHitlessAam,
       "hzCpHitlessAamEnable": hzCpHitlessAamEnable,
       "hzCpHitlessAamManualMode": hzCpHitlessAamManualMode,
       "hzCpHitlessAamWaitToRestore": hzCpHitlessAamWaitToRestore,
       "hzCpHitlessAamOrgSpecEoamMsg": hzCpHitlessAamOrgSpecEoamMsg,
       "hzCpHitlessAamTable": hzCpHitlessAamTable,
       "hzCpHitlessAamEntry": hzCpHitlessAamEntry,
       "hzCpWirelessPortIndex": hzCpWirelessPortIndex,
       "hzCpHitlessAamCurrentMode": hzCpHitlessAamCurrentMode,
       "hzCpHitlessAamModeTable": hzCpHitlessAamModeTable,
       "hzCpHitlessAamModeEntry": hzCpHitlessAamModeEntry,
       "hzCpHitlessAamModeIndex": hzCpHitlessAamModeIndex,
       "hzCpHitlessAammModeName": hzCpHitlessAammModeName,
       "hzCpHitlessAamModeRange": hzCpHitlessAamModeRange,
       "hzCpSnmpNotifications": hzCpSnmpNotifications,
       "hzCpLinkDown": hzCpLinkDown,
       "hzCpLinkUp": hzCpLinkUp,
       "hzCpPeerAuthenticationFailure": hzCpPeerAuthenticationFailure,
       "hzCpPeerAuthenticationFailureCleared": hzCpPeerAuthenticationFailureCleared,
       "hzCpHitlessAamConfigMisMatch": hzCpHitlessAamConfigMisMatch,
       "hzCpHitlessAamConfigMisMatchCleared": hzCpHitlessAamConfigMisMatchCleared,
       "hzCpHitlessAamModulationLowered": hzCpHitlessAamModulationLowered,
       "hzCpHitlessAamModulationLoweredCleared": hzCpHitlessAamModulationLoweredCleared,
       "hzCpHitlessAamModulationChangedEvent": hzCpHitlessAamModulationChangedEvent,
       "hzCpAtpcConfigMismatch": hzCpAtpcConfigMismatch,
       "hzCpAtpcConfigMismatchCleared": hzCpAtpcConfigMismatchCleared,
       "hzCpAtpcAutoDisabled": hzCpAtpcAutoDisabled,
       "hzCpAtpcAutoDisabledCleared": hzCpAtpcAutoDisabledCleared,
       "hzCpNoSntpServersReachable": hzCpNoSntpServersReachable,
       "hzCpNoSntpServersReachableCleared": hzCpNoSntpServersReachableCleared,
       "hzCpFrequencyFileInvalid": hzCpFrequencyFileInvalid,
       "hzCpAggregateDroppedFramesThreshold": hzCpAggregateDroppedFramesThreshold,
       "hzCpAggregateDroppedFramesThresholdCleared": hzCpAggregateDroppedFramesThresholdCleared,
       "hzCpQueueDroppedFramesThreshold": hzCpQueueDroppedFramesThreshold,
       "hzCpQueueDroppedFramesThresholdCleared": hzCpQueueDroppedFramesThresholdCleared,
       "hzCpBwUtilizationThreshold": hzCpBwUtilizationThreshold,
       "hzCpBwUtilizationThresholdCleared": hzCpBwUtilizationThresholdCleared,
       "hzCpQueueDepthThreshold": hzCpQueueDepthThreshold,
       "hzCpQueueDepthThresholdCleared": hzCpQueueDepthThresholdCleared,
       "hzCpRlsConfigMismatch": hzCpRlsConfigMismatch,
       "hzCpRlsConfigMismatchCleared": hzCpRlsConfigMismatchCleared,
       "hzCpRlsShutdownActivated": hzCpRlsShutdownActivated,
       "hzCpRlsShutdownActivatedCleared": hzCpRlsShutdownActivatedCleared,
       "hzCpRlsQueueBasedShutdownActivated": hzCpRlsQueueBasedShutdownActivated,
       "hzCpRlsQueueBasedShutdownActivatedCleared": hzCpRlsQueueBasedShutdownActivatedCleared,
       "hzCpModemRxLossOfSignalLock": hzCpModemRxLossOfSignalLock,
       "hzCpModemRxLossOfSignalLockCleared": hzCpModemRxLossOfSignalLockCleared,
       "hzCpModemSnrBelowThreshold": hzCpModemSnrBelowThreshold,
       "hzCpModemSnrBelowThresholdCleared": hzCpModemSnrBelowThresholdCleared,
       "hzCpModemEqualizerStressThreshold": hzCpModemEqualizerStressThreshold,
       "hzCpModemEqualizerStressThresholdCleared": hzCpModemEqualizerStressThresholdCleared,
       "hzCpRslBelowThreshold": hzCpRslBelowThreshold,
       "hzCpRslBelowThresholdCleared": hzCpRslBelowThresholdCleared,
       "hzCpRadioSynthLostLock": hzCpRadioSynthLostLock,
       "hzCpRadioSynthLostLockCleared": hzCpRadioSynthLostLockCleared,
       "hzCpRadioCalTableNotAvailable": hzCpRadioCalTableNotAvailable,
       "hzCpRadioCalTableNotAvailableCleared": hzCpRadioCalTableNotAvailableCleared,
       "hzCpRadioDrainCurrentOutOfLimit": hzCpRadioDrainCurrentOutOfLimit,
       "hzCpRadioDrainCurrentOutOfLimitCleared": hzCpRadioDrainCurrentOutOfLimitCleared,
       "hzCpRadioPowerAmplifier": hzCpRadioPowerAmplifier,
       "hzCpRadioPowerAmplifierCleared": hzCpRadioPowerAmplifierCleared,
       "hzCpTemperatureOutOfLimit": hzCpTemperatureOutOfLimit,
       "hzCpTemperatureOutOfLimitCleared": hzCpTemperatureOutOfLimitCleared,
       "hzCpRedundancyConfigMismatch": hzCpRedundancyConfigMismatch,
       "hzCpRedundancyConfigMismatchCleared": hzCpRedundancyConfigMismatchCleared,
       "hzCpRedundancyActiveOnSecondary": hzCpRedundancyActiveOnSecondary,
       "hzCpRedundancyActiveOnSecondaryCleared": hzCpRedundancyActiveOnSecondaryCleared,
       "hzCpRedundancyOperatingInForcedSwitch": hzCpRedundancyOperatingInForcedSwitch,
       "hzCpRedundancyOperatingInForcedSwitchCleared": hzCpRedundancyOperatingInForcedSwitchCleared,
       "hzCpRedundancyEnetCrossLink": hzCpRedundancyEnetCrossLink,
       "hzCpRedundancyEnetCrossLinkCleared": hzCpRedundancyEnetCrossLinkCleared,
       "hzCpRedundancyActiveUsingPartnerWLink": hzCpRedundancyActiveUsingPartnerWLink,
       "hzCpRedundancyActiveUsingPartnerWLinkCleared": hzCpRedundancyActiveUsingPartnerWLinkCleared,
       "hzCpRedundancyStandbyWLinkInUse": hzCpRedundancyStandbyWLinkInUse,
       "hzCpRedundancyStandbyWLinkInUseCleared": hzCpRedundancyStandbyWLinkInUseCleared,
       "hzCpRedundancyStandbyOnPrimary": hzCpRedundancyStandbyOnPrimary,
       "hzCpRedundancyStandbyOnPrimaryCleared": hzCpRedundancyStandbyOnPrimaryCleared,
       "hzCpX2DeliveringHalfCapacity": hzCpX2DeliveringHalfCapacity,
       "hzCpX2DeliveringHalfCapacityCleared": hzCpX2DeliveringHalfCapacityCleared,
       "hzCpBncCableSignalNotDetected": hzCpBncCableSignalNotDetected,
       "hzCpBncCableSignalNotDetectedCleared": hzCpBncCableSignalNotDetectedCleared,
       "hzCpEthernetSpeedReduced": hzCpEthernetSpeedReduced,
       "hzCpEthernetSpeedReducedCleared": hzCpEthernetSpeedReducedCleared,
       "hzCpSynceLostLock": hzCpSynceLostLock,
       "hzCpSynceLostLockCleared": hzCpSynceLostLockCleared,
       "hzCpSynceSecondarySourceInUse": hzCpSynceSecondarySourceInUse,
       "hzCpSynceSecondarySourceInUseCleared": hzCpSynceSecondarySourceInUseCleared,
       "hzCpUserSession": hzCpUserSession,
       "hzCpUserSessionCleared": hzCpUserSessionCleared,
       "hzCpInvalidSystemConfig": hzCpInvalidSystemConfig,
       "hzCpInvalidSystemConfigCleared": hzCpInvalidSystemConfigCleared,
       "hzCpMibChangeNotSaved": hzCpMibChangeNotSaved,
       "hzCpMibChangeNotSavedCleared": hzCpMibChangeNotSavedCleared,
       "hzCpTransmitterLossOfSync": hzCpTransmitterLossOfSync,
       "hzCpTransmitterLossOfSyncCleared": hzCpTransmitterLossOfSyncCleared,
       "hzCpRadioLinearityCalError": hzCpRadioLinearityCalError,
       "hzCpRadioLinearityCalErrorCleared": hzCpRadioLinearityCalErrorCleared,
       "hzCpSynceConfigMismatch": hzCpSynceConfigMismatch,
       "hzCpSynceConfigMismatchCleared": hzCpSynceConfigMismatchCleared,
       "hzCpCryptoPowerUpTestsFailed": hzCpCryptoPowerUpTestsFailed,
       "hzCpCryptoConfigMismatch": hzCpCryptoConfigMismatch,
       "hzCpCryptoConfigMismatchCleared": hzCpCryptoConfigMismatchCleared,
       "hzCpSystemTimeChange": hzCpSystemTimeChange,
       "hzCpCodeCheck": hzCpCodeCheck,
       "hzCpConfigChanged": hzCpConfigChanged,
       "hzCpModIdentity": hzCpModIdentity}
)
