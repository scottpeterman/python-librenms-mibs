# SNMP MIB module (DELLEMC-OS10-BGP4V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELLEMC-OS10-BGP4V2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:56 2025
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

(os10Experiment,) = mibBuilder.importSymbols(
    "DELLEMC-OS10-SMI-MIB",
    "os10Experiment")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

os10Bgp4V2Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1)
)
if mibBuilder.loadTexts:
    os10Bgp4V2Mib.setRevisions(
        ("2020-02-25 12:00",
         "2018-07-04 12:00",
         "2014-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Os10Bgp4V2IdentifierTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d."
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



class Os10Bgp4V2AddressFamilyIdentifierTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )



class Os10Bgp4V2SubsequentAddressFamilyIdentifierTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("mpls", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Os10bgp4V2Notifications_ObjectIdentity = ObjectIdentity
os10bgp4V2Notifications = _Os10bgp4V2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 0)
)
_Os10bgp4V2Objects_ObjectIdentity = ObjectIdentity
os10bgp4V2Objects = _Os10bgp4V2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1)
)
_Os10bgp4V2DiscontinuityTable_Object = MibTable
os10bgp4V2DiscontinuityTable = _Os10bgp4V2DiscontinuityTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 1)
)
if mibBuilder.loadTexts:
    os10bgp4V2DiscontinuityTable.setStatus("current")
_Os10bgp4V2DiscontinuityEntry_Object = MibTableRow
os10bgp4V2DiscontinuityEntry = _Os10bgp4V2DiscontinuityEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 1, 1)
)
os10bgp4V2DiscontinuityEntry.setIndexNames(
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerInstance"),
)
if mibBuilder.loadTexts:
    os10bgp4V2DiscontinuityEntry.setStatus("current")
_Os10bgp4V2DiscontinuityTime_Type = TimeStamp
_Os10bgp4V2DiscontinuityTime_Object = MibTableColumn
os10bgp4V2DiscontinuityTime = _Os10bgp4V2DiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 1, 1, 1),
    _Os10bgp4V2DiscontinuityTime_Type()
)
os10bgp4V2DiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2DiscontinuityTime.setStatus("current")
_Os10bgp4V2PeerTable_Object = MibTable
os10bgp4V2PeerTable = _Os10bgp4V2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerTable.setStatus("current")
_Os10bgp4V2PeerEntry_Object = MibTableRow
os10bgp4V2PeerEntry = _Os10bgp4V2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1)
)
os10bgp4V2PeerEntry.setIndexNames(
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerInstance"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerRemoteAddrType"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerEntry.setStatus("current")


class _Os10bgp4V2PeerInstance_Type(Unsigned32):
    """Custom type os10bgp4V2PeerInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Os10bgp4V2PeerInstance_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerInstance_Object = MibTableColumn
os10bgp4V2PeerInstance = _Os10bgp4V2PeerInstance_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 1),
    _Os10bgp4V2PeerInstance_Type()
)
os10bgp4V2PeerInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2PeerInstance.setStatus("current")
_Os10bgp4V2PeerLocalAddrType_Type = InetAddressType
_Os10bgp4V2PeerLocalAddrType_Object = MibTableColumn
os10bgp4V2PeerLocalAddrType = _Os10bgp4V2PeerLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 2),
    _Os10bgp4V2PeerLocalAddrType_Type()
)
os10bgp4V2PeerLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLocalAddrType.setStatus("current")
_Os10bgp4V2PeerLocalAddr_Type = InetAddress
_Os10bgp4V2PeerLocalAddr_Object = MibTableColumn
os10bgp4V2PeerLocalAddr = _Os10bgp4V2PeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 3),
    _Os10bgp4V2PeerLocalAddr_Type()
)
os10bgp4V2PeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLocalAddr.setStatus("current")
_Os10bgp4V2PeerRemoteAddrType_Type = InetAddressType
_Os10bgp4V2PeerRemoteAddrType_Object = MibTableColumn
os10bgp4V2PeerRemoteAddrType = _Os10bgp4V2PeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 4),
    _Os10bgp4V2PeerRemoteAddrType_Type()
)
os10bgp4V2PeerRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2PeerRemoteAddrType.setStatus("current")
_Os10bgp4V2PeerRemoteAddr_Type = InetAddress
_Os10bgp4V2PeerRemoteAddr_Object = MibTableColumn
os10bgp4V2PeerRemoteAddr = _Os10bgp4V2PeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 5),
    _Os10bgp4V2PeerRemoteAddr_Type()
)
os10bgp4V2PeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2PeerRemoteAddr.setStatus("current")
_Os10bgp4V2PeerLocalPort_Type = InetPortNumber
_Os10bgp4V2PeerLocalPort_Object = MibTableColumn
os10bgp4V2PeerLocalPort = _Os10bgp4V2PeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 6),
    _Os10bgp4V2PeerLocalPort_Type()
)
os10bgp4V2PeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLocalPort.setStatus("current")
_Os10bgp4V2PeerLocalAs_Type = InetAutonomousSystemNumber
_Os10bgp4V2PeerLocalAs_Object = MibTableColumn
os10bgp4V2PeerLocalAs = _Os10bgp4V2PeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 7),
    _Os10bgp4V2PeerLocalAs_Type()
)
os10bgp4V2PeerLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLocalAs.setStatus("current")
_Os10bgp4V2PeerLocalIdentifier_Type = Os10Bgp4V2IdentifierTC
_Os10bgp4V2PeerLocalIdentifier_Object = MibTableColumn
os10bgp4V2PeerLocalIdentifier = _Os10bgp4V2PeerLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 8),
    _Os10bgp4V2PeerLocalIdentifier_Type()
)
os10bgp4V2PeerLocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLocalIdentifier.setStatus("current")
_Os10bgp4V2PeerRemotePort_Type = InetPortNumber
_Os10bgp4V2PeerRemotePort_Object = MibTableColumn
os10bgp4V2PeerRemotePort = _Os10bgp4V2PeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 9),
    _Os10bgp4V2PeerRemotePort_Type()
)
os10bgp4V2PeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerRemotePort.setStatus("current")
_Os10bgp4V2PeerRemoteAs_Type = InetAutonomousSystemNumber
_Os10bgp4V2PeerRemoteAs_Object = MibTableColumn
os10bgp4V2PeerRemoteAs = _Os10bgp4V2PeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 10),
    _Os10bgp4V2PeerRemoteAs_Type()
)
os10bgp4V2PeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerRemoteAs.setStatus("current")
_Os10bgp4V2PeerRemoteIdentifier_Type = Os10Bgp4V2IdentifierTC
_Os10bgp4V2PeerRemoteIdentifier_Object = MibTableColumn
os10bgp4V2PeerRemoteIdentifier = _Os10bgp4V2PeerRemoteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 11),
    _Os10bgp4V2PeerRemoteIdentifier_Type()
)
os10bgp4V2PeerRemoteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerRemoteIdentifier.setStatus("current")


class _Os10bgp4V2PeerAdminStatus_Type(Integer32):
    """Custom type os10bgp4V2PeerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halted", 1),
          ("running", 2))
    )


_Os10bgp4V2PeerAdminStatus_Type.__name__ = "Integer32"
_Os10bgp4V2PeerAdminStatus_Object = MibTableColumn
os10bgp4V2PeerAdminStatus = _Os10bgp4V2PeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 12),
    _Os10bgp4V2PeerAdminStatus_Type()
)
os10bgp4V2PeerAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerAdminStatus.setStatus("current")


class _Os10bgp4V2PeerState_Type(Integer32):
    """Custom type os10bgp4V2PeerState based on Integer32"""
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
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_Os10bgp4V2PeerState_Type.__name__ = "Integer32"
_Os10bgp4V2PeerState_Object = MibTableColumn
os10bgp4V2PeerState = _Os10bgp4V2PeerState_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 13),
    _Os10bgp4V2PeerState_Type()
)
os10bgp4V2PeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerState.setStatus("current")
_Os10bgp4V2PeerDescription_Type = SnmpAdminString
_Os10bgp4V2PeerDescription_Object = MibTableColumn
os10bgp4V2PeerDescription = _Os10bgp4V2PeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 2, 1, 14),
    _Os10bgp4V2PeerDescription_Type()
)
os10bgp4V2PeerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerDescription.setStatus("current")
_Os10bgp4V2PeerErrorsTable_Object = MibTable
os10bgp4V2PeerErrorsTable = _Os10bgp4V2PeerErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerErrorsTable.setStatus("current")
_Os10bgp4V2PeerErrorsEntry_Object = MibTableRow
os10bgp4V2PeerErrorsEntry = _Os10bgp4V2PeerErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerErrorsEntry.setStatus("current")


class _Os10bgp4V2PeerLastErrorCodeReceived_Type(Unsigned32):
    """Custom type os10bgp4V2PeerLastErrorCodeReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Os10bgp4V2PeerLastErrorCodeReceived_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerLastErrorCodeReceived_Object = MibTableColumn
os10bgp4V2PeerLastErrorCodeReceived = _Os10bgp4V2PeerLastErrorCodeReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1, 1),
    _Os10bgp4V2PeerLastErrorCodeReceived_Type()
)
os10bgp4V2PeerLastErrorCodeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLastErrorCodeReceived.setStatus("current")


class _Os10bgp4V2PeerLastErrorSubCodeReceived_Type(Unsigned32):
    """Custom type os10bgp4V2PeerLastErrorSubCodeReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Os10bgp4V2PeerLastErrorSubCodeReceived_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerLastErrorSubCodeReceived_Object = MibTableColumn
os10bgp4V2PeerLastErrorSubCodeReceived = _Os10bgp4V2PeerLastErrorSubCodeReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1, 2),
    _Os10bgp4V2PeerLastErrorSubCodeReceived_Type()
)
os10bgp4V2PeerLastErrorSubCodeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLastErrorSubCodeReceived.setStatus("current")
_Os10bgp4V2PeerLastErrorReceivedTime_Type = TimeStamp
_Os10bgp4V2PeerLastErrorReceivedTime_Object = MibTableColumn
os10bgp4V2PeerLastErrorReceivedTime = _Os10bgp4V2PeerLastErrorReceivedTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1, 3),
    _Os10bgp4V2PeerLastErrorReceivedTime_Type()
)
os10bgp4V2PeerLastErrorReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLastErrorReceivedTime.setStatus("current")
_Os10bgp4V2PeerLastErrorReceivedText_Type = SnmpAdminString
_Os10bgp4V2PeerLastErrorReceivedText_Object = MibTableColumn
os10bgp4V2PeerLastErrorReceivedText = _Os10bgp4V2PeerLastErrorReceivedText_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1, 4),
    _Os10bgp4V2PeerLastErrorReceivedText_Type()
)
os10bgp4V2PeerLastErrorReceivedText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLastErrorReceivedText.setStatus("current")


class _Os10bgp4V2PeerLastErrorReceivedData_Type(OctetString):
    """Custom type os10bgp4V2PeerLastErrorReceivedData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_Os10bgp4V2PeerLastErrorReceivedData_Type.__name__ = "OctetString"
_Os10bgp4V2PeerLastErrorReceivedData_Object = MibTableColumn
os10bgp4V2PeerLastErrorReceivedData = _Os10bgp4V2PeerLastErrorReceivedData_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1, 5),
    _Os10bgp4V2PeerLastErrorReceivedData_Type()
)
os10bgp4V2PeerLastErrorReceivedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLastErrorReceivedData.setStatus("current")


class _Os10bgp4V2PeerLastErrorCodeSent_Type(Unsigned32):
    """Custom type os10bgp4V2PeerLastErrorCodeSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Os10bgp4V2PeerLastErrorCodeSent_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerLastErrorCodeSent_Object = MibTableColumn
os10bgp4V2PeerLastErrorCodeSent = _Os10bgp4V2PeerLastErrorCodeSent_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1, 6),
    _Os10bgp4V2PeerLastErrorCodeSent_Type()
)
os10bgp4V2PeerLastErrorCodeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLastErrorCodeSent.setStatus("current")


class _Os10bgp4V2PeerLastErrorSubCodeSent_Type(Unsigned32):
    """Custom type os10bgp4V2PeerLastErrorSubCodeSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Os10bgp4V2PeerLastErrorSubCodeSent_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerLastErrorSubCodeSent_Object = MibTableColumn
os10bgp4V2PeerLastErrorSubCodeSent = _Os10bgp4V2PeerLastErrorSubCodeSent_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1, 7),
    _Os10bgp4V2PeerLastErrorSubCodeSent_Type()
)
os10bgp4V2PeerLastErrorSubCodeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLastErrorSubCodeSent.setStatus("current")
_Os10bgp4V2PeerLastErrorSentTime_Type = TimeStamp
_Os10bgp4V2PeerLastErrorSentTime_Object = MibTableColumn
os10bgp4V2PeerLastErrorSentTime = _Os10bgp4V2PeerLastErrorSentTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1, 8),
    _Os10bgp4V2PeerLastErrorSentTime_Type()
)
os10bgp4V2PeerLastErrorSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLastErrorSentTime.setStatus("current")
_Os10bgp4V2PeerLastErrorSentText_Type = SnmpAdminString
_Os10bgp4V2PeerLastErrorSentText_Object = MibTableColumn
os10bgp4V2PeerLastErrorSentText = _Os10bgp4V2PeerLastErrorSentText_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1, 9),
    _Os10bgp4V2PeerLastErrorSentText_Type()
)
os10bgp4V2PeerLastErrorSentText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLastErrorSentText.setStatus("current")


class _Os10bgp4V2PeerLastErrorSentData_Type(OctetString):
    """Custom type os10bgp4V2PeerLastErrorSentData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4075),
    )


_Os10bgp4V2PeerLastErrorSentData_Type.__name__ = "OctetString"
_Os10bgp4V2PeerLastErrorSentData_Object = MibTableColumn
os10bgp4V2PeerLastErrorSentData = _Os10bgp4V2PeerLastErrorSentData_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 3, 1, 10),
    _Os10bgp4V2PeerLastErrorSentData_Type()
)
os10bgp4V2PeerLastErrorSentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerLastErrorSentData.setStatus("current")
_Os10bgp4V2PeerEventTimesTable_Object = MibTable
os10bgp4V2PeerEventTimesTable = _Os10bgp4V2PeerEventTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 4)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerEventTimesTable.setStatus("current")
_Os10bgp4V2PeerEventTimesEntry_Object = MibTableRow
os10bgp4V2PeerEventTimesEntry = _Os10bgp4V2PeerEventTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerEventTimesEntry.setStatus("current")
_Os10bgp4V2PeerFsmEstablishedTime_Type = Gauge32
_Os10bgp4V2PeerFsmEstablishedTime_Object = MibTableColumn
os10bgp4V2PeerFsmEstablishedTime = _Os10bgp4V2PeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 4, 1, 1),
    _Os10bgp4V2PeerFsmEstablishedTime_Type()
)
os10bgp4V2PeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerFsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    os10bgp4V2PeerFsmEstablishedTime.setUnits("seconds")
_Os10bgp4V2PeerInUpdatesElapsedTime_Type = Gauge32
_Os10bgp4V2PeerInUpdatesElapsedTime_Object = MibTableColumn
os10bgp4V2PeerInUpdatesElapsedTime = _Os10bgp4V2PeerInUpdatesElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 4, 1, 2),
    _Os10bgp4V2PeerInUpdatesElapsedTime_Type()
)
os10bgp4V2PeerInUpdatesElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerInUpdatesElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    os10bgp4V2PeerInUpdatesElapsedTime.setUnits("seconds")
_Os10bgp4V2PeerConfiguredTimersTable_Object = MibTable
os10bgp4V2PeerConfiguredTimersTable = _Os10bgp4V2PeerConfiguredTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 5)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerConfiguredTimersTable.setStatus("current")
_Os10bgp4V2PeerConfiguredTimersEntry_Object = MibTableRow
os10bgp4V2PeerConfiguredTimersEntry = _Os10bgp4V2PeerConfiguredTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerConfiguredTimersEntry.setStatus("current")


class _Os10bgp4V2PeerConnectRetryInterval_Type(Unsigned32):
    """Custom type os10bgp4V2PeerConnectRetryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Os10bgp4V2PeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerConnectRetryInterval_Object = MibTableColumn
os10bgp4V2PeerConnectRetryInterval = _Os10bgp4V2PeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 5, 1, 1),
    _Os10bgp4V2PeerConnectRetryInterval_Type()
)
os10bgp4V2PeerConnectRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    os10bgp4V2PeerConnectRetryInterval.setUnits("seconds")


class _Os10bgp4V2PeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type os10bgp4V2PeerHoldTimeConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_Os10bgp4V2PeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerHoldTimeConfigured_Object = MibTableColumn
os10bgp4V2PeerHoldTimeConfigured = _Os10bgp4V2PeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 5, 1, 2),
    _Os10bgp4V2PeerHoldTimeConfigured_Type()
)
os10bgp4V2PeerHoldTimeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerHoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    os10bgp4V2PeerHoldTimeConfigured.setUnits("seconds")


class _Os10bgp4V2PeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type os10bgp4V2PeerKeepAliveConfigured based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_Os10bgp4V2PeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerKeepAliveConfigured_Object = MibTableColumn
os10bgp4V2PeerKeepAliveConfigured = _Os10bgp4V2PeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 5, 1, 3),
    _Os10bgp4V2PeerKeepAliveConfigured_Type()
)
os10bgp4V2PeerKeepAliveConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerKeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    os10bgp4V2PeerKeepAliveConfigured.setUnits("seconds")


class _Os10bgp4V2PeerMinASOrigInterval_Type(Unsigned32):
    """Custom type os10bgp4V2PeerMinASOrigInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Os10bgp4V2PeerMinASOrigInterval_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerMinASOrigInterval_Object = MibTableColumn
os10bgp4V2PeerMinASOrigInterval = _Os10bgp4V2PeerMinASOrigInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 5, 1, 4),
    _Os10bgp4V2PeerMinASOrigInterval_Type()
)
os10bgp4V2PeerMinASOrigInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerMinASOrigInterval.setStatus("current")
if mibBuilder.loadTexts:
    os10bgp4V2PeerMinASOrigInterval.setUnits("seconds")


class _Os10bgp4V2PeerMinRouteAdverInterval_Type(Unsigned32):
    """Custom type os10bgp4V2PeerMinRouteAdverInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Os10bgp4V2PeerMinRouteAdverInterval_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerMinRouteAdverInterval_Object = MibTableColumn
os10bgp4V2PeerMinRouteAdverInterval = _Os10bgp4V2PeerMinRouteAdverInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 5, 1, 5),
    _Os10bgp4V2PeerMinRouteAdverInterval_Type()
)
os10bgp4V2PeerMinRouteAdverInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerMinRouteAdverInterval.setStatus("current")
if mibBuilder.loadTexts:
    os10bgp4V2PeerMinRouteAdverInterval.setUnits("seconds")
_Os10bgp4V2PeerNegotiatedTimersTable_Object = MibTable
os10bgp4V2PeerNegotiatedTimersTable = _Os10bgp4V2PeerNegotiatedTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 6)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerNegotiatedTimersTable.setStatus("current")
_Os10bgp4V2PeerNegotiatedTimersEntry_Object = MibTableRow
os10bgp4V2PeerNegotiatedTimersEntry = _Os10bgp4V2PeerNegotiatedTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerNegotiatedTimersEntry.setStatus("current")


class _Os10bgp4V2PeerHoldTime_Type(Unsigned32):
    """Custom type os10bgp4V2PeerHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_Os10bgp4V2PeerHoldTime_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerHoldTime_Object = MibTableColumn
os10bgp4V2PeerHoldTime = _Os10bgp4V2PeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 6, 1, 1),
    _Os10bgp4V2PeerHoldTime_Type()
)
os10bgp4V2PeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    os10bgp4V2PeerHoldTime.setUnits("seconds")


class _Os10bgp4V2PeerKeepAlive_Type(Unsigned32):
    """Custom type os10bgp4V2PeerKeepAlive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_Os10bgp4V2PeerKeepAlive_Type.__name__ = "Unsigned32"
_Os10bgp4V2PeerKeepAlive_Object = MibTableColumn
os10bgp4V2PeerKeepAlive = _Os10bgp4V2PeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 6, 1, 2),
    _Os10bgp4V2PeerKeepAlive_Type()
)
os10bgp4V2PeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    os10bgp4V2PeerKeepAlive.setUnits("seconds")
_Os10bgp4V2PeerCountersTable_Object = MibTable
os10bgp4V2PeerCountersTable = _Os10bgp4V2PeerCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 7)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerCountersTable.setStatus("current")
_Os10bgp4V2PeerCountersEntry_Object = MibTableRow
os10bgp4V2PeerCountersEntry = _Os10bgp4V2PeerCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    os10bgp4V2PeerCountersEntry.setStatus("current")
_Os10bgp4V2PeerInUpdates_Type = Counter32
_Os10bgp4V2PeerInUpdates_Object = MibTableColumn
os10bgp4V2PeerInUpdates = _Os10bgp4V2PeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 7, 1, 1),
    _Os10bgp4V2PeerInUpdates_Type()
)
os10bgp4V2PeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerInUpdates.setStatus("current")
_Os10bgp4V2PeerOutUpdates_Type = Counter32
_Os10bgp4V2PeerOutUpdates_Object = MibTableColumn
os10bgp4V2PeerOutUpdates = _Os10bgp4V2PeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 7, 1, 2),
    _Os10bgp4V2PeerOutUpdates_Type()
)
os10bgp4V2PeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerOutUpdates.setStatus("current")
_Os10bgp4V2PeerInTotalMessages_Type = Counter32
_Os10bgp4V2PeerInTotalMessages_Object = MibTableColumn
os10bgp4V2PeerInTotalMessages = _Os10bgp4V2PeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 7, 1, 3),
    _Os10bgp4V2PeerInTotalMessages_Type()
)
os10bgp4V2PeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerInTotalMessages.setStatus("current")
_Os10bgp4V2PeerOutTotalMessages_Type = Counter32
_Os10bgp4V2PeerOutTotalMessages_Object = MibTableColumn
os10bgp4V2PeerOutTotalMessages = _Os10bgp4V2PeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 7, 1, 4),
    _Os10bgp4V2PeerOutTotalMessages_Type()
)
os10bgp4V2PeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerOutTotalMessages.setStatus("current")
_Os10bgp4V2PeerFsmEstablishedTransitions_Type = Counter32
_Os10bgp4V2PeerFsmEstablishedTransitions_Object = MibTableColumn
os10bgp4V2PeerFsmEstablishedTransitions = _Os10bgp4V2PeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 7, 1, 5),
    _Os10bgp4V2PeerFsmEstablishedTransitions_Type()
)
os10bgp4V2PeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PeerFsmEstablishedTransitions.setStatus("current")
_Os10bgp4V2PrefixGaugesTable_Object = MibTable
os10bgp4V2PrefixGaugesTable = _Os10bgp4V2PrefixGaugesTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 8)
)
if mibBuilder.loadTexts:
    os10bgp4V2PrefixGaugesTable.setStatus("current")
_Os10bgp4V2PrefixGaugesEntry_Object = MibTableRow
os10bgp4V2PrefixGaugesEntry = _Os10bgp4V2PrefixGaugesEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 8, 1)
)
os10bgp4V2PrefixGaugesEntry.setIndexNames(
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerInstance"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerRemoteAddrType"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerRemoteAddr"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PrefixGaugesAfi"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PrefixGaugesSafi"),
)
if mibBuilder.loadTexts:
    os10bgp4V2PrefixGaugesEntry.setStatus("current")
_Os10bgp4V2PrefixGaugesAfi_Type = Os10Bgp4V2AddressFamilyIdentifierTC
_Os10bgp4V2PrefixGaugesAfi_Object = MibTableColumn
os10bgp4V2PrefixGaugesAfi = _Os10bgp4V2PrefixGaugesAfi_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 8, 1, 1),
    _Os10bgp4V2PrefixGaugesAfi_Type()
)
os10bgp4V2PrefixGaugesAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2PrefixGaugesAfi.setStatus("current")
_Os10bgp4V2PrefixGaugesSafi_Type = Os10Bgp4V2SubsequentAddressFamilyIdentifierTC
_Os10bgp4V2PrefixGaugesSafi_Object = MibTableColumn
os10bgp4V2PrefixGaugesSafi = _Os10bgp4V2PrefixGaugesSafi_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 8, 1, 2),
    _Os10bgp4V2PrefixGaugesSafi_Type()
)
os10bgp4V2PrefixGaugesSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2PrefixGaugesSafi.setStatus("current")
_Os10bgp4V2PrefixInPrefixes_Type = Gauge32
_Os10bgp4V2PrefixInPrefixes_Object = MibTableColumn
os10bgp4V2PrefixInPrefixes = _Os10bgp4V2PrefixInPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 8, 1, 3),
    _Os10bgp4V2PrefixInPrefixes_Type()
)
os10bgp4V2PrefixInPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PrefixInPrefixes.setStatus("current")
_Os10bgp4V2PrefixInPrefixesAccepted_Type = Gauge32
_Os10bgp4V2PrefixInPrefixesAccepted_Object = MibTableColumn
os10bgp4V2PrefixInPrefixesAccepted = _Os10bgp4V2PrefixInPrefixesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 8, 1, 4),
    _Os10bgp4V2PrefixInPrefixesAccepted_Type()
)
os10bgp4V2PrefixInPrefixesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PrefixInPrefixesAccepted.setStatus("current")
_Os10bgp4V2PrefixOutPrefixes_Type = Gauge32
_Os10bgp4V2PrefixOutPrefixes_Object = MibTableColumn
os10bgp4V2PrefixOutPrefixes = _Os10bgp4V2PrefixOutPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 8, 1, 5),
    _Os10bgp4V2PrefixOutPrefixes_Type()
)
os10bgp4V2PrefixOutPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2PrefixOutPrefixes.setStatus("current")
_Os10bgp4V2NlriTable_Object = MibTable
os10bgp4V2NlriTable = _Os10bgp4V2NlriTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9)
)
if mibBuilder.loadTexts:
    os10bgp4V2NlriTable.setStatus("current")
_Os10bgp4V2NlriEntry_Object = MibTableRow
os10bgp4V2NlriEntry = _Os10bgp4V2NlriEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1)
)
os10bgp4V2NlriEntry.setIndexNames(
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerInstance"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriAfi"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriSafi"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriPrefixType"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriPrefix"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriPrefixLen"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerRemoteAddrType"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerRemoteAddr"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriIndex"),
)
if mibBuilder.loadTexts:
    os10bgp4V2NlriEntry.setStatus("current")


class _Os10bgp4V2NlriIndex_Type(Unsigned32):
    """Custom type os10bgp4V2NlriIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Os10bgp4V2NlriIndex_Type.__name__ = "Unsigned32"
_Os10bgp4V2NlriIndex_Object = MibTableColumn
os10bgp4V2NlriIndex = _Os10bgp4V2NlriIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 1),
    _Os10bgp4V2NlriIndex_Type()
)
os10bgp4V2NlriIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2NlriIndex.setStatus("current")
_Os10bgp4V2NlriAfi_Type = Os10Bgp4V2AddressFamilyIdentifierTC
_Os10bgp4V2NlriAfi_Object = MibTableColumn
os10bgp4V2NlriAfi = _Os10bgp4V2NlriAfi_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 2),
    _Os10bgp4V2NlriAfi_Type()
)
os10bgp4V2NlriAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2NlriAfi.setStatus("current")
_Os10bgp4V2NlriSafi_Type = Os10Bgp4V2SubsequentAddressFamilyIdentifierTC
_Os10bgp4V2NlriSafi_Object = MibTableColumn
os10bgp4V2NlriSafi = _Os10bgp4V2NlriSafi_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 3),
    _Os10bgp4V2NlriSafi_Type()
)
os10bgp4V2NlriSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2NlriSafi.setStatus("current")
_Os10bgp4V2NlriPrefixType_Type = InetAddressType
_Os10bgp4V2NlriPrefixType_Object = MibTableColumn
os10bgp4V2NlriPrefixType = _Os10bgp4V2NlriPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 4),
    _Os10bgp4V2NlriPrefixType_Type()
)
os10bgp4V2NlriPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2NlriPrefixType.setStatus("current")
_Os10bgp4V2NlriPrefix_Type = InetAddress
_Os10bgp4V2NlriPrefix_Object = MibTableColumn
os10bgp4V2NlriPrefix = _Os10bgp4V2NlriPrefix_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 5),
    _Os10bgp4V2NlriPrefix_Type()
)
os10bgp4V2NlriPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2NlriPrefix.setStatus("current")
_Os10bgp4V2NlriPrefixLen_Type = InetAddressPrefixLength
_Os10bgp4V2NlriPrefixLen_Object = MibTableColumn
os10bgp4V2NlriPrefixLen = _Os10bgp4V2NlriPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 6),
    _Os10bgp4V2NlriPrefixLen_Type()
)
os10bgp4V2NlriPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2NlriPrefixLen.setStatus("current")
_Os10bgp4V2NlriBest_Type = TruthValue
_Os10bgp4V2NlriBest_Object = MibTableColumn
os10bgp4V2NlriBest = _Os10bgp4V2NlriBest_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 7),
    _Os10bgp4V2NlriBest_Type()
)
os10bgp4V2NlriBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriBest.setStatus("current")
_Os10bgp4V2NlriCalcLocalPref_Type = Unsigned32
_Os10bgp4V2NlriCalcLocalPref_Object = MibTableColumn
os10bgp4V2NlriCalcLocalPref = _Os10bgp4V2NlriCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 8),
    _Os10bgp4V2NlriCalcLocalPref_Type()
)
os10bgp4V2NlriCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriCalcLocalPref.setStatus("current")


class _Os10bgp4V2NlriOrigin_Type(Integer32):
    """Custom type os10bgp4V2NlriOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("egp", 2),
          ("incomplete", 3))
    )


_Os10bgp4V2NlriOrigin_Type.__name__ = "Integer32"
_Os10bgp4V2NlriOrigin_Object = MibTableColumn
os10bgp4V2NlriOrigin = _Os10bgp4V2NlriOrigin_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 9),
    _Os10bgp4V2NlriOrigin_Type()
)
os10bgp4V2NlriOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriOrigin.setStatus("current")
_Os10bgp4V2NlriNextHopAddrType_Type = InetAddressType
_Os10bgp4V2NlriNextHopAddrType_Object = MibTableColumn
os10bgp4V2NlriNextHopAddrType = _Os10bgp4V2NlriNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 10),
    _Os10bgp4V2NlriNextHopAddrType_Type()
)
os10bgp4V2NlriNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriNextHopAddrType.setStatus("current")


class _Os10bgp4V2NlriNextHopAddr_Type(InetAddress):
    """Custom type os10bgp4V2NlriNextHopAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_Os10bgp4V2NlriNextHopAddr_Type.__name__ = "InetAddress"
_Os10bgp4V2NlriNextHopAddr_Object = MibTableColumn
os10bgp4V2NlriNextHopAddr = _Os10bgp4V2NlriNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 11),
    _Os10bgp4V2NlriNextHopAddr_Type()
)
os10bgp4V2NlriNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriNextHopAddr.setStatus("current")
_Os10bgp4V2NlriLinkLocalNextHopAddrType_Type = InetAddressType
_Os10bgp4V2NlriLinkLocalNextHopAddrType_Object = MibTableColumn
os10bgp4V2NlriLinkLocalNextHopAddrType = _Os10bgp4V2NlriLinkLocalNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 12),
    _Os10bgp4V2NlriLinkLocalNextHopAddrType_Type()
)
os10bgp4V2NlriLinkLocalNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriLinkLocalNextHopAddrType.setStatus("current")
_Os10bgp4V2NlriLinkLocalNextHopAddr_Type = InetAddress
_Os10bgp4V2NlriLinkLocalNextHopAddr_Object = MibTableColumn
os10bgp4V2NlriLinkLocalNextHopAddr = _Os10bgp4V2NlriLinkLocalNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 13),
    _Os10bgp4V2NlriLinkLocalNextHopAddr_Type()
)
os10bgp4V2NlriLinkLocalNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriLinkLocalNextHopAddr.setStatus("current")
_Os10bgp4V2NlriLocalPrefPresent_Type = TruthValue
_Os10bgp4V2NlriLocalPrefPresent_Object = MibTableColumn
os10bgp4V2NlriLocalPrefPresent = _Os10bgp4V2NlriLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 14),
    _Os10bgp4V2NlriLocalPrefPresent_Type()
)
os10bgp4V2NlriLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriLocalPrefPresent.setStatus("current")
_Os10bgp4V2NlriLocalPref_Type = Unsigned32
_Os10bgp4V2NlriLocalPref_Object = MibTableColumn
os10bgp4V2NlriLocalPref = _Os10bgp4V2NlriLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 15),
    _Os10bgp4V2NlriLocalPref_Type()
)
os10bgp4V2NlriLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriLocalPref.setStatus("current")
_Os10bgp4V2NlriMedPresent_Type = TruthValue
_Os10bgp4V2NlriMedPresent_Object = MibTableColumn
os10bgp4V2NlriMedPresent = _Os10bgp4V2NlriMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 16),
    _Os10bgp4V2NlriMedPresent_Type()
)
os10bgp4V2NlriMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriMedPresent.setStatus("current")
_Os10bgp4V2NlriMed_Type = Unsigned32
_Os10bgp4V2NlriMed_Object = MibTableColumn
os10bgp4V2NlriMed = _Os10bgp4V2NlriMed_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 17),
    _Os10bgp4V2NlriMed_Type()
)
os10bgp4V2NlriMed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriMed.setStatus("current")
_Os10bgp4V2NlriAtomicAggregate_Type = TruthValue
_Os10bgp4V2NlriAtomicAggregate_Object = MibTableColumn
os10bgp4V2NlriAtomicAggregate = _Os10bgp4V2NlriAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 18),
    _Os10bgp4V2NlriAtomicAggregate_Type()
)
os10bgp4V2NlriAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriAtomicAggregate.setStatus("current")
_Os10bgp4V2NlriAggregatorPresent_Type = TruthValue
_Os10bgp4V2NlriAggregatorPresent_Object = MibTableColumn
os10bgp4V2NlriAggregatorPresent = _Os10bgp4V2NlriAggregatorPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 19),
    _Os10bgp4V2NlriAggregatorPresent_Type()
)
os10bgp4V2NlriAggregatorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriAggregatorPresent.setStatus("current")
_Os10bgp4V2NlriAggregatorAS_Type = InetAutonomousSystemNumber
_Os10bgp4V2NlriAggregatorAS_Object = MibTableColumn
os10bgp4V2NlriAggregatorAS = _Os10bgp4V2NlriAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 20),
    _Os10bgp4V2NlriAggregatorAS_Type()
)
os10bgp4V2NlriAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriAggregatorAS.setStatus("current")
_Os10bgp4V2NlriAggregatorAddr_Type = Os10Bgp4V2IdentifierTC
_Os10bgp4V2NlriAggregatorAddr_Object = MibTableColumn
os10bgp4V2NlriAggregatorAddr = _Os10bgp4V2NlriAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 21),
    _Os10bgp4V2NlriAggregatorAddr_Type()
)
os10bgp4V2NlriAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriAggregatorAddr.setStatus("current")
_Os10bgp4V2NlriAsPathCalcLength_Type = Unsigned32
_Os10bgp4V2NlriAsPathCalcLength_Object = MibTableColumn
os10bgp4V2NlriAsPathCalcLength = _Os10bgp4V2NlriAsPathCalcLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 22),
    _Os10bgp4V2NlriAsPathCalcLength_Type()
)
os10bgp4V2NlriAsPathCalcLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriAsPathCalcLength.setStatus("current")
_Os10bgp4V2NlriAsPathString_Type = SnmpAdminString
_Os10bgp4V2NlriAsPathString_Object = MibTableColumn
os10bgp4V2NlriAsPathString = _Os10bgp4V2NlriAsPathString_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 23),
    _Os10bgp4V2NlriAsPathString_Type()
)
os10bgp4V2NlriAsPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriAsPathString.setStatus("current")


class _Os10bgp4V2NlriAsPath_Type(OctetString):
    """Custom type os10bgp4V2NlriAsPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4072),
    )


_Os10bgp4V2NlriAsPath_Type.__name__ = "OctetString"
_Os10bgp4V2NlriAsPath_Object = MibTableColumn
os10bgp4V2NlriAsPath = _Os10bgp4V2NlriAsPath_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 24),
    _Os10bgp4V2NlriAsPath_Type()
)
os10bgp4V2NlriAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriAsPath.setStatus("current")


class _Os10bgp4V2NlriPathAttrUnknown_Type(OctetString):
    """Custom type os10bgp4V2NlriPathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4072),
    )


_Os10bgp4V2NlriPathAttrUnknown_Type.__name__ = "OctetString"
_Os10bgp4V2NlriPathAttrUnknown_Object = MibTableColumn
os10bgp4V2NlriPathAttrUnknown = _Os10bgp4V2NlriPathAttrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 9, 1, 25),
    _Os10bgp4V2NlriPathAttrUnknown_Type()
)
os10bgp4V2NlriPathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2NlriPathAttrUnknown.setStatus("current")
_Os10bgp4V2AdjRibsOutTable_Object = MibTable
os10bgp4V2AdjRibsOutTable = _Os10bgp4V2AdjRibsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 10)
)
if mibBuilder.loadTexts:
    os10bgp4V2AdjRibsOutTable.setStatus("current")
_Os10bgp4V2AdjRibsOutEntry_Object = MibTableRow
os10bgp4V2AdjRibsOutEntry = _Os10bgp4V2AdjRibsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 10, 1)
)
os10bgp4V2AdjRibsOutEntry.setIndexNames(
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerInstance"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriAfi"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriSafi"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriPrefixType"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriPrefix"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2NlriPrefixLen"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerRemoteAddrType"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2PeerRemoteAddr"),
    (0, "DELLEMC-OS10-BGP4V2-MIB", "os10bgp4V2AdjRibsOutIndex"),
)
if mibBuilder.loadTexts:
    os10bgp4V2AdjRibsOutEntry.setStatus("current")


class _Os10bgp4V2AdjRibsOutIndex_Type(Unsigned32):
    """Custom type os10bgp4V2AdjRibsOutIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Os10bgp4V2AdjRibsOutIndex_Type.__name__ = "Unsigned32"
_Os10bgp4V2AdjRibsOutIndex_Object = MibTableColumn
os10bgp4V2AdjRibsOutIndex = _Os10bgp4V2AdjRibsOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 10, 1, 1),
    _Os10bgp4V2AdjRibsOutIndex_Type()
)
os10bgp4V2AdjRibsOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10bgp4V2AdjRibsOutIndex.setStatus("current")
_Os10bgp4V2AdjRibsOutRoute_Type = RowPointer
_Os10bgp4V2AdjRibsOutRoute_Object = MibTableColumn
os10bgp4V2AdjRibsOutRoute = _Os10bgp4V2AdjRibsOutRoute_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 1, 10, 1, 2),
    _Os10bgp4V2AdjRibsOutRoute_Type()
)
os10bgp4V2AdjRibsOutRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10bgp4V2AdjRibsOutRoute.setStatus("current")
_Os10bgp4V2Conformance_ObjectIdentity = ObjectIdentity
os10bgp4V2Conformance = _Os10bgp4V2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 200, 1, 2)
)
os10bgp4V2PeerEntry.registerAugmentions(
    ("DELLEMC-OS10-BGP4V2-MIB",
     "os10bgp4V2PeerErrorsEntry")
)
os10bgp4V2PeerErrorsEntry.setIndexNames(*os10bgp4V2PeerEntry.getIndexNames())
os10bgp4V2PeerEntry.registerAugmentions(
    ("DELLEMC-OS10-BGP4V2-MIB",
     "os10bgp4V2PeerEventTimesEntry")
)
os10bgp4V2PeerEventTimesEntry.setIndexNames(*os10bgp4V2PeerEntry.getIndexNames())
os10bgp4V2PeerEntry.registerAugmentions(
    ("DELLEMC-OS10-BGP4V2-MIB",
     "os10bgp4V2PeerConfiguredTimersEntry")
)
os10bgp4V2PeerConfiguredTimersEntry.setIndexNames(*os10bgp4V2PeerEntry.getIndexNames())
os10bgp4V2PeerEntry.registerAugmentions(
    ("DELLEMC-OS10-BGP4V2-MIB",
     "os10bgp4V2PeerNegotiatedTimersEntry")
)
os10bgp4V2PeerNegotiatedTimersEntry.setIndexNames(*os10bgp4V2PeerEntry.getIndexNames())
os10bgp4V2PeerEntry.registerAugmentions(
    ("DELLEMC-OS10-BGP4V2-MIB",
     "os10bgp4V2PeerCountersEntry")
)
os10bgp4V2PeerCountersEntry.setIndexNames(*os10bgp4V2PeerEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELLEMC-OS10-BGP4V2-MIB",
    **{"Os10Bgp4V2IdentifierTC": Os10Bgp4V2IdentifierTC,
       "Os10Bgp4V2AddressFamilyIdentifierTC": Os10Bgp4V2AddressFamilyIdentifierTC,
       "Os10Bgp4V2SubsequentAddressFamilyIdentifierTC": Os10Bgp4V2SubsequentAddressFamilyIdentifierTC,
       "os10Bgp4V2Mib": os10Bgp4V2Mib,
       "os10bgp4V2Notifications": os10bgp4V2Notifications,
       "os10bgp4V2Objects": os10bgp4V2Objects,
       "os10bgp4V2DiscontinuityTable": os10bgp4V2DiscontinuityTable,
       "os10bgp4V2DiscontinuityEntry": os10bgp4V2DiscontinuityEntry,
       "os10bgp4V2DiscontinuityTime": os10bgp4V2DiscontinuityTime,
       "os10bgp4V2PeerTable": os10bgp4V2PeerTable,
       "os10bgp4V2PeerEntry": os10bgp4V2PeerEntry,
       "os10bgp4V2PeerInstance": os10bgp4V2PeerInstance,
       "os10bgp4V2PeerLocalAddrType": os10bgp4V2PeerLocalAddrType,
       "os10bgp4V2PeerLocalAddr": os10bgp4V2PeerLocalAddr,
       "os10bgp4V2PeerRemoteAddrType": os10bgp4V2PeerRemoteAddrType,
       "os10bgp4V2PeerRemoteAddr": os10bgp4V2PeerRemoteAddr,
       "os10bgp4V2PeerLocalPort": os10bgp4V2PeerLocalPort,
       "os10bgp4V2PeerLocalAs": os10bgp4V2PeerLocalAs,
       "os10bgp4V2PeerLocalIdentifier": os10bgp4V2PeerLocalIdentifier,
       "os10bgp4V2PeerRemotePort": os10bgp4V2PeerRemotePort,
       "os10bgp4V2PeerRemoteAs": os10bgp4V2PeerRemoteAs,
       "os10bgp4V2PeerRemoteIdentifier": os10bgp4V2PeerRemoteIdentifier,
       "os10bgp4V2PeerAdminStatus": os10bgp4V2PeerAdminStatus,
       "os10bgp4V2PeerState": os10bgp4V2PeerState,
       "os10bgp4V2PeerDescription": os10bgp4V2PeerDescription,
       "os10bgp4V2PeerErrorsTable": os10bgp4V2PeerErrorsTable,
       "os10bgp4V2PeerErrorsEntry": os10bgp4V2PeerErrorsEntry,
       "os10bgp4V2PeerLastErrorCodeReceived": os10bgp4V2PeerLastErrorCodeReceived,
       "os10bgp4V2PeerLastErrorSubCodeReceived": os10bgp4V2PeerLastErrorSubCodeReceived,
       "os10bgp4V2PeerLastErrorReceivedTime": os10bgp4V2PeerLastErrorReceivedTime,
       "os10bgp4V2PeerLastErrorReceivedText": os10bgp4V2PeerLastErrorReceivedText,
       "os10bgp4V2PeerLastErrorReceivedData": os10bgp4V2PeerLastErrorReceivedData,
       "os10bgp4V2PeerLastErrorCodeSent": os10bgp4V2PeerLastErrorCodeSent,
       "os10bgp4V2PeerLastErrorSubCodeSent": os10bgp4V2PeerLastErrorSubCodeSent,
       "os10bgp4V2PeerLastErrorSentTime": os10bgp4V2PeerLastErrorSentTime,
       "os10bgp4V2PeerLastErrorSentText": os10bgp4V2PeerLastErrorSentText,
       "os10bgp4V2PeerLastErrorSentData": os10bgp4V2PeerLastErrorSentData,
       "os10bgp4V2PeerEventTimesTable": os10bgp4V2PeerEventTimesTable,
       "os10bgp4V2PeerEventTimesEntry": os10bgp4V2PeerEventTimesEntry,
       "os10bgp4V2PeerFsmEstablishedTime": os10bgp4V2PeerFsmEstablishedTime,
       "os10bgp4V2PeerInUpdatesElapsedTime": os10bgp4V2PeerInUpdatesElapsedTime,
       "os10bgp4V2PeerConfiguredTimersTable": os10bgp4V2PeerConfiguredTimersTable,
       "os10bgp4V2PeerConfiguredTimersEntry": os10bgp4V2PeerConfiguredTimersEntry,
       "os10bgp4V2PeerConnectRetryInterval": os10bgp4V2PeerConnectRetryInterval,
       "os10bgp4V2PeerHoldTimeConfigured": os10bgp4V2PeerHoldTimeConfigured,
       "os10bgp4V2PeerKeepAliveConfigured": os10bgp4V2PeerKeepAliveConfigured,
       "os10bgp4V2PeerMinASOrigInterval": os10bgp4V2PeerMinASOrigInterval,
       "os10bgp4V2PeerMinRouteAdverInterval": os10bgp4V2PeerMinRouteAdverInterval,
       "os10bgp4V2PeerNegotiatedTimersTable": os10bgp4V2PeerNegotiatedTimersTable,
       "os10bgp4V2PeerNegotiatedTimersEntry": os10bgp4V2PeerNegotiatedTimersEntry,
       "os10bgp4V2PeerHoldTime": os10bgp4V2PeerHoldTime,
       "os10bgp4V2PeerKeepAlive": os10bgp4V2PeerKeepAlive,
       "os10bgp4V2PeerCountersTable": os10bgp4V2PeerCountersTable,
       "os10bgp4V2PeerCountersEntry": os10bgp4V2PeerCountersEntry,
       "os10bgp4V2PeerInUpdates": os10bgp4V2PeerInUpdates,
       "os10bgp4V2PeerOutUpdates": os10bgp4V2PeerOutUpdates,
       "os10bgp4V2PeerInTotalMessages": os10bgp4V2PeerInTotalMessages,
       "os10bgp4V2PeerOutTotalMessages": os10bgp4V2PeerOutTotalMessages,
       "os10bgp4V2PeerFsmEstablishedTransitions": os10bgp4V2PeerFsmEstablishedTransitions,
       "os10bgp4V2PrefixGaugesTable": os10bgp4V2PrefixGaugesTable,
       "os10bgp4V2PrefixGaugesEntry": os10bgp4V2PrefixGaugesEntry,
       "os10bgp4V2PrefixGaugesAfi": os10bgp4V2PrefixGaugesAfi,
       "os10bgp4V2PrefixGaugesSafi": os10bgp4V2PrefixGaugesSafi,
       "os10bgp4V2PrefixInPrefixes": os10bgp4V2PrefixInPrefixes,
       "os10bgp4V2PrefixInPrefixesAccepted": os10bgp4V2PrefixInPrefixesAccepted,
       "os10bgp4V2PrefixOutPrefixes": os10bgp4V2PrefixOutPrefixes,
       "os10bgp4V2NlriTable": os10bgp4V2NlriTable,
       "os10bgp4V2NlriEntry": os10bgp4V2NlriEntry,
       "os10bgp4V2NlriIndex": os10bgp4V2NlriIndex,
       "os10bgp4V2NlriAfi": os10bgp4V2NlriAfi,
       "os10bgp4V2NlriSafi": os10bgp4V2NlriSafi,
       "os10bgp4V2NlriPrefixType": os10bgp4V2NlriPrefixType,
       "os10bgp4V2NlriPrefix": os10bgp4V2NlriPrefix,
       "os10bgp4V2NlriPrefixLen": os10bgp4V2NlriPrefixLen,
       "os10bgp4V2NlriBest": os10bgp4V2NlriBest,
       "os10bgp4V2NlriCalcLocalPref": os10bgp4V2NlriCalcLocalPref,
       "os10bgp4V2NlriOrigin": os10bgp4V2NlriOrigin,
       "os10bgp4V2NlriNextHopAddrType": os10bgp4V2NlriNextHopAddrType,
       "os10bgp4V2NlriNextHopAddr": os10bgp4V2NlriNextHopAddr,
       "os10bgp4V2NlriLinkLocalNextHopAddrType": os10bgp4V2NlriLinkLocalNextHopAddrType,
       "os10bgp4V2NlriLinkLocalNextHopAddr": os10bgp4V2NlriLinkLocalNextHopAddr,
       "os10bgp4V2NlriLocalPrefPresent": os10bgp4V2NlriLocalPrefPresent,
       "os10bgp4V2NlriLocalPref": os10bgp4V2NlriLocalPref,
       "os10bgp4V2NlriMedPresent": os10bgp4V2NlriMedPresent,
       "os10bgp4V2NlriMed": os10bgp4V2NlriMed,
       "os10bgp4V2NlriAtomicAggregate": os10bgp4V2NlriAtomicAggregate,
       "os10bgp4V2NlriAggregatorPresent": os10bgp4V2NlriAggregatorPresent,
       "os10bgp4V2NlriAggregatorAS": os10bgp4V2NlriAggregatorAS,
       "os10bgp4V2NlriAggregatorAddr": os10bgp4V2NlriAggregatorAddr,
       "os10bgp4V2NlriAsPathCalcLength": os10bgp4V2NlriAsPathCalcLength,
       "os10bgp4V2NlriAsPathString": os10bgp4V2NlriAsPathString,
       "os10bgp4V2NlriAsPath": os10bgp4V2NlriAsPath,
       "os10bgp4V2NlriPathAttrUnknown": os10bgp4V2NlriPathAttrUnknown,
       "os10bgp4V2AdjRibsOutTable": os10bgp4V2AdjRibsOutTable,
       "os10bgp4V2AdjRibsOutEntry": os10bgp4V2AdjRibsOutEntry,
       "os10bgp4V2AdjRibsOutIndex": os10bgp4V2AdjRibsOutIndex,
       "os10bgp4V2AdjRibsOutRoute": os10bgp4V2AdjRibsOutRoute,
       "os10bgp4V2Conformance": os10bgp4V2Conformance}
)
