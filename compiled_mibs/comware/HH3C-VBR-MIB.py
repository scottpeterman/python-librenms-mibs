# SNMP MIB module (HH3C-VBR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-VBR-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:13 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cVbr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180)
)
if mibBuilder.loadTexts:
    hh3cVbr.setRevisions(
        ("2018-07-11 11:29",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVbrSpecInfo_ObjectIdentity = ObjectIdentity
hh3cVbrSpecInfo = _Hh3cVbrSpecInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 1)
)
_Hh3cVbrGroupMinId_Type = Integer32
_Hh3cVbrGroupMinId_Object = MibScalar
hh3cVbrGroupMinId = _Hh3cVbrGroupMinId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 1, 1),
    _Hh3cVbrGroupMinId_Type()
)
hh3cVbrGroupMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrGroupMinId.setStatus("current")
_Hh3cVbrGroupMaxId_Type = Integer32
_Hh3cVbrGroupMaxId_Object = MibScalar
hh3cVbrGroupMaxId = _Hh3cVbrGroupMaxId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 1, 2),
    _Hh3cVbrGroupMaxId_Type()
)
hh3cVbrGroupMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrGroupMaxId.setStatus("current")
_Hh3cVbrMinAssociateId_Type = Integer32
_Hh3cVbrMinAssociateId_Object = MibScalar
hh3cVbrMinAssociateId = _Hh3cVbrMinAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 1, 3),
    _Hh3cVbrMinAssociateId_Type()
)
hh3cVbrMinAssociateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrMinAssociateId.setStatus("current")
_Hh3cVbrMaxAssociateId_Type = Integer32
_Hh3cVbrMaxAssociateId_Object = MibScalar
hh3cVbrMaxAssociateId = _Hh3cVbrMaxAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 1, 4),
    _Hh3cVbrMaxAssociateId_Type()
)
hh3cVbrMaxAssociateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrMaxAssociateId.setStatus("current")
_Hh3cVbrTable_ObjectIdentity = ObjectIdentity
hh3cVbrTable = _Hh3cVbrTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2)
)
_Hh3cVbrGroupTable_Object = MibTable
hh3cVbrGroupTable = _Hh3cVbrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cVbrGroupTable.setStatus("current")
_Hh3cVbrGroupEntry_Object = MibTableRow
hh3cVbrGroupEntry = _Hh3cVbrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 1, 1)
)
hh3cVbrGroupEntry.setIndexNames(
    (0, "HH3C-VBR-MIB", "hh3cVbrGroupId"),
)
if mibBuilder.loadTexts:
    hh3cVbrGroupEntry.setStatus("current")


class _Hh3cVbrGroupId_Type(Integer32):
    """Custom type hh3cVbrGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cVbrGroupId_Type.__name__ = "Integer32"
_Hh3cVbrGroupId_Object = MibTableColumn
hh3cVbrGroupId = _Hh3cVbrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 1, 1, 1),
    _Hh3cVbrGroupId_Type()
)
hh3cVbrGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrGroupId.setStatus("current")


class _Hh3cVbrGroupDescr_Type(DisplayString):
    """Custom type hh3cVbrGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_Hh3cVbrGroupDescr_Type.__name__ = "DisplayString"
_Hh3cVbrGroupDescr_Object = MibTableColumn
hh3cVbrGroupDescr = _Hh3cVbrGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 1, 1, 2),
    _Hh3cVbrGroupDescr_Type()
)
hh3cVbrGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVbrGroupDescr.setStatus("current")
_Hh3cVbrGroupRowStatus_Type = RowStatus
_Hh3cVbrGroupRowStatus_Object = MibTableColumn
hh3cVbrGroupRowStatus = _Hh3cVbrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 1, 1, 3),
    _Hh3cVbrGroupRowStatus_Type()
)
hh3cVbrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVbrGroupRowStatus.setStatus("current")
_Hh3cVbrCasPortTable_Object = MibTable
hh3cVbrCasPortTable = _Hh3cVbrCasPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cVbrCasPortTable.setStatus("current")
_Hh3cVbrCasPortEntry_Object = MibTableRow
hh3cVbrCasPortEntry = _Hh3cVbrCasPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1)
)
hh3cVbrCasPortEntry.setIndexNames(
    (0, "HH3C-VBR-MIB", "hh3cVbrCasPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cVbrCasPortEntry.setStatus("current")


class _Hh3cVbrCasPortIndex_Type(Integer32):
    """Custom type hh3cVbrCasPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cVbrCasPortIndex_Type.__name__ = "Integer32"
_Hh3cVbrCasPortIndex_Object = MibTableColumn
hh3cVbrCasPortIndex = _Hh3cVbrCasPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1, 1),
    _Hh3cVbrCasPortIndex_Type()
)
hh3cVbrCasPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVbrCasPortIndex.setStatus("current")


class _Hh3cVbrCasPortAssociateId_Type(Integer32):
    """Custom type hh3cVbrCasPortAssociateId based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVbrCasPortAssociateId_Type.__name__ = "Integer32"
_Hh3cVbrCasPortAssociateId_Object = MibTableColumn
hh3cVbrCasPortAssociateId = _Hh3cVbrCasPortAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1, 2),
    _Hh3cVbrCasPortAssociateId_Type()
)
hh3cVbrCasPortAssociateId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVbrCasPortAssociateId.setStatus("current")


class _Hh3cVbrCasPortGroupID_Type(Integer32):
    """Custom type hh3cVbrCasPortGroupID based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cVbrCasPortGroupID_Type.__name__ = "Integer32"
_Hh3cVbrCasPortGroupID_Object = MibTableColumn
hh3cVbrCasPortGroupID = _Hh3cVbrCasPortGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1, 3),
    _Hh3cVbrCasPortGroupID_Type()
)
hh3cVbrCasPortGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVbrCasPortGroupID.setStatus("current")


class _Hh3cVbrPEXStatus_Type(Integer32):
    """Custom type hh3cVbrPEXStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_Hh3cVbrPEXStatus_Type.__name__ = "Integer32"
_Hh3cVbrPEXStatus_Object = MibTableColumn
hh3cVbrPEXStatus = _Hh3cVbrPEXStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1, 4),
    _Hh3cVbrPEXStatus_Type()
)
hh3cVbrPEXStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrPEXStatus.setStatus("current")


class _Hh3cVbrPEXTier_Type(Integer32):
    """Custom type hh3cVbrPEXTier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVbrPEXTier_Type.__name__ = "Integer32"
_Hh3cVbrPEXTier_Object = MibTableColumn
hh3cVbrPEXTier = _Hh3cVbrPEXTier_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1, 5),
    _Hh3cVbrPEXTier_Type()
)
hh3cVbrPEXTier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrPEXTier.setStatus("current")


class _Hh3cVbrPEXDeviceMac_Type(DisplayString):
    """Custom type hh3cVbrPEXDeviceMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cVbrPEXDeviceMac_Type.__name__ = "DisplayString"
_Hh3cVbrPEXDeviceMac_Object = MibTableColumn
hh3cVbrPEXDeviceMac = _Hh3cVbrPEXDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1, 6),
    _Hh3cVbrPEXDeviceMac_Type()
)
hh3cVbrPEXDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrPEXDeviceMac.setStatus("current")


class _Hh3cVbrPEXSysname_Type(DisplayString):
    """Custom type hh3cVbrPEXSysname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cVbrPEXSysname_Type.__name__ = "DisplayString"
_Hh3cVbrPEXSysname_Object = MibTableColumn
hh3cVbrPEXSysname = _Hh3cVbrPEXSysname_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1, 7),
    _Hh3cVbrPEXSysname_Type()
)
hh3cVbrPEXSysname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrPEXSysname.setStatus("current")


class _Hh3cVbrPEXBoardType_Type(DisplayString):
    """Custom type hh3cVbrPEXBoardType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cVbrPEXBoardType_Type.__name__ = "DisplayString"
_Hh3cVbrPEXBoardType_Object = MibTableColumn
hh3cVbrPEXBoardType = _Hh3cVbrPEXBoardType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1, 8),
    _Hh3cVbrPEXBoardType_Type()
)
hh3cVbrPEXBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrPEXBoardType.setStatus("current")


class _Hh3cVbrPEXParent_Type(Integer32):
    """Custom type hh3cVbrPEXParent based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVbrPEXParent_Type.__name__ = "Integer32"
_Hh3cVbrPEXParent_Object = MibTableColumn
hh3cVbrPEXParent = _Hh3cVbrPEXParent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1, 9),
    _Hh3cVbrPEXParent_Type()
)
hh3cVbrPEXParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrPEXParent.setStatus("current")
_Hh3cVbrCasPortRowStatus_Type = RowStatus
_Hh3cVbrCasPortRowStatus_Object = MibTableColumn
hh3cVbrCasPortRowStatus = _Hh3cVbrCasPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 2, 1, 10),
    _Hh3cVbrCasPortRowStatus_Type()
)
hh3cVbrCasPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVbrCasPortRowStatus.setStatus("current")
_Hh3cVbrUpgradeTable_Object = MibTable
hh3cVbrUpgradeTable = _Hh3cVbrUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cVbrUpgradeTable.setStatus("current")
_Hh3cVbrUpgradeEntry_Object = MibTableRow
hh3cVbrUpgradeEntry = _Hh3cVbrUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 3, 1)
)
hh3cVbrUpgradeEntry.setIndexNames(
    (0, "HH3C-VBR-MIB", "hh3cVbrUpgradeAssociateId"),
)
if mibBuilder.loadTexts:
    hh3cVbrUpgradeEntry.setStatus("current")


class _Hh3cVbrUpgradeAssociateId_Type(Integer32):
    """Custom type hh3cVbrUpgradeAssociateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVbrUpgradeAssociateId_Type.__name__ = "Integer32"
_Hh3cVbrUpgradeAssociateId_Object = MibTableColumn
hh3cVbrUpgradeAssociateId = _Hh3cVbrUpgradeAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 3, 1, 1),
    _Hh3cVbrUpgradeAssociateId_Type()
)
hh3cVbrUpgradeAssociateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVbrUpgradeAssociateId.setStatus("current")


class _Hh3cVbrUpgradeIPEFile_Type(DisplayString):
    """Custom type hh3cVbrUpgradeIPEFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cVbrUpgradeIPEFile_Type.__name__ = "DisplayString"
_Hh3cVbrUpgradeIPEFile_Object = MibTableColumn
hh3cVbrUpgradeIPEFile = _Hh3cVbrUpgradeIPEFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 3, 1, 2),
    _Hh3cVbrUpgradeIPEFile_Type()
)
hh3cVbrUpgradeIPEFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVbrUpgradeIPEFile.setStatus("current")


class _Hh3cVbrUpgradePatchFile_Type(DisplayString):
    """Custom type hh3cVbrUpgradePatchFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cVbrUpgradePatchFile_Type.__name__ = "DisplayString"
_Hh3cVbrUpgradePatchFile_Object = MibTableColumn
hh3cVbrUpgradePatchFile = _Hh3cVbrUpgradePatchFile_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 3, 1, 3),
    _Hh3cVbrUpgradePatchFile_Type()
)
hh3cVbrUpgradePatchFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVbrUpgradePatchFile.setStatus("current")


class _Hh3cVbrUpgradePatchAction_Type(Integer32):
    """Custom type hh3cVbrUpgradePatchAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Hh3cVbrUpgradePatchAction_Type.__name__ = "Integer32"
_Hh3cVbrUpgradePatchAction_Object = MibTableColumn
hh3cVbrUpgradePatchAction = _Hh3cVbrUpgradePatchAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 3, 1, 4),
    _Hh3cVbrUpgradePatchAction_Type()
)
hh3cVbrUpgradePatchAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVbrUpgradePatchAction.setStatus("current")


class _Hh3cVbrUpgradeStatus_Type(Integer32):
    """Custom type hh3cVbrUpgradeStatus based on Integer32"""
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
        *(("initial", 1),
          ("downloading", 2),
          ("upgrading", 3),
          ("succeeded", 4),
          ("failed", 5))
    )


_Hh3cVbrUpgradeStatus_Type.__name__ = "Integer32"
_Hh3cVbrUpgradeStatus_Object = MibTableColumn
hh3cVbrUpgradeStatus = _Hh3cVbrUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 3, 1, 5),
    _Hh3cVbrUpgradeStatus_Type()
)
hh3cVbrUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVbrUpgradeStatus.setStatus("current")


class _Hh3cVbrInitUpgradeStatus_Type(TruthValue):
    """Custom type hh3cVbrInitUpgradeStatus based on TruthValue"""
    defaultValue = 2


_Hh3cVbrInitUpgradeStatus_Type.__name__ = "TruthValue"
_Hh3cVbrInitUpgradeStatus_Object = MibTableColumn
hh3cVbrInitUpgradeStatus = _Hh3cVbrInitUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 2, 3, 1, 6),
    _Hh3cVbrInitUpgradeStatus_Type()
)
hh3cVbrInitUpgradeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVbrInitUpgradeStatus.setStatus("current")
_Hh3cVbrTraps_ObjectIdentity = ObjectIdentity
hh3cVbrTraps = _Hh3cVbrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 3)
)
_Hh3cVbrTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cVbrTrapPrefix = _Hh3cVbrTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cVbrPEXRemoveOrInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 180, 3, 0, 1)
)
hh3cVbrPEXRemoveOrInsert.setObjects(
      *(("HH3C-VBR-MIB", "hh3cVbrCasPortIndex"),
        ("HH3C-VBR-MIB", "hh3cVbrCasPortAssociateId"),
        ("HH3C-VBR-MIB", "hh3cVbrPEXStatus"))
)
if mibBuilder.loadTexts:
    hh3cVbrPEXRemoveOrInsert.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VBR-MIB",
    **{"hh3cVbr": hh3cVbr,
       "hh3cVbrSpecInfo": hh3cVbrSpecInfo,
       "hh3cVbrGroupMinId": hh3cVbrGroupMinId,
       "hh3cVbrGroupMaxId": hh3cVbrGroupMaxId,
       "hh3cVbrMinAssociateId": hh3cVbrMinAssociateId,
       "hh3cVbrMaxAssociateId": hh3cVbrMaxAssociateId,
       "hh3cVbrTable": hh3cVbrTable,
       "hh3cVbrGroupTable": hh3cVbrGroupTable,
       "hh3cVbrGroupEntry": hh3cVbrGroupEntry,
       "hh3cVbrGroupId": hh3cVbrGroupId,
       "hh3cVbrGroupDescr": hh3cVbrGroupDescr,
       "hh3cVbrGroupRowStatus": hh3cVbrGroupRowStatus,
       "hh3cVbrCasPortTable": hh3cVbrCasPortTable,
       "hh3cVbrCasPortEntry": hh3cVbrCasPortEntry,
       "hh3cVbrCasPortIndex": hh3cVbrCasPortIndex,
       "hh3cVbrCasPortAssociateId": hh3cVbrCasPortAssociateId,
       "hh3cVbrCasPortGroupID": hh3cVbrCasPortGroupID,
       "hh3cVbrPEXStatus": hh3cVbrPEXStatus,
       "hh3cVbrPEXTier": hh3cVbrPEXTier,
       "hh3cVbrPEXDeviceMac": hh3cVbrPEXDeviceMac,
       "hh3cVbrPEXSysname": hh3cVbrPEXSysname,
       "hh3cVbrPEXBoardType": hh3cVbrPEXBoardType,
       "hh3cVbrPEXParent": hh3cVbrPEXParent,
       "hh3cVbrCasPortRowStatus": hh3cVbrCasPortRowStatus,
       "hh3cVbrUpgradeTable": hh3cVbrUpgradeTable,
       "hh3cVbrUpgradeEntry": hh3cVbrUpgradeEntry,
       "hh3cVbrUpgradeAssociateId": hh3cVbrUpgradeAssociateId,
       "hh3cVbrUpgradeIPEFile": hh3cVbrUpgradeIPEFile,
       "hh3cVbrUpgradePatchFile": hh3cVbrUpgradePatchFile,
       "hh3cVbrUpgradePatchAction": hh3cVbrUpgradePatchAction,
       "hh3cVbrUpgradeStatus": hh3cVbrUpgradeStatus,
       "hh3cVbrInitUpgradeStatus": hh3cVbrInitUpgradeStatus,
       "hh3cVbrTraps": hh3cVbrTraps,
       "hh3cVbrTrapPrefix": hh3cVbrTrapPrefix,
       "hh3cVbrPEXRemoveOrInsert": hh3cVbrPEXRemoveOrInsert}
)
