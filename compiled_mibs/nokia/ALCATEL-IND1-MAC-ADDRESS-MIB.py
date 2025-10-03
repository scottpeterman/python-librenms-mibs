# SNMP MIB module (ALCATEL-IND1-MAC-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\ALCATEL-IND1-MAC-ADDRESS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:13:45 2025
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

(softentIND1MacAddress,
 sourceLearningTraps) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1MacAddress",
    "sourceLearningTraps")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(dot1qVlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanIndex")

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

alcatelIND1MacAddressMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MacAddressProtocolType(TextualConvention, Integer32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1MacAddressMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1MacAddressMIBObjects = _AlcatelIND1MacAddressMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBObjects.setStatus("current")
_SlMacAddressTable_Object = MibTable
slMacAddressTable = _SlMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    slMacAddressTable.setStatus("current")
_SlMacAddressEntry_Object = MibTableRow
slMacAddressEntry = _SlMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 1, 1)
)
slMacAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddress"),
)
if mibBuilder.loadTexts:
    slMacAddressEntry.setStatus("current")
_SlMacAddress_Type = MacAddress
_SlMacAddress_Object = MibTableColumn
slMacAddress = _SlMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 1, 1, 1),
    _SlMacAddress_Type()
)
slMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacAddress.setStatus("current")


class _SlMacAddressManagement_Type(Integer32):
    """Custom type slMacAddressManagement based on Integer32"""
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
        *(("permanent", 1),
          ("deleteOnReset", 2),
          ("deleteOnTimeout", 3),
          ("learned", 4),
          ("staticMulticast", 5))
    )


_SlMacAddressManagement_Type.__name__ = "Integer32"
_SlMacAddressManagement_Object = MibTableColumn
slMacAddressManagement = _SlMacAddressManagement_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 1, 1, 2),
    _SlMacAddressManagement_Type()
)
slMacAddressManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacAddressManagement.setStatus("current")


class _SlMacAddressDisposition_Type(Integer32):
    """Custom type slMacAddressDisposition based on Integer32"""
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
        *(("bridging", 1),
          ("filtering", 2),
          ("quarantined", 3),
          ("hostIntegrity", 4),
          ("userNetworkProf", 5))
    )


_SlMacAddressDisposition_Type.__name__ = "Integer32"
_SlMacAddressDisposition_Object = MibTableColumn
slMacAddressDisposition = _SlMacAddressDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 1, 1, 3),
    _SlMacAddressDisposition_Type()
)
slMacAddressDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacAddressDisposition.setStatus("current")
_SlMacAddressRowStatus_Type = RowStatus
_SlMacAddressRowStatus_Object = MibTableColumn
slMacAddressRowStatus = _SlMacAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 1, 1, 4),
    _SlMacAddressRowStatus_Type()
)
slMacAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacAddressRowStatus.setStatus("current")
_SlMacAddressProtocol_Type = MacAddressProtocolType
_SlMacAddressProtocol_Object = MibTableColumn
slMacAddressProtocol = _SlMacAddressProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 1, 1, 5),
    _SlMacAddressProtocol_Type()
)
slMacAddressProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slMacAddressProtocol.setStatus("current")
_SlMacAddressAgingTable_Object = MibTable
slMacAddressAgingTable = _SlMacAddressAgingTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    slMacAddressAgingTable.setStatus("current")
_SlMacAddressAgingEntry_Object = MibTableRow
slMacAddressAgingEntry = _SlMacAddressAgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 2, 1)
)
slMacAddressAgingEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    slMacAddressAgingEntry.setStatus("current")


class _SlMacAgingValue_Type(Integer32):
    """Custom type slMacAgingValue based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_SlMacAgingValue_Type.__name__ = "Integer32"
_SlMacAgingValue_Object = MibTableColumn
slMacAgingValue = _SlMacAgingValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 2, 1, 1),
    _SlMacAgingValue_Type()
)
slMacAgingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacAgingValue.setStatus("current")
_SlMacAgingRowStatus_Type = RowStatus
_SlMacAgingRowStatus_Object = MibTableColumn
slMacAgingRowStatus = _SlMacAgingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 2, 1, 2),
    _SlMacAgingRowStatus_Type()
)
slMacAgingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacAgingRowStatus.setStatus("current")
_SlPCamTrapObj_ObjectIdentity = ObjectIdentity
slPCamTrapObj = _SlPCamTrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 3)
)


class _SlPCAMSlotNumber_Type(Integer32):
    """Custom type slPCAMSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SlPCAMSlotNumber_Type.__name__ = "Integer32"
_SlPCAMSlotNumber_Object = MibScalar
slPCAMSlotNumber = _SlPCAMSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 3, 1),
    _SlPCAMSlotNumber_Type()
)
slPCAMSlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slPCAMSlotNumber.setStatus("current")


class _SlPCAMSliceNumber_Type(Integer32):
    """Custom type slPCAMSliceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SlPCAMSliceNumber_Type.__name__ = "Integer32"
_SlPCAMSliceNumber_Object = MibScalar
slPCAMSliceNumber = _SlPCAMSliceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 3, 2),
    _SlPCAMSliceNumber_Type()
)
slPCAMSliceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slPCAMSliceNumber.setStatus("current")


class _SlPCAMStatus_Type(Integer32):
    """Custom type slPCAMStatus based on Integer32"""
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
        *(("lowWaterMark", 1),
          ("highWaterMark", 2),
          ("floodWaterMark", 3),
          ("full", 4))
    )


_SlPCAMStatus_Type.__name__ = "Integer32"
_SlPCAMStatus_Object = MibScalar
slPCAMStatus = _SlPCAMStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 3, 3),
    _SlPCAMStatus_Type()
)
slPCAMStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    slPCAMStatus.setStatus("current")
_SlMacToPortMacTable_Object = MibTable
slMacToPortMacTable = _SlMacToPortMacTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    slMacToPortMacTable.setStatus("current")
_SlMacToPortMacEntry_Object = MibTableRow
slMacToPortMacEntry = _SlMacToPortMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 4, 1)
)
slMacToPortMacEntry.setIndexNames(
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacToPortMacVlanId"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacToPortMacAddress"),
)
if mibBuilder.loadTexts:
    slMacToPortMacEntry.setStatus("current")


class _SlMacToPortMacVlanId_Type(Integer32):
    """Custom type slMacToPortMacVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SlMacToPortMacVlanId_Type.__name__ = "Integer32"
_SlMacToPortMacVlanId_Object = MibTableColumn
slMacToPortMacVlanId = _SlMacToPortMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 4, 1, 1),
    _SlMacToPortMacVlanId_Type()
)
slMacToPortMacVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacToPortMacVlanId.setStatus("current")
_SlMacToPortMacAddress_Type = MacAddress
_SlMacToPortMacAddress_Object = MibTableColumn
slMacToPortMacAddress = _SlMacToPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 4, 1, 2),
    _SlMacToPortMacAddress_Type()
)
slMacToPortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacToPortMacAddress.setStatus("current")
_SlMacToPortMacRowStatus_Type = RowStatus
_SlMacToPortMacRowStatus_Object = MibTableColumn
slMacToPortMacRowStatus = _SlMacToPortMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 4, 1, 3),
    _SlMacToPortMacRowStatus_Type()
)
slMacToPortMacRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacToPortMacRowStatus.setStatus("current")


class _SlDistributedMacMode_Type(Integer32):
    """Custom type slDistributedMacMode based on Integer32"""
    defaultValue = 2

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


_SlDistributedMacMode_Type.__name__ = "Integer32"
_SlDistributedMacMode_Object = MibScalar
slDistributedMacMode = _SlDistributedMacMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 5),
    _SlDistributedMacMode_Type()
)
slDistributedMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slDistributedMacMode.setStatus("current")
_BcmHashCollisionTrapObj_ObjectIdentity = ObjectIdentity
bcmHashCollisionTrapObj = _BcmHashCollisionTrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 6)
)
_BcmHashCollisionMac_Type = MacAddress
_BcmHashCollisionMac_Object = MibScalar
bcmHashCollisionMac = _BcmHashCollisionMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 6, 1),
    _BcmHashCollisionMac_Type()
)
bcmHashCollisionMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcmHashCollisionMac.setStatus("current")
_BcmHashCollisionSlot_Type = Unsigned32
_BcmHashCollisionSlot_Object = MibScalar
bcmHashCollisionSlot = _BcmHashCollisionSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 6, 2),
    _BcmHashCollisionSlot_Type()
)
bcmHashCollisionSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcmHashCollisionSlot.setStatus("current")
_BcmHashCollisionPort_Type = Unsigned32
_BcmHashCollisionPort_Object = MibScalar
bcmHashCollisionPort = _BcmHashCollisionPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 6, 3),
    _BcmHashCollisionPort_Type()
)
bcmHashCollisionPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcmHashCollisionPort.setStatus("current")
_BcmHashCollisionVlan_Type = Unsigned32
_BcmHashCollisionVlan_Object = MibScalar
bcmHashCollisionVlan = _BcmHashCollisionVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 6, 4),
    _BcmHashCollisionVlan_Type()
)
bcmHashCollisionVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcmHashCollisionVlan.setStatus("current")


class _BcmHashCollisionTable_Type(DisplayString):
    """Custom type bcmHashCollisionTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_BcmHashCollisionTable_Type.__name__ = "DisplayString"
_BcmHashCollisionTable_Object = MibScalar
bcmHashCollisionTable = _BcmHashCollisionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 6, 5),
    _BcmHashCollisionTable_Type()
)
bcmHashCollisionTable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcmHashCollisionTable.setStatus("current")
_SlMacLearningControlTable_Object = MibTable
slMacLearningControlTable = _SlMacLearningControlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 7)
)
if mibBuilder.loadTexts:
    slMacLearningControlTable.setStatus("current")
_SlMacLearningControlEntry_Object = MibTableRow
slMacLearningControlEntry = _SlMacLearningControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 7, 1)
)
slMacLearningControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    slMacLearningControlEntry.setStatus("current")


class _SlMacLearningControlStatus_Type(Integer32):
    """Custom type slMacLearningControlStatus based on Integer32"""
    defaultValue = 1

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


_SlMacLearningControlStatus_Type.__name__ = "Integer32"
_SlMacLearningControlStatus_Object = MibTableColumn
slMacLearningControlStatus = _SlMacLearningControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 7, 1, 1),
    _SlMacLearningControlStatus_Type()
)
slMacLearningControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacLearningControlStatus.setStatus("current")
_AlaSlMacAddressGlobalTable_Object = MibTable
alaSlMacAddressGlobalTable = _AlaSlMacAddressGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaSlMacAddressGlobalTable.setStatus("current")
_AlaSlMacAddressGlobalEntry_Object = MibTableRow
alaSlMacAddressGlobalEntry = _AlaSlMacAddressGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1)
)
alaSlMacAddressGlobalEntry.setIndexNames(
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacDomain"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slLocaleType"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slOriginId"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slServiceId"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slSubId"),
    (0, "ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGbl"),
)
if mibBuilder.loadTexts:
    alaSlMacAddressGlobalEntry.setStatus("current")


class _SlMacDomain_Type(Integer32):
    """Custom type slMacDomain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("vlan", 1),
          ("vpls", 2))
    )


_SlMacDomain_Type.__name__ = "Integer32"
_SlMacDomain_Object = MibTableColumn
slMacDomain = _SlMacDomain_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1, 1),
    _SlMacDomain_Type()
)
slMacDomain.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slMacDomain.setStatus("current")


class _SlLocaleType_Type(Integer32):
    """Custom type slLocaleType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("sap", 1),
          ("sBind", 2))
    )


_SlLocaleType_Type.__name__ = "Integer32"
_SlLocaleType_Object = MibTableColumn
slLocaleType = _SlLocaleType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1, 2),
    _SlLocaleType_Type()
)
slLocaleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slLocaleType.setStatus("current")


class _SlOriginId_Type(Integer32):
    """Custom type slOriginId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SlOriginId_Type.__name__ = "Integer32"
_SlOriginId_Object = MibTableColumn
slOriginId = _SlOriginId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1, 3),
    _SlOriginId_Type()
)
slOriginId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slOriginId.setStatus("current")


class _SlServiceId_Type(Integer32):
    """Custom type slServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlServiceId_Type.__name__ = "Integer32"
_SlServiceId_Object = MibTableColumn
slServiceId = _SlServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1, 4),
    _SlServiceId_Type()
)
slServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slServiceId.setStatus("current")


class _SlSubId_Type(Integer32):
    """Custom type slSubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SlSubId_Type.__name__ = "Integer32"
_SlSubId_Object = MibTableColumn
slSubId = _SlSubId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1, 5),
    _SlSubId_Type()
)
slSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slSubId.setStatus("current")
_SlMacAddressGbl_Type = MacAddress
_SlMacAddressGbl_Object = MibTableColumn
slMacAddressGbl = _SlMacAddressGbl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1, 6),
    _SlMacAddressGbl_Type()
)
slMacAddressGbl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slMacAddressGbl.setStatus("current")


class _SlMacAddressGblManagement_Type(Integer32):
    """Custom type slMacAddressGblManagement based on Integer32"""
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
        *(("permanent", 1),
          ("deleteOnReset", 2),
          ("deleteOnTimeout", 3),
          ("learned", 4),
          ("staticMulticast", 5))
    )


_SlMacAddressGblManagement_Type.__name__ = "Integer32"
_SlMacAddressGblManagement_Object = MibTableColumn
slMacAddressGblManagement = _SlMacAddressGblManagement_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1, 7),
    _SlMacAddressGblManagement_Type()
)
slMacAddressGblManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacAddressGblManagement.setStatus("current")


class _SlMacAddressGblDisposition_Type(Integer32):
    """Custom type slMacAddressGblDisposition based on Integer32"""
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
        *(("bridging", 1),
          ("filtering", 2),
          ("quarantined", 3),
          ("hostIntegrity", 4),
          ("userNetworkProf", 5))
    )


_SlMacAddressGblDisposition_Type.__name__ = "Integer32"
_SlMacAddressGblDisposition_Object = MibTableColumn
slMacAddressGblDisposition = _SlMacAddressGblDisposition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1, 8),
    _SlMacAddressGblDisposition_Type()
)
slMacAddressGblDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacAddressGblDisposition.setStatus("current")
_SlMacAddressGblRowStatus_Type = RowStatus
_SlMacAddressGblRowStatus_Object = MibTableColumn
slMacAddressGblRowStatus = _SlMacAddressGblRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1, 9),
    _SlMacAddressGblRowStatus_Type()
)
slMacAddressGblRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slMacAddressGblRowStatus.setStatus("current")
_SlMacAddressGblProtocol_Type = MacAddressProtocolType
_SlMacAddressGblProtocol_Object = MibTableColumn
slMacAddressGblProtocol = _SlMacAddressGblProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 8, 1, 10),
    _SlMacAddressGblProtocol_Type()
)
slMacAddressGblProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slMacAddressGblProtocol.setStatus("current")
_HalHashCollisionTrapObj_ObjectIdentity = ObjectIdentity
halHashCollisionTrapObj = _HalHashCollisionTrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 10)
)
_HalHashCollisionMac_Type = MacAddress
_HalHashCollisionMac_Object = MibScalar
halHashCollisionMac = _HalHashCollisionMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 10, 1),
    _HalHashCollisionMac_Type()
)
halHashCollisionMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    halHashCollisionMac.setStatus("current")
_HalHashCollisionSlot_Type = Unsigned32
_HalHashCollisionSlot_Object = MibScalar
halHashCollisionSlot = _HalHashCollisionSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 10, 2),
    _HalHashCollisionSlot_Type()
)
halHashCollisionSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    halHashCollisionSlot.setStatus("current")
_HalHashCollisionPort_Type = Unsigned32
_HalHashCollisionPort_Object = MibScalar
halHashCollisionPort = _HalHashCollisionPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 10, 3),
    _HalHashCollisionPort_Type()
)
halHashCollisionPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    halHashCollisionPort.setStatus("current")
_HalHashCollisionVlan_Type = Unsigned32
_HalHashCollisionVlan_Object = MibScalar
halHashCollisionVlan = _HalHashCollisionVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 10, 4),
    _HalHashCollisionVlan_Type()
)
halHashCollisionVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    halHashCollisionVlan.setStatus("current")


class _HalHashCollisionTable_Type(DisplayString):
    """Custom type halHashCollisionTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HalHashCollisionTable_Type.__name__ = "DisplayString"
_HalHashCollisionTable_Object = MibScalar
halHashCollisionTable = _HalHashCollisionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 1, 10, 5),
    _HalHashCollisionTable_Type()
)
halHashCollisionTable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    halHashCollisionTable.setStatus("current")
_AlcatelIND1MacAddressMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1MacAddressMIBConformance = _AlcatelIND1MacAddressMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBConformance.setStatus("current")
_AlcatelIND1MacAddressMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1MacAddressMIBGroups = _AlcatelIND1MacAddressMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBGroups.setStatus("current")
_AlcatelIND1MacAddressMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1MacAddressMIBCompliances = _AlcatelIND1MacAddressMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBCompliances.setStatus("current")

# Managed Objects groups

slMacAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 2, 1, 1)
)
slMacAddressGroup.setObjects(
      *(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddress"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressManagement"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressDisposition"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressRowStatus"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressProtocol"))
)
if mibBuilder.loadTexts:
    slMacAddressGroup.setStatus("current")

slMacAgingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 2, 1, 2)
)
slMacAgingGroup.setObjects(
      *(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAgingValue"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAgingRowStatus"))
)
if mibBuilder.loadTexts:
    slMacAgingGroup.setStatus("current")

slMacGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 2, 1, 4)
)
slMacGeneralGroup.setObjects(
    ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slDistributedMacMode")
)
if mibBuilder.loadTexts:
    slMacGeneralGroup.setStatus("current")

slMacLearningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 2, 1, 5)
)
slMacLearningGroup.setObjects(
    ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacLearningControlStatus")
)
if mibBuilder.loadTexts:
    slMacLearningGroup.setStatus("current")


# Notification objects

slPCAMStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 9, 0, 1)
)
slPCAMStatusTrap.setObjects(
      *(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slPCAMSlotNumber"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slPCAMSliceNumber"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slPCAMStatus"))
)
if mibBuilder.loadTexts:
    slPCAMStatusTrap.setStatus(
        "current"
    )

bcmHashCollisionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 9, 0, 3)
)
bcmHashCollisionTrap.setObjects(
      *(("ALCATEL-IND1-MAC-ADDRESS-MIB", "bcmHashCollisionMac"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "bcmHashCollisionSlot"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "bcmHashCollisionPort"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "bcmHashCollisionVlan"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "bcmHashCollisionTable"))
)
if mibBuilder.loadTexts:
    bcmHashCollisionTrap.setStatus(
        "current"
    )

halHashCollisionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 9, 0, 4)
)
halHashCollisionTrap.setObjects(
      *(("ALCATEL-IND1-MAC-ADDRESS-MIB", "halHashCollisionMac"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "halHashCollisionSlot"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "halHashCollisionPort"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "halHashCollisionVlan"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "halHashCollisionTable"))
)
if mibBuilder.loadTexts:
    halHashCollisionTrap.setStatus(
        "current"
    )


# Notifications groups

slPCamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 2, 1, 3)
)
slPCamNotificationGroup.setObjects(
    ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slPCAMStatusTrap")
)
if mibBuilder.loadTexts:
    slPCamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1MacAddressMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 8, 1, 2, 2, 1)
)
alcatelIND1MacAddressMIBCompliance.setObjects(
      *(("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAddressGroup"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacAgingGroup"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slPCamNotificationGroup"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacGeneralGroup"),
        ("ALCATEL-IND1-MAC-ADDRESS-MIB", "slMacLearningGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1MacAddressMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-MAC-ADDRESS-MIB",
    **{"MacAddressProtocolType": MacAddressProtocolType,
       "alcatelIND1MacAddressMIB": alcatelIND1MacAddressMIB,
       "alcatelIND1MacAddressMIBObjects": alcatelIND1MacAddressMIBObjects,
       "slMacAddressTable": slMacAddressTable,
       "slMacAddressEntry": slMacAddressEntry,
       "slMacAddress": slMacAddress,
       "slMacAddressManagement": slMacAddressManagement,
       "slMacAddressDisposition": slMacAddressDisposition,
       "slMacAddressRowStatus": slMacAddressRowStatus,
       "slMacAddressProtocol": slMacAddressProtocol,
       "slMacAddressAgingTable": slMacAddressAgingTable,
       "slMacAddressAgingEntry": slMacAddressAgingEntry,
       "slMacAgingValue": slMacAgingValue,
       "slMacAgingRowStatus": slMacAgingRowStatus,
       "slPCamTrapObj": slPCamTrapObj,
       "slPCAMSlotNumber": slPCAMSlotNumber,
       "slPCAMSliceNumber": slPCAMSliceNumber,
       "slPCAMStatus": slPCAMStatus,
       "slMacToPortMacTable": slMacToPortMacTable,
       "slMacToPortMacEntry": slMacToPortMacEntry,
       "slMacToPortMacVlanId": slMacToPortMacVlanId,
       "slMacToPortMacAddress": slMacToPortMacAddress,
       "slMacToPortMacRowStatus": slMacToPortMacRowStatus,
       "slDistributedMacMode": slDistributedMacMode,
       "bcmHashCollisionTrapObj": bcmHashCollisionTrapObj,
       "bcmHashCollisionMac": bcmHashCollisionMac,
       "bcmHashCollisionSlot": bcmHashCollisionSlot,
       "bcmHashCollisionPort": bcmHashCollisionPort,
       "bcmHashCollisionVlan": bcmHashCollisionVlan,
       "bcmHashCollisionTable": bcmHashCollisionTable,
       "slMacLearningControlTable": slMacLearningControlTable,
       "slMacLearningControlEntry": slMacLearningControlEntry,
       "slMacLearningControlStatus": slMacLearningControlStatus,
       "alaSlMacAddressGlobalTable": alaSlMacAddressGlobalTable,
       "alaSlMacAddressGlobalEntry": alaSlMacAddressGlobalEntry,
       "slMacDomain": slMacDomain,
       "slLocaleType": slLocaleType,
       "slOriginId": slOriginId,
       "slServiceId": slServiceId,
       "slSubId": slSubId,
       "slMacAddressGbl": slMacAddressGbl,
       "slMacAddressGblManagement": slMacAddressGblManagement,
       "slMacAddressGblDisposition": slMacAddressGblDisposition,
       "slMacAddressGblRowStatus": slMacAddressGblRowStatus,
       "slMacAddressGblProtocol": slMacAddressGblProtocol,
       "halHashCollisionTrapObj": halHashCollisionTrapObj,
       "halHashCollisionMac": halHashCollisionMac,
       "halHashCollisionSlot": halHashCollisionSlot,
       "halHashCollisionPort": halHashCollisionPort,
       "halHashCollisionVlan": halHashCollisionVlan,
       "halHashCollisionTable": halHashCollisionTable,
       "alcatelIND1MacAddressMIBConformance": alcatelIND1MacAddressMIBConformance,
       "alcatelIND1MacAddressMIBGroups": alcatelIND1MacAddressMIBGroups,
       "slMacAddressGroup": slMacAddressGroup,
       "slMacAgingGroup": slMacAgingGroup,
       "slPCamNotificationGroup": slPCamNotificationGroup,
       "slMacGeneralGroup": slMacGeneralGroup,
       "slMacLearningGroup": slMacLearningGroup,
       "alcatelIND1MacAddressMIBCompliances": alcatelIND1MacAddressMIBCompliances,
       "alcatelIND1MacAddressMIBCompliance": alcatelIND1MacAddressMIBCompliance,
       "slPCAMStatusTrap": slPCAMStatusTrap,
       "bcmHashCollisionTrap": bcmHashCollisionTrap,
       "halHashCollisionTrap": halHashCollisionTrap}
)
