# SNMP MIB module (SLE-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-DHCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:25 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleDhcp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6)
)
if mibBuilder.loadTexts:
    sleDhcp.setRevisions(
        ("2004-12-10 16:32",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleDhcpBase_ObjectIdentity = ObjectIdentity
sleDhcpBase = _SleDhcpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1)
)
_SleDhcpBaseInfo_ObjectIdentity = ObjectIdentity
sleDhcpBaseInfo = _SleDhcpBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1)
)


class _SleDhcpDefaultLeaseTime_Type(Integer32):
    """Custom type sleDhcpDefaultLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleDhcpDefaultLeaseTime_Type.__name__ = "Integer32"
_SleDhcpDefaultLeaseTime_Object = MibScalar
sleDhcpDefaultLeaseTime = _SleDhcpDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 1),
    _SleDhcpDefaultLeaseTime_Type()
)
sleDhcpDefaultLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpDefaultLeaseTime.setStatus("current")


class _SleDhcpMaxLeaseTime_Type(Integer32):
    """Custom type sleDhcpMaxLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleDhcpMaxLeaseTime_Type.__name__ = "Integer32"
_SleDhcpMaxLeaseTime_Object = MibScalar
sleDhcpMaxLeaseTime = _SleDhcpMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 2),
    _SleDhcpMaxLeaseTime_Type()
)
sleDhcpMaxLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpMaxLeaseTime.setStatus("current")
_SleDhcpDnsIp1_Type = IpAddress
_SleDhcpDnsIp1_Object = MibScalar
sleDhcpDnsIp1 = _SleDhcpDnsIp1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 3),
    _SleDhcpDnsIp1_Type()
)
sleDhcpDnsIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpDnsIp1.setStatus("current")
_SleDhcpDnsIp2_Type = IpAddress
_SleDhcpDnsIp2_Object = MibScalar
sleDhcpDnsIp2 = _SleDhcpDnsIp2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 4),
    _SleDhcpDnsIp2_Type()
)
sleDhcpDnsIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpDnsIp2.setStatus("current")
_SleDhcpDnsIp3_Type = IpAddress
_SleDhcpDnsIp3_Object = MibScalar
sleDhcpDnsIp3 = _SleDhcpDnsIp3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 5),
    _SleDhcpDnsIp3_Type()
)
sleDhcpDnsIp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpDnsIp3.setStatus("current")


class _SleDhcpMode_Type(Integer32):
    """Custom type sleDhcpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("serverMode", 1),
          ("relayMode", 2))
    )


_SleDhcpMode_Type.__name__ = "Integer32"
_SleDhcpMode_Object = MibScalar
sleDhcpMode = _SleDhcpMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 6),
    _SleDhcpMode_Type()
)
sleDhcpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpMode.setStatus("current")
_SleDhcpLeasedbBackupIp_Type = IpAddress
_SleDhcpLeasedbBackupIp_Object = MibScalar
sleDhcpLeasedbBackupIp = _SleDhcpLeasedbBackupIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 7),
    _SleDhcpLeasedbBackupIp_Type()
)
sleDhcpLeasedbBackupIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpLeasedbBackupIp.setStatus("current")


class _SleDhcpLeasedbBackupInterval_Type(Integer32):
    """Custom type sleDhcpLeasedbBackupInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483637),
    )


_SleDhcpLeasedbBackupInterval_Type.__name__ = "Integer32"
_SleDhcpLeasedbBackupInterval_Object = MibScalar
sleDhcpLeasedbBackupInterval = _SleDhcpLeasedbBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 8),
    _SleDhcpLeasedbBackupInterval_Type()
)
sleDhcpLeasedbBackupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpLeasedbBackupInterval.setStatus("current")


class _SleDhcpDatabaseKey_Type(Integer32):
    """Custom type sleDhcpDatabaseKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clientid", 0),
          ("hwaddress", 1))
    )


_SleDhcpDatabaseKey_Type.__name__ = "Integer32"
_SleDhcpDatabaseKey_Object = MibScalar
sleDhcpDatabaseKey = _SleDhcpDatabaseKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 9),
    _SleDhcpDatabaseKey_Type()
)
sleDhcpDatabaseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpDatabaseKey.setStatus("current")


class _SleDhcpDebugStatus_Type(Bits):
    """Custom type sleDhcpDebugStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugFilter", 0),
          ("debugLease", 1),
          ("debugPacket", 2),
          ("debugServices", 3))
    )

_SleDhcpDebugStatus_Type.__name__ = "Bits"
_SleDhcpDebugStatus_Object = MibScalar
sleDhcpDebugStatus = _SleDhcpDebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 10),
    _SleDhcpDebugStatus_Type()
)
sleDhcpDebugStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpDebugStatus.setStatus("current")


class _SleDhcpOption82_Type(Integer32):
    """Custom type sleDhcpOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleDhcpOption82_Type.__name__ = "Integer32"
_SleDhcpOption82_Object = MibScalar
sleDhcpOption82 = _SleDhcpOption82_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 11),
    _SleDhcpOption82_Type()
)
sleDhcpOption82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpOption82.setStatus("current")


class _SleDhcpOption82Policy_Type(Integer32):
    """Custom type sleDhcpOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 0),
          ("replace", 1),
          ("drop", 2))
    )


_SleDhcpOption82Policy_Type.__name__ = "Integer32"
_SleDhcpOption82Policy_Object = MibScalar
sleDhcpOption82Policy = _SleDhcpOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 12),
    _SleDhcpOption82Policy_Type()
)
sleDhcpOption82Policy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpOption82Policy.setStatus("current")


class _SleDhcpOption82SystemRtype_Type(Integer32):
    """Custom type sleDhcpOption82SystemRtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("ipaddress", 1),
          ("binary", 2),
          ("text", 3))
    )


_SleDhcpOption82SystemRtype_Type.__name__ = "Integer32"
_SleDhcpOption82SystemRtype_Object = MibScalar
sleDhcpOption82SystemRtype = _SleDhcpOption82SystemRtype_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 13),
    _SleDhcpOption82SystemRtype_Type()
)
sleDhcpOption82SystemRtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpOption82SystemRtype.setStatus("current")


class _SleDhcpOption82SystemRid_Type(OctetString):
    """Custom type sleDhcpOption82SystemRid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleDhcpOption82SystemRid_Type.__name__ = "OctetString"
_SleDhcpOption82SystemRid_Object = MibScalar
sleDhcpOption82SystemRid = _SleDhcpOption82SystemRid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 14),
    _SleDhcpOption82SystemRid_Type()
)
sleDhcpOption82SystemRid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpOption82SystemRid.setStatus("current")


class _SleDhcpAuthorizedArp_Type(Integer32):
    """Custom type sleDhcpAuthorizedArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noSet", 0),
          ("defaultLeaseTime", 1),
          ("halfLeaseTime", 2),
          ("maxLeaseTime", 3))
    )


_SleDhcpAuthorizedArp_Type.__name__ = "Integer32"
_SleDhcpAuthorizedArp_Object = MibScalar
sleDhcpAuthorizedArp = _SleDhcpAuthorizedArp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 15),
    _SleDhcpAuthorizedArp_Type()
)
sleDhcpAuthorizedArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpAuthorizedArp.setStatus("current")
_SleDhcpAuthArpStarted_Type = OctetString
_SleDhcpAuthArpStarted_Object = MibScalar
sleDhcpAuthArpStarted = _SleDhcpAuthArpStarted_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 16),
    _SleDhcpAuthArpStarted_Type()
)
sleDhcpAuthArpStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpAuthArpStarted.setStatus("current")
_SleDhcpAuthArpLeft_Type = OctetString
_SleDhcpAuthArpLeft_Object = MibScalar
sleDhcpAuthArpLeft = _SleDhcpAuthArpLeft_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 17),
    _SleDhcpAuthArpLeft_Type()
)
sleDhcpAuthArpLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpAuthArpLeft.setStatus("current")
_SleDhcpStatisticReceived_Type = Unsigned32
_SleDhcpStatisticReceived_Object = MibScalar
sleDhcpStatisticReceived = _SleDhcpStatisticReceived_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 18),
    _SleDhcpStatisticReceived_Type()
)
sleDhcpStatisticReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticReceived.setStatus("current")
_SleDhcpStatisticSent_Type = Unsigned32
_SleDhcpStatisticSent_Object = MibScalar
sleDhcpStatisticSent = _SleDhcpStatisticSent_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 19),
    _SleDhcpStatisticSent_Type()
)
sleDhcpStatisticSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticSent.setStatus("current")
_SleDhcpStatisticReceivedErrors_Type = Unsigned32
_SleDhcpStatisticReceivedErrors_Object = MibScalar
sleDhcpStatisticReceivedErrors = _SleDhcpStatisticReceivedErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 20),
    _SleDhcpStatisticReceivedErrors_Type()
)
sleDhcpStatisticReceivedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticReceivedErrors.setStatus("current")
_SleDhcpStatisticSentErrors_Type = Unsigned32
_SleDhcpStatisticSentErrors_Object = MibScalar
sleDhcpStatisticSentErrors = _SleDhcpStatisticSentErrors_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 21),
    _SleDhcpStatisticSentErrors_Type()
)
sleDhcpStatisticSentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticSentErrors.setStatus("current")
_SleDhcpStatisticBootpReceivedRequests_Type = Unsigned32
_SleDhcpStatisticBootpReceivedRequests_Object = MibScalar
sleDhcpStatisticBootpReceivedRequests = _SleDhcpStatisticBootpReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 22),
    _SleDhcpStatisticBootpReceivedRequests_Type()
)
sleDhcpStatisticBootpReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticBootpReceivedRequests.setStatus("current")
_SleDhcpStatisticBootpReceivedReplies_Type = Unsigned32
_SleDhcpStatisticBootpReceivedReplies_Object = MibScalar
sleDhcpStatisticBootpReceivedReplies = _SleDhcpStatisticBootpReceivedReplies_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 23),
    _SleDhcpStatisticBootpReceivedReplies_Type()
)
sleDhcpStatisticBootpReceivedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticBootpReceivedReplies.setStatus("current")
_SleDhcpStatisticBootpSentRequests_Type = Unsigned32
_SleDhcpStatisticBootpSentRequests_Object = MibScalar
sleDhcpStatisticBootpSentRequests = _SleDhcpStatisticBootpSentRequests_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 24),
    _SleDhcpStatisticBootpSentRequests_Type()
)
sleDhcpStatisticBootpSentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticBootpSentRequests.setStatus("current")
_SleDhcpStatisticBootpSentReplies_Type = Unsigned32
_SleDhcpStatisticBootpSentReplies_Object = MibScalar
sleDhcpStatisticBootpSentReplies = _SleDhcpStatisticBootpSentReplies_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 25),
    _SleDhcpStatisticBootpSentReplies_Type()
)
sleDhcpStatisticBootpSentReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticBootpSentReplies.setStatus("current")
_SleDhcpStatisticReceivedDiscover_Type = Unsigned32
_SleDhcpStatisticReceivedDiscover_Object = MibScalar
sleDhcpStatisticReceivedDiscover = _SleDhcpStatisticReceivedDiscover_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 26),
    _SleDhcpStatisticReceivedDiscover_Type()
)
sleDhcpStatisticReceivedDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticReceivedDiscover.setStatus("current")
_SleDhcpStatisticReceivedRequest_Type = Unsigned32
_SleDhcpStatisticReceivedRequest_Object = MibScalar
sleDhcpStatisticReceivedRequest = _SleDhcpStatisticReceivedRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 27),
    _SleDhcpStatisticReceivedRequest_Type()
)
sleDhcpStatisticReceivedRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticReceivedRequest.setStatus("current")
_SleDhcpStatisticReceivedRelease_Type = Unsigned32
_SleDhcpStatisticReceivedRelease_Object = MibScalar
sleDhcpStatisticReceivedRelease = _SleDhcpStatisticReceivedRelease_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 28),
    _SleDhcpStatisticReceivedRelease_Type()
)
sleDhcpStatisticReceivedRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticReceivedRelease.setStatus("current")
_SleDhcpStatisticReceivedInform_Type = Unsigned32
_SleDhcpStatisticReceivedInform_Object = MibScalar
sleDhcpStatisticReceivedInform = _SleDhcpStatisticReceivedInform_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 29),
    _SleDhcpStatisticReceivedInform_Type()
)
sleDhcpStatisticReceivedInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticReceivedInform.setStatus("current")
_SleDhcpStatisticReceivedDecline_Type = Unsigned32
_SleDhcpStatisticReceivedDecline_Object = MibScalar
sleDhcpStatisticReceivedDecline = _SleDhcpStatisticReceivedDecline_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 30),
    _SleDhcpStatisticReceivedDecline_Type()
)
sleDhcpStatisticReceivedDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticReceivedDecline.setStatus("current")
_SleDhcpStatisticSentOffer_Type = Unsigned32
_SleDhcpStatisticSentOffer_Object = MibScalar
sleDhcpStatisticSentOffer = _SleDhcpStatisticSentOffer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 31),
    _SleDhcpStatisticSentOffer_Type()
)
sleDhcpStatisticSentOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticSentOffer.setStatus("current")
_SleDhcpStatisticSentAck_Type = Unsigned32
_SleDhcpStatisticSentAck_Object = MibScalar
sleDhcpStatisticSentAck = _SleDhcpStatisticSentAck_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 32),
    _SleDhcpStatisticSentAck_Type()
)
sleDhcpStatisticSentAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticSentAck.setStatus("current")
_SleDhcpStatisticSentNak_Type = Unsigned32
_SleDhcpStatisticSentNak_Object = MibScalar
sleDhcpStatisticSentNak = _SleDhcpStatisticSentNak_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 33),
    _SleDhcpStatisticSentNak_Type()
)
sleDhcpStatisticSentNak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpStatisticSentNak.setStatus("current")
_SleDhcpSummaryPoolCnt_Type = Unsigned32
_SleDhcpSummaryPoolCnt_Object = MibScalar
sleDhcpSummaryPoolCnt = _SleDhcpSummaryPoolCnt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 34),
    _SleDhcpSummaryPoolCnt_Type()
)
sleDhcpSummaryPoolCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSummaryPoolCnt.setStatus("current")
_SleDhcpSummaryTotal_Type = Unsigned32
_SleDhcpSummaryTotal_Object = MibScalar
sleDhcpSummaryTotal = _SleDhcpSummaryTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 35),
    _SleDhcpSummaryTotal_Type()
)
sleDhcpSummaryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSummaryTotal.setStatus("current")
_SleDhcpSummaryAvailable_Type = Unsigned32
_SleDhcpSummaryAvailable_Object = MibScalar
sleDhcpSummaryAvailable = _SleDhcpSummaryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 36),
    _SleDhcpSummaryAvailable_Type()
)
sleDhcpSummaryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSummaryAvailable.setStatus("current")
_SleDhcpSummaryAbandon_Type = Unsigned32
_SleDhcpSummaryAbandon_Object = MibScalar
sleDhcpSummaryAbandon = _SleDhcpSummaryAbandon_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 37),
    _SleDhcpSummaryAbandon_Type()
)
sleDhcpSummaryAbandon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSummaryAbandon.setStatus("current")
_SleDhcpSummaryBound_Type = Unsigned32
_SleDhcpSummaryBound_Object = MibScalar
sleDhcpSummaryBound = _SleDhcpSummaryBound_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 38),
    _SleDhcpSummaryBound_Type()
)
sleDhcpSummaryBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSummaryBound.setStatus("current")
_SleDhcpSummaryOffered_Type = Unsigned32
_SleDhcpSummaryOffered_Object = MibScalar
sleDhcpSummaryOffered = _SleDhcpSummaryOffered_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 39),
    _SleDhcpSummaryOffered_Type()
)
sleDhcpSummaryOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSummaryOffered.setStatus("current")
_SleDhcpSummaryFixed_Type = Unsigned32
_SleDhcpSummaryFixed_Object = MibScalar
sleDhcpSummaryFixed = _SleDhcpSummaryFixed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 40),
    _SleDhcpSummaryFixed_Type()
)
sleDhcpSummaryFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSummaryFixed.setStatus("current")


class _SleDhcpClientHardwareAddress_Type(Integer32):
    """Custom type sleDhcpClientHardwareAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleDhcpClientHardwareAddress_Type.__name__ = "Integer32"
_SleDhcpClientHardwareAddress_Object = MibScalar
sleDhcpClientHardwareAddress = _SleDhcpClientHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 41),
    _SleDhcpClientHardwareAddress_Type()
)
sleDhcpClientHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpClientHardwareAddress.setStatus("current")


class _SleDhcpSimplifiedOption82_Type(Integer32):
    """Custom type sleDhcpSimplifiedOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleDhcpSimplifiedOption82_Type.__name__ = "Integer32"
_SleDhcpSimplifiedOption82_Object = MibScalar
sleDhcpSimplifiedOption82 = _SleDhcpSimplifiedOption82_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 42),
    _SleDhcpSimplifiedOption82_Type()
)
sleDhcpSimplifiedOption82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSimplifiedOption82.setStatus("current")
_SleDhcpSummaryAllocated_Type = Unsigned32
_SleDhcpSummaryAllocated_Object = MibScalar
sleDhcpSummaryAllocated = _SleDhcpSummaryAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 1, 43),
    _SleDhcpSummaryAllocated_Type()
)
sleDhcpSummaryAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSummaryAllocated.setStatus("current")
_SleDhcpBaseControl_ObjectIdentity = ObjectIdentity
sleDhcpBaseControl = _SleDhcpBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2)
)


class _SleDhcpControlRequest_Type(Integer32):
    """Custom type sleDhcpControlRequest based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("setDhcpLeaseTimeProfile", 1),
          ("setDhcpDnsIpProfile", 2),
          ("setDhcpServerMode", 3),
          ("setDhcpLeasedbBackupProfile", 4),
          ("setDhcpDatabaseKey", 5),
          ("setDhcpDebugStatus", 6),
          ("setDhcpOption82SystemProfile", 7),
          ("setDhcpAuthorizedArp", 8),
          ("clearDhcpStatistics", 9),
          ("setDhcpClientHardwareAddress", 10),
          ("setSimplifiedOption82", 11))
    )


_SleDhcpControlRequest_Type.__name__ = "Integer32"
_SleDhcpControlRequest_Object = MibScalar
sleDhcpControlRequest = _SleDhcpControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 1),
    _SleDhcpControlRequest_Type()
)
sleDhcpControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlRequest.setStatus("current")
_SleDhcpControlStatus_Type = SleControlStatusType
_SleDhcpControlStatus_Object = MibScalar
sleDhcpControlStatus = _SleDhcpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 2),
    _SleDhcpControlStatus_Type()
)
sleDhcpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpControlStatus.setStatus("current")
_SleDhcpControlTimer_Type = Gauge32
_SleDhcpControlTimer_Object = MibScalar
sleDhcpControlTimer = _SleDhcpControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 3),
    _SleDhcpControlTimer_Type()
)
sleDhcpControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlTimer.setStatus("current")
_SleDhcpControlTimeStamp_Type = TimeTicks
_SleDhcpControlTimeStamp_Object = MibScalar
sleDhcpControlTimeStamp = _SleDhcpControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 4),
    _SleDhcpControlTimeStamp_Type()
)
sleDhcpControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpControlTimeStamp.setStatus("current")
_SleDhcpControlReqResult_Type = SleControlRequestResultType
_SleDhcpControlReqResult_Object = MibScalar
sleDhcpControlReqResult = _SleDhcpControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 5),
    _SleDhcpControlReqResult_Type()
)
sleDhcpControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpControlReqResult.setStatus("current")


class _SleDhcpControlDefaultLeaseTime_Type(Integer32):
    """Custom type sleDhcpControlDefaultLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleDhcpControlDefaultLeaseTime_Type.__name__ = "Integer32"
_SleDhcpControlDefaultLeaseTime_Object = MibScalar
sleDhcpControlDefaultLeaseTime = _SleDhcpControlDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 6),
    _SleDhcpControlDefaultLeaseTime_Type()
)
sleDhcpControlDefaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlDefaultLeaseTime.setStatus("current")


class _SleDhcpControlMaxLeaseTime_Type(Integer32):
    """Custom type sleDhcpControlMaxLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SleDhcpControlMaxLeaseTime_Type.__name__ = "Integer32"
_SleDhcpControlMaxLeaseTime_Object = MibScalar
sleDhcpControlMaxLeaseTime = _SleDhcpControlMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 7),
    _SleDhcpControlMaxLeaseTime_Type()
)
sleDhcpControlMaxLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlMaxLeaseTime.setStatus("current")
_SleDhcpControlDnsIp1_Type = IpAddress
_SleDhcpControlDnsIp1_Object = MibScalar
sleDhcpControlDnsIp1 = _SleDhcpControlDnsIp1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 8),
    _SleDhcpControlDnsIp1_Type()
)
sleDhcpControlDnsIp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlDnsIp1.setStatus("current")
_SleDhcpControlDnsIp2_Type = IpAddress
_SleDhcpControlDnsIp2_Object = MibScalar
sleDhcpControlDnsIp2 = _SleDhcpControlDnsIp2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 9),
    _SleDhcpControlDnsIp2_Type()
)
sleDhcpControlDnsIp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlDnsIp2.setStatus("current")
_SleDhcpControlDnsIp3_Type = IpAddress
_SleDhcpControlDnsIp3_Object = MibScalar
sleDhcpControlDnsIp3 = _SleDhcpControlDnsIp3_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 10),
    _SleDhcpControlDnsIp3_Type()
)
sleDhcpControlDnsIp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlDnsIp3.setStatus("current")


class _SleDhcpControlServerMode_Type(Integer32):
    """Custom type sleDhcpControlServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("set", 1))
    )


_SleDhcpControlServerMode_Type.__name__ = "Integer32"
_SleDhcpControlServerMode_Object = MibScalar
sleDhcpControlServerMode = _SleDhcpControlServerMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 11),
    _SleDhcpControlServerMode_Type()
)
sleDhcpControlServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlServerMode.setStatus("current")
_SleDhcpControlLeasedbBackupIp_Type = IpAddress
_SleDhcpControlLeasedbBackupIp_Object = MibScalar
sleDhcpControlLeasedbBackupIp = _SleDhcpControlLeasedbBackupIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 12),
    _SleDhcpControlLeasedbBackupIp_Type()
)
sleDhcpControlLeasedbBackupIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlLeasedbBackupIp.setStatus("current")


class _SleDhcpControlLeasedbBackupInterval_Type(Integer32):
    """Custom type sleDhcpControlLeasedbBackupInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483637),
    )


_SleDhcpControlLeasedbBackupInterval_Type.__name__ = "Integer32"
_SleDhcpControlLeasedbBackupInterval_Object = MibScalar
sleDhcpControlLeasedbBackupInterval = _SleDhcpControlLeasedbBackupInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 13),
    _SleDhcpControlLeasedbBackupInterval_Type()
)
sleDhcpControlLeasedbBackupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlLeasedbBackupInterval.setStatus("current")


class _SleDhcpControlDatabaseKey_Type(Integer32):
    """Custom type sleDhcpControlDatabaseKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clientid", 0),
          ("hwaddress", 1))
    )


_SleDhcpControlDatabaseKey_Type.__name__ = "Integer32"
_SleDhcpControlDatabaseKey_Object = MibScalar
sleDhcpControlDatabaseKey = _SleDhcpControlDatabaseKey_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 14),
    _SleDhcpControlDatabaseKey_Type()
)
sleDhcpControlDatabaseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlDatabaseKey.setStatus("current")


class _SleDhcpControlDebugStatus_Type(Bits):
    """Custom type sleDhcpControlDebugStatus based on Bits"""
    namedValues = NamedValues(
        *(("debugFilter", 0),
          ("debugLease", 1),
          ("debugPacket", 2),
          ("debugServices", 3))
    )

_SleDhcpControlDebugStatus_Type.__name__ = "Bits"
_SleDhcpControlDebugStatus_Object = MibScalar
sleDhcpControlDebugStatus = _SleDhcpControlDebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 15),
    _SleDhcpControlDebugStatus_Type()
)
sleDhcpControlDebugStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlDebugStatus.setStatus("current")


class _SleDhcpControlOption82_Type(Integer32):
    """Custom type sleDhcpControlOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleDhcpControlOption82_Type.__name__ = "Integer32"
_SleDhcpControlOption82_Object = MibScalar
sleDhcpControlOption82 = _SleDhcpControlOption82_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 16),
    _SleDhcpControlOption82_Type()
)
sleDhcpControlOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlOption82.setStatus("current")


class _SleDhcpControlOption82Policy_Type(Integer32):
    """Custom type sleDhcpControlOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 0),
          ("replace", 1),
          ("drop", 2))
    )


_SleDhcpControlOption82Policy_Type.__name__ = "Integer32"
_SleDhcpControlOption82Policy_Object = MibScalar
sleDhcpControlOption82Policy = _SleDhcpControlOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 17),
    _SleDhcpControlOption82Policy_Type()
)
sleDhcpControlOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlOption82Policy.setStatus("current")


class _SleDhcpControlOption82SystemRtype_Type(Integer32):
    """Custom type sleDhcpControlOption82SystemRtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("ipaddress", 1),
          ("binary", 2),
          ("text", 3))
    )


_SleDhcpControlOption82SystemRtype_Type.__name__ = "Integer32"
_SleDhcpControlOption82SystemRtype_Object = MibScalar
sleDhcpControlOption82SystemRtype = _SleDhcpControlOption82SystemRtype_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 18),
    _SleDhcpControlOption82SystemRtype_Type()
)
sleDhcpControlOption82SystemRtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlOption82SystemRtype.setStatus("current")


class _SleDhcpControlOption82SystemRid_Type(OctetString):
    """Custom type sleDhcpControlOption82SystemRid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleDhcpControlOption82SystemRid_Type.__name__ = "OctetString"
_SleDhcpControlOption82SystemRid_Object = MibScalar
sleDhcpControlOption82SystemRid = _SleDhcpControlOption82SystemRid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 19),
    _SleDhcpControlOption82SystemRid_Type()
)
sleDhcpControlOption82SystemRid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlOption82SystemRid.setStatus("current")


class _SleDhcpControlAuthorizedArp_Type(Integer32):
    """Custom type sleDhcpControlAuthorizedArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noSet", 0),
          ("defaultLeaseTime", 1),
          ("halfLeaseTime", 2),
          ("maxLeaseTime", 3))
    )


_SleDhcpControlAuthorizedArp_Type.__name__ = "Integer32"
_SleDhcpControlAuthorizedArp_Object = MibScalar
sleDhcpControlAuthorizedArp = _SleDhcpControlAuthorizedArp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 20),
    _SleDhcpControlAuthorizedArp_Type()
)
sleDhcpControlAuthorizedArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlAuthorizedArp.setStatus("current")


class _SleDhcpControlClientHardwareAddress_Type(Integer32):
    """Custom type sleDhcpControlClientHardwareAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleDhcpControlClientHardwareAddress_Type.__name__ = "Integer32"
_SleDhcpControlClientHardwareAddress_Object = MibScalar
sleDhcpControlClientHardwareAddress = _SleDhcpControlClientHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 21),
    _SleDhcpControlClientHardwareAddress_Type()
)
sleDhcpControlClientHardwareAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlClientHardwareAddress.setStatus("current")


class _SleDhcpControlSimplifiedOption82_Type(Integer32):
    """Custom type sleDhcpControlSimplifiedOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleDhcpControlSimplifiedOption82_Type.__name__ = "Integer32"
_SleDhcpControlSimplifiedOption82_Object = MibScalar
sleDhcpControlSimplifiedOption82 = _SleDhcpControlSimplifiedOption82_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 2, 22),
    _SleDhcpControlSimplifiedOption82_Type()
)
sleDhcpControlSimplifiedOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDhcpControlSimplifiedOption82.setStatus("current")
_SleDhcpBaseNotification_ObjectIdentity = ObjectIdentity
sleDhcpBaseNotification = _SleDhcpBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3)
)
_SleFilterPort_ObjectIdentity = ObjectIdentity
sleFilterPort = _SleFilterPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2)
)
_SleFilterPortTable_Object = MibTable
sleFilterPortTable = _SleFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 1)
)
if mibBuilder.loadTexts:
    sleFilterPortTable.setStatus("current")
_SleFilterPortEntry_Object = MibTableRow
sleFilterPortEntry = _SleFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 1, 1)
)
sleFilterPortEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "sleFilterPortIndex"),
)
if mibBuilder.loadTexts:
    sleFilterPortEntry.setStatus("current")
_SleFilterPortIndex_Type = InterfaceIndex
_SleFilterPortIndex_Object = MibTableColumn
sleFilterPortIndex = _SleFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 1, 1, 1),
    _SleFilterPortIndex_Type()
)
sleFilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFilterPortIndex.setStatus("current")


class _SleFilterPortMode_Type(Integer32):
    """Custom type sleFilterPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
    )


_SleFilterPortMode_Type.__name__ = "Integer32"
_SleFilterPortMode_Object = MibTableColumn
sleFilterPortMode = _SleFilterPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 1, 1, 2),
    _SleFilterPortMode_Type()
)
sleFilterPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFilterPortMode.setStatus("current")
_SleFilterPortControl_ObjectIdentity = ObjectIdentity
sleFilterPortControl = _SleFilterPortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 2)
)


class _SleFilterPortControlRequest_Type(Integer32):
    """Custom type sleFilterPortControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setFilterPortMode", 1)
    )


_SleFilterPortControlRequest_Type.__name__ = "Integer32"
_SleFilterPortControlRequest_Object = MibScalar
sleFilterPortControlRequest = _SleFilterPortControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 2, 1),
    _SleFilterPortControlRequest_Type()
)
sleFilterPortControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFilterPortControlRequest.setStatus("current")
_SleFilterPortControlStatus_Type = SleControlStatusType
_SleFilterPortControlStatus_Object = MibScalar
sleFilterPortControlStatus = _SleFilterPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 2, 2),
    _SleFilterPortControlStatus_Type()
)
sleFilterPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFilterPortControlStatus.setStatus("current")
_SleFilterPortControlTimer_Type = Gauge32
_SleFilterPortControlTimer_Object = MibScalar
sleFilterPortControlTimer = _SleFilterPortControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 2, 3),
    _SleFilterPortControlTimer_Type()
)
sleFilterPortControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFilterPortControlTimer.setStatus("current")
_SleFilterPortControlTImeStamp_Type = TimeTicks
_SleFilterPortControlTImeStamp_Object = MibScalar
sleFilterPortControlTImeStamp = _SleFilterPortControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 2, 4),
    _SleFilterPortControlTImeStamp_Type()
)
sleFilterPortControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFilterPortControlTImeStamp.setStatus("current")
_SleFilterPortControlReqResult_Type = SleControlRequestResultType
_SleFilterPortControlReqResult_Object = MibScalar
sleFilterPortControlReqResult = _SleFilterPortControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 2, 5),
    _SleFilterPortControlReqResult_Type()
)
sleFilterPortControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFilterPortControlReqResult.setStatus("current")


class _SleFilterPortControlIndex_Type(Integer32):
    """Custom type sleFilterPortControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleFilterPortControlIndex_Type.__name__ = "Integer32"
_SleFilterPortControlIndex_Object = MibScalar
sleFilterPortControlIndex = _SleFilterPortControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 2, 6),
    _SleFilterPortControlIndex_Type()
)
sleFilterPortControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFilterPortControlIndex.setStatus("current")


class _SleFilterPortControlMode_Type(Integer32):
    """Custom type sleFilterPortControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("set", 1))
    )


_SleFilterPortControlMode_Type.__name__ = "Integer32"
_SleFilterPortControlMode_Object = MibScalar
sleFilterPortControlMode = _SleFilterPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 2, 7),
    _SleFilterPortControlMode_Type()
)
sleFilterPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFilterPortControlMode.setStatus("current")
_SleFilterPortNotification_ObjectIdentity = ObjectIdentity
sleFilterPortNotification = _SleFilterPortNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 3)
)
_SleFilterAddress_ObjectIdentity = ObjectIdentity
sleFilterAddress = _SleFilterAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3)
)
_SleFilterAddressTable_Object = MibTable
sleFilterAddressTable = _SleFilterAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 1)
)
if mibBuilder.loadTexts:
    sleFilterAddressTable.setStatus("current")
_SleFilterAddressEntry_Object = MibTableRow
sleFilterAddressEntry = _SleFilterAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 1, 1)
)
sleFilterAddressEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "sleFilterAddressMac"),
)
if mibBuilder.loadTexts:
    sleFilterAddressEntry.setStatus("current")
_SleFilterAddressMac_Type = MacAddress
_SleFilterAddressMac_Object = MibTableColumn
sleFilterAddressMac = _SleFilterAddressMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 1, 1, 1),
    _SleFilterAddressMac_Type()
)
sleFilterAddressMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFilterAddressMac.setStatus("current")
_SleFilterAddressControl_ObjectIdentity = ObjectIdentity
sleFilterAddressControl = _SleFilterAddressControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 2)
)


class _SleFilterAddressControlRequest_Type(Integer32):
    """Custom type sleFilterAddressControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createFilterAddress", 1),
          ("destroyFilterAddress", 2))
    )


_SleFilterAddressControlRequest_Type.__name__ = "Integer32"
_SleFilterAddressControlRequest_Object = MibScalar
sleFilterAddressControlRequest = _SleFilterAddressControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 2, 1),
    _SleFilterAddressControlRequest_Type()
)
sleFilterAddressControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFilterAddressControlRequest.setStatus("current")
_SleFilterAddressControlStatus_Type = SleControlStatusType
_SleFilterAddressControlStatus_Object = MibScalar
sleFilterAddressControlStatus = _SleFilterAddressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 2, 2),
    _SleFilterAddressControlStatus_Type()
)
sleFilterAddressControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFilterAddressControlStatus.setStatus("current")
_SleFilterAddressControlTimer_Type = Gauge32
_SleFilterAddressControlTimer_Object = MibScalar
sleFilterAddressControlTimer = _SleFilterAddressControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 2, 3),
    _SleFilterAddressControlTimer_Type()
)
sleFilterAddressControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFilterAddressControlTimer.setStatus("current")
_SleFilterAddressControlTImeStamp_Type = TimeTicks
_SleFilterAddressControlTImeStamp_Object = MibScalar
sleFilterAddressControlTImeStamp = _SleFilterAddressControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 2, 4),
    _SleFilterAddressControlTImeStamp_Type()
)
sleFilterAddressControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFilterAddressControlTImeStamp.setStatus("current")
_SleFilterAddressControlReqResult_Type = SleControlRequestResultType
_SleFilterAddressControlReqResult_Object = MibScalar
sleFilterAddressControlReqResult = _SleFilterAddressControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 2, 5),
    _SleFilterAddressControlReqResult_Type()
)
sleFilterAddressControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFilterAddressControlReqResult.setStatus("current")
_SleFilterAddressControlMac_Type = MacAddress
_SleFilterAddressControlMac_Object = MibScalar
sleFilterAddressControlMac = _SleFilterAddressControlMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 2, 6),
    _SleFilterAddressControlMac_Type()
)
sleFilterAddressControlMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFilterAddressControlMac.setStatus("current")
_SleFilterAddressNotification_ObjectIdentity = ObjectIdentity
sleFilterAddressNotification = _SleFilterAddressNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 3)
)
_SleRelayServer_ObjectIdentity = ObjectIdentity
sleRelayServer = _SleRelayServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4)
)
_SleRelayServerTable_Object = MibTable
sleRelayServerTable = _SleRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 1)
)
if mibBuilder.loadTexts:
    sleRelayServerTable.setStatus("current")
_SleRelayServerEntry_Object = MibTableRow
sleRelayServerEntry = _SleRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 1, 1)
)
sleRelayServerEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "sleRelayServerIndex"),
)
if mibBuilder.loadTexts:
    sleRelayServerEntry.setStatus("current")


class _SleRelayServerIndex_Type(Integer32):
    """Custom type sleRelayServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SleRelayServerIndex_Type.__name__ = "Integer32"
_SleRelayServerIndex_Object = MibTableColumn
sleRelayServerIndex = _SleRelayServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 1, 1, 1),
    _SleRelayServerIndex_Type()
)
sleRelayServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRelayServerIndex.setStatus("current")
_SleRelayServerIp_Type = IpAddress
_SleRelayServerIp_Object = MibTableColumn
sleRelayServerIp = _SleRelayServerIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 1, 1, 2),
    _SleRelayServerIp_Type()
)
sleRelayServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRelayServerIp.setStatus("current")


class _SleRelayServerVid_Type(Integer32):
    """Custom type sleRelayServerVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleRelayServerVid_Type.__name__ = "Integer32"
_SleRelayServerVid_Object = MibTableColumn
sleRelayServerVid = _SleRelayServerVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 1, 1, 3),
    _SleRelayServerVid_Type()
)
sleRelayServerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRelayServerVid.setStatus("current")


class _SleRelayServerOUI_Type(OctetString):
    """Custom type sleRelayServerOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_SleRelayServerOUI_Type.__name__ = "OctetString"
_SleRelayServerOUI_Object = MibTableColumn
sleRelayServerOUI = _SleRelayServerOUI_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 1, 1, 4),
    _SleRelayServerOUI_Type()
)
sleRelayServerOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRelayServerOUI.setStatus("current")
_SleRelayServerControl_ObjectIdentity = ObjectIdentity
sleRelayServerControl = _SleRelayServerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 2)
)


class _SleRelayServerControlRequest_Type(Integer32):
    """Custom type sleRelayServerControlRequest based on Integer32"""
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
        *(("createRelayServer", 1),
          ("destroyRelayServer", 2),
          ("createRelayServerOUI", 3),
          ("destroyRelayServerOUI", 4))
    )


_SleRelayServerControlRequest_Type.__name__ = "Integer32"
_SleRelayServerControlRequest_Object = MibScalar
sleRelayServerControlRequest = _SleRelayServerControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 2, 1),
    _SleRelayServerControlRequest_Type()
)
sleRelayServerControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRelayServerControlRequest.setStatus("current")
_SleRelayServerControlStatus_Type = SleControlStatusType
_SleRelayServerControlStatus_Object = MibScalar
sleRelayServerControlStatus = _SleRelayServerControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 2, 2),
    _SleRelayServerControlStatus_Type()
)
sleRelayServerControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRelayServerControlStatus.setStatus("current")
_SleRelayServerControlTimer_Type = Gauge32
_SleRelayServerControlTimer_Object = MibScalar
sleRelayServerControlTimer = _SleRelayServerControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 2, 3),
    _SleRelayServerControlTimer_Type()
)
sleRelayServerControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRelayServerControlTimer.setStatus("current")
_SleRelayServerControlTImeStamp_Type = TimeTicks
_SleRelayServerControlTImeStamp_Object = MibScalar
sleRelayServerControlTImeStamp = _SleRelayServerControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 2, 4),
    _SleRelayServerControlTImeStamp_Type()
)
sleRelayServerControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRelayServerControlTImeStamp.setStatus("current")
_SleRelayServerControlReqResult_Type = SleControlRequestResultType
_SleRelayServerControlReqResult_Object = MibScalar
sleRelayServerControlReqResult = _SleRelayServerControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 2, 5),
    _SleRelayServerControlReqResult_Type()
)
sleRelayServerControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRelayServerControlReqResult.setStatus("current")


class _SleRelayServerControlIndex_Type(Integer32):
    """Custom type sleRelayServerControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SleRelayServerControlIndex_Type.__name__ = "Integer32"
_SleRelayServerControlIndex_Object = MibScalar
sleRelayServerControlIndex = _SleRelayServerControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 2, 6),
    _SleRelayServerControlIndex_Type()
)
sleRelayServerControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRelayServerControlIndex.setStatus("current")
_SleRelayServerControlIp_Type = IpAddress
_SleRelayServerControlIp_Object = MibScalar
sleRelayServerControlIp = _SleRelayServerControlIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 2, 7),
    _SleRelayServerControlIp_Type()
)
sleRelayServerControlIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRelayServerControlIp.setStatus("current")


class _SleRelayServerControlVid_Type(Integer32):
    """Custom type sleRelayServerControlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SleRelayServerControlVid_Type.__name__ = "Integer32"
_SleRelayServerControlVid_Object = MibScalar
sleRelayServerControlVid = _SleRelayServerControlVid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 2, 8),
    _SleRelayServerControlVid_Type()
)
sleRelayServerControlVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRelayServerControlVid.setStatus("current")


class _SleRelayServerControlOUI_Type(OctetString):
    """Custom type sleRelayServerControlOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_SleRelayServerControlOUI_Type.__name__ = "OctetString"
_SleRelayServerControlOUI_Object = MibScalar
sleRelayServerControlOUI = _SleRelayServerControlOUI_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 2, 9),
    _SleRelayServerControlOUI_Type()
)
sleRelayServerControlOUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRelayServerControlOUI.setStatus("current")
_SleRelayServerNotification_ObjectIdentity = ObjectIdentity
sleRelayServerNotification = _SleRelayServerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 3)
)
_SlePool_ObjectIdentity = ObjectIdentity
slePool = _SlePool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5)
)
_SlePoolTable_Object = MibTable
slePoolTable = _SlePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1)
)
if mibBuilder.loadTexts:
    slePoolTable.setStatus("current")
_SlePoolEntry_Object = MibTableRow
slePoolEntry = _SlePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1)
)
slePoolEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "slePoolIndex"),
)
if mibBuilder.loadTexts:
    slePoolEntry.setStatus("current")


class _SlePoolIndex_Type(Integer32):
    """Custom type slePoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlePoolIndex_Type.__name__ = "Integer32"
_SlePoolIndex_Object = MibTableColumn
slePoolIndex = _SlePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 1),
    _SlePoolIndex_Type()
)
slePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolIndex.setStatus("current")
_SlePoolName_Type = OctetString
_SlePoolName_Object = MibTableColumn
slePoolName = _SlePoolName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 2),
    _SlePoolName_Type()
)
slePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolName.setStatus("current")


class _SlePoolDefaultLeaseTime_Type(Integer32):
    """Custom type slePoolDefaultLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 2147483637),
    )


_SlePoolDefaultLeaseTime_Type.__name__ = "Integer32"
_SlePoolDefaultLeaseTime_Object = MibTableColumn
slePoolDefaultLeaseTime = _SlePoolDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 3),
    _SlePoolDefaultLeaseTime_Type()
)
slePoolDefaultLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolDefaultLeaseTime.setStatus("current")


class _SlePoolMaxLeaseTime_Type(Integer32):
    """Custom type slePoolMaxLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 2147483637),
    )


_SlePoolMaxLeaseTime_Type.__name__ = "Integer32"
_SlePoolMaxLeaseTime_Object = MibTableColumn
slePoolMaxLeaseTime = _SlePoolMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 4),
    _SlePoolMaxLeaseTime_Type()
)
slePoolMaxLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolMaxLeaseTime.setStatus("current")
_SlePoolSummaryTotal_Type = Unsigned32
_SlePoolSummaryTotal_Object = MibTableColumn
slePoolSummaryTotal = _SlePoolSummaryTotal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 5),
    _SlePoolSummaryTotal_Type()
)
slePoolSummaryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolSummaryTotal.setStatus("current")
_SlePoolSummaryAllocated_Type = Unsigned32
_SlePoolSummaryAllocated_Object = MibTableColumn
slePoolSummaryAllocated = _SlePoolSummaryAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 6),
    _SlePoolSummaryAllocated_Type()
)
slePoolSummaryAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolSummaryAllocated.setStatus("current")
_SlePoolSummaryBound_Type = Unsigned32
_SlePoolSummaryBound_Object = MibTableColumn
slePoolSummaryBound = _SlePoolSummaryBound_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 7),
    _SlePoolSummaryBound_Type()
)
slePoolSummaryBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolSummaryBound.setStatus("current")
_SlePoolSummaryOffered_Type = Unsigned32
_SlePoolSummaryOffered_Object = MibTableColumn
slePoolSummaryOffered = _SlePoolSummaryOffered_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 8),
    _SlePoolSummaryOffered_Type()
)
slePoolSummaryOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolSummaryOffered.setStatus("current")
_SlePoolSummaryFixed_Type = Unsigned32
_SlePoolSummaryFixed_Object = MibTableColumn
slePoolSummaryFixed = _SlePoolSummaryFixed_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 9),
    _SlePoolSummaryFixed_Type()
)
slePoolSummaryFixed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolSummaryFixed.setStatus("current")
_SlePoolSummaryAbandon_Type = Unsigned32
_SlePoolSummaryAbandon_Object = MibTableColumn
slePoolSummaryAbandon = _SlePoolSummaryAbandon_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 10),
    _SlePoolSummaryAbandon_Type()
)
slePoolSummaryAbandon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolSummaryAbandon.setStatus("current")
_SlePoolSummaryAvailable_Type = Unsigned32
_SlePoolSummaryAvailable_Object = MibTableColumn
slePoolSummaryAvailable = _SlePoolSummaryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 11),
    _SlePoolSummaryAvailable_Type()
)
slePoolSummaryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolSummaryAvailable.setStatus("current")
_SlePoolSummarySubnet_Type = Unsigned32
_SlePoolSummarySubnet_Object = MibTableColumn
slePoolSummarySubnet = _SlePoolSummarySubnet_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 12),
    _SlePoolSummarySubnet_Type()
)
slePoolSummarySubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolSummarySubnet.setStatus("current")


class _SlePoolDomainName_Type(OctetString):
    """Custom type slePoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SlePoolDomainName_Type.__name__ = "OctetString"
_SlePoolDomainName_Object = MibTableColumn
slePoolDomainName = _SlePoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 1, 1, 13),
    _SlePoolDomainName_Type()
)
slePoolDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolDomainName.setStatus("current")
_SlePoolControl_ObjectIdentity = ObjectIdentity
slePoolControl = _SlePoolControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2)
)


class _SlePoolControlRequest_Type(Integer32):
    """Custom type slePoolControlRequest based on Integer32"""
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
        *(("createPool", 1),
          ("destroyPool", 2),
          ("setPoolLeaseTimeProfile", 3),
          ("setPoolDomainName", 4))
    )


_SlePoolControlRequest_Type.__name__ = "Integer32"
_SlePoolControlRequest_Object = MibScalar
slePoolControlRequest = _SlePoolControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2, 1),
    _SlePoolControlRequest_Type()
)
slePoolControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePoolControlRequest.setStatus("current")
_SlePoolControlStatus_Type = SleControlStatusType
_SlePoolControlStatus_Object = MibScalar
slePoolControlStatus = _SlePoolControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2, 2),
    _SlePoolControlStatus_Type()
)
slePoolControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolControlStatus.setStatus("current")
_SlePoolControlTimer_Type = Gauge32
_SlePoolControlTimer_Object = MibScalar
slePoolControlTimer = _SlePoolControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2, 3),
    _SlePoolControlTimer_Type()
)
slePoolControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePoolControlTimer.setStatus("current")
_SlePoolControlTImeStamp_Type = TimeTicks
_SlePoolControlTImeStamp_Object = MibScalar
slePoolControlTImeStamp = _SlePoolControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2, 4),
    _SlePoolControlTImeStamp_Type()
)
slePoolControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolControlTImeStamp.setStatus("current")
_SlePoolControlReqResult_Type = SleControlRequestResultType
_SlePoolControlReqResult_Object = MibScalar
slePoolControlReqResult = _SlePoolControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2, 5),
    _SlePoolControlReqResult_Type()
)
slePoolControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePoolControlReqResult.setStatus("current")


class _SlePoolControlIndex_Type(Integer32):
    """Custom type slePoolControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SlePoolControlIndex_Type.__name__ = "Integer32"
_SlePoolControlIndex_Object = MibScalar
slePoolControlIndex = _SlePoolControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2, 6),
    _SlePoolControlIndex_Type()
)
slePoolControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePoolControlIndex.setStatus("current")
_SlePoolControlName_Type = OctetString
_SlePoolControlName_Object = MibScalar
slePoolControlName = _SlePoolControlName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2, 7),
    _SlePoolControlName_Type()
)
slePoolControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePoolControlName.setStatus("current")


class _SlePoolControlDefaultLeaseTime_Type(Integer32):
    """Custom type slePoolControlDefaultLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SlePoolControlDefaultLeaseTime_Type.__name__ = "Integer32"
_SlePoolControlDefaultLeaseTime_Object = MibScalar
slePoolControlDefaultLeaseTime = _SlePoolControlDefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2, 8),
    _SlePoolControlDefaultLeaseTime_Type()
)
slePoolControlDefaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePoolControlDefaultLeaseTime.setStatus("current")


class _SlePoolControlMaxLeaseTime_Type(Integer32):
    """Custom type slePoolControlMaxLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 2147483637),
    )


_SlePoolControlMaxLeaseTime_Type.__name__ = "Integer32"
_SlePoolControlMaxLeaseTime_Object = MibScalar
slePoolControlMaxLeaseTime = _SlePoolControlMaxLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2, 9),
    _SlePoolControlMaxLeaseTime_Type()
)
slePoolControlMaxLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePoolControlMaxLeaseTime.setStatus("current")


class _SlePoolControlDomainName_Type(OctetString):
    """Custom type slePoolControlDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 64),
    )


_SlePoolControlDomainName_Type.__name__ = "OctetString"
_SlePoolControlDomainName_Object = MibScalar
slePoolControlDomainName = _SlePoolControlDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 2, 10),
    _SlePoolControlDomainName_Type()
)
slePoolControlDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slePoolControlDomainName.setStatus("current")
_SlePoolNotification_ObjectIdentity = ObjectIdentity
slePoolNotification = _SlePoolNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 3)
)
_SleDns_ObjectIdentity = ObjectIdentity
sleDns = _SleDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6)
)
_SleDnsTable_Object = MibTable
sleDnsTable = _SleDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 1)
)
if mibBuilder.loadTexts:
    sleDnsTable.setStatus("current")
_SleDnsEntry_Object = MibTableRow
sleDnsEntry = _SleDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 1, 1)
)
sleDnsEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "slePoolIndex"),
    (0, "SLE-DHCP-MIB", "sleDnsIndex"),
)
if mibBuilder.loadTexts:
    sleDnsEntry.setStatus("current")


class _SleDnsIndex_Type(Integer32):
    """Custom type sleDnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SleDnsIndex_Type.__name__ = "Integer32"
_SleDnsIndex_Object = MibTableColumn
sleDnsIndex = _SleDnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 1, 1, 1),
    _SleDnsIndex_Type()
)
sleDnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDnsIndex.setStatus("current")
_SleDnsIp_Type = IpAddress
_SleDnsIp_Object = MibTableColumn
sleDnsIp = _SleDnsIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 1, 1, 2),
    _SleDnsIp_Type()
)
sleDnsIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDnsIp.setStatus("current")
_SleDnsControl_ObjectIdentity = ObjectIdentity
sleDnsControl = _SleDnsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 2)
)


class _SleDnsControlRequest_Type(Integer32):
    """Custom type sleDnsControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDns", 1),
          ("destroyDns", 2))
    )


_SleDnsControlRequest_Type.__name__ = "Integer32"
_SleDnsControlRequest_Object = MibScalar
sleDnsControlRequest = _SleDnsControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 2, 1),
    _SleDnsControlRequest_Type()
)
sleDnsControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDnsControlRequest.setStatus("current")
_SleDnsControlStatus_Type = SleControlStatusType
_SleDnsControlStatus_Object = MibScalar
sleDnsControlStatus = _SleDnsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 2, 2),
    _SleDnsControlStatus_Type()
)
sleDnsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDnsControlStatus.setStatus("current")
_SleDnsControlTimer_Type = Gauge32
_SleDnsControlTimer_Object = MibScalar
sleDnsControlTimer = _SleDnsControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 2, 3),
    _SleDnsControlTimer_Type()
)
sleDnsControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDnsControlTimer.setStatus("current")
_SleDnsControlTImeStamp_Type = TimeTicks
_SleDnsControlTImeStamp_Object = MibScalar
sleDnsControlTImeStamp = _SleDnsControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 2, 4),
    _SleDnsControlTImeStamp_Type()
)
sleDnsControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDnsControlTImeStamp.setStatus("current")
_SleDnsControlReqResult_Type = SleControlRequestResultType
_SleDnsControlReqResult_Object = MibScalar
sleDnsControlReqResult = _SleDnsControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 2, 5),
    _SleDnsControlReqResult_Type()
)
sleDnsControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDnsControlReqResult.setStatus("current")


class _SleDnsControlPoolIndex_Type(Integer32):
    """Custom type sleDnsControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDnsControlPoolIndex_Type.__name__ = "Integer32"
_SleDnsControlPoolIndex_Object = MibScalar
sleDnsControlPoolIndex = _SleDnsControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 2, 6),
    _SleDnsControlPoolIndex_Type()
)
sleDnsControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDnsControlPoolIndex.setStatus("current")


class _SleDnsControlIndex_Type(Integer32):
    """Custom type sleDnsControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SleDnsControlIndex_Type.__name__ = "Integer32"
_SleDnsControlIndex_Object = MibScalar
sleDnsControlIndex = _SleDnsControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 2, 7),
    _SleDnsControlIndex_Type()
)
sleDnsControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDnsControlIndex.setStatus("current")
_SleDnsControlIp_Type = IpAddress
_SleDnsControlIp_Object = MibScalar
sleDnsControlIp = _SleDnsControlIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 2, 8),
    _SleDnsControlIp_Type()
)
sleDnsControlIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDnsControlIp.setStatus("current")
_SleDnsNotification_ObjectIdentity = ObjectIdentity
sleDnsNotification = _SleDnsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 3)
)
_SleSubnet_ObjectIdentity = ObjectIdentity
sleSubnet = _SleSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7)
)
_SleSubnetTable_Object = MibTable
sleSubnetTable = _SleSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 1)
)
if mibBuilder.loadTexts:
    sleSubnetTable.setStatus("current")
_SleSubnetEntry_Object = MibTableRow
sleSubnetEntry = _SleSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 1, 1)
)
sleSubnetEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "slePoolIndex"),
    (0, "SLE-DHCP-MIB", "sleSubnetIp"),
    (0, "SLE-DHCP-MIB", "sleSubnetMask"),
)
if mibBuilder.loadTexts:
    sleSubnetEntry.setStatus("current")
_SleSubnetIp_Type = IpAddress
_SleSubnetIp_Object = MibTableColumn
sleSubnetIp = _SleSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 1, 1, 1),
    _SleSubnetIp_Type()
)
sleSubnetIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSubnetIp.setStatus("current")


class _SleSubnetMask_Type(Integer32):
    """Custom type sleSubnetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleSubnetMask_Type.__name__ = "Integer32"
_SleSubnetMask_Object = MibTableColumn
sleSubnetMask = _SleSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 1, 1, 2),
    _SleSubnetMask_Type()
)
sleSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSubnetMask.setStatus("current")
_SleSubnetDefaultGateway_Type = IpAddress
_SleSubnetDefaultGateway_Object = MibTableColumn
sleSubnetDefaultGateway = _SleSubnetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 1, 1, 3),
    _SleSubnetDefaultGateway_Type()
)
sleSubnetDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSubnetDefaultGateway.setStatus("current")
_SleSubnetControl_ObjectIdentity = ObjectIdentity
sleSubnetControl = _SleSubnetControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 2)
)


class _SleSubnetControlRequest_Type(Integer32):
    """Custom type sleSubnetControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createSubnet", 1),
          ("destroySubnet", 2))
    )


_SleSubnetControlRequest_Type.__name__ = "Integer32"
_SleSubnetControlRequest_Object = MibScalar
sleSubnetControlRequest = _SleSubnetControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 2, 1),
    _SleSubnetControlRequest_Type()
)
sleSubnetControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSubnetControlRequest.setStatus("current")
_SleSubnetControlStatus_Type = SleControlStatusType
_SleSubnetControlStatus_Object = MibScalar
sleSubnetControlStatus = _SleSubnetControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 2, 2),
    _SleSubnetControlStatus_Type()
)
sleSubnetControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSubnetControlStatus.setStatus("current")
_SleSubnetControlTimer_Type = Gauge32
_SleSubnetControlTimer_Object = MibScalar
sleSubnetControlTimer = _SleSubnetControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 2, 3),
    _SleSubnetControlTimer_Type()
)
sleSubnetControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSubnetControlTimer.setStatus("current")
_SleSubnetControlTImeStamp_Type = TimeTicks
_SleSubnetControlTImeStamp_Object = MibScalar
sleSubnetControlTImeStamp = _SleSubnetControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 2, 4),
    _SleSubnetControlTImeStamp_Type()
)
sleSubnetControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSubnetControlTImeStamp.setStatus("current")
_SleSubnetControlReqResult_Type = SleControlRequestResultType
_SleSubnetControlReqResult_Object = MibScalar
sleSubnetControlReqResult = _SleSubnetControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 2, 5),
    _SleSubnetControlReqResult_Type()
)
sleSubnetControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSubnetControlReqResult.setStatus("current")


class _SleSubnetControlPoolIndex_Type(Integer32):
    """Custom type sleSubnetControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleSubnetControlPoolIndex_Type.__name__ = "Integer32"
_SleSubnetControlPoolIndex_Object = MibScalar
sleSubnetControlPoolIndex = _SleSubnetControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 2, 6),
    _SleSubnetControlPoolIndex_Type()
)
sleSubnetControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSubnetControlPoolIndex.setStatus("current")
_SleSubnetControlIp_Type = IpAddress
_SleSubnetControlIp_Object = MibScalar
sleSubnetControlIp = _SleSubnetControlIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 2, 7),
    _SleSubnetControlIp_Type()
)
sleSubnetControlIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSubnetControlIp.setStatus("current")


class _SleSubnetControlMask_Type(Integer32):
    """Custom type sleSubnetControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleSubnetControlMask_Type.__name__ = "Integer32"
_SleSubnetControlMask_Object = MibScalar
sleSubnetControlMask = _SleSubnetControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 2, 8),
    _SleSubnetControlMask_Type()
)
sleSubnetControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleSubnetControlMask.setStatus("current")
_SleSubnetNotification_ObjectIdentity = ObjectIdentity
sleSubnetNotification = _SleSubnetNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 3)
)
_SleDefaultGateway_ObjectIdentity = ObjectIdentity
sleDefaultGateway = _SleDefaultGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8)
)
_SleDefaultGatewayTable_Object = MibTable
sleDefaultGatewayTable = _SleDefaultGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 1)
)
if mibBuilder.loadTexts:
    sleDefaultGatewayTable.setStatus("current")
_SleDefaultGatewayEntry_Object = MibTableRow
sleDefaultGatewayEntry = _SleDefaultGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 1, 1)
)
sleDefaultGatewayEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "slePoolIndex"),
    (0, "SLE-DHCP-MIB", "sleDefaultGatewayIndex"),
)
if mibBuilder.loadTexts:
    sleDefaultGatewayEntry.setStatus("current")


class _SleDefaultGatewayIndex_Type(Integer32):
    """Custom type sleDefaultGatewayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SleDefaultGatewayIndex_Type.__name__ = "Integer32"
_SleDefaultGatewayIndex_Object = MibTableColumn
sleDefaultGatewayIndex = _SleDefaultGatewayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 1, 1, 1),
    _SleDefaultGatewayIndex_Type()
)
sleDefaultGatewayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDefaultGatewayIndex.setStatus("current")
_SleDefaultGatewayIp_Type = IpAddress
_SleDefaultGatewayIp_Object = MibTableColumn
sleDefaultGatewayIp = _SleDefaultGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 1, 1, 2),
    _SleDefaultGatewayIp_Type()
)
sleDefaultGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDefaultGatewayIp.setStatus("current")
_SleDefaultGatewayControl_ObjectIdentity = ObjectIdentity
sleDefaultGatewayControl = _SleDefaultGatewayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 2)
)


class _SleDefaultGatewayControlRequest_Type(Integer32):
    """Custom type sleDefaultGatewayControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createDefaultGateway", 1),
          ("destroyDefaultGateway", 2))
    )


_SleDefaultGatewayControlRequest_Type.__name__ = "Integer32"
_SleDefaultGatewayControlRequest_Object = MibScalar
sleDefaultGatewayControlRequest = _SleDefaultGatewayControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 2, 1),
    _SleDefaultGatewayControlRequest_Type()
)
sleDefaultGatewayControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDefaultGatewayControlRequest.setStatus("current")
_SleDefaultGatewayControlStatus_Type = SleControlStatusType
_SleDefaultGatewayControlStatus_Object = MibScalar
sleDefaultGatewayControlStatus = _SleDefaultGatewayControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 2, 2),
    _SleDefaultGatewayControlStatus_Type()
)
sleDefaultGatewayControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDefaultGatewayControlStatus.setStatus("current")
_SleDefaultGatewayControlTimer_Type = Gauge32
_SleDefaultGatewayControlTimer_Object = MibScalar
sleDefaultGatewayControlTimer = _SleDefaultGatewayControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 2, 3),
    _SleDefaultGatewayControlTimer_Type()
)
sleDefaultGatewayControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDefaultGatewayControlTimer.setStatus("current")
_SleDefaultGatewayControlTImeStamp_Type = TimeTicks
_SleDefaultGatewayControlTImeStamp_Object = MibScalar
sleDefaultGatewayControlTImeStamp = _SleDefaultGatewayControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 2, 4),
    _SleDefaultGatewayControlTImeStamp_Type()
)
sleDefaultGatewayControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDefaultGatewayControlTImeStamp.setStatus("current")
_SleDefaultGatewayControlReqResult_Type = SleControlRequestResultType
_SleDefaultGatewayControlReqResult_Object = MibScalar
sleDefaultGatewayControlReqResult = _SleDefaultGatewayControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 2, 5),
    _SleDefaultGatewayControlReqResult_Type()
)
sleDefaultGatewayControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDefaultGatewayControlReqResult.setStatus("current")


class _SleDefaultGatewayControlPoolIndex_Type(Integer32):
    """Custom type sleDefaultGatewayControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleDefaultGatewayControlPoolIndex_Type.__name__ = "Integer32"
_SleDefaultGatewayControlPoolIndex_Object = MibScalar
sleDefaultGatewayControlPoolIndex = _SleDefaultGatewayControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 2, 6),
    _SleDefaultGatewayControlPoolIndex_Type()
)
sleDefaultGatewayControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDefaultGatewayControlPoolIndex.setStatus("current")


class _SleDefaultGatewayControlIndex_Type(Integer32):
    """Custom type sleDefaultGatewayControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SleDefaultGatewayControlIndex_Type.__name__ = "Integer32"
_SleDefaultGatewayControlIndex_Object = MibScalar
sleDefaultGatewayControlIndex = _SleDefaultGatewayControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 2, 7),
    _SleDefaultGatewayControlIndex_Type()
)
sleDefaultGatewayControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDefaultGatewayControlIndex.setStatus("current")
_SleDefaultGatewayControlIp_Type = IpAddress
_SleDefaultGatewayControlIp_Object = MibScalar
sleDefaultGatewayControlIp = _SleDefaultGatewayControlIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 2, 8),
    _SleDefaultGatewayControlIp_Type()
)
sleDefaultGatewayControlIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleDefaultGatewayControlIp.setStatus("current")
_SleDefaultGatewayNotification_ObjectIdentity = ObjectIdentity
sleDefaultGatewayNotification = _SleDefaultGatewayNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 3)
)
_SleRange_ObjectIdentity = ObjectIdentity
sleRange = _SleRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9)
)
_SleRangeTable_Object = MibTable
sleRangeTable = _SleRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 1)
)
if mibBuilder.loadTexts:
    sleRangeTable.setStatus("current")
_SleRangeEntry_Object = MibTableRow
sleRangeEntry = _SleRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 1, 1)
)
sleRangeEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "slePoolIndex"),
    (0, "SLE-DHCP-MIB", "sleRangeStart"),
    (0, "SLE-DHCP-MIB", "sleRangeEnd"),
)
if mibBuilder.loadTexts:
    sleRangeEntry.setStatus("current")
_SleRangeStart_Type = IpAddress
_SleRangeStart_Object = MibTableColumn
sleRangeStart = _SleRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 1, 1, 1),
    _SleRangeStart_Type()
)
sleRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRangeStart.setStatus("current")
_SleRangeEnd_Type = IpAddress
_SleRangeEnd_Object = MibTableColumn
sleRangeEnd = _SleRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 1, 1, 2),
    _SleRangeEnd_Type()
)
sleRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRangeEnd.setStatus("current")
_SleRangeSubnetIP_Type = IpAddress
_SleRangeSubnetIP_Object = MibTableColumn
sleRangeSubnetIP = _SleRangeSubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 1, 1, 3),
    _SleRangeSubnetIP_Type()
)
sleRangeSubnetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRangeSubnetIP.setStatus("current")


class _SleRangeSubnetMask_Type(Integer32):
    """Custom type sleRangeSubnetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleRangeSubnetMask_Type.__name__ = "Integer32"
_SleRangeSubnetMask_Object = MibTableColumn
sleRangeSubnetMask = _SleRangeSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 1, 1, 4),
    _SleRangeSubnetMask_Type()
)
sleRangeSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRangeSubnetMask.setStatus("current")
_SleRangeControl_ObjectIdentity = ObjectIdentity
sleRangeControl = _SleRangeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 2)
)


class _SleRangeControlRequest_Type(Integer32):
    """Custom type sleRangeControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRange", 1),
          ("destroyRange", 2))
    )


_SleRangeControlRequest_Type.__name__ = "Integer32"
_SleRangeControlRequest_Object = MibScalar
sleRangeControlRequest = _SleRangeControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 2, 1),
    _SleRangeControlRequest_Type()
)
sleRangeControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRangeControlRequest.setStatus("current")
_SleRangeControlStatus_Type = SleControlStatusType
_SleRangeControlStatus_Object = MibScalar
sleRangeControlStatus = _SleRangeControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 2, 2),
    _SleRangeControlStatus_Type()
)
sleRangeControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRangeControlStatus.setStatus("current")
_SleRangeControlTimer_Type = Gauge32
_SleRangeControlTimer_Object = MibScalar
sleRangeControlTimer = _SleRangeControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 2, 3),
    _SleRangeControlTimer_Type()
)
sleRangeControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRangeControlTimer.setStatus("current")
_SleRangeControlTImeStamp_Type = TimeTicks
_SleRangeControlTImeStamp_Object = MibScalar
sleRangeControlTImeStamp = _SleRangeControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 2, 4),
    _SleRangeControlTImeStamp_Type()
)
sleRangeControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRangeControlTImeStamp.setStatus("current")
_SleRangeControlReqResult_Type = SleControlRequestResultType
_SleRangeControlReqResult_Object = MibScalar
sleRangeControlReqResult = _SleRangeControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 2, 5),
    _SleRangeControlReqResult_Type()
)
sleRangeControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRangeControlReqResult.setStatus("current")


class _SleRangeControlPoolIndex_Type(Integer32):
    """Custom type sleRangeControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleRangeControlPoolIndex_Type.__name__ = "Integer32"
_SleRangeControlPoolIndex_Object = MibScalar
sleRangeControlPoolIndex = _SleRangeControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 2, 6),
    _SleRangeControlPoolIndex_Type()
)
sleRangeControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRangeControlPoolIndex.setStatus("current")
_SleRangeControlStart_Type = IpAddress
_SleRangeControlStart_Object = MibScalar
sleRangeControlStart = _SleRangeControlStart_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 2, 7),
    _SleRangeControlStart_Type()
)
sleRangeControlStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRangeControlStart.setStatus("current")
_SleRangeControlEnd_Type = IpAddress
_SleRangeControlEnd_Object = MibScalar
sleRangeControlEnd = _SleRangeControlEnd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 2, 8),
    _SleRangeControlEnd_Type()
)
sleRangeControlEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleRangeControlEnd.setStatus("current")
_SleRangeNotification_ObjectIdentity = ObjectIdentity
sleRangeNotification = _SleRangeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 3)
)
_SleFixed_ObjectIdentity = ObjectIdentity
sleFixed = _SleFixed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10)
)
_SleFixedTable_Object = MibTable
sleFixedTable = _SleFixedTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 1)
)
if mibBuilder.loadTexts:
    sleFixedTable.setStatus("current")
_SleFixedEntry_Object = MibTableRow
sleFixedEntry = _SleFixedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 1, 1)
)
sleFixedEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "slePoolIndex"),
    (0, "SLE-DHCP-MIB", "sleFixedIp"),
    (0, "SLE-DHCP-MIB", "sleFixedMac"),
)
if mibBuilder.loadTexts:
    sleFixedEntry.setStatus("current")
_SleFixedIp_Type = IpAddress
_SleFixedIp_Object = MibTableColumn
sleFixedIp = _SleFixedIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 1, 1, 1),
    _SleFixedIp_Type()
)
sleFixedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFixedIp.setStatus("current")
_SleFixedMac_Type = MacAddress
_SleFixedMac_Object = MibTableColumn
sleFixedMac = _SleFixedMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 1, 1, 2),
    _SleFixedMac_Type()
)
sleFixedMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFixedMac.setStatus("current")
_SleFixedControl_ObjectIdentity = ObjectIdentity
sleFixedControl = _SleFixedControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 2)
)


class _SleFixedControlRequest_Type(Integer32):
    """Custom type sleFixedControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createFixed", 1),
          ("destroyFixed", 2))
    )


_SleFixedControlRequest_Type.__name__ = "Integer32"
_SleFixedControlRequest_Object = MibScalar
sleFixedControlRequest = _SleFixedControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 2, 1),
    _SleFixedControlRequest_Type()
)
sleFixedControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFixedControlRequest.setStatus("current")
_SleFixedControlStatus_Type = SleControlStatusType
_SleFixedControlStatus_Object = MibScalar
sleFixedControlStatus = _SleFixedControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 2, 2),
    _SleFixedControlStatus_Type()
)
sleFixedControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFixedControlStatus.setStatus("current")
_SleFixedControlTimer_Type = Gauge32
_SleFixedControlTimer_Object = MibScalar
sleFixedControlTimer = _SleFixedControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 2, 3),
    _SleFixedControlTimer_Type()
)
sleFixedControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFixedControlTimer.setStatus("current")
_SleFixedControlTImeStamp_Type = TimeTicks
_SleFixedControlTImeStamp_Object = MibScalar
sleFixedControlTImeStamp = _SleFixedControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 2, 4),
    _SleFixedControlTImeStamp_Type()
)
sleFixedControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFixedControlTImeStamp.setStatus("current")
_SleFixedControlReqResult_Type = SleControlRequestResultType
_SleFixedControlReqResult_Object = MibScalar
sleFixedControlReqResult = _SleFixedControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 2, 5),
    _SleFixedControlReqResult_Type()
)
sleFixedControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFixedControlReqResult.setStatus("current")


class _SleFixedControlPoolIndex_Type(Integer32):
    """Custom type sleFixedControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleFixedControlPoolIndex_Type.__name__ = "Integer32"
_SleFixedControlPoolIndex_Object = MibScalar
sleFixedControlPoolIndex = _SleFixedControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 2, 6),
    _SleFixedControlPoolIndex_Type()
)
sleFixedControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFixedControlPoolIndex.setStatus("current")
_SleFixedControlIp_Type = IpAddress
_SleFixedControlIp_Object = MibScalar
sleFixedControlIp = _SleFixedControlIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 2, 7),
    _SleFixedControlIp_Type()
)
sleFixedControlIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFixedControlIp.setStatus("current")
_SleFixedControlMac_Type = MacAddress
_SleFixedControlMac_Object = MibScalar
sleFixedControlMac = _SleFixedControlMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 2, 8),
    _SleFixedControlMac_Type()
)
sleFixedControlMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleFixedControlMac.setStatus("current")
_SleFixedNotification_ObjectIdentity = ObjectIdentity
sleFixedNotification = _SleFixedNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 3)
)
_SleOption82_ObjectIdentity = ObjectIdentity
sleOption82 = _SleOption82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11)
)
_SleOption82Table_Object = MibTable
sleOption82Table = _SleOption82Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 1)
)
if mibBuilder.loadTexts:
    sleOption82Table.setStatus("current")
_SleOption82Entry_Object = MibTableRow
sleOption82Entry = _SleOption82Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 1, 1)
)
sleOption82Entry.setIndexNames(
    (0, "SLE-DHCP-MIB", "sleOption82RemoteType"),
    (0, "SLE-DHCP-MIB", "sleOption82RemoteId"),
    (0, "SLE-DHCP-MIB", "sleOption82CircuitType"),
    (0, "SLE-DHCP-MIB", "sleOption82CircuitId"),
)
if mibBuilder.loadTexts:
    sleOption82Entry.setStatus("current")


class _SleOption82RemoteType_Type(Integer32):
    """Custom type sleOption82RemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipaddress", 1),
          ("binary", 2),
          ("text", 3))
    )


_SleOption82RemoteType_Type.__name__ = "Integer32"
_SleOption82RemoteType_Object = MibTableColumn
sleOption82RemoteType = _SleOption82RemoteType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 1, 1, 1),
    _SleOption82RemoteType_Type()
)
sleOption82RemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82RemoteType.setStatus("current")


class _SleOption82RemoteId_Type(OctetString):
    """Custom type sleOption82RemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleOption82RemoteId_Type.__name__ = "OctetString"
_SleOption82RemoteId_Object = MibTableColumn
sleOption82RemoteId = _SleOption82RemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 1, 1, 2),
    _SleOption82RemoteId_Type()
)
sleOption82RemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82RemoteId.setStatus("current")


class _SleOption82CircuitType_Type(Integer32):
    """Custom type sleOption82CircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("index", 1),
          ("binary", 2),
          ("text", 3))
    )


_SleOption82CircuitType_Type.__name__ = "Integer32"
_SleOption82CircuitType_Object = MibTableColumn
sleOption82CircuitType = _SleOption82CircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 1, 1, 3),
    _SleOption82CircuitType_Type()
)
sleOption82CircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82CircuitType.setStatus("current")


class _SleOption82CircuitId_Type(OctetString):
    """Custom type sleOption82CircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SleOption82CircuitId_Type.__name__ = "OctetString"
_SleOption82CircuitId_Object = MibTableColumn
sleOption82CircuitId = _SleOption82CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 1, 1, 4),
    _SleOption82CircuitId_Type()
)
sleOption82CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82CircuitId.setStatus("current")


class _SleOption82Limit_Type(Integer32):
    """Custom type sleOption82Limit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483637),
    )


_SleOption82Limit_Type.__name__ = "Integer32"
_SleOption82Limit_Object = MibTableColumn
sleOption82Limit = _SleOption82Limit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 1, 1, 5),
    _SleOption82Limit_Type()
)
sleOption82Limit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82Limit.setStatus("current")
_SleOption82PoolName_Type = OctetString
_SleOption82PoolName_Object = MibTableColumn
sleOption82PoolName = _SleOption82PoolName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 1, 1, 6),
    _SleOption82PoolName_Type()
)
sleOption82PoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82PoolName.setStatus("current")
_SleOption82Control_ObjectIdentity = ObjectIdentity
sleOption82Control = _SleOption82Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2)
)


class _SleOption82ControlRequest_Type(Integer32):
    """Custom type sleOption82ControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createOption82", 1),
          ("destroyOption82", 2),
          ("setOption82Profile", 3))
    )


_SleOption82ControlRequest_Type.__name__ = "Integer32"
_SleOption82ControlRequest_Object = MibScalar
sleOption82ControlRequest = _SleOption82ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 1),
    _SleOption82ControlRequest_Type()
)
sleOption82ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82ControlRequest.setStatus("current")
_SleOption82ControlStatus_Type = SleControlStatusType
_SleOption82ControlStatus_Object = MibScalar
sleOption82ControlStatus = _SleOption82ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 2),
    _SleOption82ControlStatus_Type()
)
sleOption82ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82ControlStatus.setStatus("current")
_SleOption82ControlTimer_Type = Gauge32
_SleOption82ControlTimer_Object = MibScalar
sleOption82ControlTimer = _SleOption82ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 3),
    _SleOption82ControlTimer_Type()
)
sleOption82ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82ControlTimer.setStatus("current")
_SleOption82ControlTImeStamp_Type = TimeTicks
_SleOption82ControlTImeStamp_Object = MibScalar
sleOption82ControlTImeStamp = _SleOption82ControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 4),
    _SleOption82ControlTImeStamp_Type()
)
sleOption82ControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82ControlTImeStamp.setStatus("current")
_SleOption82ControlReqResult_Type = SleControlRequestResultType
_SleOption82ControlReqResult_Object = MibScalar
sleOption82ControlReqResult = _SleOption82ControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 5),
    _SleOption82ControlReqResult_Type()
)
sleOption82ControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82ControlReqResult.setStatus("current")


class _SleOption82ControlRemoteType_Type(Integer32):
    """Custom type sleOption82ControlRemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipaddress", 1),
          ("binary", 2),
          ("text", 3))
    )


_SleOption82ControlRemoteType_Type.__name__ = "Integer32"
_SleOption82ControlRemoteType_Object = MibScalar
sleOption82ControlRemoteType = _SleOption82ControlRemoteType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 6),
    _SleOption82ControlRemoteType_Type()
)
sleOption82ControlRemoteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82ControlRemoteType.setStatus("current")


class _SleOption82ControlRemoteId_Type(OctetString):
    """Custom type sleOption82ControlRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_SleOption82ControlRemoteId_Type.__name__ = "OctetString"
_SleOption82ControlRemoteId_Object = MibScalar
sleOption82ControlRemoteId = _SleOption82ControlRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 7),
    _SleOption82ControlRemoteId_Type()
)
sleOption82ControlRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82ControlRemoteId.setStatus("current")


class _SleOption82ControlCircuitType_Type(Integer32):
    """Custom type sleOption82ControlCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("index", 1),
          ("binary", 2),
          ("text", 3))
    )


_SleOption82ControlCircuitType_Type.__name__ = "Integer32"
_SleOption82ControlCircuitType_Object = MibScalar
sleOption82ControlCircuitType = _SleOption82ControlCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 8),
    _SleOption82ControlCircuitType_Type()
)
sleOption82ControlCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82ControlCircuitType.setStatus("current")


class _SleOption82ControlCircuitId_Type(OctetString):
    """Custom type sleOption82ControlCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SleOption82ControlCircuitId_Type.__name__ = "OctetString"
_SleOption82ControlCircuitId_Object = MibScalar
sleOption82ControlCircuitId = _SleOption82ControlCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 9),
    _SleOption82ControlCircuitId_Type()
)
sleOption82ControlCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82ControlCircuitId.setStatus("current")


class _SleOption82ControlLimit_Type(Integer32):
    """Custom type sleOption82ControlLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483637),
    )


_SleOption82ControlLimit_Type.__name__ = "Integer32"
_SleOption82ControlLimit_Object = MibScalar
sleOption82ControlLimit = _SleOption82ControlLimit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 10),
    _SleOption82ControlLimit_Type()
)
sleOption82ControlLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82ControlLimit.setStatus("current")
_SleOption82ControlPoolName_Type = OctetString
_SleOption82ControlPoolName_Object = MibScalar
sleOption82ControlPoolName = _SleOption82ControlPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 2, 11),
    _SleOption82ControlPoolName_Type()
)
sleOption82ControlPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82ControlPoolName.setStatus("current")
_SleOption82Notification_ObjectIdentity = ObjectIdentity
sleOption82Notification = _SleOption82Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 3)
)
_SleOption82System_ObjectIdentity = ObjectIdentity
sleOption82System = _SleOption82System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12)
)
_SleOption82SystemTable_Object = MibTable
sleOption82SystemTable = _SleOption82SystemTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 1)
)
if mibBuilder.loadTexts:
    sleOption82SystemTable.setStatus("current")
_SleOption82SystemEntry_Object = MibTableRow
sleOption82SystemEntry = _SleOption82SystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 1, 1)
)
sleOption82SystemEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "sleOption82SystemIndex"),
)
if mibBuilder.loadTexts:
    sleOption82SystemEntry.setStatus("current")
_SleOption82SystemIndex_Type = InterfaceIndex
_SleOption82SystemIndex_Object = MibTableColumn
sleOption82SystemIndex = _SleOption82SystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 1, 1, 1),
    _SleOption82SystemIndex_Type()
)
sleOption82SystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82SystemIndex.setStatus("current")


class _SleOption82SystemCtype_Type(Integer32):
    """Custom type sleOption82SystemCtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("index", 1),
          ("binary", 2),
          ("text", 3))
    )


_SleOption82SystemCtype_Type.__name__ = "Integer32"
_SleOption82SystemCtype_Object = MibTableColumn
sleOption82SystemCtype = _SleOption82SystemCtype_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 1, 1, 2),
    _SleOption82SystemCtype_Type()
)
sleOption82SystemCtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82SystemCtype.setStatus("current")


class _SleOption82SystemCid_Type(OctetString):
    """Custom type sleOption82SystemCid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleOption82SystemCid_Type.__name__ = "OctetString"
_SleOption82SystemCid_Object = MibTableColumn
sleOption82SystemCid = _SleOption82SystemCid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 1, 1, 3),
    _SleOption82SystemCid_Type()
)
sleOption82SystemCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82SystemCid.setStatus("current")
_SleOption82SystemControl_ObjectIdentity = ObjectIdentity
sleOption82SystemControl = _SleOption82SystemControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 2)
)


class _SleOption82SystemControlRequest_Type(Integer32):
    """Custom type sleOption82SystemControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setOption82SystemCircuit", 1)
    )


_SleOption82SystemControlRequest_Type.__name__ = "Integer32"
_SleOption82SystemControlRequest_Object = MibScalar
sleOption82SystemControlRequest = _SleOption82SystemControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 2, 1),
    _SleOption82SystemControlRequest_Type()
)
sleOption82SystemControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82SystemControlRequest.setStatus("current")
_SleOption82SystemControlStatus_Type = SleControlStatusType
_SleOption82SystemControlStatus_Object = MibScalar
sleOption82SystemControlStatus = _SleOption82SystemControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 2, 2),
    _SleOption82SystemControlStatus_Type()
)
sleOption82SystemControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82SystemControlStatus.setStatus("current")
_SleOption82SystemControlTimer_Type = Gauge32
_SleOption82SystemControlTimer_Object = MibScalar
sleOption82SystemControlTimer = _SleOption82SystemControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 2, 3),
    _SleOption82SystemControlTimer_Type()
)
sleOption82SystemControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82SystemControlTimer.setStatus("current")
_SleOption82SystemControlTImeStamp_Type = TimeTicks
_SleOption82SystemControlTImeStamp_Object = MibScalar
sleOption82SystemControlTImeStamp = _SleOption82SystemControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 2, 4),
    _SleOption82SystemControlTImeStamp_Type()
)
sleOption82SystemControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82SystemControlTImeStamp.setStatus("current")
_SleOption82SystemControlReqResult_Type = SleControlRequestResultType
_SleOption82SystemControlReqResult_Object = MibScalar
sleOption82SystemControlReqResult = _SleOption82SystemControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 2, 5),
    _SleOption82SystemControlReqResult_Type()
)
sleOption82SystemControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleOption82SystemControlReqResult.setStatus("current")


class _SleOption82SystemControlIndex_Type(Integer32):
    """Custom type sleOption82SystemControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleOption82SystemControlIndex_Type.__name__ = "Integer32"
_SleOption82SystemControlIndex_Object = MibScalar
sleOption82SystemControlIndex = _SleOption82SystemControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 2, 6),
    _SleOption82SystemControlIndex_Type()
)
sleOption82SystemControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82SystemControlIndex.setStatus("current")


class _SleOption82SystemControlCtype_Type(Integer32):
    """Custom type sleOption82SystemControlCtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("index", 1),
          ("binary", 2),
          ("text", 3))
    )


_SleOption82SystemControlCtype_Type.__name__ = "Integer32"
_SleOption82SystemControlCtype_Object = MibScalar
sleOption82SystemControlCtype = _SleOption82SystemControlCtype_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 2, 7),
    _SleOption82SystemControlCtype_Type()
)
sleOption82SystemControlCtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82SystemControlCtype.setStatus("current")


class _SleOption82SystemControlCid_Type(OctetString):
    """Custom type sleOption82SystemControlCid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SleOption82SystemControlCid_Type.__name__ = "OctetString"
_SleOption82SystemControlCid_Object = MibScalar
sleOption82SystemControlCid = _SleOption82SystemControlCid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 2, 8),
    _SleOption82SystemControlCid_Type()
)
sleOption82SystemControlCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleOption82SystemControlCid.setStatus("current")
_SleOption82CircuitNotification_ObjectIdentity = ObjectIdentity
sleOption82CircuitNotification = _SleOption82CircuitNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 3)
)
_SleIllegal_ObjectIdentity = ObjectIdentity
sleIllegal = _SleIllegal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13)
)
_SleIllegalTable_Object = MibTable
sleIllegalTable = _SleIllegalTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 1)
)
if mibBuilder.loadTexts:
    sleIllegalTable.setStatus("current")
_SleIllegalEntry_Object = MibTableRow
sleIllegalEntry = _SleIllegalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 1, 1)
)
sleIllegalEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "sleIllegalIp"),
    (0, "SLE-DHCP-MIB", "sleIllegalMac"),
)
if mibBuilder.loadTexts:
    sleIllegalEntry.setStatus("current")
_SleIllegalIp_Type = IpAddress
_SleIllegalIp_Object = MibTableColumn
sleIllegalIp = _SleIllegalIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 1, 1, 1),
    _SleIllegalIp_Type()
)
sleIllegalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIllegalIp.setStatus("current")
_SleIllegalMac_Type = MacAddress
_SleIllegalMac_Object = MibTableColumn
sleIllegalMac = _SleIllegalMac_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 1, 1, 2),
    _SleIllegalMac_Type()
)
sleIllegalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIllegalMac.setStatus("current")
_SleIllegalTime_Type = OctetString
_SleIllegalTime_Object = MibTableColumn
sleIllegalTime = _SleIllegalTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 1, 1, 3),
    _SleIllegalTime_Type()
)
sleIllegalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIllegalTime.setStatus("current")
_SleIllegalControl_ObjectIdentity = ObjectIdentity
sleIllegalControl = _SleIllegalControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 2)
)


class _SleIllegalControlRequest_Type(Integer32):
    """Custom type sleIllegalControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearIllegal", 1)
    )


_SleIllegalControlRequest_Type.__name__ = "Integer32"
_SleIllegalControlRequest_Object = MibScalar
sleIllegalControlRequest = _SleIllegalControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 2, 1),
    _SleIllegalControlRequest_Type()
)
sleIllegalControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIllegalControlRequest.setStatus("current")
_SleIllegalControlStatus_Type = SleControlStatusType
_SleIllegalControlStatus_Object = MibScalar
sleIllegalControlStatus = _SleIllegalControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 2, 2),
    _SleIllegalControlStatus_Type()
)
sleIllegalControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIllegalControlStatus.setStatus("current")
_SleIllegalControlTimer_Type = Gauge32
_SleIllegalControlTimer_Object = MibScalar
sleIllegalControlTimer = _SleIllegalControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 2, 3),
    _SleIllegalControlTimer_Type()
)
sleIllegalControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleIllegalControlTimer.setStatus("current")
_SleIllegalControlTImeStamp_Type = TimeTicks
_SleIllegalControlTImeStamp_Object = MibScalar
sleIllegalControlTImeStamp = _SleIllegalControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 2, 4),
    _SleIllegalControlTImeStamp_Type()
)
sleIllegalControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIllegalControlTImeStamp.setStatus("current")
_SleIllegalControlReqResult_Type = SleControlRequestResultType
_SleIllegalControlReqResult_Object = MibScalar
sleIllegalControlReqResult = _SleIllegalControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 2, 5),
    _SleIllegalControlReqResult_Type()
)
sleIllegalControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIllegalControlReqResult.setStatus("current")
_SleIllegalNotification_ObjectIdentity = ObjectIdentity
sleIllegalNotification = _SleIllegalNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 3)
)
_SleLeased_ObjectIdentity = ObjectIdentity
sleLeased = _SleLeased_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14)
)
_SleLeasedTable_Object = MibTable
sleLeasedTable = _SleLeasedTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1)
)
if mibBuilder.loadTexts:
    sleLeasedTable.setStatus("current")
_SleLeasedEntry_Object = MibTableRow
sleLeasedEntry = _SleLeasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1, 1)
)
sleLeasedEntry.setIndexNames(
    (0, "SLE-DHCP-MIB", "sleLeasedIp"),
)
if mibBuilder.loadTexts:
    sleLeasedEntry.setStatus("current")
_SleLeasedIp_Type = IpAddress
_SleLeasedIp_Object = MibTableColumn
sleLeasedIp = _SleLeasedIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1, 1, 1),
    _SleLeasedIp_Type()
)
sleLeasedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedIp.setStatus("current")


class _SleLeasedPoolIndex_Type(Integer32):
    """Custom type sleLeasedPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleLeasedPoolIndex_Type.__name__ = "Integer32"
_SleLeasedPoolIndex_Object = MibTableColumn
sleLeasedPoolIndex = _SleLeasedPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1, 1, 2),
    _SleLeasedPoolIndex_Type()
)
sleLeasedPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleLeasedPoolIndex.setStatus("current")
_SleLeasedPoolName_Type = OctetString
_SleLeasedPoolName_Object = MibTableColumn
sleLeasedPoolName = _SleLeasedPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1, 1, 3),
    _SleLeasedPoolName_Type()
)
sleLeasedPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedPoolName.setStatus("current")
_SleLeasedTime_Type = OctetString
_SleLeasedTime_Object = MibTableColumn
sleLeasedTime = _SleLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1, 1, 4),
    _SleLeasedTime_Type()
)
sleLeasedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedTime.setStatus("current")
_SleLeasedHwaddr_Type = OctetString
_SleLeasedHwaddr_Object = MibTableColumn
sleLeasedHwaddr = _SleLeasedHwaddr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1, 1, 5),
    _SleLeasedHwaddr_Type()
)
sleLeasedHwaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedHwaddr.setStatus("current")
_SleLeasedHostname_Type = OctetString
_SleLeasedHostname_Object = MibTableColumn
sleLeasedHostname = _SleLeasedHostname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1, 1, 6),
    _SleLeasedHostname_Type()
)
sleLeasedHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedHostname.setStatus("current")
_SleLeasedUid_Type = OctetString
_SleLeasedUid_Object = MibTableColumn
sleLeasedUid = _SleLeasedUid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1, 1, 7),
    _SleLeasedUid_Type()
)
sleLeasedUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedUid.setStatus("current")
_SleLeasedRid_Type = OctetString
_SleLeasedRid_Object = MibTableColumn
sleLeasedRid = _SleLeasedRid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1, 1, 8),
    _SleLeasedRid_Type()
)
sleLeasedRid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedRid.setStatus("current")
_SleLeasedCid_Type = OctetString
_SleLeasedCid_Object = MibTableColumn
sleLeasedCid = _SleLeasedCid_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 1, 1, 9),
    _SleLeasedCid_Type()
)
sleLeasedCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedCid.setStatus("current")
_SleLeasedControl_ObjectIdentity = ObjectIdentity
sleLeasedControl = _SleLeasedControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 2)
)


class _SleLeasedControlRequest_Type(Integer32):
    """Custom type sleLeasedControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushLeasedIpMask", 1),
          ("flushLeasedPool", 2))
    )


_SleLeasedControlRequest_Type.__name__ = "Integer32"
_SleLeasedControlRequest_Object = MibScalar
sleLeasedControlRequest = _SleLeasedControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 2, 1),
    _SleLeasedControlRequest_Type()
)
sleLeasedControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleLeasedControlRequest.setStatus("current")
_SleLeasedControlStatus_Type = SleControlStatusType
_SleLeasedControlStatus_Object = MibScalar
sleLeasedControlStatus = _SleLeasedControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 2, 2),
    _SleLeasedControlStatus_Type()
)
sleLeasedControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedControlStatus.setStatus("current")
_SleLeasedControlTimer_Type = Gauge32
_SleLeasedControlTimer_Object = MibScalar
sleLeasedControlTimer = _SleLeasedControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 2, 3),
    _SleLeasedControlTimer_Type()
)
sleLeasedControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleLeasedControlTimer.setStatus("current")
_SleLeasedControlTImeStamp_Type = TimeTicks
_SleLeasedControlTImeStamp_Object = MibScalar
sleLeasedControlTImeStamp = _SleLeasedControlTImeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 2, 4),
    _SleLeasedControlTImeStamp_Type()
)
sleLeasedControlTImeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedControlTImeStamp.setStatus("current")
_SleLeasedControlReqResult_Type = SleControlRequestResultType
_SleLeasedControlReqResult_Object = MibScalar
sleLeasedControlReqResult = _SleLeasedControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 2, 5),
    _SleLeasedControlReqResult_Type()
)
sleLeasedControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleLeasedControlReqResult.setStatus("current")
_SleLeasedControlIp_Type = IpAddress
_SleLeasedControlIp_Object = MibScalar
sleLeasedControlIp = _SleLeasedControlIp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 2, 6),
    _SleLeasedControlIp_Type()
)
sleLeasedControlIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleLeasedControlIp.setStatus("current")


class _SleLeasedControlMask_Type(Integer32):
    """Custom type sleLeasedControlMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SleLeasedControlMask_Type.__name__ = "Integer32"
_SleLeasedControlMask_Object = MibScalar
sleLeasedControlMask = _SleLeasedControlMask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 2, 7),
    _SleLeasedControlMask_Type()
)
sleLeasedControlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleLeasedControlMask.setStatus("current")


class _SleLeasedControlPoolIndex_Type(Integer32):
    """Custom type sleLeasedControlPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleLeasedControlPoolIndex_Type.__name__ = "Integer32"
_SleLeasedControlPoolIndex_Object = MibScalar
sleLeasedControlPoolIndex = _SleLeasedControlPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 2, 8),
    _SleLeasedControlPoolIndex_Type()
)
sleLeasedControlPoolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleLeasedControlPoolIndex.setStatus("current")
_SleLeasedNotification_ObjectIdentity = ObjectIdentity
sleLeasedNotification = _SleLeasedNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 3)
)

# Managed Objects groups

sleDhcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 15)
)
sleDhcpGroup.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpDefaultLeaseTime"),
        ("SLE-DHCP-MIB", "sleDhcpMaxLeaseTime"),
        ("SLE-DHCP-MIB", "sleDhcpDnsIp1"),
        ("SLE-DHCP-MIB", "sleDhcpDnsIp2"),
        ("SLE-DHCP-MIB", "sleDhcpDnsIp3"),
        ("SLE-DHCP-MIB", "sleDhcpMode"),
        ("SLE-DHCP-MIB", "sleDhcpLeasedbBackupIp"),
        ("SLE-DHCP-MIB", "sleDhcpLeasedbBackupInterval"),
        ("SLE-DHCP-MIB", "sleDhcpDatabaseKey"),
        ("SLE-DHCP-MIB", "sleDhcpDebugStatus"),
        ("SLE-DHCP-MIB", "sleDhcpOption82"),
        ("SLE-DHCP-MIB", "sleDhcpOption82Policy"),
        ("SLE-DHCP-MIB", "sleDhcpOption82SystemRid"),
        ("SLE-DHCP-MIB", "sleDhcpAuthorizedArp"),
        ("SLE-DHCP-MIB", "sleDhcpAuthArpStarted"),
        ("SLE-DHCP-MIB", "sleDhcpAuthArpLeft"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticReceived"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticSent"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticReceivedErrors"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticSentErrors"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticBootpReceivedRequests"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticBootpReceivedReplies"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticBootpSentRequests"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticBootpSentReplies"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticReceivedDiscover"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticReceivedRequest"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticReceivedRelease"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticReceivedInform"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticReceivedDecline"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticSentOffer"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticSentAck"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticSentNak"),
        ("SLE-DHCP-MIB", "sleDhcpSummaryPoolCnt"),
        ("SLE-DHCP-MIB", "sleDhcpSummaryTotal"),
        ("SLE-DHCP-MIB", "sleDhcpSummaryAvailable"),
        ("SLE-DHCP-MIB", "sleDhcpSummaryAbandon"),
        ("SLE-DHCP-MIB", "sleDhcpSummaryBound"),
        ("SLE-DHCP-MIB", "sleDhcpSummaryOffered"),
        ("SLE-DHCP-MIB", "sleDhcpSummaryFixed"),
        ("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlStatus"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimer"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"),
        ("SLE-DHCP-MIB", "sleDhcpControlDefaultLeaseTime"),
        ("SLE-DHCP-MIB", "sleDhcpControlMaxLeaseTime"),
        ("SLE-DHCP-MIB", "sleDhcpControlDnsIp1"),
        ("SLE-DHCP-MIB", "sleDhcpControlDnsIp2"),
        ("SLE-DHCP-MIB", "sleDhcpControlDnsIp3"),
        ("SLE-DHCP-MIB", "sleDhcpControlServerMode"),
        ("SLE-DHCP-MIB", "sleDhcpControlLeasedbBackupIp"),
        ("SLE-DHCP-MIB", "sleDhcpControlLeasedbBackupInterval"),
        ("SLE-DHCP-MIB", "sleDhcpControlDatabaseKey"),
        ("SLE-DHCP-MIB", "sleDhcpControlDebugStatus"),
        ("SLE-DHCP-MIB", "sleDhcpControlOption82"),
        ("SLE-DHCP-MIB", "sleDhcpControlOption82Policy"),
        ("SLE-DHCP-MIB", "sleDhcpControlOption82SystemRid"),
        ("SLE-DHCP-MIB", "sleDhcpControlAuthorizedArp"),
        ("SLE-DHCP-MIB", "sleFilterPortIndex"),
        ("SLE-DHCP-MIB", "sleFilterPortMode"),
        ("SLE-DHCP-MIB", "sleFilterPortControlRequest"),
        ("SLE-DHCP-MIB", "sleFilterPortControlStatus"),
        ("SLE-DHCP-MIB", "sleFilterPortControlTimer"),
        ("SLE-DHCP-MIB", "sleFilterPortControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleFilterPortControlReqResult"),
        ("SLE-DHCP-MIB", "sleFilterPortControlIndex"),
        ("SLE-DHCP-MIB", "sleFilterPortControlMode"),
        ("SLE-DHCP-MIB", "sleFilterAddressMac"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlRequest"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlStatus"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlTimer"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlReqResult"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlMac"),
        ("SLE-DHCP-MIB", "sleRelayServerIp"),
        ("SLE-DHCP-MIB", "sleRelayServerControlRequest"),
        ("SLE-DHCP-MIB", "sleRelayServerControlStatus"),
        ("SLE-DHCP-MIB", "sleRelayServerControlTimer"),
        ("SLE-DHCP-MIB", "sleRelayServerControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleRelayServerControlReqResult"),
        ("SLE-DHCP-MIB", "sleRelayServerControlIp"),
        ("SLE-DHCP-MIB", "slePoolIndex"),
        ("SLE-DHCP-MIB", "slePoolName"),
        ("SLE-DHCP-MIB", "slePoolDefaultLeaseTime"),
        ("SLE-DHCP-MIB", "slePoolMaxLeaseTime"),
        ("SLE-DHCP-MIB", "slePoolSummaryTotal"),
        ("SLE-DHCP-MIB", "slePoolSummaryAllocated"),
        ("SLE-DHCP-MIB", "slePoolSummaryBound"),
        ("SLE-DHCP-MIB", "slePoolSummaryOffered"),
        ("SLE-DHCP-MIB", "slePoolSummaryFixed"),
        ("SLE-DHCP-MIB", "slePoolSummaryAbandon"),
        ("SLE-DHCP-MIB", "slePoolSummaryAvailable"),
        ("SLE-DHCP-MIB", "slePoolControlRequest"),
        ("SLE-DHCP-MIB", "slePoolControlStatus"),
        ("SLE-DHCP-MIB", "slePoolControlTimer"),
        ("SLE-DHCP-MIB", "slePoolControlTImeStamp"),
        ("SLE-DHCP-MIB", "slePoolControlReqResult"),
        ("SLE-DHCP-MIB", "slePoolControlIndex"),
        ("SLE-DHCP-MIB", "slePoolControlName"),
        ("SLE-DHCP-MIB", "slePoolControlDefaultLeaseTime"),
        ("SLE-DHCP-MIB", "slePoolControlMaxLeaseTime"),
        ("SLE-DHCP-MIB", "sleDnsIp"),
        ("SLE-DHCP-MIB", "sleDnsControlRequest"),
        ("SLE-DHCP-MIB", "sleDnsControlStatus"),
        ("SLE-DHCP-MIB", "sleDnsControlTimer"),
        ("SLE-DHCP-MIB", "sleDnsControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleDnsControlReqResult"),
        ("SLE-DHCP-MIB", "sleDnsControlPoolIndex"),
        ("SLE-DHCP-MIB", "sleDnsControlIp"),
        ("SLE-DHCP-MIB", "sleSubnetIp"),
        ("SLE-DHCP-MIB", "sleSubnetMask"),
        ("SLE-DHCP-MIB", "sleSubnetDefaultGateway"),
        ("SLE-DHCP-MIB", "sleSubnetControlRequest"),
        ("SLE-DHCP-MIB", "sleSubnetControlStatus"),
        ("SLE-DHCP-MIB", "sleSubnetControlTimer"),
        ("SLE-DHCP-MIB", "sleSubnetControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleSubnetControlReqResult"),
        ("SLE-DHCP-MIB", "sleSubnetControlPoolIndex"),
        ("SLE-DHCP-MIB", "sleSubnetControlIp"),
        ("SLE-DHCP-MIB", "sleSubnetControlMask"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayIp"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlRequest"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlStatus"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlTimer"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlReqResult"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlPoolIndex"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlIp"),
        ("SLE-DHCP-MIB", "sleRangeStart"),
        ("SLE-DHCP-MIB", "sleRangeEnd"),
        ("SLE-DHCP-MIB", "sleRangeSubnetIP"),
        ("SLE-DHCP-MIB", "sleRangeSubnetMask"),
        ("SLE-DHCP-MIB", "sleRangeControlRequest"),
        ("SLE-DHCP-MIB", "sleRangeControlStatus"),
        ("SLE-DHCP-MIB", "sleRangeControlTimer"),
        ("SLE-DHCP-MIB", "sleRangeControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleRangeControlReqResult"),
        ("SLE-DHCP-MIB", "sleRangeControlPoolIndex"),
        ("SLE-DHCP-MIB", "sleRangeControlStart"),
        ("SLE-DHCP-MIB", "sleRangeControlEnd"),
        ("SLE-DHCP-MIB", "sleFixedIp"),
        ("SLE-DHCP-MIB", "sleFixedMac"),
        ("SLE-DHCP-MIB", "sleFixedControlRequest"),
        ("SLE-DHCP-MIB", "sleFixedControlStatus"),
        ("SLE-DHCP-MIB", "sleFixedControlTimer"),
        ("SLE-DHCP-MIB", "sleFixedControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleFixedControlReqResult"),
        ("SLE-DHCP-MIB", "sleFixedControlPoolIndex"),
        ("SLE-DHCP-MIB", "sleFixedControlIp"),
        ("SLE-DHCP-MIB", "sleFixedControlMac"),
        ("SLE-DHCP-MIB", "sleOption82RemoteType"),
        ("SLE-DHCP-MIB", "sleIllegalIp"),
        ("SLE-DHCP-MIB", "sleIllegalControlRequest"),
        ("SLE-DHCP-MIB", "sleIllegalControlStatus"),
        ("SLE-DHCP-MIB", "sleIllegalControlTimer"),
        ("SLE-DHCP-MIB", "sleIllegalControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleIllegalControlReqResult"),
        ("SLE-DHCP-MIB", "sleLeasedControlRequest"),
        ("SLE-DHCP-MIB", "sleLeasedControlStatus"),
        ("SLE-DHCP-MIB", "sleLeasedControlTimer"),
        ("SLE-DHCP-MIB", "sleLeasedControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleLeasedControlReqResult"),
        ("SLE-DHCP-MIB", "sleLeasedControlIp"),
        ("SLE-DHCP-MIB", "sleLeasedControlMask"),
        ("SLE-DHCP-MIB", "sleRelayServerIndex"),
        ("SLE-DHCP-MIB", "sleRelayServerControlIndex"),
        ("SLE-DHCP-MIB", "sleDnsIndex"),
        ("SLE-DHCP-MIB", "sleDnsControlIndex"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayIndex"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlIndex"),
        ("SLE-DHCP-MIB", "sleOption82CircuitType"),
        ("SLE-DHCP-MIB", "sleDhcpOption82SystemRtype"),
        ("SLE-DHCP-MIB", "sleDhcpControlOption82SystemRtype"),
        ("SLE-DHCP-MIB", "sleOption82RemoteId"),
        ("SLE-DHCP-MIB", "sleOption82CircuitId"),
        ("SLE-DHCP-MIB", "sleOption82Limit"),
        ("SLE-DHCP-MIB", "sleOption82PoolName"),
        ("SLE-DHCP-MIB", "sleOption82ControlRequest"),
        ("SLE-DHCP-MIB", "sleOption82ControlStatus"),
        ("SLE-DHCP-MIB", "sleOption82ControlTimer"),
        ("SLE-DHCP-MIB", "sleOption82ControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleOption82ControlReqResult"),
        ("SLE-DHCP-MIB", "sleOption82ControlRemoteType"),
        ("SLE-DHCP-MIB", "sleOption82ControlRemoteId"),
        ("SLE-DHCP-MIB", "sleOption82ControlCircuitType"),
        ("SLE-DHCP-MIB", "sleOption82ControlCircuitId"),
        ("SLE-DHCP-MIB", "sleOption82ControlLimit"),
        ("SLE-DHCP-MIB", "sleOption82ControlPoolName"),
        ("SLE-DHCP-MIB", "sleOption82SystemIndex"),
        ("SLE-DHCP-MIB", "sleOption82SystemCtype"),
        ("SLE-DHCP-MIB", "sleOption82SystemCid"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlRequest"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlStatus"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlTimer"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlReqResult"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlIndex"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlCtype"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlCid"),
        ("SLE-DHCP-MIB", "sleLeasedHostname"),
        ("SLE-DHCP-MIB", "sleLeasedUid"),
        ("SLE-DHCP-MIB", "sleLeasedRid"),
        ("SLE-DHCP-MIB", "sleLeasedCid"),
        ("SLE-DHCP-MIB", "sleDhcpClientHardwareAddress"),
        ("SLE-DHCP-MIB", "sleDhcpControlClientHardwareAddress"),
        ("SLE-DHCP-MIB", "sleDhcpSimplifiedOption82"),
        ("SLE-DHCP-MIB", "sleDhcpControlSimplifiedOption82"),
        ("SLE-DHCP-MIB", "sleRelayServerVid"),
        ("SLE-DHCP-MIB", "sleRelayServerOUI"),
        ("SLE-DHCP-MIB", "sleRelayServerControlVid"),
        ("SLE-DHCP-MIB", "sleRelayServerControlOUI"),
        ("SLE-DHCP-MIB", "sleDhcpSummaryAllocated"),
        ("SLE-DHCP-MIB", "slePoolSummarySubnet"),
        ("SLE-DHCP-MIB", "slePoolDomainName"),
        ("SLE-DHCP-MIB", "slePoolControlDomainName"),
        ("SLE-DHCP-MIB", "sleLeasedControlPoolIndex"),
        ("SLE-DHCP-MIB", "sleIllegalMac"),
        ("SLE-DHCP-MIB", "sleIllegalTime"),
        ("SLE-DHCP-MIB", "sleLeasedIp"),
        ("SLE-DHCP-MIB", "sleLeasedPoolIndex"),
        ("SLE-DHCP-MIB", "sleLeasedPoolName"),
        ("SLE-DHCP-MIB", "sleLeasedTime"),
        ("SLE-DHCP-MIB", "sleLeasedHwaddr"))
)
if mibBuilder.loadTexts:
    sleDhcpGroup.setStatus("current")


# Notification objects

sleDhcpLeaseTimeProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 1)
)
sleDhcpLeaseTimeProfileChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpDefaultLeaseTime"),
        ("SLE-DHCP-MIB", "sleDhcpMaxLeaseTime"),
        ("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcpLeaseTimeProfileChanged.setStatus(
        "current"
    )

sleDhcpDnsIpProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 2)
)
sleDhcpDnsIpProfileChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpDnsIp1"),
        ("SLE-DHCP-MIB", "sleDhcpDnsIp2"),
        ("SLE-DHCP-MIB", "sleDhcpDnsIp3"),
        ("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcpDnsIpProfileChanged.setStatus(
        "current"
    )

sleDhcpServerModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 3)
)
sleDhcpServerModeChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpMode"),
        ("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcpServerModeChanged.setStatus(
        "current"
    )

sleDhcpLeasedbBackupProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 4)
)
sleDhcpLeasedbBackupProfileChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpLeasedbBackupIp"),
        ("SLE-DHCP-MIB", "sleDhcpLeasedbBackupInterval"),
        ("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcpLeasedbBackupProfileChanged.setStatus(
        "current"
    )

sleDhcpDatabaseKeyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 5)
)
sleDhcpDatabaseKeyChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpDatabaseKey"),
        ("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcpDatabaseKeyChanged.setStatus(
        "current"
    )

sleDhcpDebugStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 6)
)
sleDhcpDebugStatusChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpDebugStatus"),
        ("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcpDebugStatusChanged.setStatus(
        "current"
    )

sleDhcpOption82SystemProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 7)
)
sleDhcpOption82SystemProfileChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"),
        ("SLE-DHCP-MIB", "sleDhcpOption82"),
        ("SLE-DHCP-MIB", "sleDhcpOption82Policy"),
        ("SLE-DHCP-MIB", "sleDhcpOption82SystemRtype"),
        ("SLE-DHCP-MIB", "sleDhcpOption82SystemRid"))
)
if mibBuilder.loadTexts:
    sleDhcpOption82SystemProfileChanged.setStatus(
        "current"
    )

sleDhcpAuthorizedArpChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 8)
)
sleDhcpAuthorizedArpChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpAuthorizedArp"),
        ("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcpAuthorizedArpChanged.setStatus(
        "current"
    )

sleDhcpStatisticsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 9)
)
sleDhcpStatisticsCleared.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDhcpStatisticsCleared.setStatus(
        "current"
    )

sleDhcpClientHardwareAddressChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 10)
)
sleDhcpClientHardwareAddressChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"),
        ("SLE-DHCP-MIB", "sleDhcpControlClientHardwareAddress"))
)
if mibBuilder.loadTexts:
    sleDhcpClientHardwareAddressChanged.setStatus(
        "current"
    )

sleDhcpSimplifiedOption82Changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 1, 3, 11)
)
sleDhcpSimplifiedOption82Changed.setObjects(
      *(("SLE-DHCP-MIB", "sleDhcpControlRequest"),
        ("SLE-DHCP-MIB", "sleDhcpControlTimeStamp"),
        ("SLE-DHCP-MIB", "sleDhcpControlReqResult"),
        ("SLE-DHCP-MIB", "sleDhcpControlSimplifiedOption82"))
)
if mibBuilder.loadTexts:
    sleDhcpSimplifiedOption82Changed.setStatus(
        "current"
    )

sleFilterPortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 2, 3, 1)
)
sleFilterPortChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleFilterPortMode"),
        ("SLE-DHCP-MIB", "sleFilterPortControlRequest"),
        ("SLE-DHCP-MIB", "sleFilterPortControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleFilterPortControlReqResult"))
)
if mibBuilder.loadTexts:
    sleFilterPortChanged.setStatus(
        "current"
    )

sleFilterAddressCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 3, 1)
)
sleFilterAddressCreated.setObjects(
      *(("SLE-DHCP-MIB", "sleFilterAddressMac"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlRequest"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlReqResult"))
)
if mibBuilder.loadTexts:
    sleFilterAddressCreated.setStatus(
        "current"
    )

sleFilterAddressDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 3, 3, 2)
)
sleFilterAddressDestroyed.setObjects(
      *(("SLE-DHCP-MIB", "sleFilterAddressMac"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlRequest"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleFilterAddressControlReqResult"))
)
if mibBuilder.loadTexts:
    sleFilterAddressDestroyed.setStatus(
        "current"
    )

sleRelayServerCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 3, 1)
)
sleRelayServerCreated.setObjects(
      *(("SLE-DHCP-MIB", "sleRelayServerControlRequest"),
        ("SLE-DHCP-MIB", "sleRelayServerControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleRelayServerControlReqResult"),
        ("SLE-DHCP-MIB", "sleRelayServerIp"),
        ("SLE-DHCP-MIB", "sleRelayServerVid"))
)
if mibBuilder.loadTexts:
    sleRelayServerCreated.setStatus(
        "current"
    )

sleRelayServerDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 3, 2)
)
sleRelayServerDestroyed.setObjects(
      *(("SLE-DHCP-MIB", "sleRelayServerControlRequest"),
        ("SLE-DHCP-MIB", "sleRelayServerControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleRelayServerControlReqResult"),
        ("SLE-DHCP-MIB", "sleRelayServerIp"),
        ("SLE-DHCP-MIB", "sleRelayServerVid"))
)
if mibBuilder.loadTexts:
    sleRelayServerDestroyed.setStatus(
        "current"
    )

sleRelayServerOUICreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 3, 3)
)
sleRelayServerOUICreated.setObjects(
      *(("SLE-DHCP-MIB", "sleRelayServerControlRequest"),
        ("SLE-DHCP-MIB", "sleRelayServerControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleRelayServerControlReqResult"),
        ("SLE-DHCP-MIB", "sleRelayServerIp"),
        ("SLE-DHCP-MIB", "sleRelayServerVid"),
        ("SLE-DHCP-MIB", "sleRelayServerOUI"))
)
if mibBuilder.loadTexts:
    sleRelayServerOUICreated.setStatus(
        "current"
    )

sleRelayServerOUIDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 4, 3, 4)
)
sleRelayServerOUIDestroyed.setObjects(
      *(("SLE-DHCP-MIB", "sleRelayServerControlRequest"),
        ("SLE-DHCP-MIB", "sleRelayServerControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleRelayServerControlReqResult"),
        ("SLE-DHCP-MIB", "sleRelayServerIp"),
        ("SLE-DHCP-MIB", "sleRelayServerVid"),
        ("SLE-DHCP-MIB", "sleRelayServerOUI"))
)
if mibBuilder.loadTexts:
    sleRelayServerOUIDestroyed.setStatus(
        "current"
    )

slePoolCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 3, 1)
)
slePoolCreated.setObjects(
      *(("SLE-DHCP-MIB", "slePoolName"),
        ("SLE-DHCP-MIB", "slePoolDefaultLeaseTime"),
        ("SLE-DHCP-MIB", "slePoolMaxLeaseTime"),
        ("SLE-DHCP-MIB", "slePoolControlRequest"),
        ("SLE-DHCP-MIB", "slePoolControlTImeStamp"),
        ("SLE-DHCP-MIB", "slePoolControlReqResult"))
)
if mibBuilder.loadTexts:
    slePoolCreated.setStatus(
        "current"
    )

slePoolDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 3, 2)
)
slePoolDestroyed.setObjects(
      *(("SLE-DHCP-MIB", "slePoolIndex"),
        ("SLE-DHCP-MIB", "slePoolControlRequest"),
        ("SLE-DHCP-MIB", "slePoolControlTImeStamp"),
        ("SLE-DHCP-MIB", "slePoolControlReqResult"))
)
if mibBuilder.loadTexts:
    slePoolDestroyed.setStatus(
        "current"
    )

slePoolLeaseTimeProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 3, 3)
)
slePoolLeaseTimeProfileChanged.setObjects(
      *(("SLE-DHCP-MIB", "slePoolDefaultLeaseTime"),
        ("SLE-DHCP-MIB", "slePoolMaxLeaseTime"),
        ("SLE-DHCP-MIB", "slePoolControlRequest"),
        ("SLE-DHCP-MIB", "slePoolControlTImeStamp"),
        ("SLE-DHCP-MIB", "slePoolControlReqResult"))
)
if mibBuilder.loadTexts:
    slePoolLeaseTimeProfileChanged.setStatus(
        "current"
    )

slePoolDomainNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 5, 3, 4)
)
slePoolDomainNameChanged.setObjects(
      *(("SLE-DHCP-MIB", "slePoolControlRequest"),
        ("SLE-DHCP-MIB", "slePoolControlTImeStamp"),
        ("SLE-DHCP-MIB", "slePoolControlReqResult"),
        ("SLE-DHCP-MIB", "slePoolDomainName"))
)
if mibBuilder.loadTexts:
    slePoolDomainNameChanged.setStatus(
        "current"
    )

sleDnsCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 3, 1)
)
sleDnsCreated.setObjects(
      *(("SLE-DHCP-MIB", "sleDnsIp"),
        ("SLE-DHCP-MIB", "sleDnsControlRequest"),
        ("SLE-DHCP-MIB", "sleDnsControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleDnsControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDnsCreated.setStatus(
        "current"
    )

sleDnsDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 6, 3, 2)
)
sleDnsDestroyed.setObjects(
      *(("SLE-DHCP-MIB", "sleDnsIndex"),
        ("SLE-DHCP-MIB", "sleDnsControlRequest"),
        ("SLE-DHCP-MIB", "sleDnsControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleDnsControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDnsDestroyed.setStatus(
        "current"
    )

sleSubnetCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 3, 1)
)
sleSubnetCreated.setObjects(
      *(("SLE-DHCP-MIB", "sleSubnetMask"),
        ("SLE-DHCP-MIB", "sleSubnetControlRequest"),
        ("SLE-DHCP-MIB", "sleSubnetControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleSubnetControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSubnetCreated.setStatus(
        "current"
    )

sleSubnetDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 7, 3, 2)
)
sleSubnetDestroyed.setObjects(
      *(("SLE-DHCP-MIB", "sleSubnetMask"),
        ("SLE-DHCP-MIB", "sleSubnetControlRequest"),
        ("SLE-DHCP-MIB", "sleSubnetControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleSubnetControlReqResult"))
)
if mibBuilder.loadTexts:
    sleSubnetDestroyed.setStatus(
        "current"
    )

sleDefaultGatewayCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 3, 1)
)
sleDefaultGatewayCreated.setObjects(
      *(("SLE-DHCP-MIB", "sleDefaultGatewayIp"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlRequest"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDefaultGatewayCreated.setStatus(
        "current"
    )

sleDefaultGatewayDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 8, 3, 2)
)
sleDefaultGatewayDestroyed.setObjects(
      *(("SLE-DHCP-MIB", "sleDefaultGatewayIndex"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlRequest"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayControlReqResult"))
)
if mibBuilder.loadTexts:
    sleDefaultGatewayDestroyed.setStatus(
        "current"
    )

sleRangeCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 3, 1)
)
sleRangeCreated.setObjects(
      *(("SLE-DHCP-MIB", "sleRangeSubnetIP"),
        ("SLE-DHCP-MIB", "sleRangeSubnetMask"),
        ("SLE-DHCP-MIB", "sleRangeControlRequest"),
        ("SLE-DHCP-MIB", "sleRangeControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleRangeControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRangeCreated.setStatus(
        "current"
    )

sleRangeDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 9, 3, 2)
)
sleRangeDestroyed.setObjects(
      *(("SLE-DHCP-MIB", "sleRangeEnd"),
        ("SLE-DHCP-MIB", "sleRangeControlRequest"),
        ("SLE-DHCP-MIB", "sleRangeControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleRangeControlReqResult"))
)
if mibBuilder.loadTexts:
    sleRangeDestroyed.setStatus(
        "current"
    )

sleFixedCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 3, 1)
)
sleFixedCreated.setObjects(
      *(("SLE-DHCP-MIB", "sleFixedMac"),
        ("SLE-DHCP-MIB", "sleFixedControlRequest"),
        ("SLE-DHCP-MIB", "sleFixedControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleFixedControlReqResult"))
)
if mibBuilder.loadTexts:
    sleFixedCreated.setStatus(
        "current"
    )

sleFixedDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 10, 3, 2)
)
sleFixedDestroyed.setObjects(
      *(("SLE-DHCP-MIB", "sleFixedMac"),
        ("SLE-DHCP-MIB", "sleFixedControlRequest"),
        ("SLE-DHCP-MIB", "sleFixedControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleFixedControlReqResult"))
)
if mibBuilder.loadTexts:
    sleFixedDestroyed.setStatus(
        "current"
    )

sleOption82Created = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 3, 1)
)
sleOption82Created.setObjects(
      *(("SLE-DHCP-MIB", "sleOption82ControlRequest"),
        ("SLE-DHCP-MIB", "sleOption82ControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleOption82ControlReqResult"),
        ("SLE-DHCP-MIB", "sleOption82ControlLimit"),
        ("SLE-DHCP-MIB", "sleOption82ControlPoolName"))
)
if mibBuilder.loadTexts:
    sleOption82Created.setStatus(
        "current"
    )

sleOption82Destroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 3, 2)
)
sleOption82Destroyed.setObjects(
      *(("SLE-DHCP-MIB", "sleOption82ControlRequest"),
        ("SLE-DHCP-MIB", "sleOption82ControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleOption82ControlReqResult"),
        ("SLE-DHCP-MIB", "sleOption82ControlCircuitId"))
)
if mibBuilder.loadTexts:
    sleOption82Destroyed.setStatus(
        "current"
    )

sleOption82ProfileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 11, 3, 3)
)
sleOption82ProfileChanged.setObjects(
      *(("SLE-DHCP-MIB", "sleOption82ControlRequest"),
        ("SLE-DHCP-MIB", "sleOption82ControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleOption82ControlReqResult"),
        ("SLE-DHCP-MIB", "sleOption82ControlLimit"),
        ("SLE-DHCP-MIB", "sleOption82ControlPoolName"))
)
if mibBuilder.loadTexts:
    sleOption82ProfileChanged.setStatus(
        "current"
    )

setOption82SystemCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 12, 3, 1)
)
setOption82SystemCircuit.setObjects(
      *(("SLE-DHCP-MIB", "sleOption82SystemControlRequest"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlReqResult"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlCtype"),
        ("SLE-DHCP-MIB", "sleOption82SystemControlCid"))
)
if mibBuilder.loadTexts:
    setOption82SystemCircuit.setStatus(
        "current"
    )

sleIllegalCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 13, 3, 1)
)
sleIllegalCleared.setObjects(
      *(("SLE-DHCP-MIB", "sleIllegalControlRequest"),
        ("SLE-DHCP-MIB", "sleIllegalControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleIllegalControlReqResult"))
)
if mibBuilder.loadTexts:
    sleIllegalCleared.setStatus(
        "current"
    )

sleLeasedIpMaskFlushed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 3, 1)
)
sleLeasedIpMaskFlushed.setObjects(
      *(("SLE-DHCP-MIB", "sleLeasedControlRequest"),
        ("SLE-DHCP-MIB", "sleLeasedControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleLeasedControlReqResult"),
        ("SLE-DHCP-MIB", "sleLeasedControlIp"),
        ("SLE-DHCP-MIB", "sleLeasedControlMask"))
)
if mibBuilder.loadTexts:
    sleLeasedIpMaskFlushed.setStatus(
        "current"
    )

sleLeasedPoolFlushed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 14, 3, 2)
)
sleLeasedPoolFlushed.setObjects(
      *(("SLE-DHCP-MIB", "sleLeasedControlRequest"),
        ("SLE-DHCP-MIB", "sleLeasedControlTImeStamp"),
        ("SLE-DHCP-MIB", "sleLeasedControlReqResult"),
        ("SLE-DHCP-MIB", "sleLeasedControlPoolIndex"))
)
if mibBuilder.loadTexts:
    sleLeasedPoolFlushed.setStatus(
        "current"
    )


# Notifications groups

sleDhcpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 6, 16)
)
sleDhcpNotificationGroup.setObjects(
      *(("SLE-DHCP-MIB", "sleFilterPortChanged"),
        ("SLE-DHCP-MIB", "sleFilterAddressCreated"),
        ("SLE-DHCP-MIB", "sleFilterAddressDestroyed"),
        ("SLE-DHCP-MIB", "sleRelayServerCreated"),
        ("SLE-DHCP-MIB", "sleRelayServerDestroyed"),
        ("SLE-DHCP-MIB", "slePoolCreated"),
        ("SLE-DHCP-MIB", "slePoolDestroyed"),
        ("SLE-DHCP-MIB", "slePoolLeaseTimeProfileChanged"),
        ("SLE-DHCP-MIB", "sleDnsCreated"),
        ("SLE-DHCP-MIB", "sleDnsDestroyed"),
        ("SLE-DHCP-MIB", "sleSubnetCreated"),
        ("SLE-DHCP-MIB", "sleSubnetDestroyed"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayCreated"),
        ("SLE-DHCP-MIB", "sleDefaultGatewayDestroyed"),
        ("SLE-DHCP-MIB", "sleRangeCreated"),
        ("SLE-DHCP-MIB", "sleRangeDestroyed"),
        ("SLE-DHCP-MIB", "sleFixedCreated"),
        ("SLE-DHCP-MIB", "sleFixedDestroyed"),
        ("SLE-DHCP-MIB", "sleIllegalCleared"),
        ("SLE-DHCP-MIB", "sleLeasedIpMaskFlushed"),
        ("SLE-DHCP-MIB", "sleLeasedPoolFlushed"),
        ("SLE-DHCP-MIB", "sleDhcpLeaseTimeProfileChanged"),
        ("SLE-DHCP-MIB", "sleDhcpDnsIpProfileChanged"),
        ("SLE-DHCP-MIB", "sleDhcpServerModeChanged"),
        ("SLE-DHCP-MIB", "sleDhcpLeasedbBackupProfileChanged"),
        ("SLE-DHCP-MIB", "sleDhcpDatabaseKeyChanged"),
        ("SLE-DHCP-MIB", "sleOption82Created"),
        ("SLE-DHCP-MIB", "sleOption82Destroyed"),
        ("SLE-DHCP-MIB", "sleOption82ProfileChanged"),
        ("SLE-DHCP-MIB", "setOption82SystemCircuit"),
        ("SLE-DHCP-MIB", "sleDhcpDebugStatusChanged"),
        ("SLE-DHCP-MIB", "sleDhcpAuthorizedArpChanged"),
        ("SLE-DHCP-MIB", "sleDhcpClientHardwareAddressChanged"),
        ("SLE-DHCP-MIB", "sleDhcpSimplifiedOption82Changed"),
        ("SLE-DHCP-MIB", "sleRelayServerOUICreated"),
        ("SLE-DHCP-MIB", "sleRelayServerOUIDestroyed"),
        ("SLE-DHCP-MIB", "slePoolDomainNameChanged"),
        ("SLE-DHCP-MIB", "sleDhcpStatisticsCleared"),
        ("SLE-DHCP-MIB", "sleDhcpOption82SystemProfileChanged"))
)
if mibBuilder.loadTexts:
    sleDhcpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-DHCP-MIB",
    **{"sleDhcp": sleDhcp,
       "sleDhcpBase": sleDhcpBase,
       "sleDhcpBaseInfo": sleDhcpBaseInfo,
       "sleDhcpDefaultLeaseTime": sleDhcpDefaultLeaseTime,
       "sleDhcpMaxLeaseTime": sleDhcpMaxLeaseTime,
       "sleDhcpDnsIp1": sleDhcpDnsIp1,
       "sleDhcpDnsIp2": sleDhcpDnsIp2,
       "sleDhcpDnsIp3": sleDhcpDnsIp3,
       "sleDhcpMode": sleDhcpMode,
       "sleDhcpLeasedbBackupIp": sleDhcpLeasedbBackupIp,
       "sleDhcpLeasedbBackupInterval": sleDhcpLeasedbBackupInterval,
       "sleDhcpDatabaseKey": sleDhcpDatabaseKey,
       "sleDhcpDebugStatus": sleDhcpDebugStatus,
       "sleDhcpOption82": sleDhcpOption82,
       "sleDhcpOption82Policy": sleDhcpOption82Policy,
       "sleDhcpOption82SystemRtype": sleDhcpOption82SystemRtype,
       "sleDhcpOption82SystemRid": sleDhcpOption82SystemRid,
       "sleDhcpAuthorizedArp": sleDhcpAuthorizedArp,
       "sleDhcpAuthArpStarted": sleDhcpAuthArpStarted,
       "sleDhcpAuthArpLeft": sleDhcpAuthArpLeft,
       "sleDhcpStatisticReceived": sleDhcpStatisticReceived,
       "sleDhcpStatisticSent": sleDhcpStatisticSent,
       "sleDhcpStatisticReceivedErrors": sleDhcpStatisticReceivedErrors,
       "sleDhcpStatisticSentErrors": sleDhcpStatisticSentErrors,
       "sleDhcpStatisticBootpReceivedRequests": sleDhcpStatisticBootpReceivedRequests,
       "sleDhcpStatisticBootpReceivedReplies": sleDhcpStatisticBootpReceivedReplies,
       "sleDhcpStatisticBootpSentRequests": sleDhcpStatisticBootpSentRequests,
       "sleDhcpStatisticBootpSentReplies": sleDhcpStatisticBootpSentReplies,
       "sleDhcpStatisticReceivedDiscover": sleDhcpStatisticReceivedDiscover,
       "sleDhcpStatisticReceivedRequest": sleDhcpStatisticReceivedRequest,
       "sleDhcpStatisticReceivedRelease": sleDhcpStatisticReceivedRelease,
       "sleDhcpStatisticReceivedInform": sleDhcpStatisticReceivedInform,
       "sleDhcpStatisticReceivedDecline": sleDhcpStatisticReceivedDecline,
       "sleDhcpStatisticSentOffer": sleDhcpStatisticSentOffer,
       "sleDhcpStatisticSentAck": sleDhcpStatisticSentAck,
       "sleDhcpStatisticSentNak": sleDhcpStatisticSentNak,
       "sleDhcpSummaryPoolCnt": sleDhcpSummaryPoolCnt,
       "sleDhcpSummaryTotal": sleDhcpSummaryTotal,
       "sleDhcpSummaryAvailable": sleDhcpSummaryAvailable,
       "sleDhcpSummaryAbandon": sleDhcpSummaryAbandon,
       "sleDhcpSummaryBound": sleDhcpSummaryBound,
       "sleDhcpSummaryOffered": sleDhcpSummaryOffered,
       "sleDhcpSummaryFixed": sleDhcpSummaryFixed,
       "sleDhcpClientHardwareAddress": sleDhcpClientHardwareAddress,
       "sleDhcpSimplifiedOption82": sleDhcpSimplifiedOption82,
       "sleDhcpSummaryAllocated": sleDhcpSummaryAllocated,
       "sleDhcpBaseControl": sleDhcpBaseControl,
       "sleDhcpControlRequest": sleDhcpControlRequest,
       "sleDhcpControlStatus": sleDhcpControlStatus,
       "sleDhcpControlTimer": sleDhcpControlTimer,
       "sleDhcpControlTimeStamp": sleDhcpControlTimeStamp,
       "sleDhcpControlReqResult": sleDhcpControlReqResult,
       "sleDhcpControlDefaultLeaseTime": sleDhcpControlDefaultLeaseTime,
       "sleDhcpControlMaxLeaseTime": sleDhcpControlMaxLeaseTime,
       "sleDhcpControlDnsIp1": sleDhcpControlDnsIp1,
       "sleDhcpControlDnsIp2": sleDhcpControlDnsIp2,
       "sleDhcpControlDnsIp3": sleDhcpControlDnsIp3,
       "sleDhcpControlServerMode": sleDhcpControlServerMode,
       "sleDhcpControlLeasedbBackupIp": sleDhcpControlLeasedbBackupIp,
       "sleDhcpControlLeasedbBackupInterval": sleDhcpControlLeasedbBackupInterval,
       "sleDhcpControlDatabaseKey": sleDhcpControlDatabaseKey,
       "sleDhcpControlDebugStatus": sleDhcpControlDebugStatus,
       "sleDhcpControlOption82": sleDhcpControlOption82,
       "sleDhcpControlOption82Policy": sleDhcpControlOption82Policy,
       "sleDhcpControlOption82SystemRtype": sleDhcpControlOption82SystemRtype,
       "sleDhcpControlOption82SystemRid": sleDhcpControlOption82SystemRid,
       "sleDhcpControlAuthorizedArp": sleDhcpControlAuthorizedArp,
       "sleDhcpControlClientHardwareAddress": sleDhcpControlClientHardwareAddress,
       "sleDhcpControlSimplifiedOption82": sleDhcpControlSimplifiedOption82,
       "sleDhcpBaseNotification": sleDhcpBaseNotification,
       "sleDhcpLeaseTimeProfileChanged": sleDhcpLeaseTimeProfileChanged,
       "sleDhcpDnsIpProfileChanged": sleDhcpDnsIpProfileChanged,
       "sleDhcpServerModeChanged": sleDhcpServerModeChanged,
       "sleDhcpLeasedbBackupProfileChanged": sleDhcpLeasedbBackupProfileChanged,
       "sleDhcpDatabaseKeyChanged": sleDhcpDatabaseKeyChanged,
       "sleDhcpDebugStatusChanged": sleDhcpDebugStatusChanged,
       "sleDhcpOption82SystemProfileChanged": sleDhcpOption82SystemProfileChanged,
       "sleDhcpAuthorizedArpChanged": sleDhcpAuthorizedArpChanged,
       "sleDhcpStatisticsCleared": sleDhcpStatisticsCleared,
       "sleDhcpClientHardwareAddressChanged": sleDhcpClientHardwareAddressChanged,
       "sleDhcpSimplifiedOption82Changed": sleDhcpSimplifiedOption82Changed,
       "sleFilterPort": sleFilterPort,
       "sleFilterPortTable": sleFilterPortTable,
       "sleFilterPortEntry": sleFilterPortEntry,
       "sleFilterPortIndex": sleFilterPortIndex,
       "sleFilterPortMode": sleFilterPortMode,
       "sleFilterPortControl": sleFilterPortControl,
       "sleFilterPortControlRequest": sleFilterPortControlRequest,
       "sleFilterPortControlStatus": sleFilterPortControlStatus,
       "sleFilterPortControlTimer": sleFilterPortControlTimer,
       "sleFilterPortControlTImeStamp": sleFilterPortControlTImeStamp,
       "sleFilterPortControlReqResult": sleFilterPortControlReqResult,
       "sleFilterPortControlIndex": sleFilterPortControlIndex,
       "sleFilterPortControlMode": sleFilterPortControlMode,
       "sleFilterPortNotification": sleFilterPortNotification,
       "sleFilterPortChanged": sleFilterPortChanged,
       "sleFilterAddress": sleFilterAddress,
       "sleFilterAddressTable": sleFilterAddressTable,
       "sleFilterAddressEntry": sleFilterAddressEntry,
       "sleFilterAddressMac": sleFilterAddressMac,
       "sleFilterAddressControl": sleFilterAddressControl,
       "sleFilterAddressControlRequest": sleFilterAddressControlRequest,
       "sleFilterAddressControlStatus": sleFilterAddressControlStatus,
       "sleFilterAddressControlTimer": sleFilterAddressControlTimer,
       "sleFilterAddressControlTImeStamp": sleFilterAddressControlTImeStamp,
       "sleFilterAddressControlReqResult": sleFilterAddressControlReqResult,
       "sleFilterAddressControlMac": sleFilterAddressControlMac,
       "sleFilterAddressNotification": sleFilterAddressNotification,
       "sleFilterAddressCreated": sleFilterAddressCreated,
       "sleFilterAddressDestroyed": sleFilterAddressDestroyed,
       "sleRelayServer": sleRelayServer,
       "sleRelayServerTable": sleRelayServerTable,
       "sleRelayServerEntry": sleRelayServerEntry,
       "sleRelayServerIndex": sleRelayServerIndex,
       "sleRelayServerIp": sleRelayServerIp,
       "sleRelayServerVid": sleRelayServerVid,
       "sleRelayServerOUI": sleRelayServerOUI,
       "sleRelayServerControl": sleRelayServerControl,
       "sleRelayServerControlRequest": sleRelayServerControlRequest,
       "sleRelayServerControlStatus": sleRelayServerControlStatus,
       "sleRelayServerControlTimer": sleRelayServerControlTimer,
       "sleRelayServerControlTImeStamp": sleRelayServerControlTImeStamp,
       "sleRelayServerControlReqResult": sleRelayServerControlReqResult,
       "sleRelayServerControlIndex": sleRelayServerControlIndex,
       "sleRelayServerControlIp": sleRelayServerControlIp,
       "sleRelayServerControlVid": sleRelayServerControlVid,
       "sleRelayServerControlOUI": sleRelayServerControlOUI,
       "sleRelayServerNotification": sleRelayServerNotification,
       "sleRelayServerCreated": sleRelayServerCreated,
       "sleRelayServerDestroyed": sleRelayServerDestroyed,
       "sleRelayServerOUICreated": sleRelayServerOUICreated,
       "sleRelayServerOUIDestroyed": sleRelayServerOUIDestroyed,
       "slePool": slePool,
       "slePoolTable": slePoolTable,
       "slePoolEntry": slePoolEntry,
       "slePoolIndex": slePoolIndex,
       "slePoolName": slePoolName,
       "slePoolDefaultLeaseTime": slePoolDefaultLeaseTime,
       "slePoolMaxLeaseTime": slePoolMaxLeaseTime,
       "slePoolSummaryTotal": slePoolSummaryTotal,
       "slePoolSummaryAllocated": slePoolSummaryAllocated,
       "slePoolSummaryBound": slePoolSummaryBound,
       "slePoolSummaryOffered": slePoolSummaryOffered,
       "slePoolSummaryFixed": slePoolSummaryFixed,
       "slePoolSummaryAbandon": slePoolSummaryAbandon,
       "slePoolSummaryAvailable": slePoolSummaryAvailable,
       "slePoolSummarySubnet": slePoolSummarySubnet,
       "slePoolDomainName": slePoolDomainName,
       "slePoolControl": slePoolControl,
       "slePoolControlRequest": slePoolControlRequest,
       "slePoolControlStatus": slePoolControlStatus,
       "slePoolControlTimer": slePoolControlTimer,
       "slePoolControlTImeStamp": slePoolControlTImeStamp,
       "slePoolControlReqResult": slePoolControlReqResult,
       "slePoolControlIndex": slePoolControlIndex,
       "slePoolControlName": slePoolControlName,
       "slePoolControlDefaultLeaseTime": slePoolControlDefaultLeaseTime,
       "slePoolControlMaxLeaseTime": slePoolControlMaxLeaseTime,
       "slePoolControlDomainName": slePoolControlDomainName,
       "slePoolNotification": slePoolNotification,
       "slePoolCreated": slePoolCreated,
       "slePoolDestroyed": slePoolDestroyed,
       "slePoolLeaseTimeProfileChanged": slePoolLeaseTimeProfileChanged,
       "slePoolDomainNameChanged": slePoolDomainNameChanged,
       "sleDns": sleDns,
       "sleDnsTable": sleDnsTable,
       "sleDnsEntry": sleDnsEntry,
       "sleDnsIndex": sleDnsIndex,
       "sleDnsIp": sleDnsIp,
       "sleDnsControl": sleDnsControl,
       "sleDnsControlRequest": sleDnsControlRequest,
       "sleDnsControlStatus": sleDnsControlStatus,
       "sleDnsControlTimer": sleDnsControlTimer,
       "sleDnsControlTImeStamp": sleDnsControlTImeStamp,
       "sleDnsControlReqResult": sleDnsControlReqResult,
       "sleDnsControlPoolIndex": sleDnsControlPoolIndex,
       "sleDnsControlIndex": sleDnsControlIndex,
       "sleDnsControlIp": sleDnsControlIp,
       "sleDnsNotification": sleDnsNotification,
       "sleDnsCreated": sleDnsCreated,
       "sleDnsDestroyed": sleDnsDestroyed,
       "sleSubnet": sleSubnet,
       "sleSubnetTable": sleSubnetTable,
       "sleSubnetEntry": sleSubnetEntry,
       "sleSubnetIp": sleSubnetIp,
       "sleSubnetMask": sleSubnetMask,
       "sleSubnetDefaultGateway": sleSubnetDefaultGateway,
       "sleSubnetControl": sleSubnetControl,
       "sleSubnetControlRequest": sleSubnetControlRequest,
       "sleSubnetControlStatus": sleSubnetControlStatus,
       "sleSubnetControlTimer": sleSubnetControlTimer,
       "sleSubnetControlTImeStamp": sleSubnetControlTImeStamp,
       "sleSubnetControlReqResult": sleSubnetControlReqResult,
       "sleSubnetControlPoolIndex": sleSubnetControlPoolIndex,
       "sleSubnetControlIp": sleSubnetControlIp,
       "sleSubnetControlMask": sleSubnetControlMask,
       "sleSubnetNotification": sleSubnetNotification,
       "sleSubnetCreated": sleSubnetCreated,
       "sleSubnetDestroyed": sleSubnetDestroyed,
       "sleDefaultGateway": sleDefaultGateway,
       "sleDefaultGatewayTable": sleDefaultGatewayTable,
       "sleDefaultGatewayEntry": sleDefaultGatewayEntry,
       "sleDefaultGatewayIndex": sleDefaultGatewayIndex,
       "sleDefaultGatewayIp": sleDefaultGatewayIp,
       "sleDefaultGatewayControl": sleDefaultGatewayControl,
       "sleDefaultGatewayControlRequest": sleDefaultGatewayControlRequest,
       "sleDefaultGatewayControlStatus": sleDefaultGatewayControlStatus,
       "sleDefaultGatewayControlTimer": sleDefaultGatewayControlTimer,
       "sleDefaultGatewayControlTImeStamp": sleDefaultGatewayControlTImeStamp,
       "sleDefaultGatewayControlReqResult": sleDefaultGatewayControlReqResult,
       "sleDefaultGatewayControlPoolIndex": sleDefaultGatewayControlPoolIndex,
       "sleDefaultGatewayControlIndex": sleDefaultGatewayControlIndex,
       "sleDefaultGatewayControlIp": sleDefaultGatewayControlIp,
       "sleDefaultGatewayNotification": sleDefaultGatewayNotification,
       "sleDefaultGatewayCreated": sleDefaultGatewayCreated,
       "sleDefaultGatewayDestroyed": sleDefaultGatewayDestroyed,
       "sleRange": sleRange,
       "sleRangeTable": sleRangeTable,
       "sleRangeEntry": sleRangeEntry,
       "sleRangeStart": sleRangeStart,
       "sleRangeEnd": sleRangeEnd,
       "sleRangeSubnetIP": sleRangeSubnetIP,
       "sleRangeSubnetMask": sleRangeSubnetMask,
       "sleRangeControl": sleRangeControl,
       "sleRangeControlRequest": sleRangeControlRequest,
       "sleRangeControlStatus": sleRangeControlStatus,
       "sleRangeControlTimer": sleRangeControlTimer,
       "sleRangeControlTImeStamp": sleRangeControlTImeStamp,
       "sleRangeControlReqResult": sleRangeControlReqResult,
       "sleRangeControlPoolIndex": sleRangeControlPoolIndex,
       "sleRangeControlStart": sleRangeControlStart,
       "sleRangeControlEnd": sleRangeControlEnd,
       "sleRangeNotification": sleRangeNotification,
       "sleRangeCreated": sleRangeCreated,
       "sleRangeDestroyed": sleRangeDestroyed,
       "sleFixed": sleFixed,
       "sleFixedTable": sleFixedTable,
       "sleFixedEntry": sleFixedEntry,
       "sleFixedIp": sleFixedIp,
       "sleFixedMac": sleFixedMac,
       "sleFixedControl": sleFixedControl,
       "sleFixedControlRequest": sleFixedControlRequest,
       "sleFixedControlStatus": sleFixedControlStatus,
       "sleFixedControlTimer": sleFixedControlTimer,
       "sleFixedControlTImeStamp": sleFixedControlTImeStamp,
       "sleFixedControlReqResult": sleFixedControlReqResult,
       "sleFixedControlPoolIndex": sleFixedControlPoolIndex,
       "sleFixedControlIp": sleFixedControlIp,
       "sleFixedControlMac": sleFixedControlMac,
       "sleFixedNotification": sleFixedNotification,
       "sleFixedCreated": sleFixedCreated,
       "sleFixedDestroyed": sleFixedDestroyed,
       "sleOption82": sleOption82,
       "sleOption82Table": sleOption82Table,
       "sleOption82Entry": sleOption82Entry,
       "sleOption82RemoteType": sleOption82RemoteType,
       "sleOption82RemoteId": sleOption82RemoteId,
       "sleOption82CircuitType": sleOption82CircuitType,
       "sleOption82CircuitId": sleOption82CircuitId,
       "sleOption82Limit": sleOption82Limit,
       "sleOption82PoolName": sleOption82PoolName,
       "sleOption82Control": sleOption82Control,
       "sleOption82ControlRequest": sleOption82ControlRequest,
       "sleOption82ControlStatus": sleOption82ControlStatus,
       "sleOption82ControlTimer": sleOption82ControlTimer,
       "sleOption82ControlTImeStamp": sleOption82ControlTImeStamp,
       "sleOption82ControlReqResult": sleOption82ControlReqResult,
       "sleOption82ControlRemoteType": sleOption82ControlRemoteType,
       "sleOption82ControlRemoteId": sleOption82ControlRemoteId,
       "sleOption82ControlCircuitType": sleOption82ControlCircuitType,
       "sleOption82ControlCircuitId": sleOption82ControlCircuitId,
       "sleOption82ControlLimit": sleOption82ControlLimit,
       "sleOption82ControlPoolName": sleOption82ControlPoolName,
       "sleOption82Notification": sleOption82Notification,
       "sleOption82Created": sleOption82Created,
       "sleOption82Destroyed": sleOption82Destroyed,
       "sleOption82ProfileChanged": sleOption82ProfileChanged,
       "sleOption82System": sleOption82System,
       "sleOption82SystemTable": sleOption82SystemTable,
       "sleOption82SystemEntry": sleOption82SystemEntry,
       "sleOption82SystemIndex": sleOption82SystemIndex,
       "sleOption82SystemCtype": sleOption82SystemCtype,
       "sleOption82SystemCid": sleOption82SystemCid,
       "sleOption82SystemControl": sleOption82SystemControl,
       "sleOption82SystemControlRequest": sleOption82SystemControlRequest,
       "sleOption82SystemControlStatus": sleOption82SystemControlStatus,
       "sleOption82SystemControlTimer": sleOption82SystemControlTimer,
       "sleOption82SystemControlTImeStamp": sleOption82SystemControlTImeStamp,
       "sleOption82SystemControlReqResult": sleOption82SystemControlReqResult,
       "sleOption82SystemControlIndex": sleOption82SystemControlIndex,
       "sleOption82SystemControlCtype": sleOption82SystemControlCtype,
       "sleOption82SystemControlCid": sleOption82SystemControlCid,
       "sleOption82CircuitNotification": sleOption82CircuitNotification,
       "setOption82SystemCircuit": setOption82SystemCircuit,
       "sleIllegal": sleIllegal,
       "sleIllegalTable": sleIllegalTable,
       "sleIllegalEntry": sleIllegalEntry,
       "sleIllegalIp": sleIllegalIp,
       "sleIllegalMac": sleIllegalMac,
       "sleIllegalTime": sleIllegalTime,
       "sleIllegalControl": sleIllegalControl,
       "sleIllegalControlRequest": sleIllegalControlRequest,
       "sleIllegalControlStatus": sleIllegalControlStatus,
       "sleIllegalControlTimer": sleIllegalControlTimer,
       "sleIllegalControlTImeStamp": sleIllegalControlTImeStamp,
       "sleIllegalControlReqResult": sleIllegalControlReqResult,
       "sleIllegalNotification": sleIllegalNotification,
       "sleIllegalCleared": sleIllegalCleared,
       "sleLeased": sleLeased,
       "sleLeasedTable": sleLeasedTable,
       "sleLeasedEntry": sleLeasedEntry,
       "sleLeasedIp": sleLeasedIp,
       "sleLeasedPoolIndex": sleLeasedPoolIndex,
       "sleLeasedPoolName": sleLeasedPoolName,
       "sleLeasedTime": sleLeasedTime,
       "sleLeasedHwaddr": sleLeasedHwaddr,
       "sleLeasedHostname": sleLeasedHostname,
       "sleLeasedUid": sleLeasedUid,
       "sleLeasedRid": sleLeasedRid,
       "sleLeasedCid": sleLeasedCid,
       "sleLeasedControl": sleLeasedControl,
       "sleLeasedControlRequest": sleLeasedControlRequest,
       "sleLeasedControlStatus": sleLeasedControlStatus,
       "sleLeasedControlTimer": sleLeasedControlTimer,
       "sleLeasedControlTImeStamp": sleLeasedControlTImeStamp,
       "sleLeasedControlReqResult": sleLeasedControlReqResult,
       "sleLeasedControlIp": sleLeasedControlIp,
       "sleLeasedControlMask": sleLeasedControlMask,
       "sleLeasedControlPoolIndex": sleLeasedControlPoolIndex,
       "sleLeasedNotification": sleLeasedNotification,
       "sleLeasedIpMaskFlushed": sleLeasedIpMaskFlushed,
       "sleLeasedPoolFlushed": sleLeasedPoolFlushed,
       "sleDhcpGroup": sleDhcpGroup,
       "sleDhcpNotificationGroup": sleDhcpNotificationGroup}
)
