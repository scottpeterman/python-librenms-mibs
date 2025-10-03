# SNMP MIB module (LINKSYS-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-LLDP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:09:25 2025
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "LINKSYS-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

(rnd,
 rndNotifications) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd",
    "rndNotifications")

(LldpXMedCapabilities,) = mibBuilder.importSymbols(
    "LLDP-EXT-MED-MIB",
    "LldpXMedCapabilities")

(LldpManAddress,
 LldpPortList,
 LldpPortNumber,
 lldpRemIndex,
 lldpRemLocalPortNum,
 lldpRemTimeMark) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpManAddress",
    "LldpPortList",
    "LldpPortNumber",
    "lldpRemIndex",
    "lldpRemLocalPortNum",
    "lldpRemTimeMark")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

rlLldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110)
)
if mibBuilder.loadTexts:
    rlLldp.setRevisions(
        ("2005-06-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PolicyNumber(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )



class PolicyContainerAppType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("unknown", 0),
          ("voice", 1),
          ("voiceSignaling", 2),
          ("guestVoice", 3),
          ("guestVoiceSignaling", 4),
          ("softPhoneVoice", 5),
          ("videoconferencing", 6),
          ("streamingVideo", 7),
          ("videoSignaling", 8))
    )



class PolicyAppVoiceUpdateMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("auto", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlLldpObjects_ObjectIdentity = ObjectIdentity
rlLldpObjects = _RlLldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1)
)
_RlLldpConfig_ObjectIdentity = ObjectIdentity
rlLldpConfig = _RlLldpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1)
)
_RlLldpEnabled_Type = TruthValue
_RlLldpEnabled_Object = MibScalar
rlLldpEnabled = _RlLldpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 1),
    _RlLldpEnabled_Type()
)
rlLldpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpEnabled.setStatus("current")


class _RlLldpClearRx_Type(PortList):
    """Custom type rlLldpClearRx based on PortList"""
    defaultHexValue = ""


_RlLldpClearRx_Type.__name__ = "PortList"
_RlLldpClearRx_Object = MibScalar
rlLldpClearRx = _RlLldpClearRx_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 2),
    _RlLldpClearRx_Type()
)
rlLldpClearRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpClearRx.setStatus("current")


class _RlLldpDuMode_Type(Integer32):
    """Custom type rlLldpDuMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filtering", 1),
          ("flooding", 2))
    )


_RlLldpDuMode_Type.__name__ = "Integer32"
_RlLldpDuMode_Object = MibScalar
rlLldpDuMode = _RlLldpDuMode_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 3),
    _RlLldpDuMode_Type()
)
rlLldpDuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpDuMode.setStatus("current")
_RlLldpAutoAdvLocPortManAddrTable_Object = MibTable
rlLldpAutoAdvLocPortManAddrTable = _RlLldpAutoAdvLocPortManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rlLldpAutoAdvLocPortManAddrTable.setStatus("current")
_RlLldpAutoAdvLocPortManAddrEntry_Object = MibTableRow
rlLldpAutoAdvLocPortManAddrEntry = _RlLldpAutoAdvLocPortManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 4, 1)
)
rlLldpAutoAdvLocPortManAddrEntry.setIndexNames(
    (0, "LINKSYS-LLDP-MIB", "rlLldpAutoAdvLocPortNum"),
)
if mibBuilder.loadTexts:
    rlLldpAutoAdvLocPortManAddrEntry.setStatus("current")
_RlLldpAutoAdvLocPortNum_Type = LldpPortNumber
_RlLldpAutoAdvLocPortNum_Object = MibTableColumn
rlLldpAutoAdvLocPortNum = _RlLldpAutoAdvLocPortNum_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 4, 1, 1),
    _RlLldpAutoAdvLocPortNum_Type()
)
rlLldpAutoAdvLocPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLldpAutoAdvLocPortNum.setStatus("current")


class _RlLldpAutoAdvManAddrOwnerIfId_Type(Integer32):
    """Custom type rlLldpAutoAdvManAddrOwnerIfId based on Integer32"""
    defaultValue = 0


_RlLldpAutoAdvManAddrOwnerIfId_Type.__name__ = "Integer32"
_RlLldpAutoAdvManAddrOwnerIfId_Object = MibTableColumn
rlLldpAutoAdvManAddrOwnerIfId = _RlLldpAutoAdvManAddrOwnerIfId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 4, 1, 2),
    _RlLldpAutoAdvManAddrOwnerIfId_Type()
)
rlLldpAutoAdvManAddrOwnerIfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpAutoAdvManAddrOwnerIfId.setStatus("current")


class _RlLldpAutoAdvManAddrNone_Type(TruthValue):
    """Custom type rlLldpAutoAdvManAddrNone based on TruthValue"""
    defaultValue = 2


_RlLldpAutoAdvManAddrNone_Type.__name__ = "TruthValue"
_RlLldpAutoAdvManAddrNone_Object = MibTableColumn
rlLldpAutoAdvManAddrNone = _RlLldpAutoAdvManAddrNone_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 4, 1, 3),
    _RlLldpAutoAdvManAddrNone_Type()
)
rlLldpAutoAdvManAddrNone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpAutoAdvManAddrNone.setStatus("current")
_RlLldpAutoAdvManAddrSubtype_Type = AddressFamilyNumbers
_RlLldpAutoAdvManAddrSubtype_Object = MibTableColumn
rlLldpAutoAdvManAddrSubtype = _RlLldpAutoAdvManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 4, 1, 4),
    _RlLldpAutoAdvManAddrSubtype_Type()
)
rlLldpAutoAdvManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpAutoAdvManAddrSubtype.setStatus("current")
_RlLldpAutoAdvManAddr_Type = LldpManAddress
_RlLldpAutoAdvManAddr_Object = MibTableColumn
rlLldpAutoAdvManAddr = _RlLldpAutoAdvManAddr_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 4, 1, 5),
    _RlLldpAutoAdvManAddr_Type()
)
rlLldpAutoAdvManAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpAutoAdvManAddr.setStatus("current")
_RlLldpAutoAdvPortsStatus_Type = RowStatus
_RlLldpAutoAdvPortsStatus_Object = MibTableColumn
rlLldpAutoAdvPortsStatus = _RlLldpAutoAdvPortsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 4, 1, 6),
    _RlLldpAutoAdvPortsStatus_Type()
)
rlLldpAutoAdvPortsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpAutoAdvPortsStatus.setStatus("current")


class _RlLldpChassisIdSubtype_Type(Integer32):
    """Custom type rlLldpChassisIdSubtype based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 4),
          ("local", 7))
    )


_RlLldpChassisIdSubtype_Type.__name__ = "Integer32"
_RlLldpChassisIdSubtype_Object = MibScalar
rlLldpChassisIdSubtype = _RlLldpChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 1, 5),
    _RlLldpChassisIdSubtype_Type()
)
rlLldpChassisIdSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpChassisIdSubtype.setStatus("current")
_RlLldpXMedConfig_ObjectIdentity = ObjectIdentity
rlLldpXMedConfig = _RlLldpXMedConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2)
)
_RlLldpXMedLocMediaPolicyContainerTable_Object = MibTable
rlLldpXMedLocMediaPolicyContainerTable = _RlLldpXMedLocMediaPolicyContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerTable.setStatus("current")
_RlLldpXMedLocMediaPolicyContainerEntry_Object = MibTableRow
rlLldpXMedLocMediaPolicyContainerEntry = _RlLldpXMedLocMediaPolicyContainerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1, 1)
)
rlLldpXMedLocMediaPolicyContainerEntry.setIndexNames(
    (0, "LINKSYS-LLDP-MIB", "rlLldpXMedLocMediaPolicyContainerIndex"),
)
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerEntry.setStatus("current")
_RlLldpXMedLocMediaPolicyContainerIndex_Type = PolicyNumber
_RlLldpXMedLocMediaPolicyContainerIndex_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerIndex = _RlLldpXMedLocMediaPolicyContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1, 1, 1),
    _RlLldpXMedLocMediaPolicyContainerIndex_Type()
)
rlLldpXMedLocMediaPolicyContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerIndex.setStatus("current")
_RlLldpXMedLocMediaPolicyContainerAppType_Type = PolicyContainerAppType
_RlLldpXMedLocMediaPolicyContainerAppType_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerAppType = _RlLldpXMedLocMediaPolicyContainerAppType_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1, 1, 2),
    _RlLldpXMedLocMediaPolicyContainerAppType_Type()
)
rlLldpXMedLocMediaPolicyContainerAppType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerAppType.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerVlanID_Type(Integer32):
    """Custom type rlLldpXMedLocMediaPolicyContainerVlanID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_RlLldpXMedLocMediaPolicyContainerVlanID_Type.__name__ = "Integer32"
_RlLldpXMedLocMediaPolicyContainerVlanID_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerVlanID = _RlLldpXMedLocMediaPolicyContainerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1, 1, 3),
    _RlLldpXMedLocMediaPolicyContainerVlanID_Type()
)
rlLldpXMedLocMediaPolicyContainerVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerVlanID.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerPriority_Type(Integer32):
    """Custom type rlLldpXMedLocMediaPolicyContainerPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlLldpXMedLocMediaPolicyContainerPriority_Type.__name__ = "Integer32"
_RlLldpXMedLocMediaPolicyContainerPriority_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerPriority = _RlLldpXMedLocMediaPolicyContainerPriority_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1, 1, 4),
    _RlLldpXMedLocMediaPolicyContainerPriority_Type()
)
rlLldpXMedLocMediaPolicyContainerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerPriority.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerDscp_Type(Dscp):
    """Custom type rlLldpXMedLocMediaPolicyContainerDscp based on Dscp"""
    defaultValue = 0


_RlLldpXMedLocMediaPolicyContainerDscp_Type.__name__ = "Dscp"
_RlLldpXMedLocMediaPolicyContainerDscp_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerDscp = _RlLldpXMedLocMediaPolicyContainerDscp_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1, 1, 5),
    _RlLldpXMedLocMediaPolicyContainerDscp_Type()
)
rlLldpXMedLocMediaPolicyContainerDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerDscp.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerUnknown_Type(TruthValue):
    """Custom type rlLldpXMedLocMediaPolicyContainerUnknown based on TruthValue"""
    defaultValue = 2


_RlLldpXMedLocMediaPolicyContainerUnknown_Type.__name__ = "TruthValue"
_RlLldpXMedLocMediaPolicyContainerUnknown_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerUnknown = _RlLldpXMedLocMediaPolicyContainerUnknown_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1, 1, 6),
    _RlLldpXMedLocMediaPolicyContainerUnknown_Type()
)
rlLldpXMedLocMediaPolicyContainerUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerUnknown.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerTagged_Type(TruthValue):
    """Custom type rlLldpXMedLocMediaPolicyContainerTagged based on TruthValue"""
    defaultValue = 2


_RlLldpXMedLocMediaPolicyContainerTagged_Type.__name__ = "TruthValue"
_RlLldpXMedLocMediaPolicyContainerTagged_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerTagged = _RlLldpXMedLocMediaPolicyContainerTagged_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1, 1, 7),
    _RlLldpXMedLocMediaPolicyContainerTagged_Type()
)
rlLldpXMedLocMediaPolicyContainerTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerTagged.setStatus("current")


class _RlLldpXMedLocMediaPolicyContainerPorts_Type(PortList):
    """Custom type rlLldpXMedLocMediaPolicyContainerPorts based on PortList"""
    defaultHexValue = ""


_RlLldpXMedLocMediaPolicyContainerPorts_Type.__name__ = "PortList"
_RlLldpXMedLocMediaPolicyContainerPorts_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerPorts = _RlLldpXMedLocMediaPolicyContainerPorts_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1, 1, 8),
    _RlLldpXMedLocMediaPolicyContainerPorts_Type()
)
rlLldpXMedLocMediaPolicyContainerPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerPorts.setStatus("current")
_RlLldpXMedLocMediaPolicyContainerRowStatus_Type = RowStatus
_RlLldpXMedLocMediaPolicyContainerRowStatus_Object = MibTableColumn
rlLldpXMedLocMediaPolicyContainerRowStatus = _RlLldpXMedLocMediaPolicyContainerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 2, 1, 1, 9),
    _RlLldpXMedLocMediaPolicyContainerRowStatus_Type()
)
rlLldpXMedLocMediaPolicyContainerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedLocMediaPolicyContainerRowStatus.setStatus("current")
_RlLldpTLVsTxOverloadingTable_Object = MibTable
rlLldpTLVsTxOverloadingTable = _RlLldpTLVsTxOverloadingTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 3)
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingTable.setStatus("current")
_RlLldpTLVsTxOverloadingEntry_Object = MibTableRow
rlLldpTLVsTxOverloadingEntry = _RlLldpTLVsTxOverloadingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 3, 1)
)
rlLldpTLVsTxOverloadingEntry.setIndexNames(
    (0, "LINKSYS-LLDP-MIB", "rlLldpTxOverloadingPortNum"),
    (0, "LINKSYS-LLDP-MIB", "rlLldpTxOverloadingIndex"),
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingEntry.setStatus("current")
_RlLldpTxOverloadingPortNum_Type = LldpPortNumber
_RlLldpTxOverloadingPortNum_Object = MibTableColumn
rlLldpTxOverloadingPortNum = _RlLldpTxOverloadingPortNum_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 3, 1, 1),
    _RlLldpTxOverloadingPortNum_Type()
)
rlLldpTxOverloadingPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLldpTxOverloadingPortNum.setStatus("current")
_RlLldpTxOverloadingIndex_Type = Unsigned32
_RlLldpTxOverloadingIndex_Object = MibTableColumn
rlLldpTxOverloadingIndex = _RlLldpTxOverloadingIndex_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 3, 1, 2),
    _RlLldpTxOverloadingIndex_Type()
)
rlLldpTxOverloadingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlLldpTxOverloadingIndex.setStatus("current")


class _RlLldpTxOverloadingGroupId_Type(Integer32):
    """Custom type rlLldpTxOverloadingGroupId based on Integer32"""
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
        *(("mandatory", 1),
          ("optional", 2),
          ("medCap", 3),
          ("medLocation", 4),
          ("medNetPolicy", 5),
          ("medPoe", 6),
          ("medInventory", 7),
          ("xDot3", 8),
          ("xDot1", 9),
          ("dcbx", 10))
    )


_RlLldpTxOverloadingGroupId_Type.__name__ = "Integer32"
_RlLldpTxOverloadingGroupId_Object = MibTableColumn
rlLldpTxOverloadingGroupId = _RlLldpTxOverloadingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 3, 1, 3),
    _RlLldpTxOverloadingGroupId_Type()
)
rlLldpTxOverloadingGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTxOverloadingGroupId.setStatus("current")
_RlLldpTLVsTxSize_Type = Unsigned32
_RlLldpTLVsTxSize_Object = MibTableColumn
rlLldpTLVsTxSize = _RlLldpTLVsTxSize_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 3, 1, 4),
    _RlLldpTLVsTxSize_Type()
)
rlLldpTLVsTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTLVsTxSize.setStatus("current")
_RlLldpTLVsTxGroupOverloading_Type = TruthValue
_RlLldpTLVsTxGroupOverloading_Object = MibTableColumn
rlLldpTLVsTxGroupOverloading = _RlLldpTLVsTxGroupOverloading_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 3, 1, 5),
    _RlLldpTLVsTxGroupOverloading_Type()
)
rlLldpTLVsTxGroupOverloading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTLVsTxGroupOverloading.setStatus("current")
_RlLldpTLVsTxLeftSize_Type = Unsigned32
_RlLldpTLVsTxLeftSize_Object = MibTableColumn
rlLldpTLVsTxLeftSize = _RlLldpTLVsTxLeftSize_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 3, 1, 6),
    _RlLldpTLVsTxLeftSize_Type()
)
rlLldpTLVsTxLeftSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTLVsTxLeftSize.setStatus("current")
_RlLldpTLVsTxOverloadingSizeTable_Object = MibTable
rlLldpTLVsTxOverloadingSizeTable = _RlLldpTLVsTxOverloadingSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 4)
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingSizeTable.setStatus("current")
_RlLldpTLVsTxOverloadingSizeEntry_Object = MibTableRow
rlLldpTLVsTxOverloadingSizeEntry = _RlLldpTLVsTxOverloadingSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 4, 1)
)
rlLldpTLVsTxOverloadingSizeEntry.setIndexNames(
    (0, "LINKSYS-LLDP-MIB", "rlLldpTxOverloadingPortNum"),
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingSizeEntry.setStatus("current")
_RlLldpTotalTLVsTxSize_Type = Unsigned32
_RlLldpTotalTLVsTxSize_Object = MibTableColumn
rlLldpTotalTLVsTxSize = _RlLldpTotalTLVsTxSize_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 4, 1, 2),
    _RlLldpTotalTLVsTxSize_Type()
)
rlLldpTotalTLVsTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTotalTLVsTxSize.setStatus("current")
_RlLldpTLVsTxOverloading_Type = TruthValue
_RlLldpTLVsTxOverloading_Object = MibTableColumn
rlLldpTLVsTxOverloading = _RlLldpTLVsTxOverloading_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 4, 1, 3),
    _RlLldpTLVsTxOverloading_Type()
)
rlLldpTLVsTxOverloading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloading.setStatus("current")
_RlLldpLeftTLVsTxSize_Type = Unsigned32
_RlLldpLeftTLVsTxSize_Object = MibTableColumn
rlLldpLeftTLVsTxSize = _RlLldpLeftTLVsTxSize_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 4, 1, 4),
    _RlLldpLeftTLVsTxSize_Type()
)
rlLldpLeftTLVsTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpLeftTLVsTxSize.setStatus("current")
_RlLldpTLVsTxOverloadingPorts_Type = PortList
_RlLldpTLVsTxOverloadingPorts_Object = MibScalar
rlLldpTLVsTxOverloadingPorts = _RlLldpTLVsTxOverloadingPorts_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 5),
    _RlLldpTLVsTxOverloadingPorts_Type()
)
rlLldpTLVsTxOverloadingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingPorts.setStatus("current")
_RlLldpXMedNetPolVoiceUpdateMode_Type = PolicyAppVoiceUpdateMode
_RlLldpXMedNetPolVoiceUpdateMode_Object = MibScalar
rlLldpXMedNetPolVoiceUpdateMode = _RlLldpXMedNetPolVoiceUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 7),
    _RlLldpXMedNetPolVoiceUpdateMode_Type()
)
rlLldpXMedNetPolVoiceUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlLldpXMedNetPolVoiceUpdateMode.setStatus("current")
_RlLldpRemTtlTable_Object = MibTable
rlLldpRemTtlTable = _RlLldpRemTtlTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 8)
)
if mibBuilder.loadTexts:
    rlLldpRemTtlTable.setStatus("current")
_RlLldpRemTtlEntry_Object = MibTableRow
rlLldpRemTtlEntry = _RlLldpRemTtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 8, 1)
)
rlLldpRemTtlEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpRemTimeMark"),
    (0, "LLDP-MIB", "lldpRemLocalPortNum"),
    (0, "LLDP-MIB", "lldpRemIndex"),
)
if mibBuilder.loadTexts:
    rlLldpRemTtlEntry.setStatus("current")
_RlLldpRemTtl_Type = Unsigned32
_RlLldpRemTtl_Object = MibTableColumn
rlLldpRemTtl = _RlLldpRemTtl_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 110, 1, 8, 1, 1),
    _RlLldpRemTtl_Type()
)
rlLldpRemTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlLldpRemTtl.setStatus("current")
if mibBuilder.loadTexts:
    rlLldpRemTtl.setUnits("seconds")

# Managed Objects groups


# Notification objects

rlLldpTLVsTxOverloadingStateEnterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 0, 209)
)
rlLldpTLVsTxOverloadingStateEnterTrap.setObjects(
      *(("LINKSYS-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("LINKSYS-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingStateEnterTrap.setStatus(
        "current"
    )

rlLldpTLVsTxOverloadingStateExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 0, 210)
)
rlLldpTLVsTxOverloadingStateExitTrap.setObjects(
      *(("LINKSYS-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("LINKSYS-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlLldpTLVsTxOverloadingStateExitTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-LLDP-MIB",
    **{"PolicyNumber": PolicyNumber,
       "PolicyContainerAppType": PolicyContainerAppType,
       "PolicyAppVoiceUpdateMode": PolicyAppVoiceUpdateMode,
       "rlLldpTLVsTxOverloadingStateEnterTrap": rlLldpTLVsTxOverloadingStateEnterTrap,
       "rlLldpTLVsTxOverloadingStateExitTrap": rlLldpTLVsTxOverloadingStateExitTrap,
       "rlLldp": rlLldp,
       "rlLldpObjects": rlLldpObjects,
       "rlLldpConfig": rlLldpConfig,
       "rlLldpEnabled": rlLldpEnabled,
       "rlLldpClearRx": rlLldpClearRx,
       "rlLldpDuMode": rlLldpDuMode,
       "rlLldpAutoAdvLocPortManAddrTable": rlLldpAutoAdvLocPortManAddrTable,
       "rlLldpAutoAdvLocPortManAddrEntry": rlLldpAutoAdvLocPortManAddrEntry,
       "rlLldpAutoAdvLocPortNum": rlLldpAutoAdvLocPortNum,
       "rlLldpAutoAdvManAddrOwnerIfId": rlLldpAutoAdvManAddrOwnerIfId,
       "rlLldpAutoAdvManAddrNone": rlLldpAutoAdvManAddrNone,
       "rlLldpAutoAdvManAddrSubtype": rlLldpAutoAdvManAddrSubtype,
       "rlLldpAutoAdvManAddr": rlLldpAutoAdvManAddr,
       "rlLldpAutoAdvPortsStatus": rlLldpAutoAdvPortsStatus,
       "rlLldpChassisIdSubtype": rlLldpChassisIdSubtype,
       "rlLldpXMedConfig": rlLldpXMedConfig,
       "rlLldpXMedLocMediaPolicyContainerTable": rlLldpXMedLocMediaPolicyContainerTable,
       "rlLldpXMedLocMediaPolicyContainerEntry": rlLldpXMedLocMediaPolicyContainerEntry,
       "rlLldpXMedLocMediaPolicyContainerIndex": rlLldpXMedLocMediaPolicyContainerIndex,
       "rlLldpXMedLocMediaPolicyContainerAppType": rlLldpXMedLocMediaPolicyContainerAppType,
       "rlLldpXMedLocMediaPolicyContainerVlanID": rlLldpXMedLocMediaPolicyContainerVlanID,
       "rlLldpXMedLocMediaPolicyContainerPriority": rlLldpXMedLocMediaPolicyContainerPriority,
       "rlLldpXMedLocMediaPolicyContainerDscp": rlLldpXMedLocMediaPolicyContainerDscp,
       "rlLldpXMedLocMediaPolicyContainerUnknown": rlLldpXMedLocMediaPolicyContainerUnknown,
       "rlLldpXMedLocMediaPolicyContainerTagged": rlLldpXMedLocMediaPolicyContainerTagged,
       "rlLldpXMedLocMediaPolicyContainerPorts": rlLldpXMedLocMediaPolicyContainerPorts,
       "rlLldpXMedLocMediaPolicyContainerRowStatus": rlLldpXMedLocMediaPolicyContainerRowStatus,
       "rlLldpTLVsTxOverloadingTable": rlLldpTLVsTxOverloadingTable,
       "rlLldpTLVsTxOverloadingEntry": rlLldpTLVsTxOverloadingEntry,
       "rlLldpTxOverloadingPortNum": rlLldpTxOverloadingPortNum,
       "rlLldpTxOverloadingIndex": rlLldpTxOverloadingIndex,
       "rlLldpTxOverloadingGroupId": rlLldpTxOverloadingGroupId,
       "rlLldpTLVsTxSize": rlLldpTLVsTxSize,
       "rlLldpTLVsTxGroupOverloading": rlLldpTLVsTxGroupOverloading,
       "rlLldpTLVsTxLeftSize": rlLldpTLVsTxLeftSize,
       "rlLldpTLVsTxOverloadingSizeTable": rlLldpTLVsTxOverloadingSizeTable,
       "rlLldpTLVsTxOverloadingSizeEntry": rlLldpTLVsTxOverloadingSizeEntry,
       "rlLldpTotalTLVsTxSize": rlLldpTotalTLVsTxSize,
       "rlLldpTLVsTxOverloading": rlLldpTLVsTxOverloading,
       "rlLldpLeftTLVsTxSize": rlLldpLeftTLVsTxSize,
       "rlLldpTLVsTxOverloadingPorts": rlLldpTLVsTxOverloadingPorts,
       "rlLldpXMedNetPolVoiceUpdateMode": rlLldpXMedNetPolVoiceUpdateMode,
       "rlLldpRemTtlTable": rlLldpRemTtlTable,
       "rlLldpRemTtlEntry": rlLldpRemTtlEntry,
       "rlLldpRemTtl": rlLldpRemTtl}
)
