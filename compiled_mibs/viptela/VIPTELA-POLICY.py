# SNMP MIB module (VIPTELA-POLICY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-POLICY
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:08 2025
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

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_policy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8)
)
if mibBuilder.loadTexts:
    viptela_policy.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Ipv4Prefix(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d/1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5



class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class SourcePort(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class DestinationIp(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Protocol(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Dscp1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class TcpFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("syn", 0)
    )


class DestinationIp1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class SourceIp(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Protocol1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Protocol2(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Protocol3(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Protocol4(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Protocol5(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class DestinationPort1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Community1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class DestinationPort2(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class DestinationPort3(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class DestinationPort4(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class DestinationPort5(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class PacketLength(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class TransportProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("transport-tcp", 0),
          ("transport-udp", 1))
    )



class ActionDataEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("drop", 1))
    )



class BgpOriginEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egp", 0),
          ("igp", 1),
          ("incomplete", 2))
    )



class Dscp(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class ActionEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accept", 0),
          ("reject", 1))
    )



class PacketLength1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class PacketLength2(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class PacketLength3(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Community(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class DataPolicyDirectionEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("from-service", 0),
          ("from-tunnel", 1),
          ("all", 2))
    )



class SourcePort1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class SourcePort2(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class SourcePort3(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class SourcePort4(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class SourcePort5(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class DirectionEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 0),
          ("out", 1))
    )



class SourceIp1(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class DestinationPort(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class ColorList(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class EncapsulationList(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class LossProtectEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fec-adaptive", 1),
          ("fec-always", 2),
          ("pkt-dup", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Policy_ObjectIdentity = ObjectIdentity
policy = _Policy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4)
)
_PolicyDataPolicyFilter_ObjectIdentity = ObjectIdentity
policyDataPolicyFilter = _PolicyDataPolicyFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1)
)
_PolicyDataPolicyFilterTable_Object = MibTable
policyDataPolicyFilterTable = _PolicyDataPolicyFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 1)
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterTable.setStatus("current")
_PolicyDataPolicyFilterEntry_Object = MibTableRow
policyDataPolicyFilterEntry = _PolicyDataPolicyFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 1, 1)
)
policyDataPolicyFilterEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyDataPolicyFilterName"),
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterEntry.setStatus("current")


class _PolicyDataPolicyFilterName_Type(String):
    """Custom type policyDataPolicyFilterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyDataPolicyFilterName_Type.__name__ = "String"
_PolicyDataPolicyFilterName_Object = MibTableColumn
policyDataPolicyFilterName = _PolicyDataPolicyFilterName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 1, 1, 1),
    _PolicyDataPolicyFilterName_Type()
)
policyDataPolicyFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterName.setStatus("current")
_PolicyDataPolicyFilterVpnlistTable_Object = MibTable
policyDataPolicyFilterVpnlistTable = _PolicyDataPolicyFilterVpnlistTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 2)
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistTable.setStatus("current")
_PolicyDataPolicyFilterVpnlistEntry_Object = MibTableRow
policyDataPolicyFilterVpnlistEntry = _PolicyDataPolicyFilterVpnlistEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 2, 1)
)
policyDataPolicyFilterVpnlistEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyDataPolicyFilterName"),
    (0, "VIPTELA-POLICY", "policyDataPolicyFilterVpnlistName"),
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistEntry.setStatus("current")


class _PolicyDataPolicyFilterVpnlistName_Type(String):
    """Custom type policyDataPolicyFilterVpnlistName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyDataPolicyFilterVpnlistName_Type.__name__ = "String"
_PolicyDataPolicyFilterVpnlistName_Object = MibTableColumn
policyDataPolicyFilterVpnlistName = _PolicyDataPolicyFilterVpnlistName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 2, 1, 1),
    _PolicyDataPolicyFilterVpnlistName_Type()
)
policyDataPolicyFilterVpnlistName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistName.setStatus("current")
_PolicyDataPolicyFilterVpnlistCounterTable_Object = MibTable
policyDataPolicyFilterVpnlistCounterTable = _PolicyDataPolicyFilterVpnlistCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 3)
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistCounterTable.setStatus("current")
_PolicyDataPolicyFilterVpnlistCounterEntry_Object = MibTableRow
policyDataPolicyFilterVpnlistCounterEntry = _PolicyDataPolicyFilterVpnlistCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 3, 1)
)
policyDataPolicyFilterVpnlistCounterEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyDataPolicyFilterName"),
    (0, "VIPTELA-POLICY", "policyDataPolicyFilterVpnlistName"),
    (0, "VIPTELA-POLICY", "policyDataPolicyFilterVpnlistCounterName"),
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistCounterEntry.setStatus("current")


class _PolicyDataPolicyFilterVpnlistCounterName_Type(String):
    """Custom type policyDataPolicyFilterVpnlistCounterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyDataPolicyFilterVpnlistCounterName_Type.__name__ = "String"
_PolicyDataPolicyFilterVpnlistCounterName_Object = MibTableColumn
policyDataPolicyFilterVpnlistCounterName = _PolicyDataPolicyFilterVpnlistCounterName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 3, 1, 1),
    _PolicyDataPolicyFilterVpnlistCounterName_Type()
)
policyDataPolicyFilterVpnlistCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistCounterName.setStatus("current")
_PolicyDataPolicyFilterVpnlistCounterPackets_Type = Counter64
_PolicyDataPolicyFilterVpnlistCounterPackets_Object = MibTableColumn
policyDataPolicyFilterVpnlistCounterPackets = _PolicyDataPolicyFilterVpnlistCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 3, 1, 2),
    _PolicyDataPolicyFilterVpnlistCounterPackets_Type()
)
policyDataPolicyFilterVpnlistCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistCounterPackets.setStatus("current")
_PolicyDataPolicyFilterVpnlistCounterBytes_Type = Counter64
_PolicyDataPolicyFilterVpnlistCounterBytes_Object = MibTableColumn
policyDataPolicyFilterVpnlistCounterBytes = _PolicyDataPolicyFilterVpnlistCounterBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 3, 1, 3),
    _PolicyDataPolicyFilterVpnlistCounterBytes_Type()
)
policyDataPolicyFilterVpnlistCounterBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistCounterBytes.setStatus("current")
_PolicyDataPolicyFilterVpnlistPolicerTable_Object = MibTable
policyDataPolicyFilterVpnlistPolicerTable = _PolicyDataPolicyFilterVpnlistPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 4)
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistPolicerTable.setStatus("current")
_PolicyDataPolicyFilterVpnlistPolicerEntry_Object = MibTableRow
policyDataPolicyFilterVpnlistPolicerEntry = _PolicyDataPolicyFilterVpnlistPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 4, 1)
)
policyDataPolicyFilterVpnlistPolicerEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyDataPolicyFilterName"),
    (0, "VIPTELA-POLICY", "policyDataPolicyFilterVpnlistName"),
    (0, "VIPTELA-POLICY", "policyDataPolicyFilterVpnlistPolicerName"),
)
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistPolicerEntry.setStatus("current")


class _PolicyDataPolicyFilterVpnlistPolicerName_Type(String):
    """Custom type policyDataPolicyFilterVpnlistPolicerName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PolicyDataPolicyFilterVpnlistPolicerName_Type.__name__ = "String"
_PolicyDataPolicyFilterVpnlistPolicerName_Object = MibTableColumn
policyDataPolicyFilterVpnlistPolicerName = _PolicyDataPolicyFilterVpnlistPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 4, 1, 1),
    _PolicyDataPolicyFilterVpnlistPolicerName_Type()
)
policyDataPolicyFilterVpnlistPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistPolicerName.setStatus("current")
_PolicyDataPolicyFilterVpnlistPolicerOosPackets_Type = Counter64
_PolicyDataPolicyFilterVpnlistPolicerOosPackets_Object = MibTableColumn
policyDataPolicyFilterVpnlistPolicerOosPackets = _PolicyDataPolicyFilterVpnlistPolicerOosPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 4, 1, 2),
    _PolicyDataPolicyFilterVpnlistPolicerOosPackets_Type()
)
policyDataPolicyFilterVpnlistPolicerOosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistPolicerOosPackets.setStatus("current")
_PolicyDataPolicyFilterVpnlistPolicerOosBytes_Type = Counter64
_PolicyDataPolicyFilterVpnlistPolicerOosBytes_Object = MibTableColumn
policyDataPolicyFilterVpnlistPolicerOosBytes = _PolicyDataPolicyFilterVpnlistPolicerOosBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 1, 4, 1, 3),
    _PolicyDataPolicyFilterVpnlistPolicerOosBytes_Type()
)
policyDataPolicyFilterVpnlistPolicerOosBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDataPolicyFilterVpnlistPolicerOosBytes.setStatus("current")
_PolicyAppRoutePolicy_ObjectIdentity = ObjectIdentity
policyAppRoutePolicy = _PolicyAppRoutePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2)
)
_PolicyAppRoutePolicyFilterTable_Object = MibTable
policyAppRoutePolicyFilterTable = _PolicyAppRoutePolicyFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 1)
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterTable.setStatus("current")
_PolicyAppRoutePolicyFilterEntry_Object = MibTableRow
policyAppRoutePolicyFilterEntry = _PolicyAppRoutePolicyFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 1, 1)
)
policyAppRoutePolicyFilterEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyAppRoutePolicyFilterName"),
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterEntry.setStatus("current")


class _PolicyAppRoutePolicyFilterName_Type(String):
    """Custom type policyAppRoutePolicyFilterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyAppRoutePolicyFilterName_Type.__name__ = "String"
_PolicyAppRoutePolicyFilterName_Object = MibTableColumn
policyAppRoutePolicyFilterName = _PolicyAppRoutePolicyFilterName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 1, 1, 1),
    _PolicyAppRoutePolicyFilterName_Type()
)
policyAppRoutePolicyFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterName.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistTable_Object = MibTable
policyAppRoutePolicyFilterVpnlistTable = _PolicyAppRoutePolicyFilterVpnlistTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 2)
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistTable.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistEntry_Object = MibTableRow
policyAppRoutePolicyFilterVpnlistEntry = _PolicyAppRoutePolicyFilterVpnlistEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 2, 1)
)
policyAppRoutePolicyFilterVpnlistEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyAppRoutePolicyFilterName"),
    (0, "VIPTELA-POLICY", "policyAppRoutePolicyFilterVpnlistName"),
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistEntry.setStatus("current")


class _PolicyAppRoutePolicyFilterVpnlistName_Type(String):
    """Custom type policyAppRoutePolicyFilterVpnlistName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyAppRoutePolicyFilterVpnlistName_Type.__name__ = "String"
_PolicyAppRoutePolicyFilterVpnlistName_Object = MibTableColumn
policyAppRoutePolicyFilterVpnlistName = _PolicyAppRoutePolicyFilterVpnlistName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 2, 1, 1),
    _PolicyAppRoutePolicyFilterVpnlistName_Type()
)
policyAppRoutePolicyFilterVpnlistName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistName.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistCounterTable_Object = MibTable
policyAppRoutePolicyFilterVpnlistCounterTable = _PolicyAppRoutePolicyFilterVpnlistCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 3)
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistCounterTable.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistCounterEntry_Object = MibTableRow
policyAppRoutePolicyFilterVpnlistCounterEntry = _PolicyAppRoutePolicyFilterVpnlistCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 3, 1)
)
policyAppRoutePolicyFilterVpnlistCounterEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyAppRoutePolicyFilterName"),
    (0, "VIPTELA-POLICY", "policyAppRoutePolicyFilterVpnlistName"),
    (0, "VIPTELA-POLICY", "policyAppRoutePolicyFilterVpnlistCounterName"),
)
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistCounterEntry.setStatus("current")


class _PolicyAppRoutePolicyFilterVpnlistCounterName_Type(String):
    """Custom type policyAppRoutePolicyFilterVpnlistCounterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyAppRoutePolicyFilterVpnlistCounterName_Type.__name__ = "String"
_PolicyAppRoutePolicyFilterVpnlistCounterName_Object = MibTableColumn
policyAppRoutePolicyFilterVpnlistCounterName = _PolicyAppRoutePolicyFilterVpnlistCounterName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 3, 1, 1),
    _PolicyAppRoutePolicyFilterVpnlistCounterName_Type()
)
policyAppRoutePolicyFilterVpnlistCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistCounterName.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistCounterPackets_Type = Counter64
_PolicyAppRoutePolicyFilterVpnlistCounterPackets_Object = MibTableColumn
policyAppRoutePolicyFilterVpnlistCounterPackets = _PolicyAppRoutePolicyFilterVpnlistCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 3, 1, 2),
    _PolicyAppRoutePolicyFilterVpnlistCounterPackets_Type()
)
policyAppRoutePolicyFilterVpnlistCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistCounterPackets.setStatus("current")
_PolicyAppRoutePolicyFilterVpnlistCounterBytes_Type = Counter64
_PolicyAppRoutePolicyFilterVpnlistCounterBytes_Object = MibTableColumn
policyAppRoutePolicyFilterVpnlistCounterBytes = _PolicyAppRoutePolicyFilterVpnlistCounterBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 2, 3, 1, 3),
    _PolicyAppRoutePolicyFilterVpnlistCounterBytes_Type()
)
policyAppRoutePolicyFilterVpnlistCounterBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAppRoutePolicyFilterVpnlistCounterBytes.setStatus("current")
_PolicyAccessListNames_ObjectIdentity = ObjectIdentity
policyAccessListNames = _PolicyAccessListNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 3)
)
_PolicyAccessListNamesTable_Object = MibTable
policyAccessListNamesTable = _PolicyAccessListNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 3, 1)
)
if mibBuilder.loadTexts:
    policyAccessListNamesTable.setStatus("current")
_PolicyAccessListNamesEntry_Object = MibTableRow
policyAccessListNamesEntry = _PolicyAccessListNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 3, 1, 1)
)
policyAccessListNamesEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyAccessListNamesName"),
)
if mibBuilder.loadTexts:
    policyAccessListNamesEntry.setStatus("current")


class _PolicyAccessListNamesName_Type(String):
    """Custom type policyAccessListNamesName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyAccessListNamesName_Type.__name__ = "String"
_PolicyAccessListNamesName_Object = MibTableColumn
policyAccessListNamesName = _PolicyAccessListNamesName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 3, 1, 1, 1),
    _PolicyAccessListNamesName_Type()
)
policyAccessListNamesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListNamesName.setStatus("current")
_PolicyAccessListCounters_ObjectIdentity = ObjectIdentity
policyAccessListCounters = _PolicyAccessListCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 4)
)
_PolicyAccessListCountersTable_Object = MibTable
policyAccessListCountersTable = _PolicyAccessListCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 4, 1)
)
if mibBuilder.loadTexts:
    policyAccessListCountersTable.setStatus("current")
_PolicyAccessListCountersEntry_Object = MibTableRow
policyAccessListCountersEntry = _PolicyAccessListCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 4, 1, 1)
)
policyAccessListCountersEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyAccessListCountersName"),
)
if mibBuilder.loadTexts:
    policyAccessListCountersEntry.setStatus("current")


class _PolicyAccessListCountersName_Type(String):
    """Custom type policyAccessListCountersName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyAccessListCountersName_Type.__name__ = "String"
_PolicyAccessListCountersName_Object = MibTableColumn
policyAccessListCountersName = _PolicyAccessListCountersName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 4, 1, 1, 1),
    _PolicyAccessListCountersName_Type()
)
policyAccessListCountersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListCountersName.setStatus("current")
_PolicyAccessListCountersAccessPolicyCounterListTable_Object = MibTable
policyAccessListCountersAccessPolicyCounterListTable = _PolicyAccessListCountersAccessPolicyCounterListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 4, 2)
)
if mibBuilder.loadTexts:
    policyAccessListCountersAccessPolicyCounterListTable.setStatus("current")
_PolicyAccessListCountersAccessPolicyCounterListEntry_Object = MibTableRow
policyAccessListCountersAccessPolicyCounterListEntry = _PolicyAccessListCountersAccessPolicyCounterListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 4, 2, 1)
)
policyAccessListCountersAccessPolicyCounterListEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyAccessListCountersName"),
    (0, "VIPTELA-POLICY", "policyAccessListCountersAccessPolicyCounterListCounterName"),
)
if mibBuilder.loadTexts:
    policyAccessListCountersAccessPolicyCounterListEntry.setStatus("current")


class _PolicyAccessListCountersAccessPolicyCounterListCounterName_Type(String):
    """Custom type policyAccessListCountersAccessPolicyCounterListCounterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyAccessListCountersAccessPolicyCounterListCounterName_Type.__name__ = "String"
_PolicyAccessListCountersAccessPolicyCounterListCounterName_Object = MibTableColumn
policyAccessListCountersAccessPolicyCounterListCounterName = _PolicyAccessListCountersAccessPolicyCounterListCounterName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 4, 2, 1, 1),
    _PolicyAccessListCountersAccessPolicyCounterListCounterName_Type()
)
policyAccessListCountersAccessPolicyCounterListCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyAccessListCountersAccessPolicyCounterListCounterName.setStatus("current")
_PolicyAccessListCountersAccessPolicyCounterListPackets_Type = Counter64
_PolicyAccessListCountersAccessPolicyCounterListPackets_Object = MibTableColumn
policyAccessListCountersAccessPolicyCounterListPackets = _PolicyAccessListCountersAccessPolicyCounterListPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 4, 2, 1, 2),
    _PolicyAccessListCountersAccessPolicyCounterListPackets_Type()
)
policyAccessListCountersAccessPolicyCounterListPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListCountersAccessPolicyCounterListPackets.setStatus("current")
_PolicyAccessListCountersAccessPolicyCounterListBytes_Type = Counter64
_PolicyAccessListCountersAccessPolicyCounterListBytes_Object = MibTableColumn
policyAccessListCountersAccessPolicyCounterListBytes = _PolicyAccessListCountersAccessPolicyCounterListBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 4, 2, 1, 3),
    _PolicyAccessListCountersAccessPolicyCounterListBytes_Type()
)
policyAccessListCountersAccessPolicyCounterListBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListCountersAccessPolicyCounterListBytes.setStatus("current")
_PolicyAccessListPolicers_ObjectIdentity = ObjectIdentity
policyAccessListPolicers = _PolicyAccessListPolicers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 5)
)
_PolicyAccessListPolicersTable_Object = MibTable
policyAccessListPolicersTable = _PolicyAccessListPolicersTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 5, 1)
)
if mibBuilder.loadTexts:
    policyAccessListPolicersTable.setStatus("current")
_PolicyAccessListPolicersEntry_Object = MibTableRow
policyAccessListPolicersEntry = _PolicyAccessListPolicersEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 5, 1, 1)
)
policyAccessListPolicersEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyAccessListPolicersName"),
)
if mibBuilder.loadTexts:
    policyAccessListPolicersEntry.setStatus("current")


class _PolicyAccessListPolicersName_Type(String):
    """Custom type policyAccessListPolicersName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyAccessListPolicersName_Type.__name__ = "String"
_PolicyAccessListPolicersName_Object = MibTableColumn
policyAccessListPolicersName = _PolicyAccessListPolicersName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 5, 1, 1, 1),
    _PolicyAccessListPolicersName_Type()
)
policyAccessListPolicersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListPolicersName.setStatus("current")
_PolicyAccessListPolicersAccessPolicyPolicerListTable_Object = MibTable
policyAccessListPolicersAccessPolicyPolicerListTable = _PolicyAccessListPolicersAccessPolicyPolicerListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 5, 2)
)
if mibBuilder.loadTexts:
    policyAccessListPolicersAccessPolicyPolicerListTable.setStatus("current")
_PolicyAccessListPolicersAccessPolicyPolicerListEntry_Object = MibTableRow
policyAccessListPolicersAccessPolicyPolicerListEntry = _PolicyAccessListPolicersAccessPolicyPolicerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 5, 2, 1)
)
policyAccessListPolicersAccessPolicyPolicerListEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyAccessListPolicersName"),
    (0, "VIPTELA-POLICY", "policyAccessListPolicersAccessPolicyPolicerListPolicerName"),
)
if mibBuilder.loadTexts:
    policyAccessListPolicersAccessPolicyPolicerListEntry.setStatus("current")


class _PolicyAccessListPolicersAccessPolicyPolicerListPolicerName_Type(String):
    """Custom type policyAccessListPolicersAccessPolicyPolicerListPolicerName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PolicyAccessListPolicersAccessPolicyPolicerListPolicerName_Type.__name__ = "String"
_PolicyAccessListPolicersAccessPolicyPolicerListPolicerName_Object = MibTableColumn
policyAccessListPolicersAccessPolicyPolicerListPolicerName = _PolicyAccessListPolicersAccessPolicyPolicerListPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 5, 2, 1, 1),
    _PolicyAccessListPolicersAccessPolicyPolicerListPolicerName_Type()
)
policyAccessListPolicersAccessPolicyPolicerListPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyAccessListPolicersAccessPolicyPolicerListPolicerName.setStatus("current")
_PolicyAccessListPolicersAccessPolicyPolicerListOosPackets_Type = Counter64
_PolicyAccessListPolicersAccessPolicyPolicerListOosPackets_Object = MibTableColumn
policyAccessListPolicersAccessPolicyPolicerListOosPackets = _PolicyAccessListPolicersAccessPolicyPolicerListOosPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 5, 2, 1, 2),
    _PolicyAccessListPolicersAccessPolicyPolicerListOosPackets_Type()
)
policyAccessListPolicersAccessPolicyPolicerListOosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListPolicersAccessPolicyPolicerListOosPackets.setStatus("current")
_PolicyAccessListPolicersAccessPolicyPolicerListOosBytes_Type = Counter64
_PolicyAccessListPolicersAccessPolicyPolicerListOosBytes_Object = MibTableColumn
policyAccessListPolicersAccessPolicyPolicerListOosBytes = _PolicyAccessListPolicersAccessPolicyPolicerListOosBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 5, 2, 1, 3),
    _PolicyAccessListPolicersAccessPolicyPolicerListOosBytes_Type()
)
policyAccessListPolicersAccessPolicyPolicerListOosBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListPolicersAccessPolicyPolicerListOosBytes.setStatus("current")
_PolicyQosSchedulerInfo_ObjectIdentity = ObjectIdentity
policyQosSchedulerInfo = _PolicyQosSchedulerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 6)
)
_PolicyQosSchedulerInfoTable_Object = MibTable
policyQosSchedulerInfoTable = _PolicyQosSchedulerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 6, 1)
)
if mibBuilder.loadTexts:
    policyQosSchedulerInfoTable.setStatus("current")
_PolicyQosSchedulerInfoEntry_Object = MibTableRow
policyQosSchedulerInfoEntry = _PolicyQosSchedulerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 6, 1, 1)
)
policyQosSchedulerInfoEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyQosSchedulerInfoQosSchedulerName"),
)
if mibBuilder.loadTexts:
    policyQosSchedulerInfoEntry.setStatus("current")


class _PolicyQosSchedulerInfoQosSchedulerName_Type(String):
    """Custom type policyQosSchedulerInfoQosSchedulerName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyQosSchedulerInfoQosSchedulerName_Type.__name__ = "String"
_PolicyQosSchedulerInfoQosSchedulerName_Object = MibTableColumn
policyQosSchedulerInfoQosSchedulerName = _PolicyQosSchedulerInfoQosSchedulerName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 6, 1, 1, 1),
    _PolicyQosSchedulerInfoQosSchedulerName_Type()
)
policyQosSchedulerInfoQosSchedulerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyQosSchedulerInfoQosSchedulerName.setStatus("current")
_PolicyQosSchedulerInfoBandwidthPercent_Type = Unsigned32
_PolicyQosSchedulerInfoBandwidthPercent_Object = MibTableColumn
policyQosSchedulerInfoBandwidthPercent = _PolicyQosSchedulerInfoBandwidthPercent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 6, 1, 1, 2),
    _PolicyQosSchedulerInfoBandwidthPercent_Type()
)
policyQosSchedulerInfoBandwidthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyQosSchedulerInfoBandwidthPercent.setStatus("current")
_PolicyQosSchedulerInfoBufferPercent_Type = Unsigned32
_PolicyQosSchedulerInfoBufferPercent_Object = MibTableColumn
policyQosSchedulerInfoBufferPercent = _PolicyQosSchedulerInfoBufferPercent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 6, 1, 1, 3),
    _PolicyQosSchedulerInfoBufferPercent_Type()
)
policyQosSchedulerInfoBufferPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyQosSchedulerInfoBufferPercent.setStatus("current")
_PolicyQosSchedulerInfoQueue_Type = Integer32
_PolicyQosSchedulerInfoQueue_Object = MibTableColumn
policyQosSchedulerInfoQueue = _PolicyQosSchedulerInfoQueue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 6, 1, 1, 4),
    _PolicyQosSchedulerInfoQueue_Type()
)
policyQosSchedulerInfoQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyQosSchedulerInfoQueue.setStatus("current")
_PolicyQosSchedulerInfoQosSchedulerMapAssociationTable_Object = MibTable
policyQosSchedulerInfoQosSchedulerMapAssociationTable = _PolicyQosSchedulerInfoQosSchedulerMapAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 6, 2)
)
if mibBuilder.loadTexts:
    policyQosSchedulerInfoQosSchedulerMapAssociationTable.setStatus("current")
_PolicyQosSchedulerInfoQosSchedulerMapAssociationEntry_Object = MibTableRow
policyQosSchedulerInfoQosSchedulerMapAssociationEntry = _PolicyQosSchedulerInfoQosSchedulerMapAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 6, 2, 1)
)
policyQosSchedulerInfoQosSchedulerMapAssociationEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyQosSchedulerInfoQosSchedulerName"),
    (0, "VIPTELA-POLICY", "policyQosSchedulerInfoQosSchedulerMapAssociationQosMapName"),
)
if mibBuilder.loadTexts:
    policyQosSchedulerInfoQosSchedulerMapAssociationEntry.setStatus("current")


class _PolicyQosSchedulerInfoQosSchedulerMapAssociationQosMapName_Type(String):
    """Custom type policyQosSchedulerInfoQosSchedulerMapAssociationQosMapName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyQosSchedulerInfoQosSchedulerMapAssociationQosMapName_Type.__name__ = "String"
_PolicyQosSchedulerInfoQosSchedulerMapAssociationQosMapName_Object = MibTableColumn
policyQosSchedulerInfoQosSchedulerMapAssociationQosMapName = _PolicyQosSchedulerInfoQosSchedulerMapAssociationQosMapName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 6, 2, 1, 1),
    _PolicyQosSchedulerInfoQosSchedulerMapAssociationQosMapName_Type()
)
policyQosSchedulerInfoQosSchedulerMapAssociationQosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyQosSchedulerInfoQosSchedulerMapAssociationQosMapName.setStatus("current")
_PolicyQosMapInfo_ObjectIdentity = ObjectIdentity
policyQosMapInfo = _PolicyQosMapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 7)
)
_PolicyQosMapInfoTable_Object = MibTable
policyQosMapInfoTable = _PolicyQosMapInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 7, 1)
)
if mibBuilder.loadTexts:
    policyQosMapInfoTable.setStatus("current")
_PolicyQosMapInfoEntry_Object = MibTableRow
policyQosMapInfoEntry = _PolicyQosMapInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 7, 1, 1)
)
policyQosMapInfoEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyQosMapInfoQosMapName"),
)
if mibBuilder.loadTexts:
    policyQosMapInfoEntry.setStatus("current")


class _PolicyQosMapInfoQosMapName_Type(String):
    """Custom type policyQosMapInfoQosMapName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyQosMapInfoQosMapName_Type.__name__ = "String"
_PolicyQosMapInfoQosMapName_Object = MibTableColumn
policyQosMapInfoQosMapName = _PolicyQosMapInfoQosMapName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 7, 1, 1, 1),
    _PolicyQosMapInfoQosMapName_Type()
)
policyQosMapInfoQosMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyQosMapInfoQosMapName.setStatus("current")
_PolicyQosMapInfoQosMapInterfaceAssociationsTable_Object = MibTable
policyQosMapInfoQosMapInterfaceAssociationsTable = _PolicyQosMapInfoQosMapInterfaceAssociationsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 7, 2)
)
if mibBuilder.loadTexts:
    policyQosMapInfoQosMapInterfaceAssociationsTable.setStatus("current")
_PolicyQosMapInfoQosMapInterfaceAssociationsEntry_Object = MibTableRow
policyQosMapInfoQosMapInterfaceAssociationsEntry = _PolicyQosMapInfoQosMapInterfaceAssociationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 7, 2, 1)
)
policyQosMapInfoQosMapInterfaceAssociationsEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyQosMapInfoQosMapName"),
    (0, "VIPTELA-POLICY", "policyQosMapInfoQosMapInterfaceAssociationsInterfaceName"),
)
if mibBuilder.loadTexts:
    policyQosMapInfoQosMapInterfaceAssociationsEntry.setStatus("current")


class _PolicyQosMapInfoQosMapInterfaceAssociationsInterfaceName_Type(String):
    """Custom type policyQosMapInfoQosMapInterfaceAssociationsInterfaceName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyQosMapInfoQosMapInterfaceAssociationsInterfaceName_Type.__name__ = "String"
_PolicyQosMapInfoQosMapInterfaceAssociationsInterfaceName_Object = MibTableColumn
policyQosMapInfoQosMapInterfaceAssociationsInterfaceName = _PolicyQosMapInfoQosMapInterfaceAssociationsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 7, 2, 1, 1),
    _PolicyQosMapInfoQosMapInterfaceAssociationsInterfaceName_Type()
)
policyQosMapInfoQosMapInterfaceAssociationsInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyQosMapInfoQosMapInterfaceAssociationsInterfaceName.setStatus("current")
_PolicyAccessListAssociations_ObjectIdentity = ObjectIdentity
policyAccessListAssociations = _PolicyAccessListAssociations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 8)
)
_PolicyAccessListAssociationsTable_Object = MibTable
policyAccessListAssociationsTable = _PolicyAccessListAssociationsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 8, 1)
)
if mibBuilder.loadTexts:
    policyAccessListAssociationsTable.setStatus("current")
_PolicyAccessListAssociationsEntry_Object = MibTableRow
policyAccessListAssociationsEntry = _PolicyAccessListAssociationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 8, 1, 1)
)
policyAccessListAssociationsEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyAccessListAssociationsName"),
)
if mibBuilder.loadTexts:
    policyAccessListAssociationsEntry.setStatus("current")


class _PolicyAccessListAssociationsName_Type(String):
    """Custom type policyAccessListAssociationsName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyAccessListAssociationsName_Type.__name__ = "String"
_PolicyAccessListAssociationsName_Object = MibTableColumn
policyAccessListAssociationsName = _PolicyAccessListAssociationsName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 8, 1, 1, 1),
    _PolicyAccessListAssociationsName_Type()
)
policyAccessListAssociationsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListAssociationsName.setStatus("current")
_PolicyAccessListAssociationsAccessPolicyInterfaceListTable_Object = MibTable
policyAccessListAssociationsAccessPolicyInterfaceListTable = _PolicyAccessListAssociationsAccessPolicyInterfaceListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 8, 2)
)
if mibBuilder.loadTexts:
    policyAccessListAssociationsAccessPolicyInterfaceListTable.setStatus("current")
_PolicyAccessListAssociationsAccessPolicyInterfaceListEntry_Object = MibTableRow
policyAccessListAssociationsAccessPolicyInterfaceListEntry = _PolicyAccessListAssociationsAccessPolicyInterfaceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 8, 2, 1)
)
policyAccessListAssociationsAccessPolicyInterfaceListEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyAccessListAssociationsName"),
    (0, "VIPTELA-POLICY", "policyAccessListAssociationsAccessPolicyInterfaceListIntName"),
    (0, "VIPTELA-POLICY", "policyAccessListAssociationsAccessPolicyInterfaceListIntDir"),
)
if mibBuilder.loadTexts:
    policyAccessListAssociationsAccessPolicyInterfaceListEntry.setStatus("current")


class _PolicyAccessListAssociationsAccessPolicyInterfaceListIntName_Type(String):
    """Custom type policyAccessListAssociationsAccessPolicyInterfaceListIntName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyAccessListAssociationsAccessPolicyInterfaceListIntName_Type.__name__ = "String"
_PolicyAccessListAssociationsAccessPolicyInterfaceListIntName_Object = MibTableColumn
policyAccessListAssociationsAccessPolicyInterfaceListIntName = _PolicyAccessListAssociationsAccessPolicyInterfaceListIntName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 8, 2, 1, 1),
    _PolicyAccessListAssociationsAccessPolicyInterfaceListIntName_Type()
)
policyAccessListAssociationsAccessPolicyInterfaceListIntName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyAccessListAssociationsAccessPolicyInterfaceListIntName.setStatus("current")
_PolicyAccessListAssociationsAccessPolicyInterfaceListIntDir_Type = DirectionEnum
_PolicyAccessListAssociationsAccessPolicyInterfaceListIntDir_Object = MibTableColumn
policyAccessListAssociationsAccessPolicyInterfaceListIntDir = _PolicyAccessListAssociationsAccessPolicyInterfaceListIntDir_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 8, 2, 1, 2),
    _PolicyAccessListAssociationsAccessPolicyInterfaceListIntDir_Type()
)
policyAccessListAssociationsAccessPolicyInterfaceListIntDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyAccessListAssociationsAccessPolicyInterfaceListIntDir.setStatus("current")
_PolicyRewriteAssociations_ObjectIdentity = ObjectIdentity
policyRewriteAssociations = _PolicyRewriteAssociations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 9)
)
_PolicyRewriteAssociationsTable_Object = MibTable
policyRewriteAssociationsTable = _PolicyRewriteAssociationsTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 9, 1)
)
if mibBuilder.loadTexts:
    policyRewriteAssociationsTable.setStatus("current")
_PolicyRewriteAssociationsEntry_Object = MibTableRow
policyRewriteAssociationsEntry = _PolicyRewriteAssociationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 9, 1, 1)
)
policyRewriteAssociationsEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyRewriteAssociationsName"),
)
if mibBuilder.loadTexts:
    policyRewriteAssociationsEntry.setStatus("current")


class _PolicyRewriteAssociationsName_Type(String):
    """Custom type policyRewriteAssociationsName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyRewriteAssociationsName_Type.__name__ = "String"
_PolicyRewriteAssociationsName_Object = MibTableColumn
policyRewriteAssociationsName = _PolicyRewriteAssociationsName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 9, 1, 1, 1),
    _PolicyRewriteAssociationsName_Type()
)
policyRewriteAssociationsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyRewriteAssociationsName.setStatus("current")
_PolicyRewriteAssociationsRewriteInterfaceListTable_Object = MibTable
policyRewriteAssociationsRewriteInterfaceListTable = _PolicyRewriteAssociationsRewriteInterfaceListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 9, 2)
)
if mibBuilder.loadTexts:
    policyRewriteAssociationsRewriteInterfaceListTable.setStatus("current")
_PolicyRewriteAssociationsRewriteInterfaceListEntry_Object = MibTableRow
policyRewriteAssociationsRewriteInterfaceListEntry = _PolicyRewriteAssociationsRewriteInterfaceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 9, 2, 1)
)
policyRewriteAssociationsRewriteInterfaceListEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyRewriteAssociationsName"),
    (0, "VIPTELA-POLICY", "policyRewriteAssociationsRewriteInterfaceListInterfaceName"),
)
if mibBuilder.loadTexts:
    policyRewriteAssociationsRewriteInterfaceListEntry.setStatus("current")


class _PolicyRewriteAssociationsRewriteInterfaceListInterfaceName_Type(String):
    """Custom type policyRewriteAssociationsRewriteInterfaceListInterfaceName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyRewriteAssociationsRewriteInterfaceListInterfaceName_Type.__name__ = "String"
_PolicyRewriteAssociationsRewriteInterfaceListInterfaceName_Object = MibTableColumn
policyRewriteAssociationsRewriteInterfaceListInterfaceName = _PolicyRewriteAssociationsRewriteInterfaceListInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 9, 2, 1, 1),
    _PolicyRewriteAssociationsRewriteInterfaceListInterfaceName_Type()
)
policyRewriteAssociationsRewriteInterfaceListInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyRewriteAssociationsRewriteInterfaceListInterfaceName.setStatus("current")
_PolicyFromVsmart_ObjectIdentity = ObjectIdentity
policyFromVsmart = _PolicyFromVsmart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10)
)
_PolicyFromVsmartSlaClassTable_Object = MibTable
policyFromVsmartSlaClassTable = _PolicyFromVsmartSlaClassTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 2)
)
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassTable.setStatus("current")
_PolicyFromVsmartSlaClassEntry_Object = MibTableRow
policyFromVsmartSlaClassEntry = _PolicyFromVsmartSlaClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 2, 1)
)
policyFromVsmartSlaClassEntry.setIndexNames(
    (1, "VIPTELA-POLICY", "policyFromVsmartSlaClassName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassEntry.setStatus("current")


class _PolicyFromVsmartSlaClassName_Type(String):
    """Custom type policyFromVsmartSlaClassName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartSlaClassName_Type.__name__ = "String"
_PolicyFromVsmartSlaClassName_Object = MibTableColumn
policyFromVsmartSlaClassName = _PolicyFromVsmartSlaClassName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 2, 1, 1),
    _PolicyFromVsmartSlaClassName_Type()
)
policyFromVsmartSlaClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassName.setStatus("current")


class _PolicyFromVsmartSlaClassLoss_Type(UnsignedByte):
    """Custom type policyFromVsmartSlaClassLoss based on UnsignedByte"""
    subtypeSpec = UnsignedByte.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PolicyFromVsmartSlaClassLoss_Type.__name__ = "UnsignedByte"
_PolicyFromVsmartSlaClassLoss_Object = MibTableColumn
policyFromVsmartSlaClassLoss = _PolicyFromVsmartSlaClassLoss_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 2, 1, 2),
    _PolicyFromVsmartSlaClassLoss_Type()
)
policyFromVsmartSlaClassLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassLoss.setStatus("current")


class _PolicyFromVsmartSlaClassLatency_Type(UnsignedShort):
    """Custom type policyFromVsmartSlaClassLatency based on UnsignedShort"""
    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PolicyFromVsmartSlaClassLatency_Type.__name__ = "UnsignedShort"
_PolicyFromVsmartSlaClassLatency_Object = MibTableColumn
policyFromVsmartSlaClassLatency = _PolicyFromVsmartSlaClassLatency_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 2, 1, 3),
    _PolicyFromVsmartSlaClassLatency_Type()
)
policyFromVsmartSlaClassLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassLatency.setStatus("current")


class _PolicyFromVsmartSlaClassJitter_Type(UnsignedShort):
    """Custom type policyFromVsmartSlaClassJitter based on UnsignedShort"""
    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PolicyFromVsmartSlaClassJitter_Type.__name__ = "UnsignedShort"
_PolicyFromVsmartSlaClassJitter_Object = MibTableColumn
policyFromVsmartSlaClassJitter = _PolicyFromVsmartSlaClassJitter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 2, 1, 4),
    _PolicyFromVsmartSlaClassJitter_Type()
)
policyFromVsmartSlaClassJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartSlaClassJitter.setStatus("current")
_PolicyFromVsmartDataPolicyTable_Object = MibTable
policyFromVsmartDataPolicyTable = _PolicyFromVsmartDataPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 3)
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyTable.setStatus("current")
_PolicyFromVsmartDataPolicyEntry_Object = MibTableRow
policyFromVsmartDataPolicyEntry = _PolicyFromVsmartDataPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 3, 1)
)
policyFromVsmartDataPolicyEntry.setIndexNames(
    (1, "VIPTELA-POLICY", "policyFromVsmartDataPolicyName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyEntry.setStatus("current")


class _PolicyFromVsmartDataPolicyName_Type(String):
    """Custom type policyFromVsmartDataPolicyName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyFromVsmartDataPolicyName_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyName_Object = MibTableColumn
policyFromVsmartDataPolicyName = _PolicyFromVsmartDataPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 3, 1, 1),
    _PolicyFromVsmartDataPolicyName_Type()
)
policyFromVsmartDataPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyName.setStatus("current")
_PolicyFromVsmartDataPolicyDirection_Type = DataPolicyDirectionEnum
_PolicyFromVsmartDataPolicyDirection_Object = MibTableColumn
policyFromVsmartDataPolicyDirection = _PolicyFromVsmartDataPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 3, 1, 2),
    _PolicyFromVsmartDataPolicyDirection_Type()
)
policyFromVsmartDataPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyDirection.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListTable_Object = MibTable
policyFromVsmartDataPolicyVpnListTable = _PolicyFromVsmartDataPolicyVpnListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 4)
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListTable.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListEntry_Object = MibTableRow
policyFromVsmartDataPolicyVpnListEntry = _PolicyFromVsmartDataPolicyVpnListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 4, 1)
)
policyFromVsmartDataPolicyVpnListEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyFromVsmartDataPolicyName"),
    (1, "VIPTELA-POLICY", "policyFromVsmartDataPolicyVpnListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListEntry.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListName_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListName_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListName_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListName = _PolicyFromVsmartDataPolicyVpnListName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 4, 1, 1),
    _PolicyFromVsmartDataPolicyVpnListName_Type()
)
policyFromVsmartDataPolicyVpnListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListName.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListDefaultAction_Type(ActionDataEnum):
    """Custom type policyFromVsmartDataPolicyVpnListDefaultAction based on ActionDataEnum"""
    defaultValue = 1


_PolicyFromVsmartDataPolicyVpnListDefaultAction_Type.__name__ = "ActionDataEnum"
_PolicyFromVsmartDataPolicyVpnListDefaultAction_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListDefaultAction = _PolicyFromVsmartDataPolicyVpnListDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 4, 1, 2),
    _PolicyFromVsmartDataPolicyVpnListDefaultAction_Type()
)
policyFromVsmartDataPolicyVpnListDefaultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListDefaultAction.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceTable_Object = MibTable
policyFromVsmartDataPolicyVpnListSequenceTable = _PolicyFromVsmartDataPolicyVpnListSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5)
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceTable.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceEntry_Object = MibTableRow
policyFromVsmartDataPolicyVpnListSequenceEntry = _PolicyFromVsmartDataPolicyVpnListSequenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1)
)
policyFromVsmartDataPolicyVpnListSequenceEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyFromVsmartDataPolicyName"),
    (0, "VIPTELA-POLICY", "policyFromVsmartDataPolicyVpnListName"),
    (0, "VIPTELA-POLICY", "policyFromVsmartDataPolicyVpnListSequenceSeqValue"),
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceEntry.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceSeqValue_Type(UnsignedShort):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceSeqValue based on UnsignedShort"""
    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceSeqValue_Type.__name__ = "UnsignedShort"
_PolicyFromVsmartDataPolicyVpnListSequenceSeqValue_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceSeqValue = _PolicyFromVsmartDataPolicyVpnListSequenceSeqValue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 1),
    _PolicyFromVsmartDataPolicyVpnListSequenceSeqValue_Type()
)
policyFromVsmartDataPolicyVpnListSequenceSeqValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceSeqValue.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst = _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 4),
    _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst_Type()
)
policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst = _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 5),
    _PolicyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst_Type()
)
policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst = _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 7),
    _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst_Type()
)
policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst = _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 8),
    _PolicyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst_Type()
)
policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceMatchTcp_Type = TcpFlags
_PolicyFromVsmartDataPolicyVpnListSequenceMatchTcp_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceMatchTcp = _PolicyFromVsmartDataPolicyVpnListSequenceMatchTcp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 10),
    _PolicyFromVsmartDataPolicyVpnListSequenceMatchTcp_Type()
)
policyFromVsmartDataPolicyVpnListSequenceMatchTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceMatchTcp.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionActionValue_Type(ActionDataEnum):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionActionValue based on ActionDataEnum"""
    defaultValue = 1


_PolicyFromVsmartDataPolicyVpnListSequenceActionActionValue_Type.__name__ = "ActionDataEnum"
_PolicyFromVsmartDataPolicyVpnListSequenceActionActionValue_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionActionValue = _PolicyFromVsmartDataPolicyVpnListSequenceActionActionValue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 11),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionActionValue_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionActionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionActionValue.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionCount_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionCount based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionCount_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceActionCount_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionCount = _PolicyFromVsmartDataPolicyVpnListSequenceActionCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 12),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionCount_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionCount.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn_Type = Unsigned32
_PolicyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn = _PolicyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 13),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionCflowd_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionCflowd_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionCflowd = _PolicyFromVsmartDataPolicyVpnListSequenceActionCflowd_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 14),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionCflowd_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionCflowd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionCflowd.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 15),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 16),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHop_Type = String
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHop_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 17),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHop_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetPolicer_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetPolicer_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetPolicer_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetPolicer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 18),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetPolicer_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpn_Type(Unsigned32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpn_Type.__name__ = "Unsigned32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpn_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetVpn = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 19),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpn_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetVpn.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel_Type = Unsigned32
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 20),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp_Type = InetAddressIP
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 21),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 22),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocList_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocList_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocList_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocList_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 23),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetTlocList_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType based on Integer32"""
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
        *(("fW", 1),
          ("iDS", 2),
          ("iDP", 3),
          ("netsvc1", 4),
          ("netsvc2", 5),
          ("netsvc3", 6),
          ("netsvc4", 7))
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 24),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn_Type(Unsigned32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn_Type.__name__ = "Unsigned32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 25),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp_Type = InetAddressIP
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 26),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 27),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst_Type(String):
    """Custom type policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst_Type.__name__ = "String"
_PolicyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst = _PolicyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 28),
    _PolicyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst_Type()
)
policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 29),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceRestrict_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceRestrict_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceRestrict = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceRestrict_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 30),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetServiceRestrict_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetServiceRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetServiceRestrict.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionLog_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionLog_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionLog = _PolicyFromVsmartDataPolicyVpnListSequenceActionLog_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 31),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionLog_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionLog.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListColor_Type = ColorList
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListColor_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListColor = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 32),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListColor_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListColor.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListEncap_Type = EncapsulationList
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListEncap_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListEncap = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 33),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListEncap_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListEncap.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListRestrict_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListRestrict_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListRestrict = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListRestrict_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 34),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListRestrict_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListRestrict.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization_Type = TruthValue
_PolicyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization = _PolicyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 35),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionLossProtect_Type = LossProtectEnum
_PolicyFromVsmartDataPolicyVpnListSequenceActionLossProtect_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionLossProtect = _PolicyFromVsmartDataPolicyVpnListSequenceActionLossProtect_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 36),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionLossProtect_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionLossProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionLossProtect.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6_Type = String
_PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6 = _PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 5, 1, 37),
    _PolicyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6_Type()
)
policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable_Object = MibTable
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 6)
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry_Object = MibTableRow
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 6, 1)
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyFromVsmartDataPolicyName"),
    (0, "VIPTELA-POLICY", "policyFromVsmartDataPolicyVpnListName"),
    (0, "VIPTELA-POLICY", "policyFromVsmartDataPolicyVpnListSequenceSeqValue"),
    (0, "VIPTELA-POLICY", "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum"),
)
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum_Type(Unsigned32):
    """Custom type policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum_Type.__name__ = "Unsigned32"
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 6, 1, 1),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl_Type = Unsigned32
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 6, 1, 2),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp_Type = InetAddressIP
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 6, 1, 3),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 6, 1, 4),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr.setStatus("current")


class _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn_Type(Integer32):
    """Custom type policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn_Type.__name__ = "Integer32"
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 6, 1, 5),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn.setStatus("current")
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf_Type = Unsigned32
_PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf_Object = MibTableColumn
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf = _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 6, 1, 6),
    _PolicyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf_Type()
)
policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf.setStatus("current")
_PolicyFromVsmartCflowdTemplateTable_Object = MibTable
policyFromVsmartCflowdTemplateTable = _PolicyFromVsmartCflowdTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 7)
)
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateTable.setStatus("current")
_PolicyFromVsmartCflowdTemplateEntry_Object = MibTableRow
policyFromVsmartCflowdTemplateEntry = _PolicyFromVsmartCflowdTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 7, 1)
)
policyFromVsmartCflowdTemplateEntry.setIndexNames(
    (1, "VIPTELA-POLICY", "policyFromVsmartCflowdTemplateName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateEntry.setStatus("current")


class _PolicyFromVsmartCflowdTemplateName_Type(String):
    """Custom type policyFromVsmartCflowdTemplateName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyFromVsmartCflowdTemplateName_Type.__name__ = "String"
_PolicyFromVsmartCflowdTemplateName_Object = MibTableColumn
policyFromVsmartCflowdTemplateName = _PolicyFromVsmartCflowdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 7, 1, 1),
    _PolicyFromVsmartCflowdTemplateName_Type()
)
policyFromVsmartCflowdTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateName.setStatus("current")


class _PolicyFromVsmartCflowdTemplateFlowActiveTimeout_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateFlowActiveTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_PolicyFromVsmartCflowdTemplateFlowActiveTimeout_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateFlowActiveTimeout_Object = MibTableColumn
policyFromVsmartCflowdTemplateFlowActiveTimeout = _PolicyFromVsmartCflowdTemplateFlowActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 7, 1, 2),
    _PolicyFromVsmartCflowdTemplateFlowActiveTimeout_Type()
)
policyFromVsmartCflowdTemplateFlowActiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateFlowActiveTimeout.setStatus("current")


class _PolicyFromVsmartCflowdTemplateFlowInactiveTimeout_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateFlowInactiveTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PolicyFromVsmartCflowdTemplateFlowInactiveTimeout_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateFlowInactiveTimeout_Object = MibTableColumn
policyFromVsmartCflowdTemplateFlowInactiveTimeout = _PolicyFromVsmartCflowdTemplateFlowInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 7, 1, 3),
    _PolicyFromVsmartCflowdTemplateFlowInactiveTimeout_Type()
)
policyFromVsmartCflowdTemplateFlowInactiveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateFlowInactiveTimeout.setStatus("current")


class _PolicyFromVsmartCflowdTemplateTemplateRefresh_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateTemplateRefresh based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_PolicyFromVsmartCflowdTemplateTemplateRefresh_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateTemplateRefresh_Object = MibTableColumn
policyFromVsmartCflowdTemplateTemplateRefresh = _PolicyFromVsmartCflowdTemplateTemplateRefresh_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 7, 1, 4),
    _PolicyFromVsmartCflowdTemplateTemplateRefresh_Type()
)
policyFromVsmartCflowdTemplateTemplateRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateTemplateRefresh.setStatus("current")


class _PolicyFromVsmartCflowdTemplateFlowSamplingInterval_Type(Unsigned32):
    """Custom type policyFromVsmartCflowdTemplateFlowSamplingInterval based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_PolicyFromVsmartCflowdTemplateFlowSamplingInterval_Type.__name__ = "Unsigned32"
_PolicyFromVsmartCflowdTemplateFlowSamplingInterval_Object = MibTableColumn
policyFromVsmartCflowdTemplateFlowSamplingInterval = _PolicyFromVsmartCflowdTemplateFlowSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 7, 1, 5),
    _PolicyFromVsmartCflowdTemplateFlowSamplingInterval_Type()
)
policyFromVsmartCflowdTemplateFlowSamplingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateFlowSamplingInterval.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorTable_Object = MibTable
policyFromVsmartCflowdTemplateCollectorTable = _PolicyFromVsmartCflowdTemplateCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 8)
)
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorTable.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorEntry_Object = MibTableRow
policyFromVsmartCflowdTemplateCollectorEntry = _PolicyFromVsmartCflowdTemplateCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 8, 1)
)
policyFromVsmartCflowdTemplateCollectorEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyFromVsmartCflowdTemplateName"),
    (0, "VIPTELA-POLICY", "policyFromVsmartCflowdTemplateCollectorVpn"),
    (0, "VIPTELA-POLICY", "policyFromVsmartCflowdTemplateCollectorAddress"),
    (0, "VIPTELA-POLICY", "policyFromVsmartCflowdTemplateCollectorPort"),
    (0, "VIPTELA-POLICY", "policyFromVsmartCflowdTemplateCollectorTransport"),
)
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorEntry.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorVpn_Type = ConfdString
_PolicyFromVsmartCflowdTemplateCollectorVpn_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorVpn = _PolicyFromVsmartCflowdTemplateCollectorVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 8, 1, 1),
    _PolicyFromVsmartCflowdTemplateCollectorVpn_Type()
)
policyFromVsmartCflowdTemplateCollectorVpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorVpn.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorAddress_Type = InetAddressIP
_PolicyFromVsmartCflowdTemplateCollectorAddress_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorAddress = _PolicyFromVsmartCflowdTemplateCollectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 8, 1, 2),
    _PolicyFromVsmartCflowdTemplateCollectorAddress_Type()
)
policyFromVsmartCflowdTemplateCollectorAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorAddress.setStatus("current")


class _PolicyFromVsmartCflowdTemplateCollectorPort_Type(UnsignedShort):
    """Custom type policyFromVsmartCflowdTemplateCollectorPort based on UnsignedShort"""
    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_PolicyFromVsmartCflowdTemplateCollectorPort_Type.__name__ = "UnsignedShort"
_PolicyFromVsmartCflowdTemplateCollectorPort_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorPort = _PolicyFromVsmartCflowdTemplateCollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 8, 1, 3),
    _PolicyFromVsmartCflowdTemplateCollectorPort_Type()
)
policyFromVsmartCflowdTemplateCollectorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorPort.setStatus("current")
_PolicyFromVsmartCflowdTemplateCollectorTransport_Type = TransportProtocol
_PolicyFromVsmartCflowdTemplateCollectorTransport_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorTransport = _PolicyFromVsmartCflowdTemplateCollectorTransport_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 8, 1, 4),
    _PolicyFromVsmartCflowdTemplateCollectorTransport_Type()
)
policyFromVsmartCflowdTemplateCollectorTransport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorTransport.setStatus("current")


class _PolicyFromVsmartCflowdTemplateCollectorSourceInterface_Type(String):
    """Custom type policyFromVsmartCflowdTemplateCollectorSourceInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartCflowdTemplateCollectorSourceInterface_Type.__name__ = "String"
_PolicyFromVsmartCflowdTemplateCollectorSourceInterface_Object = MibTableColumn
policyFromVsmartCflowdTemplateCollectorSourceInterface = _PolicyFromVsmartCflowdTemplateCollectorSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 8, 1, 5),
    _PolicyFromVsmartCflowdTemplateCollectorSourceInterface_Type()
)
policyFromVsmartCflowdTemplateCollectorSourceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartCflowdTemplateCollectorSourceInterface.setStatus("current")
_PolicyFromVsmartAppRoutePolicyTable_Object = MibTable
policyFromVsmartAppRoutePolicyTable = _PolicyFromVsmartAppRoutePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 9)
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyTable.setStatus("current")
_PolicyFromVsmartAppRoutePolicyEntry_Object = MibTableRow
policyFromVsmartAppRoutePolicyEntry = _PolicyFromVsmartAppRoutePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 9, 1)
)
policyFromVsmartAppRoutePolicyEntry.setIndexNames(
    (1, "VIPTELA-POLICY", "policyFromVsmartAppRoutePolicyName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyEntry.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyName_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyFromVsmartAppRoutePolicyName_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyName_Object = MibTableColumn
policyFromVsmartAppRoutePolicyName = _PolicyFromVsmartAppRoutePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 9, 1, 1),
    _PolicyFromVsmartAppRoutePolicyName_Type()
)
policyFromVsmartAppRoutePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyName.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListTable_Object = MibTable
policyFromVsmartAppRoutePolicyVpnListTable = _PolicyFromVsmartAppRoutePolicyVpnListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 10)
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListTable.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListEntry_Object = MibTableRow
policyFromVsmartAppRoutePolicyVpnListEntry = _PolicyFromVsmartAppRoutePolicyVpnListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 10, 1)
)
policyFromVsmartAppRoutePolicyVpnListEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyFromVsmartAppRoutePolicyName"),
    (1, "VIPTELA-POLICY", "policyFromVsmartAppRoutePolicyVpnListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListEntry.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListName_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListName_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListName_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListName = _PolicyFromVsmartAppRoutePolicyVpnListName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 10, 1, 1),
    _PolicyFromVsmartAppRoutePolicyVpnListName_Type()
)
policyFromVsmartAppRoutePolicyVpnListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListName.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListDefActSlaClassName_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListDefActSlaClassName_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListDefActSlaClassName_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName = _PolicyFromVsmartAppRoutePolicyVpnListDefActSlaClassName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 10, 1, 13),
    _PolicyFromVsmartAppRoutePolicyVpnListDefActSlaClassName_Type()
)
policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceTable_Object = MibTable
policyFromVsmartAppRoutePolicyVpnListSequenceTable = _PolicyFromVsmartAppRoutePolicyVpnListSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11)
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceTable.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceEntry_Object = MibTableRow
policyFromVsmartAppRoutePolicyVpnListSequenceEntry = _PolicyFromVsmartAppRoutePolicyVpnListSequenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1)
)
policyFromVsmartAppRoutePolicyVpnListSequenceEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyFromVsmartAppRoutePolicyName"),
    (0, "VIPTELA-POLICY", "policyFromVsmartAppRoutePolicyVpnListName"),
    (0, "VIPTELA-POLICY", "policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue"),
)
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceEntry.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceSeqValue_Type(UnsignedShort):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue based on UnsignedShort"""
    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65530),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceSeqValue_Type.__name__ = "UnsignedShort"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceSeqValue_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue = _PolicyFromVsmartAppRoutePolicyVpnListSequenceSeqValue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 1),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceSeqValue_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst = _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 4),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst = _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 5),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst = _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 7),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst = _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 8),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionCount_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceActionCount based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionCount_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionCount_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionCount = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 10),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionCount_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionCount.setStatus("current")


class _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName_Type(String):
    """Custom type policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName_Type.__name__ = "String"
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 11),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict_Type = TruthValue
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 12),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr_Type = ColorList
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 14),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionLog_Type = TruthValue
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionLog_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionLog = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionLog_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 15),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionLog_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionLog.setStatus("current")
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionBackupSlaPrefClr_Type = ColorList
_PolicyFromVsmartAppRoutePolicyVpnListSequenceActionBackupSlaPrefClr_Object = MibTableColumn
policyFromVsmartAppRoutePolicyVpnListSequenceActionBackupSlaPrefClr = _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionBackupSlaPrefClr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 11, 1, 16),
    _PolicyFromVsmartAppRoutePolicyVpnListSequenceActionBackupSlaPrefClr_Type()
)
policyFromVsmartAppRoutePolicyVpnListSequenceActionBackupSlaPrefClr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartAppRoutePolicyVpnListSequenceActionBackupSlaPrefClr.setStatus("current")
_PolicyFromVsmartPolicerTable_Object = MibTable
policyFromVsmartPolicerTable = _PolicyFromVsmartPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 12)
)
if mibBuilder.loadTexts:
    policyFromVsmartPolicerTable.setStatus("current")
_PolicyFromVsmartPolicerEntry_Object = MibTableRow
policyFromVsmartPolicerEntry = _PolicyFromVsmartPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 12, 1)
)
policyFromVsmartPolicerEntry.setIndexNames(
    (1, "VIPTELA-POLICY", "policyFromVsmartPolicerName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartPolicerEntry.setStatus("current")


class _PolicyFromVsmartPolicerName_Type(String):
    """Custom type policyFromVsmartPolicerName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartPolicerName_Type.__name__ = "String"
_PolicyFromVsmartPolicerName_Object = MibTableColumn
policyFromVsmartPolicerName = _PolicyFromVsmartPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 12, 1, 1),
    _PolicyFromVsmartPolicerName_Type()
)
policyFromVsmartPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartPolicerName.setStatus("current")
_PolicyFromVsmartPolicerRate_Type = Counter64
_PolicyFromVsmartPolicerRate_Object = MibTableColumn
policyFromVsmartPolicerRate = _PolicyFromVsmartPolicerRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 12, 1, 2),
    _PolicyFromVsmartPolicerRate_Type()
)
policyFromVsmartPolicerRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartPolicerRate.setStatus("current")


class _PolicyFromVsmartPolicerBurst_Type(Unsigned32):
    """Custom type policyFromVsmartPolicerBurst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 10000000),
    )


_PolicyFromVsmartPolicerBurst_Type.__name__ = "Unsigned32"
_PolicyFromVsmartPolicerBurst_Object = MibTableColumn
policyFromVsmartPolicerBurst = _PolicyFromVsmartPolicerBurst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 12, 1, 3),
    _PolicyFromVsmartPolicerBurst_Type()
)
policyFromVsmartPolicerBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartPolicerBurst.setStatus("current")


class _PolicyFromVsmartPolicerExceed_Type(Integer32):
    """Custom type policyFromVsmartPolicerExceed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("remark", 1))
    )


_PolicyFromVsmartPolicerExceed_Type.__name__ = "Integer32"
_PolicyFromVsmartPolicerExceed_Object = MibTableColumn
policyFromVsmartPolicerExceed = _PolicyFromVsmartPolicerExceed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 12, 1, 4),
    _PolicyFromVsmartPolicerExceed_Type()
)
policyFromVsmartPolicerExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartPolicerExceed.setStatus("current")
_PolicyFromVsmartListsVpnListTable_Object = MibTable
policyFromVsmartListsVpnListTable = _PolicyFromVsmartListsVpnListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 13)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListTable.setStatus("current")
_PolicyFromVsmartListsVpnListEntry_Object = MibTableRow
policyFromVsmartListsVpnListEntry = _PolicyFromVsmartListsVpnListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 13, 1)
)
policyFromVsmartListsVpnListEntry.setIndexNames(
    (1, "VIPTELA-POLICY", "policyFromVsmartListsVpnListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListEntry.setStatus("current")


class _PolicyFromVsmartListsVpnListName_Type(String):
    """Custom type policyFromVsmartListsVpnListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartListsVpnListName_Type.__name__ = "String"
_PolicyFromVsmartListsVpnListName_Object = MibTableColumn
policyFromVsmartListsVpnListName = _PolicyFromVsmartListsVpnListName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 13, 1, 1),
    _PolicyFromVsmartListsVpnListName_Type()
)
policyFromVsmartListsVpnListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListName.setStatus("current")
_PolicyFromVsmartListsVpnListVpnTable_Object = MibTable
policyFromVsmartListsVpnListVpnTable = _PolicyFromVsmartListsVpnListVpnTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 14)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListVpnTable.setStatus("current")
_PolicyFromVsmartListsVpnListVpnEntry_Object = MibTableRow
policyFromVsmartListsVpnListVpnEntry = _PolicyFromVsmartListsVpnListVpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 14, 1)
)
policyFromVsmartListsVpnListVpnEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyFromVsmartListsVpnListName"),
    (1, "VIPTELA-POLICY", "policyFromVsmartListsVpnListVpnId"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListVpnEntry.setStatus("current")


class _PolicyFromVsmartListsVpnListVpnId_Type(String):
    """Custom type policyFromVsmartListsVpnListVpnId based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartListsVpnListVpnId_Type.__name__ = "String"
_PolicyFromVsmartListsVpnListVpnId_Object = MibTableColumn
policyFromVsmartListsVpnListVpnId = _PolicyFromVsmartListsVpnListVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 14, 1, 1),
    _PolicyFromVsmartListsVpnListVpnId_Type()
)
policyFromVsmartListsVpnListVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsVpnListVpnId.setStatus("current")
_PolicyFromVsmartListsDataPrefixListTable_Object = MibTable
policyFromVsmartListsDataPrefixListTable = _PolicyFromVsmartListsDataPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 15)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListTable.setStatus("current")
_PolicyFromVsmartListsDataPrefixListEntry_Object = MibTableRow
policyFromVsmartListsDataPrefixListEntry = _PolicyFromVsmartListsDataPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 15, 1)
)
policyFromVsmartListsDataPrefixListEntry.setIndexNames(
    (1, "VIPTELA-POLICY", "policyFromVsmartListsDataPrefixListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListEntry.setStatus("current")


class _PolicyFromVsmartListsDataPrefixListName_Type(String):
    """Custom type policyFromVsmartListsDataPrefixListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartListsDataPrefixListName_Type.__name__ = "String"
_PolicyFromVsmartListsDataPrefixListName_Object = MibTableColumn
policyFromVsmartListsDataPrefixListName = _PolicyFromVsmartListsDataPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 15, 1, 1),
    _PolicyFromVsmartListsDataPrefixListName_Type()
)
policyFromVsmartListsDataPrefixListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListName.setStatus("current")
_PolicyFromVsmartListsDataPrefixListIpPrefixTable_Object = MibTable
policyFromVsmartListsDataPrefixListIpPrefixTable = _PolicyFromVsmartListsDataPrefixListIpPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 16)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListIpPrefixTable.setStatus("current")
_PolicyFromVsmartListsDataPrefixListIpPrefixEntry_Object = MibTableRow
policyFromVsmartListsDataPrefixListIpPrefixEntry = _PolicyFromVsmartListsDataPrefixListIpPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 16, 1)
)
policyFromVsmartListsDataPrefixListIpPrefixEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyFromVsmartListsDataPrefixListName"),
    (0, "VIPTELA-POLICY", "policyFromVsmartListsDataPrefixListIpPrefixIp"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListIpPrefixEntry.setStatus("current")
_PolicyFromVsmartListsDataPrefixListIpPrefixIp_Type = Ipv4Prefix
_PolicyFromVsmartListsDataPrefixListIpPrefixIp_Object = MibTableColumn
policyFromVsmartListsDataPrefixListIpPrefixIp = _PolicyFromVsmartListsDataPrefixListIpPrefixIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 16, 1, 1),
    _PolicyFromVsmartListsDataPrefixListIpPrefixIp_Type()
)
policyFromVsmartListsDataPrefixListIpPrefixIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsDataPrefixListIpPrefixIp.setStatus("current")
_PolicyFromVsmartListsTlocListTable_Object = MibTable
policyFromVsmartListsTlocListTable = _PolicyFromVsmartListsTlocListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 17)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTable.setStatus("current")
_PolicyFromVsmartListsTlocListEntry_Object = MibTableRow
policyFromVsmartListsTlocListEntry = _PolicyFromVsmartListsTlocListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 17, 1)
)
policyFromVsmartListsTlocListEntry.setIndexNames(
    (1, "VIPTELA-POLICY", "policyFromVsmartListsTlocListName"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListEntry.setStatus("current")


class _PolicyFromVsmartListsTlocListName_Type(String):
    """Custom type policyFromVsmartListsTlocListName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyFromVsmartListsTlocListName_Type.__name__ = "String"
_PolicyFromVsmartListsTlocListName_Object = MibTableColumn
policyFromVsmartListsTlocListName = _PolicyFromVsmartListsTlocListName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 17, 1, 1),
    _PolicyFromVsmartListsTlocListName_Type()
)
policyFromVsmartListsTlocListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListName.setStatus("current")
_PolicyFromVsmartListsTlocListTlocTable_Object = MibTable
policyFromVsmartListsTlocListTlocTable = _PolicyFromVsmartListsTlocListTlocTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 18)
)
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocTable.setStatus("current")
_PolicyFromVsmartListsTlocListTlocEntry_Object = MibTableRow
policyFromVsmartListsTlocListTlocEntry = _PolicyFromVsmartListsTlocListTlocEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 18, 1)
)
policyFromVsmartListsTlocListTlocEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyFromVsmartListsTlocListName"),
    (0, "VIPTELA-POLICY", "policyFromVsmartListsTlocListTlocIp"),
    (0, "VIPTELA-POLICY", "policyFromVsmartListsTlocListTlocColor"),
    (0, "VIPTELA-POLICY", "policyFromVsmartListsTlocListTlocEncap"),
)
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocEntry.setStatus("current")
_PolicyFromVsmartListsTlocListTlocIp_Type = InetAddressIP
_PolicyFromVsmartListsTlocListTlocIp_Object = MibTableColumn
policyFromVsmartListsTlocListTlocIp = _PolicyFromVsmartListsTlocListTlocIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 18, 1, 1),
    _PolicyFromVsmartListsTlocListTlocIp_Type()
)
policyFromVsmartListsTlocListTlocIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocIp.setStatus("current")


class _PolicyFromVsmartListsTlocListTlocColor_Type(Integer32):
    """Custom type policyFromVsmartListsTlocListTlocColor based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mpls", 2),
          ("metro-ethernet", 3),
          ("biz-internet", 4),
          ("public-internet", 5),
          ("lte", 6),
          ("threeG", 7),
          ("red", 8),
          ("green", 9),
          ("blue", 10),
          ("gold", 11),
          ("silver", 12),
          ("bronze", 13),
          ("custom1", 14),
          ("custom2", 15),
          ("custom3", 16),
          ("private1", 17),
          ("private2", 18),
          ("private3", 19),
          ("private4", 20),
          ("private5", 21),
          ("private6", 22))
    )


_PolicyFromVsmartListsTlocListTlocColor_Type.__name__ = "Integer32"
_PolicyFromVsmartListsTlocListTlocColor_Object = MibTableColumn
policyFromVsmartListsTlocListTlocColor = _PolicyFromVsmartListsTlocListTlocColor_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 18, 1, 2),
    _PolicyFromVsmartListsTlocListTlocColor_Type()
)
policyFromVsmartListsTlocListTlocColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocColor.setStatus("current")


class _PolicyFromVsmartListsTlocListTlocEncap_Type(Integer32):
    """Custom type policyFromVsmartListsTlocListTlocEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("ipsec", 2))
    )


_PolicyFromVsmartListsTlocListTlocEncap_Type.__name__ = "Integer32"
_PolicyFromVsmartListsTlocListTlocEncap_Object = MibTableColumn
policyFromVsmartListsTlocListTlocEncap = _PolicyFromVsmartListsTlocListTlocEncap_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 18, 1, 3),
    _PolicyFromVsmartListsTlocListTlocEncap_Type()
)
policyFromVsmartListsTlocListTlocEncap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocEncap.setStatus("current")
_PolicyFromVsmartListsTlocListTlocPreference_Type = Unsigned32
_PolicyFromVsmartListsTlocListTlocPreference_Object = MibTableColumn
policyFromVsmartListsTlocListTlocPreference = _PolicyFromVsmartListsTlocListTlocPreference_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 10, 18, 1, 4),
    _PolicyFromVsmartListsTlocListTlocPreference_Type()
)
policyFromVsmartListsTlocListTlocPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyFromVsmartListsTlocListTlocPreference.setStatus("current")
_PolicyDeviceAccessPolicyCounters_ObjectIdentity = ObjectIdentity
policyDeviceAccessPolicyCounters = _PolicyDeviceAccessPolicyCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 11)
)
_PolicyDeviceAccessPolicyCountersTable_Object = MibTable
policyDeviceAccessPolicyCountersTable = _PolicyDeviceAccessPolicyCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 11, 1)
)
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyCountersTable.setStatus("current")
_PolicyDeviceAccessPolicyCountersEntry_Object = MibTableRow
policyDeviceAccessPolicyCountersEntry = _PolicyDeviceAccessPolicyCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 11, 1, 1)
)
policyDeviceAccessPolicyCountersEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyDeviceAccessPolicyCountersName"),
)
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyCountersEntry.setStatus("current")


class _PolicyDeviceAccessPolicyCountersName_Type(String):
    """Custom type policyDeviceAccessPolicyCountersName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyDeviceAccessPolicyCountersName_Type.__name__ = "String"
_PolicyDeviceAccessPolicyCountersName_Object = MibTableColumn
policyDeviceAccessPolicyCountersName = _PolicyDeviceAccessPolicyCountersName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 11, 1, 1, 1),
    _PolicyDeviceAccessPolicyCountersName_Type()
)
policyDeviceAccessPolicyCountersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyCountersName.setStatus("current")
_PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListTable_Object = MibTable
policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListTable = _PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 11, 2)
)
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListTable.setStatus("current")
_PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListEntry_Object = MibTableRow
policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListEntry = _PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 11, 2, 1)
)
policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyDeviceAccessPolicyCountersName"),
    (0, "VIPTELA-POLICY", "policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName"),
)
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListEntry.setStatus("current")


class _PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName_Type(String):
    """Custom type policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName_Type.__name__ = "String"
_PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName_Object = MibTableColumn
policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName = _PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 11, 2, 1, 1),
    _PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName_Type()
)
policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName.setStatus("current")
_PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListPackets_Type = Counter64
_PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListPackets_Object = MibTableColumn
policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListPackets = _PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 11, 2, 1, 2),
    _PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListPackets_Type()
)
policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListPackets.setStatus("current")
_PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListBytes_Type = Counter64
_PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListBytes_Object = MibTableColumn
policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListBytes = _PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 11, 2, 1, 3),
    _PolicyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListBytes_Type()
)
policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListBytes.setStatus("current")
_PolicyDeviceAccessPolicyNames_ObjectIdentity = ObjectIdentity
policyDeviceAccessPolicyNames = _PolicyDeviceAccessPolicyNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 12)
)
_PolicyDeviceAccessPolicyNamesTable_Object = MibTable
policyDeviceAccessPolicyNamesTable = _PolicyDeviceAccessPolicyNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 12, 1)
)
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyNamesTable.setStatus("current")
_PolicyDeviceAccessPolicyNamesEntry_Object = MibTableRow
policyDeviceAccessPolicyNamesEntry = _PolicyDeviceAccessPolicyNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 12, 1, 1)
)
policyDeviceAccessPolicyNamesEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyDeviceAccessPolicyNamesName"),
)
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyNamesEntry.setStatus("current")


class _PolicyDeviceAccessPolicyNamesName_Type(String):
    """Custom type policyDeviceAccessPolicyNamesName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyDeviceAccessPolicyNamesName_Type.__name__ = "String"
_PolicyDeviceAccessPolicyNamesName_Object = MibTableColumn
policyDeviceAccessPolicyNamesName = _PolicyDeviceAccessPolicyNamesName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 4, 12, 1, 1, 1),
    _PolicyDeviceAccessPolicyNamesName_Type()
)
policyDeviceAccessPolicyNamesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDeviceAccessPolicyNamesName.setStatus("current")
_PolicerTable_Object = MibTable
policerTable = _PolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 5)
)
if mibBuilder.loadTexts:
    policerTable.setStatus("current")
_PolicerEntry_Object = MibTableRow
policerEntry = _PolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 5, 1)
)
policerEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policerName"),
    (0, "VIPTELA-POLICY", "policerIndex"),
    (0, "VIPTELA-POLICY", "policerDirection"),
)
if mibBuilder.loadTexts:
    policerEntry.setStatus("current")


class _PolicerName_Type(String):
    """Custom type policerName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicerName_Type.__name__ = "String"
_PolicerName_Object = MibTableColumn
policerName = _PolicerName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 5, 1, 1),
    _PolicerName_Type()
)
policerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policerName.setStatus("current")
_PolicerIndex_Type = Unsigned32
_PolicerIndex_Object = MibTableColumn
policerIndex = _PolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 5, 1, 2),
    _PolicerIndex_Type()
)
policerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policerIndex.setStatus("current")
_PolicerDirection_Type = DirectionEnum
_PolicerDirection_Object = MibTableColumn
policerDirection = _PolicerDirection_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 5, 1, 3),
    _PolicerDirection_Type()
)
policerDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policerDirection.setStatus("current")
_PolicerRate_Type = Counter64
_PolicerRate_Object = MibTableColumn
policerRate = _PolicerRate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 5, 1, 4),
    _PolicerRate_Type()
)
policerRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerRate.setStatus("current")
_PolicerBurst_Type = Unsigned32
_PolicerBurst_Object = MibTableColumn
policerBurst = _PolicerBurst_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 5, 1, 5),
    _PolicerBurst_Type()
)
policerBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerBurst.setStatus("current")
_PolicerOosAction_Type = String
_PolicerOosAction_Object = MibTableColumn
policerOosAction = _PolicerOosAction_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 5, 1, 6),
    _PolicerOosAction_Type()
)
policerOosAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOosAction.setStatus("current")
_PolicerOosPkts_Type = Counter64
_PolicerOosPkts_Object = MibTableColumn
policerOosPkts = _PolicerOosPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 5, 1, 7),
    _PolicerOosPkts_Type()
)
policerOosPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOosPkts.setStatus("current")
_PolicerOosBytes_Type = Counter64
_PolicerOosBytes_Object = MibTableColumn
policerOosBytes = _PolicerOosBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 5, 1, 8),
    _PolicerOosBytes_Type()
)
policerOosBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policerOosBytes.setStatus("current")
_Zbfw_ObjectIdentity = ObjectIdentity
zbfw = _Zbfw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7)
)
_ZonepairInspectSessionTable_Object = MibTable
zonepairInspectSessionTable = _ZonepairInspectSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1)
)
if mibBuilder.loadTexts:
    zonepairInspectSessionTable.setStatus("current")
_ZonepairInspectSessionEntry_Object = MibTableRow
zonepairInspectSessionEntry = _ZonepairInspectSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1)
)
zonepairInspectSessionEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "zonepairInspectSessionZonepairName"),
    (0, "VIPTELA-POLICY", "zonepairInspectSessionVpn"),
    (0, "VIPTELA-POLICY", "zonepairInspectSessionSourceIpAddress"),
    (0, "VIPTELA-POLICY", "zonepairInspectSessionDestinationIpAddress"),
    (0, "VIPTELA-POLICY", "zonepairInspectSessionSourcePort"),
    (0, "VIPTELA-POLICY", "zonepairInspectSessionDestinationPort"),
    (0, "VIPTELA-POLICY", "zonepairInspectSessionProtocol"),
)
if mibBuilder.loadTexts:
    zonepairInspectSessionEntry.setStatus("current")


class _ZonepairInspectSessionZonepairName_Type(String):
    """Custom type zonepairInspectSessionZonepairName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZonepairInspectSessionZonepairName_Type.__name__ = "String"
_ZonepairInspectSessionZonepairName_Object = MibTableColumn
zonepairInspectSessionZonepairName = _ZonepairInspectSessionZonepairName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 1),
    _ZonepairInspectSessionZonepairName_Type()
)
zonepairInspectSessionZonepairName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zonepairInspectSessionZonepairName.setStatus("current")


class _ZonepairInspectSessionVpn_Type(Unsigned32):
    """Custom type zonepairInspectSessionVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_ZonepairInspectSessionVpn_Type.__name__ = "Unsigned32"
_ZonepairInspectSessionVpn_Object = MibTableColumn
zonepairInspectSessionVpn = _ZonepairInspectSessionVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 2),
    _ZonepairInspectSessionVpn_Type()
)
zonepairInspectSessionVpn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zonepairInspectSessionVpn.setStatus("current")
_ZonepairInspectSessionSourceIpAddress_Type = IpAddress
_ZonepairInspectSessionSourceIpAddress_Object = MibTableColumn
zonepairInspectSessionSourceIpAddress = _ZonepairInspectSessionSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 3),
    _ZonepairInspectSessionSourceIpAddress_Type()
)
zonepairInspectSessionSourceIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zonepairInspectSessionSourceIpAddress.setStatus("current")
_ZonepairInspectSessionDestinationIpAddress_Type = IpAddress
_ZonepairInspectSessionDestinationIpAddress_Object = MibTableColumn
zonepairInspectSessionDestinationIpAddress = _ZonepairInspectSessionDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 4),
    _ZonepairInspectSessionDestinationIpAddress_Type()
)
zonepairInspectSessionDestinationIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zonepairInspectSessionDestinationIpAddress.setStatus("current")
_ZonepairInspectSessionSourcePort_Type = Unsigned32
_ZonepairInspectSessionSourcePort_Object = MibTableColumn
zonepairInspectSessionSourcePort = _ZonepairInspectSessionSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 5),
    _ZonepairInspectSessionSourcePort_Type()
)
zonepairInspectSessionSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zonepairInspectSessionSourcePort.setStatus("current")
_ZonepairInspectSessionDestinationPort_Type = Unsigned32
_ZonepairInspectSessionDestinationPort_Object = MibTableColumn
zonepairInspectSessionDestinationPort = _ZonepairInspectSessionDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 6),
    _ZonepairInspectSessionDestinationPort_Type()
)
zonepairInspectSessionDestinationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zonepairInspectSessionDestinationPort.setStatus("current")


class _ZonepairInspectSessionProtocol_Type(Integer32):
    """Custom type zonepairInspectSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 6),
          ("udp", 17))
    )


_ZonepairInspectSessionProtocol_Type.__name__ = "Integer32"
_ZonepairInspectSessionProtocol_Object = MibTableColumn
zonepairInspectSessionProtocol = _ZonepairInspectSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 7),
    _ZonepairInspectSessionProtocol_Type()
)
zonepairInspectSessionProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zonepairInspectSessionProtocol.setStatus("current")


class _ZonepairInspectSessionSourceVpn_Type(Unsigned32):
    """Custom type zonepairInspectSessionSourceVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_ZonepairInspectSessionSourceVpn_Type.__name__ = "Unsigned32"
_ZonepairInspectSessionSourceVpn_Object = MibTableColumn
zonepairInspectSessionSourceVpn = _ZonepairInspectSessionSourceVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 8),
    _ZonepairInspectSessionSourceVpn_Type()
)
zonepairInspectSessionSourceVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonepairInspectSessionSourceVpn.setStatus("current")


class _ZonepairInspectSessionDestinationVpn_Type(Unsigned32):
    """Custom type zonepairInspectSessionDestinationVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_ZonepairInspectSessionDestinationVpn_Type.__name__ = "Unsigned32"
_ZonepairInspectSessionDestinationVpn_Object = MibTableColumn
zonepairInspectSessionDestinationVpn = _ZonepairInspectSessionDestinationVpn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 9),
    _ZonepairInspectSessionDestinationVpn_Type()
)
zonepairInspectSessionDestinationVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonepairInspectSessionDestinationVpn.setStatus("current")
_ZonepairInspectSessionIdleTimeout_Type = String
_ZonepairInspectSessionIdleTimeout_Object = MibTableColumn
zonepairInspectSessionIdleTimeout = _ZonepairInspectSessionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 10),
    _ZonepairInspectSessionIdleTimeout_Type()
)
zonepairInspectSessionIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonepairInspectSessionIdleTimeout.setStatus("current")
_ZonepairInspectSessionOutboundPackets_Type = Counter32
_ZonepairInspectSessionOutboundPackets_Object = MibTableColumn
zonepairInspectSessionOutboundPackets = _ZonepairInspectSessionOutboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 11),
    _ZonepairInspectSessionOutboundPackets_Type()
)
zonepairInspectSessionOutboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonepairInspectSessionOutboundPackets.setStatus("current")
_ZonepairInspectSessionOutboundOctets_Type = Counter64
_ZonepairInspectSessionOutboundOctets_Object = MibTableColumn
zonepairInspectSessionOutboundOctets = _ZonepairInspectSessionOutboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 12),
    _ZonepairInspectSessionOutboundOctets_Type()
)
zonepairInspectSessionOutboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonepairInspectSessionOutboundOctets.setStatus("current")
_ZonepairInspectSessionInboundPackets_Type = Counter32
_ZonepairInspectSessionInboundPackets_Object = MibTableColumn
zonepairInspectSessionInboundPackets = _ZonepairInspectSessionInboundPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 13),
    _ZonepairInspectSessionInboundPackets_Type()
)
zonepairInspectSessionInboundPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonepairInspectSessionInboundPackets.setStatus("current")
_ZonepairInspectSessionInboundOctets_Type = Counter64
_ZonepairInspectSessionInboundOctets_Object = MibTableColumn
zonepairInspectSessionInboundOctets = _ZonepairInspectSessionInboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 14),
    _ZonepairInspectSessionInboundOctets_Type()
)
zonepairInspectSessionInboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonepairInspectSessionInboundOctets.setStatus("current")


class _ZonepairInspectSessionFilterState_Type(Integer32):
    """Custom type zonepairInspectSessionFilterState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("listen", 1),
          ("syn-sent", 2),
          ("syn-received", 3),
          ("established", 4),
          ("close-wait", 5),
          ("last-ack", 6),
          ("timewait", 7))
    )


_ZonepairInspectSessionFilterState_Type.__name__ = "Integer32"
_ZonepairInspectSessionFilterState_Object = MibTableColumn
zonepairInspectSessionFilterState = _ZonepairInspectSessionFilterState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 1, 1, 15),
    _ZonepairInspectSessionFilterState_Type()
)
zonepairInspectSessionFilterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zonepairInspectSessionFilterState.setStatus("current")
_ZoneBasedFirewallStatistics_ObjectIdentity = ObjectIdentity
zoneBasedFirewallStatistics = _ZoneBasedFirewallStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2)
)
_ZoneBasedFirewallStatisticsFragFail_Type = Integer32
_ZoneBasedFirewallStatisticsFragFail_Object = MibScalar
zoneBasedFirewallStatisticsFragFail = _ZoneBasedFirewallStatisticsFragFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 1),
    _ZoneBasedFirewallStatisticsFragFail_Type()
)
zoneBasedFirewallStatisticsFragFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsFragFail.setStatus("current")
_ZoneBasedFirewallStatisticsStateCheckFail_Type = Integer32
_ZoneBasedFirewallStatisticsStateCheckFail_Object = MibScalar
zoneBasedFirewallStatisticsStateCheckFail = _ZoneBasedFirewallStatisticsStateCheckFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 2),
    _ZoneBasedFirewallStatisticsStateCheckFail_Type()
)
zoneBasedFirewallStatisticsStateCheckFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsStateCheckFail.setStatus("current")
_ZoneBasedFirewallStatisticsFlowAddFail_Type = Integer32
_ZoneBasedFirewallStatisticsFlowAddFail_Object = MibScalar
zoneBasedFirewallStatisticsFlowAddFail = _ZoneBasedFirewallStatisticsFlowAddFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 3),
    _ZoneBasedFirewallStatisticsFlowAddFail_Type()
)
zoneBasedFirewallStatisticsFlowAddFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsFlowAddFail.setStatus("current")
_ZoneBasedFirewallStatisticsUnsupportedProto_Type = Integer32
_ZoneBasedFirewallStatisticsUnsupportedProto_Object = MibScalar
zoneBasedFirewallStatisticsUnsupportedProto = _ZoneBasedFirewallStatisticsUnsupportedProto_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 4),
    _ZoneBasedFirewallStatisticsUnsupportedProto_Type()
)
zoneBasedFirewallStatisticsUnsupportedProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsUnsupportedProto.setStatus("current")
_ZoneBasedFirewallStatisticsNumFlowEntries_Type = Integer32
_ZoneBasedFirewallStatisticsNumFlowEntries_Object = MibScalar
zoneBasedFirewallStatisticsNumFlowEntries = _ZoneBasedFirewallStatisticsNumFlowEntries_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 5),
    _ZoneBasedFirewallStatisticsNumFlowEntries_Type()
)
zoneBasedFirewallStatisticsNumFlowEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsNumFlowEntries.setStatus("current")
_ZoneBasedFirewallStatisticsMaxHalfOpenExceeded_Type = Integer32
_ZoneBasedFirewallStatisticsMaxHalfOpenExceeded_Object = MibScalar
zoneBasedFirewallStatisticsMaxHalfOpenExceeded = _ZoneBasedFirewallStatisticsMaxHalfOpenExceeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 6),
    _ZoneBasedFirewallStatisticsMaxHalfOpenExceeded_Type()
)
zoneBasedFirewallStatisticsMaxHalfOpenExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsMaxHalfOpenExceeded.setStatus("current")
_ZoneBasedFirewallStatisticsFragments_Type = Counter64
_ZoneBasedFirewallStatisticsFragments_Object = MibScalar
zoneBasedFirewallStatisticsFragments = _ZoneBasedFirewallStatisticsFragments_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 7),
    _ZoneBasedFirewallStatisticsFragments_Type()
)
zoneBasedFirewallStatisticsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsFragments.setStatus("current")
_ZoneBasedFirewallStatisticsPolicyChangeDropped_Type = Integer32
_ZoneBasedFirewallStatisticsPolicyChangeDropped_Object = MibScalar
zoneBasedFirewallStatisticsPolicyChangeDropped = _ZoneBasedFirewallStatisticsPolicyChangeDropped_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 8),
    _ZoneBasedFirewallStatisticsPolicyChangeDropped_Type()
)
zoneBasedFirewallStatisticsPolicyChangeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsPolicyChangeDropped.setStatus("current")
_ZoneBasedFirewallStatisticsNoPairSameZoneAllowed_Type = Counter64
_ZoneBasedFirewallStatisticsNoPairSameZoneAllowed_Object = MibScalar
zoneBasedFirewallStatisticsNoPairSameZoneAllowed = _ZoneBasedFirewallStatisticsNoPairSameZoneAllowed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 9),
    _ZoneBasedFirewallStatisticsNoPairSameZoneAllowed_Type()
)
zoneBasedFirewallStatisticsNoPairSameZoneAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsNoPairSameZoneAllowed.setStatus("current")
_ZoneBasedFirewallStatisticsNoPairDiffZoneDropped_Type = Counter64
_ZoneBasedFirewallStatisticsNoPairDiffZoneDropped_Object = MibScalar
zoneBasedFirewallStatisticsNoPairDiffZoneDropped = _ZoneBasedFirewallStatisticsNoPairDiffZoneDropped_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 10),
    _ZoneBasedFirewallStatisticsNoPairDiffZoneDropped_Type()
)
zoneBasedFirewallStatisticsNoPairDiffZoneDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsNoPairDiffZoneDropped.setStatus("current")
_ZoneBasedFirewallStatisticsZoneNoZoneDropped_Type = Counter64
_ZoneBasedFirewallStatisticsZoneNoZoneDropped_Object = MibScalar
zoneBasedFirewallStatisticsZoneNoZoneDropped = _ZoneBasedFirewallStatisticsZoneNoZoneDropped_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 11),
    _ZoneBasedFirewallStatisticsZoneNoZoneDropped_Type()
)
zoneBasedFirewallStatisticsZoneNoZoneDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsZoneNoZoneDropped.setStatus("current")
_ZoneBasedFirewallStatisticsNoZoneNoZoneAllowed_Type = Counter64
_ZoneBasedFirewallStatisticsNoZoneNoZoneAllowed_Object = MibScalar
zoneBasedFirewallStatisticsNoZoneNoZoneAllowed = _ZoneBasedFirewallStatisticsNoZoneNoZoneAllowed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 12),
    _ZoneBasedFirewallStatisticsNoZoneNoZoneAllowed_Type()
)
zoneBasedFirewallStatisticsNoZoneNoZoneAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsNoZoneNoZoneAllowed.setStatus("current")
_ZoneBasedFirewallStatisticsZoneNoZoneInetAllowed_Type = Counter64
_ZoneBasedFirewallStatisticsZoneNoZoneInetAllowed_Object = MibScalar
zoneBasedFirewallStatisticsZoneNoZoneInetAllowed = _ZoneBasedFirewallStatisticsZoneNoZoneInetAllowed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 13),
    _ZoneBasedFirewallStatisticsZoneNoZoneInetAllowed_Type()
)
zoneBasedFirewallStatisticsZoneNoZoneInetAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsZoneNoZoneInetAllowed.setStatus("current")
_ZoneBasedFirewallStatisticsZoneNoZoneInetDenied_Type = Counter64
_ZoneBasedFirewallStatisticsZoneNoZoneInetDenied_Object = MibScalar
zoneBasedFirewallStatisticsZoneNoZoneInetDenied = _ZoneBasedFirewallStatisticsZoneNoZoneInetDenied_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 14),
    _ZoneBasedFirewallStatisticsZoneNoZoneInetDenied_Type()
)
zoneBasedFirewallStatisticsZoneNoZoneInetDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsZoneNoZoneInetDenied.setStatus("current")
_ZoneBasedFirewallStatisticsTcpRetransSeg_Type = Integer32
_ZoneBasedFirewallStatisticsTcpRetransSeg_Object = MibScalar
zoneBasedFirewallStatisticsTcpRetransSeg = _ZoneBasedFirewallStatisticsTcpRetransSeg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 15),
    _ZoneBasedFirewallStatisticsTcpRetransSeg_Type()
)
zoneBasedFirewallStatisticsTcpRetransSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpRetransSeg.setStatus("current")
_ZoneBasedFirewallStatisticsTcpOooSeg_Type = Integer32
_ZoneBasedFirewallStatisticsTcpOooSeg_Object = MibScalar
zoneBasedFirewallStatisticsTcpOooSeg = _ZoneBasedFirewallStatisticsTcpOooSeg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 16),
    _ZoneBasedFirewallStatisticsTcpOooSeg_Type()
)
zoneBasedFirewallStatisticsTcpOooSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpOooSeg.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInternalInvalidTcpState_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInternalInvalidTcpState_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInternalInvalidTcpState = _ZoneBasedFirewallStatisticsTcpDropInternalInvalidTcpState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 17),
    _ZoneBasedFirewallStatisticsTcpDropInternalInvalidTcpState_Type()
)
zoneBasedFirewallStatisticsTcpDropInternalInvalidTcpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInternalInvalidTcpState.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropStraySeg_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropStraySeg_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropStraySeg = _ZoneBasedFirewallStatisticsTcpDropStraySeg_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 18),
    _ZoneBasedFirewallStatisticsTcpDropStraySeg_Type()
)
zoneBasedFirewallStatisticsTcpDropStraySeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropStraySeg.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidFlags_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidFlags_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidFlags = _ZoneBasedFirewallStatisticsTcpDropInvalidFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 19),
    _ZoneBasedFirewallStatisticsTcpDropInvalidFlags_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidFlags.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropSynWithData_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropSynWithData_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropSynWithData = _ZoneBasedFirewallStatisticsTcpDropSynWithData_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 20),
    _ZoneBasedFirewallStatisticsTcpDropSynWithData_Type()
)
zoneBasedFirewallStatisticsTcpDropSynWithData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropSynWithData.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidWinScaleOption_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidWinScaleOption_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidWinScaleOption = _ZoneBasedFirewallStatisticsTcpDropInvalidWinScaleOption_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 21),
    _ZoneBasedFirewallStatisticsTcpDropInvalidWinScaleOption_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidWinScaleOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidWinScaleOption.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidSegSynsentState_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidSegSynsentState_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidSegSynsentState = _ZoneBasedFirewallStatisticsTcpDropInvalidSegSynsentState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 22),
    _ZoneBasedFirewallStatisticsTcpDropInvalidSegSynsentState_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidSegSynsentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidSegSynsentState.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidAckNum_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidAckNum_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidAckNum = _ZoneBasedFirewallStatisticsTcpDropInvalidAckNum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 23),
    _ZoneBasedFirewallStatisticsTcpDropInvalidAckNum_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidAckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidAckNum.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidAckFlag_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidAckFlag_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidAckFlag = _ZoneBasedFirewallStatisticsTcpDropInvalidAckFlag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 24),
    _ZoneBasedFirewallStatisticsTcpDropInvalidAckFlag_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidAckFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidAckFlag.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropRstToResp_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropRstToResp_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropRstToResp = _ZoneBasedFirewallStatisticsTcpDropRstToResp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 25),
    _ZoneBasedFirewallStatisticsTcpDropRstToResp_Type()
)
zoneBasedFirewallStatisticsTcpDropRstToResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropRstToResp.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropRetransInvalidFlags_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropRetransInvalidFlags_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropRetransInvalidFlags = _ZoneBasedFirewallStatisticsTcpDropRetransInvalidFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 26),
    _ZoneBasedFirewallStatisticsTcpDropRetransInvalidFlags_Type()
)
zoneBasedFirewallStatisticsTcpDropRetransInvalidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropRetransInvalidFlags.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropRstInWin_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropRstInWin_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropRstInWin = _ZoneBasedFirewallStatisticsTcpDropRstInWin_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 27),
    _ZoneBasedFirewallStatisticsTcpDropRstInWin_Type()
)
zoneBasedFirewallStatisticsTcpDropRstInWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropRstInWin.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidSeq_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidSeq_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidSeq = _ZoneBasedFirewallStatisticsTcpDropInvalidSeq_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 28),
    _ZoneBasedFirewallStatisticsTcpDropInvalidSeq_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidSeq.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidSegSynrcvdState_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidSegSynrcvdState_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidSegSynrcvdState = _ZoneBasedFirewallStatisticsTcpDropInvalidSegSynrcvdState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 29),
    _ZoneBasedFirewallStatisticsTcpDropInvalidSegSynrcvdState_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidSegSynrcvdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidSegSynrcvdState.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropSynInWin_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropSynInWin_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropSynInWin = _ZoneBasedFirewallStatisticsTcpDropSynInWin_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 30),
    _ZoneBasedFirewallStatisticsTcpDropSynInWin_Type()
)
zoneBasedFirewallStatisticsTcpDropSynInWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropSynInWin.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropUnexpectTcpPyld_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropUnexpectTcpPyld_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropUnexpectTcpPyld = _ZoneBasedFirewallStatisticsTcpDropUnexpectTcpPyld_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 31),
    _ZoneBasedFirewallStatisticsTcpDropUnexpectTcpPyld_Type()
)
zoneBasedFirewallStatisticsTcpDropUnexpectTcpPyld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropUnexpectTcpPyld.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidSegPktTooOld_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidSegPktTooOld_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidSegPktTooOld = _ZoneBasedFirewallStatisticsTcpDropInvalidSegPktTooOld_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 32),
    _ZoneBasedFirewallStatisticsTcpDropInvalidSegPktTooOld_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidSegPktTooOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidSegPktTooOld.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidSegPktWinOverflow_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidSegPktWinOverflow_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidSegPktWinOverflow = _ZoneBasedFirewallStatisticsTcpDropInvalidSegPktWinOverflow_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 33),
    _ZoneBasedFirewallStatisticsTcpDropInvalidSegPktWinOverflow_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidSegPktWinOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidSegPktWinOverflow.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidSegPyldAfterFinSend_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidSegPyldAfterFinSend_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidSegPyldAfterFinSend = _ZoneBasedFirewallStatisticsTcpDropInvalidSegPyldAfterFinSend_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 34),
    _ZoneBasedFirewallStatisticsTcpDropInvalidSegPyldAfterFinSend_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidSegPyldAfterFinSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidSegPyldAfterFinSend.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropNoSynInListenState_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropNoSynInListenState_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropNoSynInListenState = _ZoneBasedFirewallStatisticsTcpDropNoSynInListenState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 35),
    _ZoneBasedFirewallStatisticsTcpDropNoSynInListenState_Type()
)
zoneBasedFirewallStatisticsTcpDropNoSynInListenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropNoSynInListenState.setStatus("current")
_ZoneBasedFirewallStatisticsTcpDropInvalidDir_Type = Integer32
_ZoneBasedFirewallStatisticsTcpDropInvalidDir_Object = MibScalar
zoneBasedFirewallStatisticsTcpDropInvalidDir = _ZoneBasedFirewallStatisticsTcpDropInvalidDir_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 36),
    _ZoneBasedFirewallStatisticsTcpDropInvalidDir_Type()
)
zoneBasedFirewallStatisticsTcpDropInvalidDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsTcpDropInvalidDir.setStatus("current")
_ZoneBasedFirewallStatisticsZbfPkts_Type = Counter64
_ZoneBasedFirewallStatisticsZbfPkts_Object = MibScalar
zoneBasedFirewallStatisticsZbfPkts = _ZoneBasedFirewallStatisticsZbfPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 37),
    _ZoneBasedFirewallStatisticsZbfPkts_Type()
)
zoneBasedFirewallStatisticsZbfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsZbfPkts.setStatus("current")
_ZoneBasedFirewallStatisticsInvalidFilterDropped_Type = Integer32
_ZoneBasedFirewallStatisticsInvalidFilterDropped_Object = MibScalar
zoneBasedFirewallStatisticsInvalidFilterDropped = _ZoneBasedFirewallStatisticsInvalidFilterDropped_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 38),
    _ZoneBasedFirewallStatisticsInvalidFilterDropped_Type()
)
zoneBasedFirewallStatisticsInvalidFilterDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsInvalidFilterDropped.setStatus("current")
_ZoneBasedFirewallStatisticsMboxMsgFull_Type = Integer32
_ZoneBasedFirewallStatisticsMboxMsgFull_Object = MibScalar
zoneBasedFirewallStatisticsMboxMsgFull = _ZoneBasedFirewallStatisticsMboxMsgFull_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 39),
    _ZoneBasedFirewallStatisticsMboxMsgFull_Type()
)
zoneBasedFirewallStatisticsMboxMsgFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsMboxMsgFull.setStatus("current")
_ZoneBasedFirewallStatisticsFragStateCheckFail_Type = Integer32
_ZoneBasedFirewallStatisticsFragStateCheckFail_Object = MibScalar
zoneBasedFirewallStatisticsFragStateCheckFail = _ZoneBasedFirewallStatisticsFragStateCheckFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 40),
    _ZoneBasedFirewallStatisticsFragStateCheckFail_Type()
)
zoneBasedFirewallStatisticsFragStateCheckFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsFragStateCheckFail.setStatus("current")
_ZoneBasedFirewallStatisticsSelfPkts_Type = Counter64
_ZoneBasedFirewallStatisticsSelfPkts_Object = MibScalar
zoneBasedFirewallStatisticsSelfPkts = _ZoneBasedFirewallStatisticsSelfPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 41),
    _ZoneBasedFirewallStatisticsSelfPkts_Type()
)
zoneBasedFirewallStatisticsSelfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsSelfPkts.setStatus("current")
_ZoneBasedFirewallStatisticsSelfPktsAllowed_Type = Counter64
_ZoneBasedFirewallStatisticsSelfPktsAllowed_Object = MibScalar
zoneBasedFirewallStatisticsSelfPktsAllowed = _ZoneBasedFirewallStatisticsSelfPktsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 42),
    _ZoneBasedFirewallStatisticsSelfPktsAllowed_Type()
)
zoneBasedFirewallStatisticsSelfPktsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsSelfPktsAllowed.setStatus("current")
_ZoneBasedFirewallStatisticsUmbrellaRegistrPktsAllowed_Type = Integer32
_ZoneBasedFirewallStatisticsUmbrellaRegistrPktsAllowed_Object = MibScalar
zoneBasedFirewallStatisticsUmbrellaRegistrPktsAllowed = _ZoneBasedFirewallStatisticsUmbrellaRegistrPktsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 2, 43),
    _ZoneBasedFirewallStatisticsUmbrellaRegistrPktsAllowed_Type()
)
zoneBasedFirewallStatisticsUmbrellaRegistrPktsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zoneBasedFirewallStatisticsUmbrellaRegistrPktsAllowed.setStatus("current")
_PolicyZonePolicyFilterTable_Object = MibTable
policyZonePolicyFilterTable = _PolicyZonePolicyFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 3)
)
if mibBuilder.loadTexts:
    policyZonePolicyFilterTable.setStatus("current")
_PolicyZonePolicyFilterEntry_Object = MibTableRow
policyZonePolicyFilterEntry = _PolicyZonePolicyFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 3, 1)
)
policyZonePolicyFilterEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyZonePolicyFilterName"),
)
if mibBuilder.loadTexts:
    policyZonePolicyFilterEntry.setStatus("current")


class _PolicyZonePolicyFilterName_Type(String):
    """Custom type policyZonePolicyFilterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_PolicyZonePolicyFilterName_Type.__name__ = "String"
_PolicyZonePolicyFilterName_Object = MibTableColumn
policyZonePolicyFilterName = _PolicyZonePolicyFilterName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 3, 1, 1),
    _PolicyZonePolicyFilterName_Type()
)
policyZonePolicyFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyZonePolicyFilterName.setStatus("current")
_PolicyZonePolicyFilterCounterTable_Object = MibTable
policyZonePolicyFilterCounterTable = _PolicyZonePolicyFilterCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 4)
)
if mibBuilder.loadTexts:
    policyZonePolicyFilterCounterTable.setStatus("current")
_PolicyZonePolicyFilterCounterEntry_Object = MibTableRow
policyZonePolicyFilterCounterEntry = _PolicyZonePolicyFilterCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 4, 1)
)
policyZonePolicyFilterCounterEntry.setIndexNames(
    (0, "VIPTELA-POLICY", "policyZonePolicyFilterName"),
    (0, "VIPTELA-POLICY", "policyZonePolicyFilterCounterName"),
)
if mibBuilder.loadTexts:
    policyZonePolicyFilterCounterEntry.setStatus("current")


class _PolicyZonePolicyFilterCounterName_Type(String):
    """Custom type policyZonePolicyFilterCounterName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PolicyZonePolicyFilterCounterName_Type.__name__ = "String"
_PolicyZonePolicyFilterCounterName_Object = MibTableColumn
policyZonePolicyFilterCounterName = _PolicyZonePolicyFilterCounterName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 4, 1, 1),
    _PolicyZonePolicyFilterCounterName_Type()
)
policyZonePolicyFilterCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyZonePolicyFilterCounterName.setStatus("current")
_PolicyZonePolicyFilterCounterPackets_Type = Counter64
_PolicyZonePolicyFilterCounterPackets_Object = MibTableColumn
policyZonePolicyFilterCounterPackets = _PolicyZonePolicyFilterCounterPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 4, 1, 2),
    _PolicyZonePolicyFilterCounterPackets_Type()
)
policyZonePolicyFilterCounterPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyZonePolicyFilterCounterPackets.setStatus("current")
_PolicyZonePolicyFilterCounterBytes_Type = Counter64
_PolicyZonePolicyFilterCounterBytes_Object = MibTableColumn
policyZonePolicyFilterCounterBytes = _PolicyZonePolicyFilterCounterBytes_Object(
    (1, 3, 6, 1, 4, 1, 41916, 8, 7, 4, 1, 3),
    _PolicyZonePolicyFilterCounterBytes_Type()
)
policyZonePolicyFilterCounterBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyZonePolicyFilterCounterBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-POLICY",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "Ipv4Prefix": Ipv4Prefix,
       "InetAddressIP": InetAddressIP,
       "String": String,
       "SourcePort": SourcePort,
       "DestinationIp": DestinationIp,
       "Protocol": Protocol,
       "Dscp1": Dscp1,
       "TcpFlags": TcpFlags,
       "DestinationIp1": DestinationIp1,
       "SourceIp": SourceIp,
       "Protocol1": Protocol1,
       "Protocol2": Protocol2,
       "Protocol3": Protocol3,
       "Protocol4": Protocol4,
       "Protocol5": Protocol5,
       "DestinationPort1": DestinationPort1,
       "Community1": Community1,
       "DestinationPort2": DestinationPort2,
       "DestinationPort3": DestinationPort3,
       "DestinationPort4": DestinationPort4,
       "DestinationPort5": DestinationPort5,
       "PacketLength": PacketLength,
       "TransportProtocol": TransportProtocol,
       "ActionDataEnum": ActionDataEnum,
       "BgpOriginEnum": BgpOriginEnum,
       "Dscp": Dscp,
       "ActionEnum": ActionEnum,
       "PacketLength1": PacketLength1,
       "PacketLength2": PacketLength2,
       "PacketLength3": PacketLength3,
       "Community": Community,
       "DataPolicyDirectionEnum": DataPolicyDirectionEnum,
       "SourcePort1": SourcePort1,
       "SourcePort2": SourcePort2,
       "SourcePort3": SourcePort3,
       "SourcePort4": SourcePort4,
       "SourcePort5": SourcePort5,
       "DirectionEnum": DirectionEnum,
       "SourceIp1": SourceIp1,
       "DestinationPort": DestinationPort,
       "ColorList": ColorList,
       "EncapsulationList": EncapsulationList,
       "LossProtectEnum": LossProtectEnum,
       "viptela-policy": viptela_policy,
       "policy": policy,
       "policyDataPolicyFilter": policyDataPolicyFilter,
       "policyDataPolicyFilterTable": policyDataPolicyFilterTable,
       "policyDataPolicyFilterEntry": policyDataPolicyFilterEntry,
       "policyDataPolicyFilterName": policyDataPolicyFilterName,
       "policyDataPolicyFilterVpnlistTable": policyDataPolicyFilterVpnlistTable,
       "policyDataPolicyFilterVpnlistEntry": policyDataPolicyFilterVpnlistEntry,
       "policyDataPolicyFilterVpnlistName": policyDataPolicyFilterVpnlistName,
       "policyDataPolicyFilterVpnlistCounterTable": policyDataPolicyFilterVpnlistCounterTable,
       "policyDataPolicyFilterVpnlistCounterEntry": policyDataPolicyFilterVpnlistCounterEntry,
       "policyDataPolicyFilterVpnlistCounterName": policyDataPolicyFilterVpnlistCounterName,
       "policyDataPolicyFilterVpnlistCounterPackets": policyDataPolicyFilterVpnlistCounterPackets,
       "policyDataPolicyFilterVpnlistCounterBytes": policyDataPolicyFilterVpnlistCounterBytes,
       "policyDataPolicyFilterVpnlistPolicerTable": policyDataPolicyFilterVpnlistPolicerTable,
       "policyDataPolicyFilterVpnlistPolicerEntry": policyDataPolicyFilterVpnlistPolicerEntry,
       "policyDataPolicyFilterVpnlistPolicerName": policyDataPolicyFilterVpnlistPolicerName,
       "policyDataPolicyFilterVpnlistPolicerOosPackets": policyDataPolicyFilterVpnlistPolicerOosPackets,
       "policyDataPolicyFilterVpnlistPolicerOosBytes": policyDataPolicyFilterVpnlistPolicerOosBytes,
       "policyAppRoutePolicy": policyAppRoutePolicy,
       "policyAppRoutePolicyFilterTable": policyAppRoutePolicyFilterTable,
       "policyAppRoutePolicyFilterEntry": policyAppRoutePolicyFilterEntry,
       "policyAppRoutePolicyFilterName": policyAppRoutePolicyFilterName,
       "policyAppRoutePolicyFilterVpnlistTable": policyAppRoutePolicyFilterVpnlistTable,
       "policyAppRoutePolicyFilterVpnlistEntry": policyAppRoutePolicyFilterVpnlistEntry,
       "policyAppRoutePolicyFilterVpnlistName": policyAppRoutePolicyFilterVpnlistName,
       "policyAppRoutePolicyFilterVpnlistCounterTable": policyAppRoutePolicyFilterVpnlistCounterTable,
       "policyAppRoutePolicyFilterVpnlistCounterEntry": policyAppRoutePolicyFilterVpnlistCounterEntry,
       "policyAppRoutePolicyFilterVpnlistCounterName": policyAppRoutePolicyFilterVpnlistCounterName,
       "policyAppRoutePolicyFilterVpnlistCounterPackets": policyAppRoutePolicyFilterVpnlistCounterPackets,
       "policyAppRoutePolicyFilterVpnlistCounterBytes": policyAppRoutePolicyFilterVpnlistCounterBytes,
       "policyAccessListNames": policyAccessListNames,
       "policyAccessListNamesTable": policyAccessListNamesTable,
       "policyAccessListNamesEntry": policyAccessListNamesEntry,
       "policyAccessListNamesName": policyAccessListNamesName,
       "policyAccessListCounters": policyAccessListCounters,
       "policyAccessListCountersTable": policyAccessListCountersTable,
       "policyAccessListCountersEntry": policyAccessListCountersEntry,
       "policyAccessListCountersName": policyAccessListCountersName,
       "policyAccessListCountersAccessPolicyCounterListTable": policyAccessListCountersAccessPolicyCounterListTable,
       "policyAccessListCountersAccessPolicyCounterListEntry": policyAccessListCountersAccessPolicyCounterListEntry,
       "policyAccessListCountersAccessPolicyCounterListCounterName": policyAccessListCountersAccessPolicyCounterListCounterName,
       "policyAccessListCountersAccessPolicyCounterListPackets": policyAccessListCountersAccessPolicyCounterListPackets,
       "policyAccessListCountersAccessPolicyCounterListBytes": policyAccessListCountersAccessPolicyCounterListBytes,
       "policyAccessListPolicers": policyAccessListPolicers,
       "policyAccessListPolicersTable": policyAccessListPolicersTable,
       "policyAccessListPolicersEntry": policyAccessListPolicersEntry,
       "policyAccessListPolicersName": policyAccessListPolicersName,
       "policyAccessListPolicersAccessPolicyPolicerListTable": policyAccessListPolicersAccessPolicyPolicerListTable,
       "policyAccessListPolicersAccessPolicyPolicerListEntry": policyAccessListPolicersAccessPolicyPolicerListEntry,
       "policyAccessListPolicersAccessPolicyPolicerListPolicerName": policyAccessListPolicersAccessPolicyPolicerListPolicerName,
       "policyAccessListPolicersAccessPolicyPolicerListOosPackets": policyAccessListPolicersAccessPolicyPolicerListOosPackets,
       "policyAccessListPolicersAccessPolicyPolicerListOosBytes": policyAccessListPolicersAccessPolicyPolicerListOosBytes,
       "policyQosSchedulerInfo": policyQosSchedulerInfo,
       "policyQosSchedulerInfoTable": policyQosSchedulerInfoTable,
       "policyQosSchedulerInfoEntry": policyQosSchedulerInfoEntry,
       "policyQosSchedulerInfoQosSchedulerName": policyQosSchedulerInfoQosSchedulerName,
       "policyQosSchedulerInfoBandwidthPercent": policyQosSchedulerInfoBandwidthPercent,
       "policyQosSchedulerInfoBufferPercent": policyQosSchedulerInfoBufferPercent,
       "policyQosSchedulerInfoQueue": policyQosSchedulerInfoQueue,
       "policyQosSchedulerInfoQosSchedulerMapAssociationTable": policyQosSchedulerInfoQosSchedulerMapAssociationTable,
       "policyQosSchedulerInfoQosSchedulerMapAssociationEntry": policyQosSchedulerInfoQosSchedulerMapAssociationEntry,
       "policyQosSchedulerInfoQosSchedulerMapAssociationQosMapName": policyQosSchedulerInfoQosSchedulerMapAssociationQosMapName,
       "policyQosMapInfo": policyQosMapInfo,
       "policyQosMapInfoTable": policyQosMapInfoTable,
       "policyQosMapInfoEntry": policyQosMapInfoEntry,
       "policyQosMapInfoQosMapName": policyQosMapInfoQosMapName,
       "policyQosMapInfoQosMapInterfaceAssociationsTable": policyQosMapInfoQosMapInterfaceAssociationsTable,
       "policyQosMapInfoQosMapInterfaceAssociationsEntry": policyQosMapInfoQosMapInterfaceAssociationsEntry,
       "policyQosMapInfoQosMapInterfaceAssociationsInterfaceName": policyQosMapInfoQosMapInterfaceAssociationsInterfaceName,
       "policyAccessListAssociations": policyAccessListAssociations,
       "policyAccessListAssociationsTable": policyAccessListAssociationsTable,
       "policyAccessListAssociationsEntry": policyAccessListAssociationsEntry,
       "policyAccessListAssociationsName": policyAccessListAssociationsName,
       "policyAccessListAssociationsAccessPolicyInterfaceListTable": policyAccessListAssociationsAccessPolicyInterfaceListTable,
       "policyAccessListAssociationsAccessPolicyInterfaceListEntry": policyAccessListAssociationsAccessPolicyInterfaceListEntry,
       "policyAccessListAssociationsAccessPolicyInterfaceListIntName": policyAccessListAssociationsAccessPolicyInterfaceListIntName,
       "policyAccessListAssociationsAccessPolicyInterfaceListIntDir": policyAccessListAssociationsAccessPolicyInterfaceListIntDir,
       "policyRewriteAssociations": policyRewriteAssociations,
       "policyRewriteAssociationsTable": policyRewriteAssociationsTable,
       "policyRewriteAssociationsEntry": policyRewriteAssociationsEntry,
       "policyRewriteAssociationsName": policyRewriteAssociationsName,
       "policyRewriteAssociationsRewriteInterfaceListTable": policyRewriteAssociationsRewriteInterfaceListTable,
       "policyRewriteAssociationsRewriteInterfaceListEntry": policyRewriteAssociationsRewriteInterfaceListEntry,
       "policyRewriteAssociationsRewriteInterfaceListInterfaceName": policyRewriteAssociationsRewriteInterfaceListInterfaceName,
       "policyFromVsmart": policyFromVsmart,
       "policyFromVsmartSlaClassTable": policyFromVsmartSlaClassTable,
       "policyFromVsmartSlaClassEntry": policyFromVsmartSlaClassEntry,
       "policyFromVsmartSlaClassName": policyFromVsmartSlaClassName,
       "policyFromVsmartSlaClassLoss": policyFromVsmartSlaClassLoss,
       "policyFromVsmartSlaClassLatency": policyFromVsmartSlaClassLatency,
       "policyFromVsmartSlaClassJitter": policyFromVsmartSlaClassJitter,
       "policyFromVsmartDataPolicyTable": policyFromVsmartDataPolicyTable,
       "policyFromVsmartDataPolicyEntry": policyFromVsmartDataPolicyEntry,
       "policyFromVsmartDataPolicyName": policyFromVsmartDataPolicyName,
       "policyFromVsmartDataPolicyDirection": policyFromVsmartDataPolicyDirection,
       "policyFromVsmartDataPolicyVpnListTable": policyFromVsmartDataPolicyVpnListTable,
       "policyFromVsmartDataPolicyVpnListEntry": policyFromVsmartDataPolicyVpnListEntry,
       "policyFromVsmartDataPolicyVpnListName": policyFromVsmartDataPolicyVpnListName,
       "policyFromVsmartDataPolicyVpnListDefaultAction": policyFromVsmartDataPolicyVpnListDefaultAction,
       "policyFromVsmartDataPolicyVpnListSequenceTable": policyFromVsmartDataPolicyVpnListSequenceTable,
       "policyFromVsmartDataPolicyVpnListSequenceEntry": policyFromVsmartDataPolicyVpnListSequenceEntry,
       "policyFromVsmartDataPolicyVpnListSequenceSeqValue": policyFromVsmartDataPolicyVpnListSequenceSeqValue,
       "policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst": policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataPrLst,
       "policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst": policyFromVsmartDataPolicyVpnListSequenceMatchSrcDataV6PrLst,
       "policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst": policyFromVsmartDataPolicyVpnListSequenceMatchDestDataPrLst,
       "policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst": policyFromVsmartDataPolicyVpnListSequenceMatchDestDataV6PrLst,
       "policyFromVsmartDataPolicyVpnListSequenceMatchTcp": policyFromVsmartDataPolicyVpnListSequenceMatchTcp,
       "policyFromVsmartDataPolicyVpnListSequenceActionActionValue": policyFromVsmartDataPolicyVpnListSequenceActionActionValue,
       "policyFromVsmartDataPolicyVpnListSequenceActionCount": policyFromVsmartDataPolicyVpnListSequenceActionCount,
       "policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn": policyFromVsmartDataPolicyVpnListSequenceActionNatUseVpn,
       "policyFromVsmartDataPolicyVpnListSequenceActionCflowd": policyFromVsmartDataPolicyVpnListSequenceActionCflowd,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor": policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocColor,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap": policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocEncap,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop": policyFromVsmartDataPolicyVpnListSequenceActionSetNextHop,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer": policyFromVsmartDataPolicyVpnListSequenceActionSetPolicer,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetVpn": policyFromVsmartDataPolicyVpnListSequenceActionSetVpn,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel": policyFromVsmartDataPolicyVpnListSequenceActionSetVpnLabel,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp": policyFromVsmartDataPolicyVpnListSequenceActionSetTlocIp,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor": policyFromVsmartDataPolicyVpnListSequenceActionSetTlocColor,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList": policyFromVsmartDataPolicyVpnListSequenceActionSetTlocList,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType": policyFromVsmartDataPolicyVpnListSequenceActionSetServiceSvcType,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn": policyFromVsmartDataPolicyVpnListSequenceActionSetServiceVpn,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp": policyFromVsmartDataPolicyVpnListSequenceActionSetServiceTlocIp,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr": policyFromVsmartDataPolicyVpnListSequenceActionSetSvcTlocClr,
       "policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst": policyFromVsmartDataPolicyVpnListSequencActionSetSvcTlocLst,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal": policyFromVsmartDataPolicyVpnListSequenceActionSetServiceLocal,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetServiceRestrict": policyFromVsmartDataPolicyVpnListSequenceActionSetServiceRestrict,
       "policyFromVsmartDataPolicyVpnListSequenceActionLog": policyFromVsmartDataPolicyVpnListSequenceActionLog,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListColor": policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListColor,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListEncap": policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListEncap,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListRestrict": policyFromVsmartDataPolicyVpnListSequenceActionSetLocalTlocListRestrict,
       "policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization": policyFromVsmartDataPolicyVpnListSequenceActionTcpOptimization,
       "policyFromVsmartDataPolicyVpnListSequenceActionLossProtect": policyFromVsmartDataPolicyVpnListSequenceActionLossProtect,
       "policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6": policyFromVsmartDataPolicyVpnListSequenceActionSetNextHopIpv6,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTable,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstEntry,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstListNum,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocLbl,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocIp,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocClr,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocEn,
       "policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf": policyFromVsmartDataPolicyVpnListSeqActSetVipTlocPrLstTlocPrf,
       "policyFromVsmartCflowdTemplateTable": policyFromVsmartCflowdTemplateTable,
       "policyFromVsmartCflowdTemplateEntry": policyFromVsmartCflowdTemplateEntry,
       "policyFromVsmartCflowdTemplateName": policyFromVsmartCflowdTemplateName,
       "policyFromVsmartCflowdTemplateFlowActiveTimeout": policyFromVsmartCflowdTemplateFlowActiveTimeout,
       "policyFromVsmartCflowdTemplateFlowInactiveTimeout": policyFromVsmartCflowdTemplateFlowInactiveTimeout,
       "policyFromVsmartCflowdTemplateTemplateRefresh": policyFromVsmartCflowdTemplateTemplateRefresh,
       "policyFromVsmartCflowdTemplateFlowSamplingInterval": policyFromVsmartCflowdTemplateFlowSamplingInterval,
       "policyFromVsmartCflowdTemplateCollectorTable": policyFromVsmartCflowdTemplateCollectorTable,
       "policyFromVsmartCflowdTemplateCollectorEntry": policyFromVsmartCflowdTemplateCollectorEntry,
       "policyFromVsmartCflowdTemplateCollectorVpn": policyFromVsmartCflowdTemplateCollectorVpn,
       "policyFromVsmartCflowdTemplateCollectorAddress": policyFromVsmartCflowdTemplateCollectorAddress,
       "policyFromVsmartCflowdTemplateCollectorPort": policyFromVsmartCflowdTemplateCollectorPort,
       "policyFromVsmartCflowdTemplateCollectorTransport": policyFromVsmartCflowdTemplateCollectorTransport,
       "policyFromVsmartCflowdTemplateCollectorSourceInterface": policyFromVsmartCflowdTemplateCollectorSourceInterface,
       "policyFromVsmartAppRoutePolicyTable": policyFromVsmartAppRoutePolicyTable,
       "policyFromVsmartAppRoutePolicyEntry": policyFromVsmartAppRoutePolicyEntry,
       "policyFromVsmartAppRoutePolicyName": policyFromVsmartAppRoutePolicyName,
       "policyFromVsmartAppRoutePolicyVpnListTable": policyFromVsmartAppRoutePolicyVpnListTable,
       "policyFromVsmartAppRoutePolicyVpnListEntry": policyFromVsmartAppRoutePolicyVpnListEntry,
       "policyFromVsmartAppRoutePolicyVpnListName": policyFromVsmartAppRoutePolicyVpnListName,
       "policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName": policyFromVsmartAppRoutePolicyVpnListDefActSlaClassName,
       "policyFromVsmartAppRoutePolicyVpnListSequenceTable": policyFromVsmartAppRoutePolicyVpnListSequenceTable,
       "policyFromVsmartAppRoutePolicyVpnListSequenceEntry": policyFromVsmartAppRoutePolicyVpnListSequenceEntry,
       "policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue": policyFromVsmartAppRoutePolicyVpnListSequenceSeqValue,
       "policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst": policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtPrLst,
       "policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst": policyFromVsmartAppRoutePolicyVpnListSequenceMatchSrcDtV6PrLst,
       "policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst": policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtPrLst,
       "policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst": policyFromVsmartAppRoutePolicyVpnListSequenceMatchDestDtV6PrLst,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionCount": policyFromVsmartAppRoutePolicyVpnListSequenceActionCount,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName": policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClName,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict": policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClStrict,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr": policyFromVsmartAppRoutePolicyVpnListSequenceActionSlaClPrefClr,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionLog": policyFromVsmartAppRoutePolicyVpnListSequenceActionLog,
       "policyFromVsmartAppRoutePolicyVpnListSequenceActionBackupSlaPrefClr": policyFromVsmartAppRoutePolicyVpnListSequenceActionBackupSlaPrefClr,
       "policyFromVsmartPolicerTable": policyFromVsmartPolicerTable,
       "policyFromVsmartPolicerEntry": policyFromVsmartPolicerEntry,
       "policyFromVsmartPolicerName": policyFromVsmartPolicerName,
       "policyFromVsmartPolicerRate": policyFromVsmartPolicerRate,
       "policyFromVsmartPolicerBurst": policyFromVsmartPolicerBurst,
       "policyFromVsmartPolicerExceed": policyFromVsmartPolicerExceed,
       "policyFromVsmartListsVpnListTable": policyFromVsmartListsVpnListTable,
       "policyFromVsmartListsVpnListEntry": policyFromVsmartListsVpnListEntry,
       "policyFromVsmartListsVpnListName": policyFromVsmartListsVpnListName,
       "policyFromVsmartListsVpnListVpnTable": policyFromVsmartListsVpnListVpnTable,
       "policyFromVsmartListsVpnListVpnEntry": policyFromVsmartListsVpnListVpnEntry,
       "policyFromVsmartListsVpnListVpnId": policyFromVsmartListsVpnListVpnId,
       "policyFromVsmartListsDataPrefixListTable": policyFromVsmartListsDataPrefixListTable,
       "policyFromVsmartListsDataPrefixListEntry": policyFromVsmartListsDataPrefixListEntry,
       "policyFromVsmartListsDataPrefixListName": policyFromVsmartListsDataPrefixListName,
       "policyFromVsmartListsDataPrefixListIpPrefixTable": policyFromVsmartListsDataPrefixListIpPrefixTable,
       "policyFromVsmartListsDataPrefixListIpPrefixEntry": policyFromVsmartListsDataPrefixListIpPrefixEntry,
       "policyFromVsmartListsDataPrefixListIpPrefixIp": policyFromVsmartListsDataPrefixListIpPrefixIp,
       "policyFromVsmartListsTlocListTable": policyFromVsmartListsTlocListTable,
       "policyFromVsmartListsTlocListEntry": policyFromVsmartListsTlocListEntry,
       "policyFromVsmartListsTlocListName": policyFromVsmartListsTlocListName,
       "policyFromVsmartListsTlocListTlocTable": policyFromVsmartListsTlocListTlocTable,
       "policyFromVsmartListsTlocListTlocEntry": policyFromVsmartListsTlocListTlocEntry,
       "policyFromVsmartListsTlocListTlocIp": policyFromVsmartListsTlocListTlocIp,
       "policyFromVsmartListsTlocListTlocColor": policyFromVsmartListsTlocListTlocColor,
       "policyFromVsmartListsTlocListTlocEncap": policyFromVsmartListsTlocListTlocEncap,
       "policyFromVsmartListsTlocListTlocPreference": policyFromVsmartListsTlocListTlocPreference,
       "policyDeviceAccessPolicyCounters": policyDeviceAccessPolicyCounters,
       "policyDeviceAccessPolicyCountersTable": policyDeviceAccessPolicyCountersTable,
       "policyDeviceAccessPolicyCountersEntry": policyDeviceAccessPolicyCountersEntry,
       "policyDeviceAccessPolicyCountersName": policyDeviceAccessPolicyCountersName,
       "policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListTable": policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListTable,
       "policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListEntry": policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListEntry,
       "policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName": policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListCounterName,
       "policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListPackets": policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListPackets,
       "policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListBytes": policyDeviceAccessPolicyCountersDeviceAccessPolicyCounterListBytes,
       "policyDeviceAccessPolicyNames": policyDeviceAccessPolicyNames,
       "policyDeviceAccessPolicyNamesTable": policyDeviceAccessPolicyNamesTable,
       "policyDeviceAccessPolicyNamesEntry": policyDeviceAccessPolicyNamesEntry,
       "policyDeviceAccessPolicyNamesName": policyDeviceAccessPolicyNamesName,
       "policerTable": policerTable,
       "policerEntry": policerEntry,
       "policerName": policerName,
       "policerIndex": policerIndex,
       "policerDirection": policerDirection,
       "policerRate": policerRate,
       "policerBurst": policerBurst,
       "policerOosAction": policerOosAction,
       "policerOosPkts": policerOosPkts,
       "policerOosBytes": policerOosBytes,
       "zbfw": zbfw,
       "zonepairInspectSessionTable": zonepairInspectSessionTable,
       "zonepairInspectSessionEntry": zonepairInspectSessionEntry,
       "zonepairInspectSessionZonepairName": zonepairInspectSessionZonepairName,
       "zonepairInspectSessionVpn": zonepairInspectSessionVpn,
       "zonepairInspectSessionSourceIpAddress": zonepairInspectSessionSourceIpAddress,
       "zonepairInspectSessionDestinationIpAddress": zonepairInspectSessionDestinationIpAddress,
       "zonepairInspectSessionSourcePort": zonepairInspectSessionSourcePort,
       "zonepairInspectSessionDestinationPort": zonepairInspectSessionDestinationPort,
       "zonepairInspectSessionProtocol": zonepairInspectSessionProtocol,
       "zonepairInspectSessionSourceVpn": zonepairInspectSessionSourceVpn,
       "zonepairInspectSessionDestinationVpn": zonepairInspectSessionDestinationVpn,
       "zonepairInspectSessionIdleTimeout": zonepairInspectSessionIdleTimeout,
       "zonepairInspectSessionOutboundPackets": zonepairInspectSessionOutboundPackets,
       "zonepairInspectSessionOutboundOctets": zonepairInspectSessionOutboundOctets,
       "zonepairInspectSessionInboundPackets": zonepairInspectSessionInboundPackets,
       "zonepairInspectSessionInboundOctets": zonepairInspectSessionInboundOctets,
       "zonepairInspectSessionFilterState": zonepairInspectSessionFilterState,
       "zoneBasedFirewallStatistics": zoneBasedFirewallStatistics,
       "zoneBasedFirewallStatisticsFragFail": zoneBasedFirewallStatisticsFragFail,
       "zoneBasedFirewallStatisticsStateCheckFail": zoneBasedFirewallStatisticsStateCheckFail,
       "zoneBasedFirewallStatisticsFlowAddFail": zoneBasedFirewallStatisticsFlowAddFail,
       "zoneBasedFirewallStatisticsUnsupportedProto": zoneBasedFirewallStatisticsUnsupportedProto,
       "zoneBasedFirewallStatisticsNumFlowEntries": zoneBasedFirewallStatisticsNumFlowEntries,
       "zoneBasedFirewallStatisticsMaxHalfOpenExceeded": zoneBasedFirewallStatisticsMaxHalfOpenExceeded,
       "zoneBasedFirewallStatisticsFragments": zoneBasedFirewallStatisticsFragments,
       "zoneBasedFirewallStatisticsPolicyChangeDropped": zoneBasedFirewallStatisticsPolicyChangeDropped,
       "zoneBasedFirewallStatisticsNoPairSameZoneAllowed": zoneBasedFirewallStatisticsNoPairSameZoneAllowed,
       "zoneBasedFirewallStatisticsNoPairDiffZoneDropped": zoneBasedFirewallStatisticsNoPairDiffZoneDropped,
       "zoneBasedFirewallStatisticsZoneNoZoneDropped": zoneBasedFirewallStatisticsZoneNoZoneDropped,
       "zoneBasedFirewallStatisticsNoZoneNoZoneAllowed": zoneBasedFirewallStatisticsNoZoneNoZoneAllowed,
       "zoneBasedFirewallStatisticsZoneNoZoneInetAllowed": zoneBasedFirewallStatisticsZoneNoZoneInetAllowed,
       "zoneBasedFirewallStatisticsZoneNoZoneInetDenied": zoneBasedFirewallStatisticsZoneNoZoneInetDenied,
       "zoneBasedFirewallStatisticsTcpRetransSeg": zoneBasedFirewallStatisticsTcpRetransSeg,
       "zoneBasedFirewallStatisticsTcpOooSeg": zoneBasedFirewallStatisticsTcpOooSeg,
       "zoneBasedFirewallStatisticsTcpDropInternalInvalidTcpState": zoneBasedFirewallStatisticsTcpDropInternalInvalidTcpState,
       "zoneBasedFirewallStatisticsTcpDropStraySeg": zoneBasedFirewallStatisticsTcpDropStraySeg,
       "zoneBasedFirewallStatisticsTcpDropInvalidFlags": zoneBasedFirewallStatisticsTcpDropInvalidFlags,
       "zoneBasedFirewallStatisticsTcpDropSynWithData": zoneBasedFirewallStatisticsTcpDropSynWithData,
       "zoneBasedFirewallStatisticsTcpDropInvalidWinScaleOption": zoneBasedFirewallStatisticsTcpDropInvalidWinScaleOption,
       "zoneBasedFirewallStatisticsTcpDropInvalidSegSynsentState": zoneBasedFirewallStatisticsTcpDropInvalidSegSynsentState,
       "zoneBasedFirewallStatisticsTcpDropInvalidAckNum": zoneBasedFirewallStatisticsTcpDropInvalidAckNum,
       "zoneBasedFirewallStatisticsTcpDropInvalidAckFlag": zoneBasedFirewallStatisticsTcpDropInvalidAckFlag,
       "zoneBasedFirewallStatisticsTcpDropRstToResp": zoneBasedFirewallStatisticsTcpDropRstToResp,
       "zoneBasedFirewallStatisticsTcpDropRetransInvalidFlags": zoneBasedFirewallStatisticsTcpDropRetransInvalidFlags,
       "zoneBasedFirewallStatisticsTcpDropRstInWin": zoneBasedFirewallStatisticsTcpDropRstInWin,
       "zoneBasedFirewallStatisticsTcpDropInvalidSeq": zoneBasedFirewallStatisticsTcpDropInvalidSeq,
       "zoneBasedFirewallStatisticsTcpDropInvalidSegSynrcvdState": zoneBasedFirewallStatisticsTcpDropInvalidSegSynrcvdState,
       "zoneBasedFirewallStatisticsTcpDropSynInWin": zoneBasedFirewallStatisticsTcpDropSynInWin,
       "zoneBasedFirewallStatisticsTcpDropUnexpectTcpPyld": zoneBasedFirewallStatisticsTcpDropUnexpectTcpPyld,
       "zoneBasedFirewallStatisticsTcpDropInvalidSegPktTooOld": zoneBasedFirewallStatisticsTcpDropInvalidSegPktTooOld,
       "zoneBasedFirewallStatisticsTcpDropInvalidSegPktWinOverflow": zoneBasedFirewallStatisticsTcpDropInvalidSegPktWinOverflow,
       "zoneBasedFirewallStatisticsTcpDropInvalidSegPyldAfterFinSend": zoneBasedFirewallStatisticsTcpDropInvalidSegPyldAfterFinSend,
       "zoneBasedFirewallStatisticsTcpDropNoSynInListenState": zoneBasedFirewallStatisticsTcpDropNoSynInListenState,
       "zoneBasedFirewallStatisticsTcpDropInvalidDir": zoneBasedFirewallStatisticsTcpDropInvalidDir,
       "zoneBasedFirewallStatisticsZbfPkts": zoneBasedFirewallStatisticsZbfPkts,
       "zoneBasedFirewallStatisticsInvalidFilterDropped": zoneBasedFirewallStatisticsInvalidFilterDropped,
       "zoneBasedFirewallStatisticsMboxMsgFull": zoneBasedFirewallStatisticsMboxMsgFull,
       "zoneBasedFirewallStatisticsFragStateCheckFail": zoneBasedFirewallStatisticsFragStateCheckFail,
       "zoneBasedFirewallStatisticsSelfPkts": zoneBasedFirewallStatisticsSelfPkts,
       "zoneBasedFirewallStatisticsSelfPktsAllowed": zoneBasedFirewallStatisticsSelfPktsAllowed,
       "zoneBasedFirewallStatisticsUmbrellaRegistrPktsAllowed": zoneBasedFirewallStatisticsUmbrellaRegistrPktsAllowed,
       "policyZonePolicyFilterTable": policyZonePolicyFilterTable,
       "policyZonePolicyFilterEntry": policyZonePolicyFilterEntry,
       "policyZonePolicyFilterName": policyZonePolicyFilterName,
       "policyZonePolicyFilterCounterTable": policyZonePolicyFilterCounterTable,
       "policyZonePolicyFilterCounterEntry": policyZonePolicyFilterCounterEntry,
       "policyZonePolicyFilterCounterName": policyZonePolicyFilterCounterName,
       "policyZonePolicyFilterCounterPackets": policyZonePolicyFilterCounterPackets,
       "policyZonePolicyFilterCounterBytes": policyZonePolicyFilterCounterBytes}
)
