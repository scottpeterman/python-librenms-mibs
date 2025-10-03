# SNMP MIB module (ARICENT-CFA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cambium\cnmatrix\ARICENT-CFA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:23:33 2025
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

(InterfaceIndex,
 ifEntry,
 ifIndex,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifEntry",
    "ifIndex",
    "ifType")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fscfa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 27)
)
if mibBuilder.loadTexts:
    fscfa.setRevisions(
        ("2021-06-11 00:00",
         "2020-05-24 00:00",
         "2019-08-26 00:00",
         "2012-09-05 00:00",
         "1999-12-17 13:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

__pysmi_if_ObjectIdentity = ObjectIdentity
_pysmi_if = __pysmi_if_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1)
)
_IfMaxInterfaces_Type = InterfaceIndex
_IfMaxInterfaces_Object = MibScalar
ifMaxInterfaces = _IfMaxInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 1),
    _IfMaxInterfaces_Type()
)
ifMaxInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMaxInterfaces.setStatus("deprecated")
_IfMaxPhysInterfaces_Type = InterfaceIndex
_IfMaxPhysInterfaces_Object = MibScalar
ifMaxPhysInterfaces = _IfMaxPhysInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 2),
    _IfMaxPhysInterfaces_Type()
)
ifMaxPhysInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMaxPhysInterfaces.setStatus("deprecated")
_IfAvailableIndex_Type = InterfaceIndex
_IfAvailableIndex_Object = MibScalar
ifAvailableIndex = _IfAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 3),
    _IfAvailableIndex_Type()
)
ifAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAvailableIndex.setStatus("current")
_IfMainTable_Object = MibTable
ifMainTable = _IfMainTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4)
)
if mibBuilder.loadTexts:
    ifMainTable.setStatus("current")
_IfMainEntry_Object = MibTableRow
ifMainEntry = _IfMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1)
)
ifMainEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifMainEntry.setStatus("current")
_IfMainIndex_Type = InterfaceIndex
_IfMainIndex_Object = MibTableColumn
ifMainIndex = _IfMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 1),
    _IfMainIndex_Type()
)
ifMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainIndex.setStatus("current")


class _IfMainType_Type(Integer32):
    """Custom type ifMainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              9,
              23,
              24,
              32,
              38,
              49,
              53,
              84,
              92,
              108,
              114,
              118,
              131,
              134,
              136,
              150,
              161,
              166,
              200,
              209,
              246,
              247,
              248)
        )
    )
    namedValues = NamedValues(
        *(("rfc877x25", 5),
          ("ethernetCsmacd", 6),
          ("iso88025TokenRing", 9),
          ("ppp", 23),
          ("softwareLoopback", 24),
          ("frameRelay", 32),
          ("miox25", 38),
          ("aal5", 49),
          ("propVirtual", 53),
          ("async", 84),
          ("frameRelayMPI", 92),
          ("pppMultilinkBundle", 108),
          ("ipOverAtm", 114),
          ("hdlc", 118),
          ("tunnel", 131),
          ("atmSubInterface", 134),
          ("l3ipvlan", 136),
          ("mplsTunnel", 150),
          ("ieee8023ad", 161),
          ("mpls", 166),
          ("teLink", 200),
          ("brgPort", 209),
          ("ifPwType", 246),
          ("ilan", 247),
          ("pip", 248))
    )


_IfMainType_Type.__name__ = "Integer32"
_IfMainType_Object = MibTableColumn
ifMainType = _IfMainType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 2),
    _IfMainType_Type()
)
ifMainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainType.setStatus("current")
_IfMainMtu_Type = Integer32
_IfMainMtu_Object = MibTableColumn
ifMainMtu = _IfMainMtu_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 3),
    _IfMainMtu_Type()
)
ifMainMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainMtu.setStatus("current")


class _IfMainAdminStatus_Type(Integer32):
    """Custom type ifMainAdminStatus based on Integer32"""
    defaultValue = 2

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
          ("loopback", 4))
    )


_IfMainAdminStatus_Type.__name__ = "Integer32"
_IfMainAdminStatus_Object = MibTableColumn
ifMainAdminStatus = _IfMainAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 4),
    _IfMainAdminStatus_Type()
)
ifMainAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainAdminStatus.setStatus("current")


class _IfMainOperStatus_Type(Integer32):
    """Custom type ifMainOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_IfMainOperStatus_Type.__name__ = "Integer32"
_IfMainOperStatus_Object = MibTableColumn
ifMainOperStatus = _IfMainOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 5),
    _IfMainOperStatus_Type()
)
ifMainOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainOperStatus.setStatus("current")


class _IfMainEncapType_Type(Integer32):
    """Custom type ifMainEncapType based on Integer32"""
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
        *(("other", 1),
          ("nlpid", 2),
          ("nlpidSnap", 3),
          ("cudNlpid", 4),
          ("cudNlpidSnap", 5),
          ("llcSnap", 6),
          ("vcMultiplexed", 7),
          ("ethernetV2", 8))
    )


_IfMainEncapType_Type.__name__ = "Integer32"
_IfMainEncapType_Object = MibTableColumn
ifMainEncapType = _IfMainEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 6),
    _IfMainEncapType_Type()
)
ifMainEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainEncapType.setStatus("current")


class _IfMainBrgPortType_Type(Integer32):
    """Custom type ifMainBrgPortType based on Integer32"""
    defaultValue = 8

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
              14)
        )
    )
    namedValues = NamedValues(
        *(("providerNetworkPort", 1),
          ("customerNetworkPortPortBased", 2),
          ("customerNetworkPortStagged", 3),
          ("customerEdgePort", 4),
          ("propCustomerEdgePort", 5),
          ("propCustomerNetworkPort", 6),
          ("propProviderNetworkPort", 7),
          ("customerBridgePort", 8),
          ("customerNetworkPortCtagged", 9),
          ("virtualInstancePort", 10),
          ("providerInstancePort", 11),
          ("customerBackbonePort", 12),
          ("uplinkAccessPort", 13),
          ("stationFacingBridgePort", 14))
    )


_IfMainBrgPortType_Type.__name__ = "Integer32"
_IfMainBrgPortType_Object = MibTableColumn
ifMainBrgPortType = _IfMainBrgPortType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 7),
    _IfMainBrgPortType_Type()
)
ifMainBrgPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainBrgPortType.setStatus("current")
_IfMainRowStatus_Type = RowStatus
_IfMainRowStatus_Object = MibTableColumn
ifMainRowStatus = _IfMainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 8),
    _IfMainRowStatus_Type()
)
ifMainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainRowStatus.setStatus("current")


class _IfMainSubType_Type(Integer32):
    """Custom type ifMainSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(251,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("extremeEther", 251),
          ("fastEther", 252),
          ("gigabitEthernet", 253),
          ("xlEthernet", 254),
          ("notApplicable", 255))
    )


_IfMainSubType_Type.__name__ = "Integer32"
_IfMainSubType_Object = MibTableColumn
ifMainSubType = _IfMainSubType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 9),
    _IfMainSubType_Type()
)
ifMainSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainSubType.setStatus("current")


class _IfMainNetworkType_Type(Integer32):
    """Custom type ifMainNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lan", 1),
          ("wan", 2))
    )


_IfMainNetworkType_Type.__name__ = "Integer32"
_IfMainNetworkType_Object = MibTableColumn
ifMainNetworkType = _IfMainNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 10),
    _IfMainNetworkType_Type()
)
ifMainNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainNetworkType.setStatus("current")


class _IfMainWanType_Type(Integer32):
    """Custom type ifMainWanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("private", 1),
          ("public", 2))
    )


_IfMainWanType_Type.__name__ = "Integer32"
_IfMainWanType_Object = MibTableColumn
ifMainWanType = _IfMainWanType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 11),
    _IfMainWanType_Type()
)
ifMainWanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainWanType.setStatus("current")
_IfMainDesc_Type = DisplayString
_IfMainDesc_Object = MibTableColumn
ifMainDesc = _IfMainDesc_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 12),
    _IfMainDesc_Type()
)
ifMainDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainDesc.setStatus("current")


class _IfMainStorageType_Type(StorageType):
    """Custom type ifMainStorageType based on StorageType"""
    defaultValue = 3


_IfMainStorageType_Type.__name__ = "StorageType"
_IfMainStorageType_Object = MibTableColumn
ifMainStorageType = _IfMainStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 13),
    _IfMainStorageType_Type()
)
ifMainStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainStorageType.setStatus("current")


class _IfMainExtSubType_Type(Integer32):
    """Custom type ifMainExtSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sisp", 0),
          ("attachmentCircuit", 1),
          ("openflow", 2))
    )


_IfMainExtSubType_Type.__name__ = "Integer32"
_IfMainExtSubType_Object = MibTableColumn
ifMainExtSubType = _IfMainExtSubType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 14),
    _IfMainExtSubType_Type()
)
ifMainExtSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainExtSubType.setStatus("current")


class _IfMainPortRole_Type(Integer32):
    """Custom type ifMainPortRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uplink", 1),
          ("downlink", 2))
    )


_IfMainPortRole_Type.__name__ = "Integer32"
_IfMainPortRole_Object = MibTableColumn
ifMainPortRole = _IfMainPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 15),
    _IfMainPortRole_Type()
)
ifMainPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainPortRole.setStatus("current")


class _IfMainUfdOperStatus_Type(Integer32):
    """Custom type ifMainUfdOperStatus based on Integer32"""
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
          ("ufdErrorDisabled", 3))
    )


_IfMainUfdOperStatus_Type.__name__ = "Integer32"
_IfMainUfdOperStatus_Object = MibTableColumn
ifMainUfdOperStatus = _IfMainUfdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 16),
    _IfMainUfdOperStatus_Type()
)
ifMainUfdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainUfdOperStatus.setStatus("current")


class _IfMainUfdGroupId_Type(Integer32):
    """Custom type ifMainUfdGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IfMainUfdGroupId_Type.__name__ = "Integer32"
_IfMainUfdGroupId_Object = MibTableColumn
ifMainUfdGroupId = _IfMainUfdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 17),
    _IfMainUfdGroupId_Type()
)
ifMainUfdGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainUfdGroupId.setStatus("current")
_IfMainUfdDownlinkDisabledCount_Type = Counter32
_IfMainUfdDownlinkDisabledCount_Object = MibTableColumn
ifMainUfdDownlinkDisabledCount = _IfMainUfdDownlinkDisabledCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 18),
    _IfMainUfdDownlinkDisabledCount_Type()
)
ifMainUfdDownlinkDisabledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainUfdDownlinkDisabledCount.setStatus("deprecated")
_IfMainUfdDownlinkEnabledCount_Type = Counter32
_IfMainUfdDownlinkEnabledCount_Object = MibTableColumn
ifMainUfdDownlinkEnabledCount = _IfMainUfdDownlinkEnabledCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 19),
    _IfMainUfdDownlinkEnabledCount_Type()
)
ifMainUfdDownlinkEnabledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainUfdDownlinkEnabledCount.setStatus("deprecated")


class _IfMainDesigUplinkStatus_Type(TruthValue):
    """Custom type ifMainDesigUplinkStatus based on TruthValue"""
    defaultValue = 2


_IfMainDesigUplinkStatus_Type.__name__ = "TruthValue"
_IfMainDesigUplinkStatus_Object = MibTableColumn
ifMainDesigUplinkStatus = _IfMainDesigUplinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 20),
    _IfMainDesigUplinkStatus_Type()
)
ifMainDesigUplinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainDesigUplinkStatus.setStatus("current")


class _IfMainEncapDot1qVlanId_Type(Integer32):
    """Custom type ifMainEncapDot1qVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IfMainEncapDot1qVlanId_Type.__name__ = "Integer32"
_IfMainEncapDot1qVlanId_Object = MibTableColumn
ifMainEncapDot1qVlanId = _IfMainEncapDot1qVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 21),
    _IfMainEncapDot1qVlanId_Type()
)
ifMainEncapDot1qVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainEncapDot1qVlanId.setStatus("current")


class _IfMainNeighborId_Type(SnmpAdminString):
    """Custom type ifMainNeighborId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfMainNeighborId_Type.__name__ = "SnmpAdminString"
_IfMainNeighborId_Object = MibTableColumn
ifMainNeighborId = _IfMainNeighborId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 22),
    _IfMainNeighborId_Type()
)
ifMainNeighborId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainNeighborId.setStatus("current")


class _IfMainName_Type(SnmpAdminString):
    """Custom type ifMainName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IfMainName_Type.__name__ = "SnmpAdminString"
_IfMainName_Object = MibTableColumn
ifMainName = _IfMainName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 23),
    _IfMainName_Type()
)
ifMainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainName.setStatus("current")


class _IfMainPrevDesc_Type(DisplayString):
    """Custom type ifMainPrevDesc based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfMainPrevDesc_Type.__name__ = "DisplayString"
_IfMainPrevDesc_Object = MibTableColumn
ifMainPrevDesc = _IfMainPrevDesc_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 4, 1, 24),
    _IfMainPrevDesc_Type()
)
ifMainPrevDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainPrevDesc.setStatus("current")
_IfIpTable_Object = MibTable
ifIpTable = _IfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5)
)
if mibBuilder.loadTexts:
    ifIpTable.setStatus("current")
_IfIpEntry_Object = MibTableRow
ifIpEntry = _IfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1)
)
ifIpEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifIpEntry.setStatus("current")


class _IfIpAddrAllocMethod_Type(Integer32):
    """Custom type ifIpAddrAllocMethod based on Integer32"""
    defaultValue = 4

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
        *(("manual", 1),
          ("negotiation", 2),
          ("dynamic", 3),
          ("none", 4))
    )


_IfIpAddrAllocMethod_Type.__name__ = "Integer32"
_IfIpAddrAllocMethod_Object = MibTableColumn
ifIpAddrAllocMethod = _IfIpAddrAllocMethod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1, 1),
    _IfIpAddrAllocMethod_Type()
)
ifIpAddrAllocMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpAddrAllocMethod.setStatus("current")


class _IfIpAddr_Type(IpAddress):
    """Custom type ifIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IfIpAddr_Type.__name__ = "IpAddress"
_IfIpAddr_Object = MibTableColumn
ifIpAddr = _IfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1, 2),
    _IfIpAddr_Type()
)
ifIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpAddr.setStatus("current")
_IfIpSubnetMask_Type = IpAddress
_IfIpSubnetMask_Object = MibTableColumn
ifIpSubnetMask = _IfIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1, 3),
    _IfIpSubnetMask_Type()
)
ifIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpSubnetMask.setStatus("current")
_IfIpBroadcastAddr_Type = IpAddress
_IfIpBroadcastAddr_Object = MibTableColumn
ifIpBroadcastAddr = _IfIpBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1, 4),
    _IfIpBroadcastAddr_Type()
)
ifIpBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpBroadcastAddr.setStatus("current")


class _IfIpForwardingEnable_Type(TruthValue):
    """Custom type ifIpForwardingEnable based on TruthValue"""
    defaultValue = 1


_IfIpForwardingEnable_Type.__name__ = "TruthValue"
_IfIpForwardingEnable_Object = MibTableColumn
ifIpForwardingEnable = _IfIpForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1, 5),
    _IfIpForwardingEnable_Type()
)
ifIpForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpForwardingEnable.setStatus("current")


class _IfIpAddrAllocProtocol_Type(Integer32):
    """Custom type ifIpAddrAllocProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rarp", 1),
          ("dhcp", 2))
    )


_IfIpAddrAllocProtocol_Type.__name__ = "Integer32"
_IfIpAddrAllocProtocol_Object = MibTableColumn
ifIpAddrAllocProtocol = _IfIpAddrAllocProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1, 6),
    _IfIpAddrAllocProtocol_Type()
)
ifIpAddrAllocProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpAddrAllocProtocol.setStatus("current")
_IfIpDestMacAddress_Type = MacAddress
_IfIpDestMacAddress_Object = MibTableColumn
ifIpDestMacAddress = _IfIpDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1, 7),
    _IfIpDestMacAddress_Type()
)
ifIpDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifIpDestMacAddress.setStatus("current")
_IfIpUnnumAssocIPIf_Type = InterfaceIndex
_IfIpUnnumAssocIPIf_Object = MibTableColumn
ifIpUnnumAssocIPIf = _IfIpUnnumAssocIPIf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1, 8),
    _IfIpUnnumAssocIPIf_Type()
)
ifIpUnnumAssocIPIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifIpUnnumAssocIPIf.setStatus("current")


class _IfIpIntfStatsEnable_Type(TruthValue):
    """Custom type ifIpIntfStatsEnable based on TruthValue"""
    defaultValue = 2


_IfIpIntfStatsEnable_Type.__name__ = "TruthValue"
_IfIpIntfStatsEnable_Object = MibTableColumn
ifIpIntfStatsEnable = _IfIpIntfStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1, 9),
    _IfIpIntfStatsEnable_Type()
)
ifIpIntfStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpIntfStatsEnable.setStatus("current")


class _IfIpPortVlanId_Type(Integer32):
    """Custom type ifIpPortVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IfIpPortVlanId_Type.__name__ = "Integer32"
_IfIpPortVlanId_Object = MibTableColumn
ifIpPortVlanId = _IfIpPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 5, 1, 10),
    _IfIpPortVlanId_Type()
)
ifIpPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIpPortVlanId.setStatus("current")
_IfWanTable_Object = MibTable
ifWanTable = _IfWanTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6)
)
if mibBuilder.loadTexts:
    ifWanTable.setStatus("deprecated")
_IfWanEntry_Object = MibTableRow
ifWanEntry = _IfWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1)
)
ifWanEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifWanEntry.setStatus("deprecated")


class _IfWanInterfaceType_Type(Integer32):
    """Custom type ifWanInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(23,
              38,
              92,
              108,
              134)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 23),
          ("miox25", 38),
          ("frameRelayMPI", 92),
          ("pppMultilinkBundle", 108),
          ("atmSubInterface", 134))
    )


_IfWanInterfaceType_Type.__name__ = "Integer32"
_IfWanInterfaceType_Object = MibTableColumn
ifWanInterfaceType = _IfWanInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 1),
    _IfWanInterfaceType_Type()
)
ifWanInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifWanInterfaceType.setStatus("deprecated")


class _IfWanConnectionType_Type(Integer32):
    """Custom type ifWanConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("permanent", 1),
          ("switched", 2))
    )


_IfWanConnectionType_Type.__name__ = "Integer32"
_IfWanConnectionType_Object = MibTableColumn
ifWanConnectionType = _IfWanConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 2),
    _IfWanConnectionType_Type()
)
ifWanConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanConnectionType.setStatus("deprecated")


class _IfWanVirtualPathId_Type(Integer32):
    """Custom type ifWanVirtualPathId based on Integer32"""
    defaultValue = 0


_IfWanVirtualPathId_Type.__name__ = "Integer32"
_IfWanVirtualPathId_Object = MibTableColumn
ifWanVirtualPathId = _IfWanVirtualPathId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 3),
    _IfWanVirtualPathId_Type()
)
ifWanVirtualPathId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanVirtualPathId.setStatus("deprecated")


class _IfWanVirtualCircuitId_Type(Integer32):
    """Custom type ifWanVirtualCircuitId based on Integer32"""
    defaultValue = 0


_IfWanVirtualCircuitId_Type.__name__ = "Integer32"
_IfWanVirtualCircuitId_Object = MibTableColumn
ifWanVirtualCircuitId = _IfWanVirtualCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 4),
    _IfWanVirtualCircuitId_Type()
)
ifWanVirtualCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanVirtualCircuitId.setStatus("deprecated")


class _IfWanPeerMediaAddress_Type(OctetString):
    """Custom type ifWanPeerMediaAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IfWanPeerMediaAddress_Type.__name__ = "OctetString"
_IfWanPeerMediaAddress_Object = MibTableColumn
ifWanPeerMediaAddress = _IfWanPeerMediaAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 5),
    _IfWanPeerMediaAddress_Type()
)
ifWanPeerMediaAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanPeerMediaAddress.setStatus("deprecated")
_IfWanSustainedSpeed_Type = Integer32
_IfWanSustainedSpeed_Object = MibTableColumn
ifWanSustainedSpeed = _IfWanSustainedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 6),
    _IfWanSustainedSpeed_Type()
)
ifWanSustainedSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanSustainedSpeed.setStatus("deprecated")
_IfWanPeakSpeed_Type = Integer32
_IfWanPeakSpeed_Object = MibTableColumn
ifWanPeakSpeed = _IfWanPeakSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 7),
    _IfWanPeakSpeed_Type()
)
ifWanPeakSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanPeakSpeed.setStatus("deprecated")
_IfWanMaxBurstSize_Type = Integer32
_IfWanMaxBurstSize_Object = MibTableColumn
ifWanMaxBurstSize = _IfWanMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 8),
    _IfWanMaxBurstSize_Type()
)
ifWanMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanMaxBurstSize.setStatus("deprecated")


class _IfWanIpQosProfileIndex_Type(Integer32):
    """Custom type ifWanIpQosProfileIndex based on Integer32"""
    defaultValue = 0


_IfWanIpQosProfileIndex_Type.__name__ = "Integer32"
_IfWanIpQosProfileIndex_Object = MibTableColumn
ifWanIpQosProfileIndex = _IfWanIpQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 9),
    _IfWanIpQosProfileIndex_Type()
)
ifWanIpQosProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanIpQosProfileIndex.setStatus("deprecated")


class _IfWanIdleTimeout_Type(Integer32):
    """Custom type ifWanIdleTimeout based on Integer32"""
    defaultValue = 0


_IfWanIdleTimeout_Type.__name__ = "Integer32"
_IfWanIdleTimeout_Object = MibTableColumn
ifWanIdleTimeout = _IfWanIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 10),
    _IfWanIdleTimeout_Type()
)
ifWanIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanIdleTimeout.setStatus("deprecated")


class _IfWanPeerIpAddr_Type(IpAddress):
    """Custom type ifWanPeerIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IfWanPeerIpAddr_Type.__name__ = "IpAddress"
_IfWanPeerIpAddr_Object = MibTableColumn
ifWanPeerIpAddr = _IfWanPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 11),
    _IfWanPeerIpAddr_Type()
)
ifWanPeerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanPeerIpAddr.setStatus("deprecated")


class _IfWanRtpHdrComprEnable_Type(TruthValue):
    """Custom type ifWanRtpHdrComprEnable based on TruthValue"""
    defaultValue = 2


_IfWanRtpHdrComprEnable_Type.__name__ = "TruthValue"
_IfWanRtpHdrComprEnable_Object = MibTableColumn
ifWanRtpHdrComprEnable = _IfWanRtpHdrComprEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 12),
    _IfWanRtpHdrComprEnable_Type()
)
ifWanRtpHdrComprEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanRtpHdrComprEnable.setStatus("deprecated")


class _IfWanPersistence_Type(Integer32):
    """Custom type ifWanPersistence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("demand", 2))
    )


_IfWanPersistence_Type.__name__ = "Integer32"
_IfWanPersistence_Object = MibTableColumn
ifWanPersistence = _IfWanPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 6, 1, 13),
    _IfWanPersistence_Type()
)
ifWanPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifWanPersistence.setStatus("deprecated")
_IfAutoCktProfileTable_Object = MibTable
ifAutoCktProfileTable = _IfAutoCktProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7)
)
if mibBuilder.loadTexts:
    ifAutoCktProfileTable.setStatus("deprecated")
_IfAutoProfileEntry_Object = MibTableRow
ifAutoProfileEntry = _IfAutoProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7, 1)
)
ifAutoProfileEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifAutoProfileIfIndex"),
)
if mibBuilder.loadTexts:
    ifAutoProfileEntry.setStatus("current")
_IfAutoProfileIfIndex_Type = InterfaceIndex
_IfAutoProfileIfIndex_Object = MibTableColumn
ifAutoProfileIfIndex = _IfAutoProfileIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7, 1, 1),
    _IfAutoProfileIfIndex_Type()
)
ifAutoProfileIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifAutoProfileIfIndex.setStatus("deprecated")


class _IfAutoProfileIfType_Type(Integer32):
    """Custom type ifAutoProfileIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              32,
              49,
              114)
        )
    )
    namedValues = NamedValues(
        *(("rfc877x25", 5),
          ("frameRelay", 32),
          ("aal5", 49),
          ("ipOverAtm", 114))
    )


_IfAutoProfileIfType_Type.__name__ = "Integer32"
_IfAutoProfileIfType_Object = MibTableColumn
ifAutoProfileIfType = _IfAutoProfileIfType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7, 1, 2),
    _IfAutoProfileIfType_Type()
)
ifAutoProfileIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAutoProfileIfType.setStatus("deprecated")


class _IfAutoProfileIpAddrAllocMethod_Type(Integer32):
    """Custom type ifAutoProfileIpAddrAllocMethod based on Integer32"""
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
        *(("other", 1),
          ("negotiation", 2),
          ("localAddressPool", 3))
    )


_IfAutoProfileIpAddrAllocMethod_Type.__name__ = "Integer32"
_IfAutoProfileIpAddrAllocMethod_Object = MibTableColumn
ifAutoProfileIpAddrAllocMethod = _IfAutoProfileIpAddrAllocMethod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7, 1, 3),
    _IfAutoProfileIpAddrAllocMethod_Type()
)
ifAutoProfileIpAddrAllocMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifAutoProfileIpAddrAllocMethod.setStatus("deprecated")
_IfAutoProfileDefIpSubnetMask_Type = IpAddress
_IfAutoProfileDefIpSubnetMask_Object = MibTableColumn
ifAutoProfileDefIpSubnetMask = _IfAutoProfileDefIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7, 1, 4),
    _IfAutoProfileDefIpSubnetMask_Type()
)
ifAutoProfileDefIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifAutoProfileDefIpSubnetMask.setStatus("deprecated")
_IfAutoProfileDefIpBroadcastAddr_Type = IpAddress
_IfAutoProfileDefIpBroadcastAddr_Object = MibTableColumn
ifAutoProfileDefIpBroadcastAddr = _IfAutoProfileDefIpBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7, 1, 5),
    _IfAutoProfileDefIpBroadcastAddr_Type()
)
ifAutoProfileDefIpBroadcastAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifAutoProfileDefIpBroadcastAddr.setStatus("deprecated")
_IfAutoProfileIdleTimeout_Type = Integer32
_IfAutoProfileIdleTimeout_Object = MibTableColumn
ifAutoProfileIdleTimeout = _IfAutoProfileIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7, 1, 6),
    _IfAutoProfileIdleTimeout_Type()
)
ifAutoProfileIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifAutoProfileIdleTimeout.setStatus("deprecated")


class _IfAutoProfileEncapType_Type(Integer32):
    """Custom type ifAutoProfileEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("nlpid", 2),
          ("nlpidSnap", 3),
          ("cudNlpid", 4),
          ("cudNlpidSnap", 5),
          ("llcSnap", 6),
          ("vcMultiplexed", 7))
    )


_IfAutoProfileEncapType_Type.__name__ = "Integer32"
_IfAutoProfileEncapType_Object = MibTableColumn
ifAutoProfileEncapType = _IfAutoProfileEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7, 1, 7),
    _IfAutoProfileEncapType_Type()
)
ifAutoProfileEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifAutoProfileEncapType.setStatus("deprecated")


class _IfAutoProfileIpQosProfileIndex_Type(Integer32):
    """Custom type ifAutoProfileIpQosProfileIndex based on Integer32"""
    defaultValue = 0


_IfAutoProfileIpQosProfileIndex_Type.__name__ = "Integer32"
_IfAutoProfileIpQosProfileIndex_Object = MibTableColumn
ifAutoProfileIpQosProfileIndex = _IfAutoProfileIpQosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7, 1, 8),
    _IfAutoProfileIpQosProfileIndex_Type()
)
ifAutoProfileIpQosProfileIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifAutoProfileIpQosProfileIndex.setStatus("deprecated")
_IfAutoProfileRowStatus_Type = RowStatus
_IfAutoProfileRowStatus_Object = MibTableColumn
ifAutoProfileRowStatus = _IfAutoProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 7, 1, 9),
    _IfAutoProfileRowStatus_Type()
)
ifAutoProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifAutoProfileRowStatus.setStatus("deprecated")
_IfIvrTable_Object = MibTable
ifIvrTable = _IfIvrTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 8)
)
if mibBuilder.loadTexts:
    ifIvrTable.setStatus("current")
_IfIvrEntry_Object = MibTableRow
ifIvrEntry = _IfIvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 8, 1)
)
ifIvrEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifIvrEntry.setStatus("current")
_IfIvrBridgedIface_Type = TruthValue
_IfIvrBridgedIface_Object = MibTableColumn
ifIvrBridgedIface = _IfIvrBridgedIface_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 8, 1, 1),
    _IfIvrBridgedIface_Type()
)
ifIvrBridgedIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifIvrBridgedIface.setStatus("current")


class _IfSetMgmtVlanList_Type(OctetString):
    """Custom type ifSetMgmtVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_IfSetMgmtVlanList_Type.__name__ = "OctetString"
_IfSetMgmtVlanList_Object = MibScalar
ifSetMgmtVlanList = _IfSetMgmtVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 9),
    _IfSetMgmtVlanList_Type()
)
ifSetMgmtVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSetMgmtVlanList.setStatus("current")


class _IfResetMgmtVlanList_Type(OctetString):
    """Custom type ifResetMgmtVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_IfResetMgmtVlanList_Type.__name__ = "OctetString"
_IfResetMgmtVlanList_Object = MibScalar
ifResetMgmtVlanList = _IfResetMgmtVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 10),
    _IfResetMgmtVlanList_Type()
)
ifResetMgmtVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifResetMgmtVlanList.setStatus("current")
_IfSecondaryIpAddressTable_Object = MibTable
ifSecondaryIpAddressTable = _IfSecondaryIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 11)
)
if mibBuilder.loadTexts:
    ifSecondaryIpAddressTable.setStatus("current")
_IfSecondaryIpAddressEntry_Object = MibTableRow
ifSecondaryIpAddressEntry = _IfSecondaryIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 11, 1)
)
ifSecondaryIpAddressEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifMainIndex"),
    (0, "ARICENT-CFA-MIB", "ifSecondaryIpAddress"),
)
if mibBuilder.loadTexts:
    ifSecondaryIpAddressEntry.setStatus("current")
_IfSecondaryIpAddress_Type = IpAddress
_IfSecondaryIpAddress_Object = MibTableColumn
ifSecondaryIpAddress = _IfSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 11, 1, 1),
    _IfSecondaryIpAddress_Type()
)
ifSecondaryIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifSecondaryIpAddress.setStatus("current")
_IfSecondaryIpSubnetMask_Type = IpAddress
_IfSecondaryIpSubnetMask_Object = MibTableColumn
ifSecondaryIpSubnetMask = _IfSecondaryIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 11, 1, 2),
    _IfSecondaryIpSubnetMask_Type()
)
ifSecondaryIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSecondaryIpSubnetMask.setStatus("current")
_IfSecondaryIpBroadcastAddr_Type = IpAddress
_IfSecondaryIpBroadcastAddr_Object = MibTableColumn
ifSecondaryIpBroadcastAddr = _IfSecondaryIpBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 11, 1, 3),
    _IfSecondaryIpBroadcastAddr_Type()
)
ifSecondaryIpBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSecondaryIpBroadcastAddr.setStatus("current")
_IfSecondaryIpRowStatus_Type = RowStatus
_IfSecondaryIpRowStatus_Object = MibTableColumn
ifSecondaryIpRowStatus = _IfSecondaryIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 11, 1, 4),
    _IfSecondaryIpRowStatus_Type()
)
ifSecondaryIpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSecondaryIpRowStatus.setStatus("current")
_IfMainExtTable_Object = MibTable
ifMainExtTable = _IfMainExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 12)
)
if mibBuilder.loadTexts:
    ifMainExtTable.setStatus("current")
_IfMainExtEntry_Object = MibTableRow
ifMainExtEntry = _IfMainExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 12, 1)
)
if mibBuilder.loadTexts:
    ifMainExtEntry.setStatus("current")
_IfMainExtMacAddress_Type = MacAddress
_IfMainExtMacAddress_Object = MibTableColumn
ifMainExtMacAddress = _IfMainExtMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 12, 1, 8),
    _IfMainExtMacAddress_Type()
)
ifMainExtMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMainExtMacAddress.setStatus("current")


class _IfMainExtSysSpecificPortID_Type(Unsigned32):
    """Custom type ifMainExtSysSpecificPortID based on Unsigned32"""
    defaultValue = 0


_IfMainExtSysSpecificPortID_Type.__name__ = "Unsigned32"
_IfMainExtSysSpecificPortID_Object = MibTableColumn
ifMainExtSysSpecificPortID = _IfMainExtSysSpecificPortID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 12, 1, 9),
    _IfMainExtSysSpecificPortID_Type()
)
ifMainExtSysSpecificPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainExtSysSpecificPortID.setStatus("current")


class _IfMainExtInterfaceType_Type(Integer32):
    """Custom type ifMainExtInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frontpanelport", 1),
          ("backplaneport", 2))
    )


_IfMainExtInterfaceType_Type.__name__ = "Integer32"
_IfMainExtInterfaceType_Object = MibTableColumn
ifMainExtInterfaceType = _IfMainExtInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 12, 1, 10),
    _IfMainExtInterfaceType_Type()
)
ifMainExtInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainExtInterfaceType.setStatus("current")


class _IfMainExtPortSecState_Type(Integer32):
    """Custom type ifMainExtPortSecState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("untrusted", 0),
          ("trusted", 1))
    )


_IfMainExtPortSecState_Type.__name__ = "Integer32"
_IfMainExtPortSecState_Object = MibTableColumn
ifMainExtPortSecState = _IfMainExtPortSecState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 12, 1, 11),
    _IfMainExtPortSecState_Type()
)
ifMainExtPortSecState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainExtPortSecState.setStatus("current")
_IfMainExtInPkts_Type = Counter32
_IfMainExtInPkts_Object = MibTableColumn
ifMainExtInPkts = _IfMainExtInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 12, 1, 12),
    _IfMainExtInPkts_Type()
)
ifMainExtInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainExtInPkts.setStatus("current")


class _IfMainExtLinkUpEnabledStatus_Type(Integer32):
    """Custom type ifMainExtLinkUpEnabledStatus based on Integer32"""
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


_IfMainExtLinkUpEnabledStatus_Type.__name__ = "Integer32"
_IfMainExtLinkUpEnabledStatus_Object = MibTableColumn
ifMainExtLinkUpEnabledStatus = _IfMainExtLinkUpEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 12, 1, 13),
    _IfMainExtLinkUpEnabledStatus_Type()
)
ifMainExtLinkUpEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainExtLinkUpEnabledStatus.setStatus("current")


class _IfMainExtLinkUpDelayTimer_Type(Unsigned32):
    """Custom type ifMainExtLinkUpDelayTimer based on Unsigned32"""
    defaultValue = 2


_IfMainExtLinkUpDelayTimer_Type.__name__ = "Unsigned32"
_IfMainExtLinkUpDelayTimer_Object = MibTableColumn
ifMainExtLinkUpDelayTimer = _IfMainExtLinkUpDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 12, 1, 14),
    _IfMainExtLinkUpDelayTimer_Type()
)
ifMainExtLinkUpDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMainExtLinkUpDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    ifMainExtLinkUpDelayTimer.setUnits("seconds")
_IfMainExtLinkUpRemainingTime_Type = Unsigned32
_IfMainExtLinkUpRemainingTime_Object = MibTableColumn
ifMainExtLinkUpRemainingTime = _IfMainExtLinkUpRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 12, 1, 15),
    _IfMainExtLinkUpRemainingTime_Type()
)
ifMainExtLinkUpRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMainExtLinkUpRemainingTime.setStatus("current")
_IfCustTLVTable_Object = MibTable
ifCustTLVTable = _IfCustTLVTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 13)
)
if mibBuilder.loadTexts:
    ifCustTLVTable.setStatus("current")
_IfCustTLVEntry_Object = MibTableRow
ifCustTLVEntry = _IfCustTLVEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 13, 1)
)
ifCustTLVEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifMainIndex"),
    (0, "ARICENT-CFA-MIB", "ifCustTLVType"),
)
if mibBuilder.loadTexts:
    ifCustTLVEntry.setStatus("current")
_IfCustTLVType_Type = Unsigned32
_IfCustTLVType_Object = MibTableColumn
ifCustTLVType = _IfCustTLVType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 13, 1, 1),
    _IfCustTLVType_Type()
)
ifCustTLVType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifCustTLVType.setStatus("current")
_IfCustTLVLength_Type = Unsigned32
_IfCustTLVLength_Object = MibTableColumn
ifCustTLVLength = _IfCustTLVLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 13, 1, 2),
    _IfCustTLVLength_Type()
)
ifCustTLVLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCustTLVLength.setStatus("current")
_IfCustTLVValue_Type = DisplayString
_IfCustTLVValue_Object = MibTableColumn
ifCustTLVValue = _IfCustTLVValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 13, 1, 3),
    _IfCustTLVValue_Type()
)
ifCustTLVValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCustTLVValue.setStatus("current")
_IfCustTLVRowStatus_Type = RowStatus
_IfCustTLVRowStatus_Object = MibTableColumn
ifCustTLVRowStatus = _IfCustTLVRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 13, 1, 4),
    _IfCustTLVRowStatus_Type()
)
ifCustTLVRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCustTLVRowStatus.setStatus("current")
_IfCustOpaqueAttrTable_Object = MibTable
ifCustOpaqueAttrTable = _IfCustOpaqueAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 14)
)
if mibBuilder.loadTexts:
    ifCustOpaqueAttrTable.setStatus("current")
_IfCustOpaqueAttrEntry_Object = MibTableRow
ifCustOpaqueAttrEntry = _IfCustOpaqueAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 14, 1)
)
ifCustOpaqueAttrEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifMainIndex"),
    (0, "ARICENT-CFA-MIB", "ifCustOpaqueAttributeID"),
)
if mibBuilder.loadTexts:
    ifCustOpaqueAttrEntry.setStatus("current")


class _IfCustOpaqueAttributeID_Type(Integer32):
    """Custom type ifCustOpaqueAttributeID based on Integer32"""
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
        *(("opaqueAttr1", 1),
          ("opaqueAttr2", 2),
          ("opaqueAttr3", 3),
          ("opaqueAttr4", 4))
    )


_IfCustOpaqueAttributeID_Type.__name__ = "Integer32"
_IfCustOpaqueAttributeID_Object = MibTableColumn
ifCustOpaqueAttributeID = _IfCustOpaqueAttributeID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 14, 1, 1),
    _IfCustOpaqueAttributeID_Type()
)
ifCustOpaqueAttributeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifCustOpaqueAttributeID.setStatus("current")


class _IfCustOpaqueAttribute_Type(Unsigned32):
    """Custom type ifCustOpaqueAttribute based on Unsigned32"""
    defaultValue = 0


_IfCustOpaqueAttribute_Type.__name__ = "Unsigned32"
_IfCustOpaqueAttribute_Object = MibTableColumn
ifCustOpaqueAttribute = _IfCustOpaqueAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 14, 1, 2),
    _IfCustOpaqueAttribute_Type()
)
ifCustOpaqueAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCustOpaqueAttribute.setStatus("current")
_IfCustOpaqueRowStatus_Type = RowStatus
_IfCustOpaqueRowStatus_Object = MibTableColumn
ifCustOpaqueRowStatus = _IfCustOpaqueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 14, 1, 3),
    _IfCustOpaqueRowStatus_Type()
)
ifCustOpaqueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifCustOpaqueRowStatus.setStatus("current")
_IfBridgeILanIfTable_Object = MibTable
ifBridgeILanIfTable = _IfBridgeILanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 15)
)
if mibBuilder.loadTexts:
    ifBridgeILanIfTable.setStatus("current")
_IfBridgeILanIfEntry_Object = MibTableRow
ifBridgeILanIfEntry = _IfBridgeILanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 15, 1)
)
ifBridgeILanIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifBridgeILanIfEntry.setStatus("current")


class _IfBridgeILanIfStatus_Type(Integer32):
    """Custom type ifBridgeILanIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("outOfService", 2))
    )


_IfBridgeILanIfStatus_Type.__name__ = "Integer32"
_IfBridgeILanIfStatus_Object = MibTableColumn
ifBridgeILanIfStatus = _IfBridgeILanIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 15, 1, 1),
    _IfBridgeILanIfStatus_Type()
)
ifBridgeILanIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBridgeILanIfStatus.setStatus("current")
_IfTypeProtoDenyTable_Object = MibTable
ifTypeProtoDenyTable = _IfTypeProtoDenyTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 16)
)
if mibBuilder.loadTexts:
    ifTypeProtoDenyTable.setStatus("current")
_IfTypeProtoDenyEntry_Object = MibTableRow
ifTypeProtoDenyEntry = _IfTypeProtoDenyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 16, 1)
)
ifTypeProtoDenyEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifTypeProtoDenyContextId"),
    (0, "ARICENT-CFA-MIB", "ifTypeProtoDenyMainType"),
    (0, "ARICENT-CFA-MIB", "ifTypeProtoDenyBrgPortType"),
    (0, "ARICENT-CFA-MIB", "ifTypeProtoDenyProtocol"),
)
if mibBuilder.loadTexts:
    ifTypeProtoDenyEntry.setStatus("current")


class _IfTypeProtoDenyContextId_Type(Unsigned32):
    """Custom type ifTypeProtoDenyContextId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfTypeProtoDenyContextId_Type.__name__ = "Unsigned32"
_IfTypeProtoDenyContextId_Object = MibTableColumn
ifTypeProtoDenyContextId = _IfTypeProtoDenyContextId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 16, 1, 1),
    _IfTypeProtoDenyContextId_Type()
)
ifTypeProtoDenyContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTypeProtoDenyContextId.setStatus("current")


class _IfTypeProtoDenyMainType_Type(Integer32):
    """Custom type ifTypeProtoDenyMainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              53,
              161,
              209,
              248)
        )
    )
    namedValues = NamedValues(
        *(("ethernetCsmacd", 6),
          ("propVirtual", 53),
          ("ieee8023ad", 161),
          ("brgPort", 209),
          ("pip", 248))
    )


_IfTypeProtoDenyMainType_Type.__name__ = "Integer32"
_IfTypeProtoDenyMainType_Object = MibTableColumn
ifTypeProtoDenyMainType = _IfTypeProtoDenyMainType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 16, 1, 2),
    _IfTypeProtoDenyMainType_Type()
)
ifTypeProtoDenyMainType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTypeProtoDenyMainType.setStatus("current")


class _IfTypeProtoDenyBrgPortType_Type(Integer32):
    """Custom type ifTypeProtoDenyBrgPortType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("providerNetworkPort", 1),
          ("customerNetworkPortPortBased", 2),
          ("customerNetworkPortStagged", 3),
          ("customerEdgePort", 4),
          ("propCustomerEdgePort", 5),
          ("propCustomerNetworkPort", 6),
          ("propProviderNetworkPort", 7),
          ("customerBridgePort", 8),
          ("customerNetworkPortCtagged", 9),
          ("virtualInstancePort", 10),
          ("providerInstancePort", 11),
          ("customerBackbonePort", 12))
    )


_IfTypeProtoDenyBrgPortType_Type.__name__ = "Integer32"
_IfTypeProtoDenyBrgPortType_Object = MibTableColumn
ifTypeProtoDenyBrgPortType = _IfTypeProtoDenyBrgPortType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 16, 1, 3),
    _IfTypeProtoDenyBrgPortType_Type()
)
ifTypeProtoDenyBrgPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTypeProtoDenyBrgPortType.setStatus("current")


class _IfTypeProtoDenyProtocol_Type(Integer32):
    """Custom type ifTypeProtoDenyProtocol based on Integer32"""
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
        *(("pnac", 1),
          ("la", 2),
          ("xstp", 3),
          ("vlan", 4),
          ("garp", 5),
          ("mrp", 6),
          ("pbb", 7),
          ("ecfm", 8),
          ("elmi", 9),
          ("snoop", 10),
          ("lldp", 11),
          ("bridge", 12),
          ("qos", 13))
    )


_IfTypeProtoDenyProtocol_Type.__name__ = "Integer32"
_IfTypeProtoDenyProtocol_Object = MibTableColumn
ifTypeProtoDenyProtocol = _IfTypeProtoDenyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 16, 1, 4),
    _IfTypeProtoDenyProtocol_Type()
)
ifTypeProtoDenyProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifTypeProtoDenyProtocol.setStatus("current")
_IfTypeProtoDenyRowStatus_Type = RowStatus
_IfTypeProtoDenyRowStatus_Object = MibTableColumn
ifTypeProtoDenyRowStatus = _IfTypeProtoDenyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 16, 1, 5),
    _IfTypeProtoDenyRowStatus_Type()
)
ifTypeProtoDenyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTypeProtoDenyRowStatus.setStatus("current")


class _IfmDebug_Type(Unsigned32):
    """Custom type ifmDebug based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IfmDebug_Type.__name__ = "Unsigned32"
_IfmDebug_Object = MibScalar
ifmDebug = _IfmDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 17),
    _IfmDebug_Type()
)
ifmDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifmDebug.setStatus("current")
_IfIvrMappingTable_Object = MibTable
ifIvrMappingTable = _IfIvrMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 18)
)
if mibBuilder.loadTexts:
    ifIvrMappingTable.setStatus("current")
_IfIvrMappingEntry_Object = MibTableRow
ifIvrMappingEntry = _IfIvrMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 18, 1)
)
ifIvrMappingEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifMainIndex"),
    (0, "ARICENT-CFA-MIB", "ifIvrAssociatedVlan"),
)
if mibBuilder.loadTexts:
    ifIvrMappingEntry.setStatus("current")
_IfIvrAssociatedVlan_Type = VlanId
_IfIvrAssociatedVlan_Object = MibTableColumn
ifIvrAssociatedVlan = _IfIvrAssociatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 18, 1, 1),
    _IfIvrAssociatedVlan_Type()
)
ifIvrAssociatedVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifIvrAssociatedVlan.setStatus("current")
_IfIvrMappingRowStatus_Type = RowStatus
_IfIvrMappingRowStatus_Object = MibTableColumn
ifIvrMappingRowStatus = _IfIvrMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 18, 1, 2),
    _IfIvrMappingRowStatus_Type()
)
ifIvrMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifIvrMappingRowStatus.setStatus("current")
_IfHCErrorTable_Object = MibTable
ifHCErrorTable = _IfHCErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 19)
)
if mibBuilder.loadTexts:
    ifHCErrorTable.setStatus("current")
_IfHCErrorEntry_Object = MibTableRow
ifHCErrorEntry = _IfHCErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 19, 1)
)
if mibBuilder.loadTexts:
    ifHCErrorEntry.setStatus("current")
_IfHCInDiscards_Type = Counter64
_IfHCInDiscards_Object = MibTableColumn
ifHCInDiscards = _IfHCInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 19, 1, 1),
    _IfHCInDiscards_Type()
)
ifHCInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInDiscards.setStatus("current")
_IfHCInErrors_Type = Counter64
_IfHCInErrors_Object = MibTableColumn
ifHCInErrors = _IfHCInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 19, 1, 2),
    _IfHCInErrors_Type()
)
ifHCInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInErrors.setStatus("current")
_IfHCInUnknownProtos_Type = Counter64
_IfHCInUnknownProtos_Object = MibTableColumn
ifHCInUnknownProtos = _IfHCInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 19, 1, 3),
    _IfHCInUnknownProtos_Type()
)
ifHCInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCInUnknownProtos.setStatus("current")
_IfHCOutDiscards_Type = Counter64
_IfHCOutDiscards_Object = MibTableColumn
ifHCOutDiscards = _IfHCOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 19, 1, 4),
    _IfHCOutDiscards_Type()
)
ifHCOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOutDiscards.setStatus("current")
_IfHCOutErrors_Type = Counter64
_IfHCOutErrors_Object = MibTableColumn
ifHCOutErrors = _IfHCOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 19, 1, 5),
    _IfHCOutErrors_Type()
)
ifHCOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifHCOutErrors.setStatus("current")


class _IfSecurityBridging_Type(Integer32):
    """Custom type ifSecurityBridging based on Integer32"""
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


_IfSecurityBridging_Type.__name__ = "Integer32"
_IfSecurityBridging_Object = MibScalar
ifSecurityBridging = _IfSecurityBridging_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 20),
    _IfSecurityBridging_Type()
)
ifSecurityBridging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSecurityBridging.setStatus("current")


class _IfSetSecVlanList_Type(OctetString):
    """Custom type ifSetSecVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_IfSetSecVlanList_Type.__name__ = "OctetString"
_IfSetSecVlanList_Object = MibScalar
ifSetSecVlanList = _IfSetSecVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 21),
    _IfSetSecVlanList_Type()
)
ifSetSecVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSetSecVlanList.setStatus("current")


class _IfResetSecVlanList_Type(OctetString):
    """Custom type ifResetSecVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_IfResetSecVlanList_Type.__name__ = "OctetString"
_IfResetSecVlanList_Object = MibScalar
ifResetSecVlanList = _IfResetSecVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 22),
    _IfResetSecVlanList_Type()
)
ifResetSecVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifResetSecVlanList.setStatus("current")
_IfSecIvrIfIndex_Type = Integer32
_IfSecIvrIfIndex_Object = MibScalar
ifSecIvrIfIndex = _IfSecIvrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 23),
    _IfSecIvrIfIndex_Type()
)
ifSecIvrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSecIvrIfIndex.setStatus("current")
_IfAvailableIndexTable_Object = MibTable
ifAvailableIndexTable = _IfAvailableIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 24)
)
if mibBuilder.loadTexts:
    ifAvailableIndexTable.setStatus("current")
_IfAvailableIndexEntry_Object = MibTableRow
ifAvailableIndexEntry = _IfAvailableIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 24, 1)
)
ifAvailableIndexEntry.setIndexNames(
    (0, "IF-MIB", "ifType"),
)
if mibBuilder.loadTexts:
    ifAvailableIndexEntry.setStatus("current")
_IfAvailableFreeIndex_Type = InterfaceIndex
_IfAvailableFreeIndex_Object = MibTableColumn
ifAvailableFreeIndex = _IfAvailableFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 24, 1, 1),
    _IfAvailableFreeIndex_Type()
)
ifAvailableFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAvailableFreeIndex.setStatus("current")
_IfACTable_Object = MibTable
ifACTable = _IfACTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 25)
)
if mibBuilder.loadTexts:
    ifACTable.setStatus("current")
_IfACEntry_Object = MibTableRow
ifACEntry = _IfACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 25, 1)
)
ifACEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifMainIndex"),
)
if mibBuilder.loadTexts:
    ifACEntry.setStatus("current")
_IfACPortIdentifier_Type = InterfaceIndex
_IfACPortIdentifier_Object = MibTableColumn
ifACPortIdentifier = _IfACPortIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 25, 1, 1),
    _IfACPortIdentifier_Type()
)
ifACPortIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifACPortIdentifier.setStatus("current")
_IfACCustomerVlan_Type = VlanId
_IfACCustomerVlan_Object = MibTableColumn
ifACCustomerVlan = _IfACCustomerVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 25, 1, 2),
    _IfACCustomerVlan_Type()
)
ifACCustomerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifACCustomerVlan.setStatus("current")


class _IfUfdSystemControl_Type(Integer32):
    """Custom type ifUfdSystemControl based on Integer32"""
    defaultValue = 2

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


_IfUfdSystemControl_Type.__name__ = "Integer32"
_IfUfdSystemControl_Object = MibScalar
ifUfdSystemControl = _IfUfdSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 26),
    _IfUfdSystemControl_Type()
)
ifUfdSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifUfdSystemControl.setStatus("current")


class _IfUfdModuleStatus_Type(Integer32):
    """Custom type ifUfdModuleStatus based on Integer32"""
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


_IfUfdModuleStatus_Type.__name__ = "Integer32"
_IfUfdModuleStatus_Object = MibScalar
ifUfdModuleStatus = _IfUfdModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 27),
    _IfUfdModuleStatus_Type()
)
ifUfdModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifUfdModuleStatus.setStatus("current")


class _IfSplitHorizonSysControl_Type(Integer32):
    """Custom type ifSplitHorizonSysControl based on Integer32"""
    defaultValue = 2

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


_IfSplitHorizonSysControl_Type.__name__ = "Integer32"
_IfSplitHorizonSysControl_Object = MibScalar
ifSplitHorizonSysControl = _IfSplitHorizonSysControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 28),
    _IfSplitHorizonSysControl_Type()
)
ifSplitHorizonSysControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSplitHorizonSysControl.setStatus("current")


class _IfSplitHorizonModStatus_Type(Integer32):
    """Custom type ifSplitHorizonModStatus based on Integer32"""
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


_IfSplitHorizonModStatus_Type.__name__ = "Integer32"
_IfSplitHorizonModStatus_Object = MibScalar
ifSplitHorizonModStatus = _IfSplitHorizonModStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 29),
    _IfSplitHorizonModStatus_Type()
)
ifSplitHorizonModStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifSplitHorizonModStatus.setStatus("current")
_IfUfdGroupTable_Object = MibTable
ifUfdGroupTable = _IfUfdGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30)
)
if mibBuilder.loadTexts:
    ifUfdGroupTable.setStatus("current")
_IfUfdGroupEntry_Object = MibTableRow
ifUfdGroupEntry = _IfUfdGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30, 1)
)
ifUfdGroupEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifUfdGroupId"),
)
if mibBuilder.loadTexts:
    ifUfdGroupEntry.setStatus("current")


class _IfUfdGroupId_Type(Integer32):
    """Custom type ifUfdGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IfUfdGroupId_Type.__name__ = "Integer32"
_IfUfdGroupId_Object = MibTableColumn
ifUfdGroupId = _IfUfdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30, 1, 1),
    _IfUfdGroupId_Type()
)
ifUfdGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifUfdGroupId.setStatus("current")


class _IfUfdGroupName_Type(DisplayString):
    """Custom type ifUfdGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IfUfdGroupName_Type.__name__ = "DisplayString"
_IfUfdGroupName_Object = MibTableColumn
ifUfdGroupName = _IfUfdGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30, 1, 2),
    _IfUfdGroupName_Type()
)
ifUfdGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifUfdGroupName.setStatus("current")


class _IfUfdGroupStatus_Type(Integer32):
    """Custom type ifUfdGroupStatus based on Integer32"""
    defaultValue = 2

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


_IfUfdGroupStatus_Type.__name__ = "Integer32"
_IfUfdGroupStatus_Object = MibTableColumn
ifUfdGroupStatus = _IfUfdGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30, 1, 3),
    _IfUfdGroupStatus_Type()
)
ifUfdGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifUfdGroupStatus.setStatus("current")
_IfUfdGroupUplinkPorts_Type = PortList
_IfUfdGroupUplinkPorts_Object = MibTableColumn
ifUfdGroupUplinkPorts = _IfUfdGroupUplinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30, 1, 4),
    _IfUfdGroupUplinkPorts_Type()
)
ifUfdGroupUplinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifUfdGroupUplinkPorts.setStatus("current")
_IfUfdGroupDownlinkPorts_Type = PortList
_IfUfdGroupDownlinkPorts_Object = MibTableColumn
ifUfdGroupDownlinkPorts = _IfUfdGroupDownlinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30, 1, 5),
    _IfUfdGroupDownlinkPorts_Type()
)
ifUfdGroupDownlinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifUfdGroupDownlinkPorts.setStatus("current")
_IfUfdGroupDesigUplinkPort_Type = InterfaceIndex
_IfUfdGroupDesigUplinkPort_Object = MibTableColumn
ifUfdGroupDesigUplinkPort = _IfUfdGroupDesigUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30, 1, 6),
    _IfUfdGroupDesigUplinkPort_Type()
)
ifUfdGroupDesigUplinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifUfdGroupDesigUplinkPort.setStatus("deprecated")


class _IfUfdGroupUplinkCount_Type(Integer32):
    """Custom type ifUfdGroupUplinkCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IfUfdGroupUplinkCount_Type.__name__ = "Integer32"
_IfUfdGroupUplinkCount_Object = MibTableColumn
ifUfdGroupUplinkCount = _IfUfdGroupUplinkCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30, 1, 7),
    _IfUfdGroupUplinkCount_Type()
)
ifUfdGroupUplinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifUfdGroupUplinkCount.setStatus("current")


class _IfUfdGroupDownlinkCount_Type(Integer32):
    """Custom type ifUfdGroupDownlinkCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IfUfdGroupDownlinkCount_Type.__name__ = "Integer32"
_IfUfdGroupDownlinkCount_Object = MibTableColumn
ifUfdGroupDownlinkCount = _IfUfdGroupDownlinkCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30, 1, 8),
    _IfUfdGroupDownlinkCount_Type()
)
ifUfdGroupDownlinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifUfdGroupDownlinkCount.setStatus("current")
_IfUfdGroupRowStatus_Type = RowStatus
_IfUfdGroupRowStatus_Object = MibTableColumn
ifUfdGroupRowStatus = _IfUfdGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 30, 1, 9),
    _IfUfdGroupRowStatus_Type()
)
ifUfdGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifUfdGroupRowStatus.setStatus("current")


class _IfLinkUpEnabledStatus_Type(Integer32):
    """Custom type ifLinkUpEnabledStatus based on Integer32"""
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


_IfLinkUpEnabledStatus_Type.__name__ = "Integer32"
_IfLinkUpEnabledStatus_Object = MibScalar
ifLinkUpEnabledStatus = _IfLinkUpEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 31),
    _IfLinkUpEnabledStatus_Type()
)
ifLinkUpEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifLinkUpEnabledStatus.setStatus("current")


class _IfOOBNode0SecondaryIpAddress_Type(IpAddress):
    """Custom type ifOOBNode0SecondaryIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IfOOBNode0SecondaryIpAddress_Type.__name__ = "IpAddress"
_IfOOBNode0SecondaryIpAddress_Object = MibScalar
ifOOBNode0SecondaryIpAddress = _IfOOBNode0SecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 32),
    _IfOOBNode0SecondaryIpAddress_Type()
)
ifOOBNode0SecondaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOOBNode0SecondaryIpAddress.setStatus("current")
_IfOOBNode0SecondaryIpMask_Type = IpAddress
_IfOOBNode0SecondaryIpMask_Object = MibScalar
ifOOBNode0SecondaryIpMask = _IfOOBNode0SecondaryIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 33),
    _IfOOBNode0SecondaryIpMask_Type()
)
ifOOBNode0SecondaryIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOOBNode0SecondaryIpMask.setStatus("current")


class _IfOOBNode1SecondaryIpAddress_Type(IpAddress):
    """Custom type ifOOBNode1SecondaryIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IfOOBNode1SecondaryIpAddress_Type.__name__ = "IpAddress"
_IfOOBNode1SecondaryIpAddress_Object = MibScalar
ifOOBNode1SecondaryIpAddress = _IfOOBNode1SecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 34),
    _IfOOBNode1SecondaryIpAddress_Type()
)
ifOOBNode1SecondaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOOBNode1SecondaryIpAddress.setStatus("current")
_IfOOBNode1SecondaryIpMask_Type = IpAddress
_IfOOBNode1SecondaryIpMask_Object = MibScalar
ifOOBNode1SecondaryIpMask = _IfOOBNode1SecondaryIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 35),
    _IfOOBNode1SecondaryIpMask_Type()
)
ifOOBNode1SecondaryIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOOBNode1SecondaryIpMask.setStatus("current")
_IfVlanIpTable_Object = MibTable
ifVlanIpTable = _IfVlanIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 36)
)
if mibBuilder.loadTexts:
    ifVlanIpTable.setStatus("current")
_IfVlanIpEntry_Object = MibTableRow
ifVlanIpEntry = _IfVlanIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 36, 1)
)
ifVlanIpEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ifVlanIpVlanId"),
)
if mibBuilder.loadTexts:
    ifVlanIpEntry.setStatus("current")
_IfVlanIpVlanId_Type = VlanId
_IfVlanIpVlanId_Object = MibTableColumn
ifVlanIpVlanId = _IfVlanIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 36, 1, 1),
    _IfVlanIpVlanId_Type()
)
ifVlanIpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifVlanIpVlanId.setStatus("current")
_IfVlanIpIfIndex_Type = InterfaceIndex
_IfVlanIpIfIndex_Object = MibTableColumn
ifVlanIpIfIndex = _IfVlanIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 36, 1, 2),
    _IfVlanIpIfIndex_Type()
)
ifVlanIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifVlanIpIfIndex.setStatus("current")


class _IfVlanIpAdminStatus_Type(Integer32):
    """Custom type ifVlanIpAdminStatus based on Integer32"""
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


_IfVlanIpAdminStatus_Type.__name__ = "Integer32"
_IfVlanIpAdminStatus_Object = MibTableColumn
ifVlanIpAdminStatus = _IfVlanIpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 36, 1, 3),
    _IfVlanIpAdminStatus_Type()
)
ifVlanIpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifVlanIpAdminStatus.setStatus("current")


class _IfVlanIpAddrAllocMethod_Type(Integer32):
    """Custom type ifVlanIpAddrAllocMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("dynamic", 2))
    )


_IfVlanIpAddrAllocMethod_Type.__name__ = "Integer32"
_IfVlanIpAddrAllocMethod_Object = MibTableColumn
ifVlanIpAddrAllocMethod = _IfVlanIpAddrAllocMethod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 36, 1, 4),
    _IfVlanIpAddrAllocMethod_Type()
)
ifVlanIpAddrAllocMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifVlanIpAddrAllocMethod.setStatus("current")
_IfVlanIpAddr_Type = IpAddress
_IfVlanIpAddr_Object = MibTableColumn
ifVlanIpAddr = _IfVlanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 36, 1, 5),
    _IfVlanIpAddr_Type()
)
ifVlanIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifVlanIpAddr.setStatus("current")
_IfVlanIpSubnetMask_Type = IpAddress
_IfVlanIpSubnetMask_Object = MibTableColumn
ifVlanIpSubnetMask = _IfVlanIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 36, 1, 6),
    _IfVlanIpSubnetMask_Type()
)
ifVlanIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifVlanIpSubnetMask.setStatus("current")
_IfVlanIpRowStatus_Type = RowStatus
_IfVlanIpRowStatus_Object = MibTableColumn
ifVlanIpRowStatus = _IfVlanIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 1, 36, 1, 10),
    _IfVlanIpRowStatus_Type()
)
ifVlanIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifVlanIpRowStatus.setStatus("current")
_Ff_ObjectIdentity = ObjectIdentity
ff = _Ff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2)
)


class _FfFastForwardingEnable_Type(TruthValue):
    """Custom type ffFastForwardingEnable based on TruthValue"""
    defaultValue = 2


_FfFastForwardingEnable_Type.__name__ = "TruthValue"
_FfFastForwardingEnable_Object = MibScalar
ffFastForwardingEnable = _FfFastForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 1),
    _FfFastForwardingEnable_Type()
)
ffFastForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffFastForwardingEnable.setStatus("deprecated")


class _FfCacheSize_Type(Integer32):
    """Custom type ffCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_FfCacheSize_Type.__name__ = "Integer32"
_FfCacheSize_Object = MibScalar
ffCacheSize = _FfCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 2),
    _FfCacheSize_Type()
)
ffCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffCacheSize.setStatus("deprecated")


class _FfIpChecksumValidationEnable_Type(TruthValue):
    """Custom type ffIpChecksumValidationEnable based on TruthValue"""
    defaultValue = 1


_FfIpChecksumValidationEnable_Type.__name__ = "TruthValue"
_FfIpChecksumValidationEnable_Object = MibScalar
ffIpChecksumValidationEnable = _FfIpChecksumValidationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 3),
    _FfIpChecksumValidationEnable_Type()
)
ffIpChecksumValidationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffIpChecksumValidationEnable.setStatus("deprecated")
_FfCachePurgeCount_Type = Counter32
_FfCachePurgeCount_Object = MibScalar
ffCachePurgeCount = _FfCachePurgeCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 4),
    _FfCachePurgeCount_Type()
)
ffCachePurgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCachePurgeCount.setStatus("deprecated")
_FfCacheLastPurgeTime_Type = TimeStamp
_FfCacheLastPurgeTime_Object = MibScalar
ffCacheLastPurgeTime = _FfCacheLastPurgeTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 5),
    _FfCacheLastPurgeTime_Type()
)
ffCacheLastPurgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCacheLastPurgeTime.setStatus("deprecated")


class _FfStaticEntryInvalidTrapEnable_Type(TruthValue):
    """Custom type ffStaticEntryInvalidTrapEnable based on TruthValue"""
    defaultValue = 1


_FfStaticEntryInvalidTrapEnable_Type.__name__ = "TruthValue"
_FfStaticEntryInvalidTrapEnable_Object = MibScalar
ffStaticEntryInvalidTrapEnable = _FfStaticEntryInvalidTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 6),
    _FfStaticEntryInvalidTrapEnable_Type()
)
ffStaticEntryInvalidTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ffStaticEntryInvalidTrapEnable.setStatus("deprecated")
_FfCurrentStaticEntryInvalidCount_Type = Counter32
_FfCurrentStaticEntryInvalidCount_Object = MibScalar
ffCurrentStaticEntryInvalidCount = _FfCurrentStaticEntryInvalidCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 7),
    _FfCurrentStaticEntryInvalidCount_Type()
)
ffCurrentStaticEntryInvalidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffCurrentStaticEntryInvalidCount.setStatus("deprecated")
_FfTotalEntryCount_Type = Counter32
_FfTotalEntryCount_Object = MibScalar
ffTotalEntryCount = _FfTotalEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 8),
    _FfTotalEntryCount_Type()
)
ffTotalEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffTotalEntryCount.setStatus("deprecated")
_FfStaticEntryCount_Type = Counter32
_FfStaticEntryCount_Object = MibScalar
ffStaticEntryCount = _FfStaticEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 9),
    _FfStaticEntryCount_Type()
)
ffStaticEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffStaticEntryCount.setStatus("deprecated")
_FfTotalPktsFastForwarded_Type = Counter32
_FfTotalPktsFastForwarded_Object = MibScalar
ffTotalPktsFastForwarded = _FfTotalPktsFastForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 10),
    _FfTotalPktsFastForwarded_Type()
)
ffTotalPktsFastForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffTotalPktsFastForwarded.setStatus("deprecated")
_FfHostCacheTable_Object = MibTable
ffHostCacheTable = _FfHostCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 11)
)
if mibBuilder.loadTexts:
    ffHostCacheTable.setStatus("deprecated")
_FfHostCacheEntry_Object = MibTableRow
ffHostCacheEntry = _FfHostCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 11, 1)
)
ffHostCacheEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "ffHostCacheDestAddr"),
)
if mibBuilder.loadTexts:
    ffHostCacheEntry.setStatus("deprecated")
_FfHostCacheDestAddr_Type = IpAddress
_FfHostCacheDestAddr_Object = MibTableColumn
ffHostCacheDestAddr = _FfHostCacheDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 11, 1, 1),
    _FfHostCacheDestAddr_Type()
)
ffHostCacheDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ffHostCacheDestAddr.setStatus("deprecated")
_FfHostCacheNextHopAddr_Type = IpAddress
_FfHostCacheNextHopAddr_Object = MibTableColumn
ffHostCacheNextHopAddr = _FfHostCacheNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 11, 1, 2),
    _FfHostCacheNextHopAddr_Type()
)
ffHostCacheNextHopAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ffHostCacheNextHopAddr.setStatus("deprecated")
_FfHostCacheIfIndex_Type = InterfaceIndex
_FfHostCacheIfIndex_Object = MibTableColumn
ffHostCacheIfIndex = _FfHostCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 11, 1, 3),
    _FfHostCacheIfIndex_Type()
)
ffHostCacheIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ffHostCacheIfIndex.setStatus("deprecated")


class _FfHostCacheNextHopMediaAddr_Type(OctetString):
    """Custom type ffHostCacheNextHopMediaAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_FfHostCacheNextHopMediaAddr_Type.__name__ = "OctetString"
_FfHostCacheNextHopMediaAddr_Object = MibTableColumn
ffHostCacheNextHopMediaAddr = _FfHostCacheNextHopMediaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 11, 1, 4),
    _FfHostCacheNextHopMediaAddr_Type()
)
ffHostCacheNextHopMediaAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ffHostCacheNextHopMediaAddr.setStatus("deprecated")
_FfHostCacheHits_Type = Counter32
_FfHostCacheHits_Object = MibTableColumn
ffHostCacheHits = _FfHostCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 11, 1, 5),
    _FfHostCacheHits_Type()
)
ffHostCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffHostCacheHits.setStatus("deprecated")
_FfHostCacheLastHitTime_Type = TimeStamp
_FfHostCacheLastHitTime_Object = MibTableColumn
ffHostCacheLastHitTime = _FfHostCacheLastHitTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 11, 1, 6),
    _FfHostCacheLastHitTime_Type()
)
ffHostCacheLastHitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ffHostCacheLastHitTime.setStatus("deprecated")


class _FfHostCacheEntryType_Type(Integer32):
    """Custom type ffHostCacheEntryType based on Integer32"""
    defaultValue = 1

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


_FfHostCacheEntryType_Type.__name__ = "Integer32"
_FfHostCacheEntryType_Object = MibTableColumn
ffHostCacheEntryType = _FfHostCacheEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 11, 1, 7),
    _FfHostCacheEntryType_Type()
)
ffHostCacheEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ffHostCacheEntryType.setStatus("deprecated")
_FfHostCacheRowStatus_Type = RowStatus
_FfHostCacheRowStatus_Object = MibTableColumn
ffHostCacheRowStatus = _FfHostCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 2, 11, 1, 8),
    _FfHostCacheRowStatus_Type()
)
ffHostCacheRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ffHostCacheRowStatus.setStatus("deprecated")
_Fm_ObjectIdentity = ObjectIdentity
fm = _Fm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 27, 3)
)


class _FmMemoryResourceTrapEnable_Type(TruthValue):
    """Custom type fmMemoryResourceTrapEnable based on TruthValue"""
    defaultValue = 1


_FmMemoryResourceTrapEnable_Type.__name__ = "TruthValue"
_FmMemoryResourceTrapEnable_Object = MibScalar
fmMemoryResourceTrapEnable = _FmMemoryResourceTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 3, 1),
    _FmMemoryResourceTrapEnable_Type()
)
fmMemoryResourceTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmMemoryResourceTrapEnable.setStatus("deprecated")


class _FmTimersResourceTrapEnable_Type(TruthValue):
    """Custom type fmTimersResourceTrapEnable based on TruthValue"""
    defaultValue = 1


_FmTimersResourceTrapEnable_Type.__name__ = "TruthValue"
_FmTimersResourceTrapEnable_Object = MibScalar
fmTimersResourceTrapEnable = _FmTimersResourceTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 3, 2),
    _FmTimersResourceTrapEnable_Type()
)
fmTimersResourceTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmTimersResourceTrapEnable.setStatus("deprecated")


class _FmTracingEnable_Type(Integer32):
    """Custom type fmTracingEnable based on Integer32"""
    defaultValue = 0


_FmTracingEnable_Type.__name__ = "Integer32"
_FmTracingEnable_Object = MibScalar
fmTracingEnable = _FmTracingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 3, 3),
    _FmTracingEnable_Type()
)
fmTracingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmTracingEnable.setStatus("deprecated")
_FmMemAllocFailCount_Type = Counter32
_FmMemAllocFailCount_Object = MibScalar
fmMemAllocFailCount = _FmMemAllocFailCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 3, 4),
    _FmMemAllocFailCount_Type()
)
fmMemAllocFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmMemAllocFailCount.setStatus("current")
_FmTimerReqFailCount_Type = Counter32
_FmTimerReqFailCount_Object = MibScalar
fmTimerReqFailCount = _FmTimerReqFailCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 3, 5),
    _FmTimerReqFailCount_Type()
)
fmTimerReqFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmTimerReqFailCount.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 27, 4)
)
_TrapPrefix_ObjectIdentity = ObjectIdentity
trapPrefix = _TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 27, 4, 0)
)
_Pa_ObjectIdentity = ObjectIdentity
pa = _Pa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5)
)
_FsPacketAnalyserTable_Object = MibTable
fsPacketAnalyserTable = _FsPacketAnalyserTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1)
)
if mibBuilder.loadTexts:
    fsPacketAnalyserTable.setStatus("current")
_FsPacketAnalyserEntry_Object = MibTableRow
fsPacketAnalyserEntry = _FsPacketAnalyserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1, 1)
)
fsPacketAnalyserEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "fsPacketAnalyserIndex"),
)
if mibBuilder.loadTexts:
    fsPacketAnalyserEntry.setStatus("current")
_FsPacketAnalyserIndex_Type = Unsigned32
_FsPacketAnalyserIndex_Object = MibTableColumn
fsPacketAnalyserIndex = _FsPacketAnalyserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1, 1, 1),
    _FsPacketAnalyserIndex_Type()
)
fsPacketAnalyserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPacketAnalyserIndex.setStatus("current")


class _FsPacketAnalyserWatchValue_Type(DisplayString):
    """Custom type fsPacketAnalyserWatchValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_FsPacketAnalyserWatchValue_Type.__name__ = "DisplayString"
_FsPacketAnalyserWatchValue_Object = MibTableColumn
fsPacketAnalyserWatchValue = _FsPacketAnalyserWatchValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1, 1, 2),
    _FsPacketAnalyserWatchValue_Type()
)
fsPacketAnalyserWatchValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPacketAnalyserWatchValue.setStatus("current")


class _FsPacketAnalyserWatchMask_Type(DisplayString):
    """Custom type fsPacketAnalyserWatchMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_FsPacketAnalyserWatchMask_Type.__name__ = "DisplayString"
_FsPacketAnalyserWatchMask_Object = MibTableColumn
fsPacketAnalyserWatchMask = _FsPacketAnalyserWatchMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1, 1, 3),
    _FsPacketAnalyserWatchMask_Type()
)
fsPacketAnalyserWatchMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPacketAnalyserWatchMask.setStatus("current")
_FsPacketAnalyserWatchPorts_Type = PortList
_FsPacketAnalyserWatchPorts_Object = MibTableColumn
fsPacketAnalyserWatchPorts = _FsPacketAnalyserWatchPorts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1, 1, 4),
    _FsPacketAnalyserWatchPorts_Type()
)
fsPacketAnalyserWatchPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPacketAnalyserWatchPorts.setStatus("current")
_FsPacketAnalyserMatchPorts_Type = PortList
_FsPacketAnalyserMatchPorts_Object = MibTableColumn
fsPacketAnalyserMatchPorts = _FsPacketAnalyserMatchPorts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1, 1, 5),
    _FsPacketAnalyserMatchPorts_Type()
)
fsPacketAnalyserMatchPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPacketAnalyserMatchPorts.setStatus("current")
_FsPacketAnalyserCounter_Type = Counter32
_FsPacketAnalyserCounter_Object = MibTableColumn
fsPacketAnalyserCounter = _FsPacketAnalyserCounter_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1, 1, 6),
    _FsPacketAnalyserCounter_Type()
)
fsPacketAnalyserCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPacketAnalyserCounter.setStatus("current")
_FsPacketAnalyserTime_Type = TimeTicks
_FsPacketAnalyserTime_Object = MibTableColumn
fsPacketAnalyserTime = _FsPacketAnalyserTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1, 1, 7),
    _FsPacketAnalyserTime_Type()
)
fsPacketAnalyserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPacketAnalyserTime.setStatus("current")
_FsPacketAnalyserCreateTime_Type = TimeTicks
_FsPacketAnalyserCreateTime_Object = MibTableColumn
fsPacketAnalyserCreateTime = _FsPacketAnalyserCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1, 1, 8),
    _FsPacketAnalyserCreateTime_Type()
)
fsPacketAnalyserCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPacketAnalyserCreateTime.setStatus("current")
_FsPacketAnalyserStatus_Type = RowStatus
_FsPacketAnalyserStatus_Object = MibTableColumn
fsPacketAnalyserStatus = _FsPacketAnalyserStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 1, 1, 9),
    _FsPacketAnalyserStatus_Type()
)
fsPacketAnalyserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPacketAnalyserStatus.setStatus("current")
_FsPacketTransmitterTable_Object = MibTable
fsPacketTransmitterTable = _FsPacketTransmitterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 2)
)
if mibBuilder.loadTexts:
    fsPacketTransmitterTable.setStatus("current")
_FsPacketTransmitterEntry_Object = MibTableRow
fsPacketTransmitterEntry = _FsPacketTransmitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 2, 1)
)
fsPacketTransmitterEntry.setIndexNames(
    (0, "ARICENT-CFA-MIB", "fsPacketTransmitterIndex"),
)
if mibBuilder.loadTexts:
    fsPacketTransmitterEntry.setStatus("current")
_FsPacketTransmitterIndex_Type = Unsigned32
_FsPacketTransmitterIndex_Object = MibTableColumn
fsPacketTransmitterIndex = _FsPacketTransmitterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 2, 1, 1),
    _FsPacketTransmitterIndex_Type()
)
fsPacketTransmitterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPacketTransmitterIndex.setStatus("current")


class _FsPacketTransmitterValue_Type(DisplayString):
    """Custom type fsPacketTransmitterValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_FsPacketTransmitterValue_Type.__name__ = "DisplayString"
_FsPacketTransmitterValue_Object = MibTableColumn
fsPacketTransmitterValue = _FsPacketTransmitterValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 2, 1, 2),
    _FsPacketTransmitterValue_Type()
)
fsPacketTransmitterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPacketTransmitterValue.setStatus("current")
_FsPacketTransmitterPort_Type = PortList
_FsPacketTransmitterPort_Object = MibTableColumn
fsPacketTransmitterPort = _FsPacketTransmitterPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 2, 1, 3),
    _FsPacketTransmitterPort_Type()
)
fsPacketTransmitterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPacketTransmitterPort.setStatus("current")
_FsPacketTransmitterInterval_Type = TimeTicks
_FsPacketTransmitterInterval_Object = MibTableColumn
fsPacketTransmitterInterval = _FsPacketTransmitterInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 2, 1, 4),
    _FsPacketTransmitterInterval_Type()
)
fsPacketTransmitterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPacketTransmitterInterval.setStatus("current")
_FsPacketTransmitterCount_Type = Unsigned32
_FsPacketTransmitterCount_Object = MibTableColumn
fsPacketTransmitterCount = _FsPacketTransmitterCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 2, 1, 5),
    _FsPacketTransmitterCount_Type()
)
fsPacketTransmitterCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPacketTransmitterCount.setStatus("current")
_FsPacketTransmitterStatus_Type = RowStatus
_FsPacketTransmitterStatus_Object = MibTableColumn
fsPacketTransmitterStatus = _FsPacketTransmitterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 27, 5, 2, 1, 6),
    _FsPacketTransmitterStatus_Type()
)
fsPacketTransmitterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPacketTransmitterStatus.setStatus("current")
ifMainEntry.registerAugmentions(
    ("ARICENT-CFA-MIB",
     "ifMainExtEntry")
)
ifMainExtEntry.setIndexNames(*ifMainEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("ARICENT-CFA-MIB",
     "ifHCErrorEntry")
)
ifHCErrorEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fmLowTimerResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 27, 4, 0, 1)
)
fmLowTimerResource.setObjects(
    ("ARICENT-CFA-MIB", "fmTimerReqFailCount")
)
if mibBuilder.loadTexts:
    fmLowTimerResource.setStatus(
        "deprecated"
    )

fmLowBufferResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 27, 4, 0, 2)
)
fmLowBufferResource.setObjects(
    ("ARICENT-CFA-MIB", "fmMemAllocFailCount")
)
if mibBuilder.loadTexts:
    fmLowBufferResource.setStatus(
        "deprecated"
    )

ffStaticEntryInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 27, 4, 0, 3)
)
ffStaticEntryInvalid.setObjects(
      *(("ARICENT-CFA-MIB", "ffHostCacheIfIndex"),
        ("ARICENT-CFA-MIB", "ffHostCacheEntryType"))
)
if mibBuilder.loadTexts:
    ffStaticEntryInvalid.setStatus(
        "deprecated"
    )

ifCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 27, 4, 0, 4)
)
ifCreated.setObjects(
    ("ARICENT-CFA-MIB", "ifMainIndex")
)
if mibBuilder.loadTexts:
    ifCreated.setStatus(
        "current"
    )

ifDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 27, 4, 0, 5)
)
ifDeleted.setObjects(
    ("ARICENT-CFA-MIB", "ifMainIndex")
)
if mibBuilder.loadTexts:
    ifDeleted.setStatus(
        "current"
    )

ifUfdEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 27, 4, 0, 6)
)
ifUfdEnabled.setObjects(
      *(("ARICENT-CFA-MIB", "ifMainIndex"),
        ("ARICENT-CFA-MIB", "ifMainUfdOperStatus"))
)
if mibBuilder.loadTexts:
    ifUfdEnabled.setStatus(
        "current"
    )

ifUfdErrorDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 27, 4, 0, 7)
)
ifUfdErrorDisabled.setObjects(
      *(("ARICENT-CFA-MIB", "ifMainIndex"),
        ("ARICENT-CFA-MIB", "ifMainUfdOperStatus"))
)
if mibBuilder.loadTexts:
    ifUfdErrorDisabled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-CFA-MIB",
    **{"fscfa": fscfa,
       "if": _pysmi_if,
       "ifMaxInterfaces": ifMaxInterfaces,
       "ifMaxPhysInterfaces": ifMaxPhysInterfaces,
       "ifAvailableIndex": ifAvailableIndex,
       "ifMainTable": ifMainTable,
       "ifMainEntry": ifMainEntry,
       "ifMainIndex": ifMainIndex,
       "ifMainType": ifMainType,
       "ifMainMtu": ifMainMtu,
       "ifMainAdminStatus": ifMainAdminStatus,
       "ifMainOperStatus": ifMainOperStatus,
       "ifMainEncapType": ifMainEncapType,
       "ifMainBrgPortType": ifMainBrgPortType,
       "ifMainRowStatus": ifMainRowStatus,
       "ifMainSubType": ifMainSubType,
       "ifMainNetworkType": ifMainNetworkType,
       "ifMainWanType": ifMainWanType,
       "ifMainDesc": ifMainDesc,
       "ifMainStorageType": ifMainStorageType,
       "ifMainExtSubType": ifMainExtSubType,
       "ifMainPortRole": ifMainPortRole,
       "ifMainUfdOperStatus": ifMainUfdOperStatus,
       "ifMainUfdGroupId": ifMainUfdGroupId,
       "ifMainUfdDownlinkDisabledCount": ifMainUfdDownlinkDisabledCount,
       "ifMainUfdDownlinkEnabledCount": ifMainUfdDownlinkEnabledCount,
       "ifMainDesigUplinkStatus": ifMainDesigUplinkStatus,
       "ifMainEncapDot1qVlanId": ifMainEncapDot1qVlanId,
       "ifMainNeighborId": ifMainNeighborId,
       "ifMainName": ifMainName,
       "ifMainPrevDesc": ifMainPrevDesc,
       "ifIpTable": ifIpTable,
       "ifIpEntry": ifIpEntry,
       "ifIpAddrAllocMethod": ifIpAddrAllocMethod,
       "ifIpAddr": ifIpAddr,
       "ifIpSubnetMask": ifIpSubnetMask,
       "ifIpBroadcastAddr": ifIpBroadcastAddr,
       "ifIpForwardingEnable": ifIpForwardingEnable,
       "ifIpAddrAllocProtocol": ifIpAddrAllocProtocol,
       "ifIpDestMacAddress": ifIpDestMacAddress,
       "ifIpUnnumAssocIPIf": ifIpUnnumAssocIPIf,
       "ifIpIntfStatsEnable": ifIpIntfStatsEnable,
       "ifIpPortVlanId": ifIpPortVlanId,
       "ifWanTable": ifWanTable,
       "ifWanEntry": ifWanEntry,
       "ifWanInterfaceType": ifWanInterfaceType,
       "ifWanConnectionType": ifWanConnectionType,
       "ifWanVirtualPathId": ifWanVirtualPathId,
       "ifWanVirtualCircuitId": ifWanVirtualCircuitId,
       "ifWanPeerMediaAddress": ifWanPeerMediaAddress,
       "ifWanSustainedSpeed": ifWanSustainedSpeed,
       "ifWanPeakSpeed": ifWanPeakSpeed,
       "ifWanMaxBurstSize": ifWanMaxBurstSize,
       "ifWanIpQosProfileIndex": ifWanIpQosProfileIndex,
       "ifWanIdleTimeout": ifWanIdleTimeout,
       "ifWanPeerIpAddr": ifWanPeerIpAddr,
       "ifWanRtpHdrComprEnable": ifWanRtpHdrComprEnable,
       "ifWanPersistence": ifWanPersistence,
       "ifAutoCktProfileTable": ifAutoCktProfileTable,
       "ifAutoProfileEntry": ifAutoProfileEntry,
       "ifAutoProfileIfIndex": ifAutoProfileIfIndex,
       "ifAutoProfileIfType": ifAutoProfileIfType,
       "ifAutoProfileIpAddrAllocMethod": ifAutoProfileIpAddrAllocMethod,
       "ifAutoProfileDefIpSubnetMask": ifAutoProfileDefIpSubnetMask,
       "ifAutoProfileDefIpBroadcastAddr": ifAutoProfileDefIpBroadcastAddr,
       "ifAutoProfileIdleTimeout": ifAutoProfileIdleTimeout,
       "ifAutoProfileEncapType": ifAutoProfileEncapType,
       "ifAutoProfileIpQosProfileIndex": ifAutoProfileIpQosProfileIndex,
       "ifAutoProfileRowStatus": ifAutoProfileRowStatus,
       "ifIvrTable": ifIvrTable,
       "ifIvrEntry": ifIvrEntry,
       "ifIvrBridgedIface": ifIvrBridgedIface,
       "ifSetMgmtVlanList": ifSetMgmtVlanList,
       "ifResetMgmtVlanList": ifResetMgmtVlanList,
       "ifSecondaryIpAddressTable": ifSecondaryIpAddressTable,
       "ifSecondaryIpAddressEntry": ifSecondaryIpAddressEntry,
       "ifSecondaryIpAddress": ifSecondaryIpAddress,
       "ifSecondaryIpSubnetMask": ifSecondaryIpSubnetMask,
       "ifSecondaryIpBroadcastAddr": ifSecondaryIpBroadcastAddr,
       "ifSecondaryIpRowStatus": ifSecondaryIpRowStatus,
       "ifMainExtTable": ifMainExtTable,
       "ifMainExtEntry": ifMainExtEntry,
       "ifMainExtMacAddress": ifMainExtMacAddress,
       "ifMainExtSysSpecificPortID": ifMainExtSysSpecificPortID,
       "ifMainExtInterfaceType": ifMainExtInterfaceType,
       "ifMainExtPortSecState": ifMainExtPortSecState,
       "ifMainExtInPkts": ifMainExtInPkts,
       "ifMainExtLinkUpEnabledStatus": ifMainExtLinkUpEnabledStatus,
       "ifMainExtLinkUpDelayTimer": ifMainExtLinkUpDelayTimer,
       "ifMainExtLinkUpRemainingTime": ifMainExtLinkUpRemainingTime,
       "ifCustTLVTable": ifCustTLVTable,
       "ifCustTLVEntry": ifCustTLVEntry,
       "ifCustTLVType": ifCustTLVType,
       "ifCustTLVLength": ifCustTLVLength,
       "ifCustTLVValue": ifCustTLVValue,
       "ifCustTLVRowStatus": ifCustTLVRowStatus,
       "ifCustOpaqueAttrTable": ifCustOpaqueAttrTable,
       "ifCustOpaqueAttrEntry": ifCustOpaqueAttrEntry,
       "ifCustOpaqueAttributeID": ifCustOpaqueAttributeID,
       "ifCustOpaqueAttribute": ifCustOpaqueAttribute,
       "ifCustOpaqueRowStatus": ifCustOpaqueRowStatus,
       "ifBridgeILanIfTable": ifBridgeILanIfTable,
       "ifBridgeILanIfEntry": ifBridgeILanIfEntry,
       "ifBridgeILanIfStatus": ifBridgeILanIfStatus,
       "ifTypeProtoDenyTable": ifTypeProtoDenyTable,
       "ifTypeProtoDenyEntry": ifTypeProtoDenyEntry,
       "ifTypeProtoDenyContextId": ifTypeProtoDenyContextId,
       "ifTypeProtoDenyMainType": ifTypeProtoDenyMainType,
       "ifTypeProtoDenyBrgPortType": ifTypeProtoDenyBrgPortType,
       "ifTypeProtoDenyProtocol": ifTypeProtoDenyProtocol,
       "ifTypeProtoDenyRowStatus": ifTypeProtoDenyRowStatus,
       "ifmDebug": ifmDebug,
       "ifIvrMappingTable": ifIvrMappingTable,
       "ifIvrMappingEntry": ifIvrMappingEntry,
       "ifIvrAssociatedVlan": ifIvrAssociatedVlan,
       "ifIvrMappingRowStatus": ifIvrMappingRowStatus,
       "ifHCErrorTable": ifHCErrorTable,
       "ifHCErrorEntry": ifHCErrorEntry,
       "ifHCInDiscards": ifHCInDiscards,
       "ifHCInErrors": ifHCInErrors,
       "ifHCInUnknownProtos": ifHCInUnknownProtos,
       "ifHCOutDiscards": ifHCOutDiscards,
       "ifHCOutErrors": ifHCOutErrors,
       "ifSecurityBridging": ifSecurityBridging,
       "ifSetSecVlanList": ifSetSecVlanList,
       "ifResetSecVlanList": ifResetSecVlanList,
       "ifSecIvrIfIndex": ifSecIvrIfIndex,
       "ifAvailableIndexTable": ifAvailableIndexTable,
       "ifAvailableIndexEntry": ifAvailableIndexEntry,
       "ifAvailableFreeIndex": ifAvailableFreeIndex,
       "ifACTable": ifACTable,
       "ifACEntry": ifACEntry,
       "ifACPortIdentifier": ifACPortIdentifier,
       "ifACCustomerVlan": ifACCustomerVlan,
       "ifUfdSystemControl": ifUfdSystemControl,
       "ifUfdModuleStatus": ifUfdModuleStatus,
       "ifSplitHorizonSysControl": ifSplitHorizonSysControl,
       "ifSplitHorizonModStatus": ifSplitHorizonModStatus,
       "ifUfdGroupTable": ifUfdGroupTable,
       "ifUfdGroupEntry": ifUfdGroupEntry,
       "ifUfdGroupId": ifUfdGroupId,
       "ifUfdGroupName": ifUfdGroupName,
       "ifUfdGroupStatus": ifUfdGroupStatus,
       "ifUfdGroupUplinkPorts": ifUfdGroupUplinkPorts,
       "ifUfdGroupDownlinkPorts": ifUfdGroupDownlinkPorts,
       "ifUfdGroupDesigUplinkPort": ifUfdGroupDesigUplinkPort,
       "ifUfdGroupUplinkCount": ifUfdGroupUplinkCount,
       "ifUfdGroupDownlinkCount": ifUfdGroupDownlinkCount,
       "ifUfdGroupRowStatus": ifUfdGroupRowStatus,
       "ifLinkUpEnabledStatus": ifLinkUpEnabledStatus,
       "ifOOBNode0SecondaryIpAddress": ifOOBNode0SecondaryIpAddress,
       "ifOOBNode0SecondaryIpMask": ifOOBNode0SecondaryIpMask,
       "ifOOBNode1SecondaryIpAddress": ifOOBNode1SecondaryIpAddress,
       "ifOOBNode1SecondaryIpMask": ifOOBNode1SecondaryIpMask,
       "ifVlanIpTable": ifVlanIpTable,
       "ifVlanIpEntry": ifVlanIpEntry,
       "ifVlanIpVlanId": ifVlanIpVlanId,
       "ifVlanIpIfIndex": ifVlanIpIfIndex,
       "ifVlanIpAdminStatus": ifVlanIpAdminStatus,
       "ifVlanIpAddrAllocMethod": ifVlanIpAddrAllocMethod,
       "ifVlanIpAddr": ifVlanIpAddr,
       "ifVlanIpSubnetMask": ifVlanIpSubnetMask,
       "ifVlanIpRowStatus": ifVlanIpRowStatus,
       "ff": ff,
       "ffFastForwardingEnable": ffFastForwardingEnable,
       "ffCacheSize": ffCacheSize,
       "ffIpChecksumValidationEnable": ffIpChecksumValidationEnable,
       "ffCachePurgeCount": ffCachePurgeCount,
       "ffCacheLastPurgeTime": ffCacheLastPurgeTime,
       "ffStaticEntryInvalidTrapEnable": ffStaticEntryInvalidTrapEnable,
       "ffCurrentStaticEntryInvalidCount": ffCurrentStaticEntryInvalidCount,
       "ffTotalEntryCount": ffTotalEntryCount,
       "ffStaticEntryCount": ffStaticEntryCount,
       "ffTotalPktsFastForwarded": ffTotalPktsFastForwarded,
       "ffHostCacheTable": ffHostCacheTable,
       "ffHostCacheEntry": ffHostCacheEntry,
       "ffHostCacheDestAddr": ffHostCacheDestAddr,
       "ffHostCacheNextHopAddr": ffHostCacheNextHopAddr,
       "ffHostCacheIfIndex": ffHostCacheIfIndex,
       "ffHostCacheNextHopMediaAddr": ffHostCacheNextHopMediaAddr,
       "ffHostCacheHits": ffHostCacheHits,
       "ffHostCacheLastHitTime": ffHostCacheLastHitTime,
       "ffHostCacheEntryType": ffHostCacheEntryType,
       "ffHostCacheRowStatus": ffHostCacheRowStatus,
       "fm": fm,
       "fmMemoryResourceTrapEnable": fmMemoryResourceTrapEnable,
       "fmTimersResourceTrapEnable": fmTimersResourceTrapEnable,
       "fmTracingEnable": fmTracingEnable,
       "fmMemAllocFailCount": fmMemAllocFailCount,
       "fmTimerReqFailCount": fmTimerReqFailCount,
       "traps": traps,
       "trapPrefix": trapPrefix,
       "fmLowTimerResource": fmLowTimerResource,
       "fmLowBufferResource": fmLowBufferResource,
       "ffStaticEntryInvalid": ffStaticEntryInvalid,
       "ifCreated": ifCreated,
       "ifDeleted": ifDeleted,
       "ifUfdEnabled": ifUfdEnabled,
       "ifUfdErrorDisabled": ifUfdErrorDisabled,
       "pa": pa,
       "fsPacketAnalyserTable": fsPacketAnalyserTable,
       "fsPacketAnalyserEntry": fsPacketAnalyserEntry,
       "fsPacketAnalyserIndex": fsPacketAnalyserIndex,
       "fsPacketAnalyserWatchValue": fsPacketAnalyserWatchValue,
       "fsPacketAnalyserWatchMask": fsPacketAnalyserWatchMask,
       "fsPacketAnalyserWatchPorts": fsPacketAnalyserWatchPorts,
       "fsPacketAnalyserMatchPorts": fsPacketAnalyserMatchPorts,
       "fsPacketAnalyserCounter": fsPacketAnalyserCounter,
       "fsPacketAnalyserTime": fsPacketAnalyserTime,
       "fsPacketAnalyserCreateTime": fsPacketAnalyserCreateTime,
       "fsPacketAnalyserStatus": fsPacketAnalyserStatus,
       "fsPacketTransmitterTable": fsPacketTransmitterTable,
       "fsPacketTransmitterEntry": fsPacketTransmitterEntry,
       "fsPacketTransmitterIndex": fsPacketTransmitterIndex,
       "fsPacketTransmitterValue": fsPacketTransmitterValue,
       "fsPacketTransmitterPort": fsPacketTransmitterPort,
       "fsPacketTransmitterInterval": fsPacketTransmitterInterval,
       "fsPacketTransmitterCount": fsPacketTransmitterCount,
       "fsPacketTransmitterStatus": fsPacketTransmitterStatus}
)
