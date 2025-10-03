# SNMP MIB module (NETELASTIC-FLEXBNG-PPPOE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\netelastic\NETELASTIC-FLEXBNG-PPPOE
# Produced by pysmi-1.6.2 at Thu Oct  2 12:11:45 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(bras,) = mibBuilder.importSymbols(
    "NETELASTIC-FLEXBNG-MIB",
    "bras")

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


# MODULE-IDENTITY

pppoeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pppoeMib.setRevisions(
        ("2015-11-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class HexList(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"


class Ppp_auth_type(TextualConvention, Integer32):
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
        *(("pap", 0),
          ("chap", 1),
          ("auto", 2))
    )



class Info_user_type(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pppoe", 0),
          ("l2tp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Connection_success_Type = Unsigned32
_Connection_success_Object = MibScalar
connection_success = _Connection_success_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 1),
    _Connection_success_Type()
)
connection_success.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connection_success.setStatus("current")
_Connection_Type = Unsigned32
_Connection_Object = MibScalar
connection = _Connection_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 2),
    _Connection_Type()
)
connection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connection.setStatus("current")
_Discovery_timeout_Type = Unsigned32
_Discovery_timeout_Object = MibScalar
discovery_timeout = _Discovery_timeout_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 3),
    _Discovery_timeout_Type()
)
discovery_timeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    discovery_timeout.setStatus("current")
_Lcp_fail_Type = Unsigned32
_Lcp_fail_Object = MibScalar
lcp_fail = _Lcp_fail_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 4),
    _Lcp_fail_Type()
)
lcp_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcp_fail.setStatus("current")
_Lcp_fail_other_Type = Unsigned32
_Lcp_fail_other_Object = MibScalar
lcp_fail_other = _Lcp_fail_other_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 5),
    _Lcp_fail_other_Type()
)
lcp_fail_other.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcp_fail_other.setStatus("current")
_Auth_fail_Type = Unsigned32
_Auth_fail_Object = MibScalar
auth_fail = _Auth_fail_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 6),
    _Auth_fail_Type()
)
auth_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auth_fail.setStatus("current")
_Auth_fail_other_Type = Unsigned32
_Auth_fail_other_Object = MibScalar
auth_fail_other = _Auth_fail_other_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 7),
    _Auth_fail_other_Type()
)
auth_fail_other.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auth_fail_other.setStatus("current")
_Ipcp_fail_Type = Unsigned32
_Ipcp_fail_Object = MibScalar
ipcp_fail = _Ipcp_fail_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 8),
    _Ipcp_fail_Type()
)
ipcp_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcp_fail.setStatus("current")
_Ipcp_fail_other_Type = Unsigned32
_Ipcp_fail_other_Object = MibScalar
ipcp_fail_other = _Ipcp_fail_other_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 9),
    _Ipcp_fail_other_Type()
)
ipcp_fail_other.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipcp_fail_other.setStatus("current")
_Ipv4_assign_fail_Type = Unsigned32
_Ipv4_assign_fail_Object = MibScalar
ipv4_assign_fail = _Ipv4_assign_fail_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 10),
    _Ipv4_assign_fail_Type()
)
ipv4_assign_fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv4_assign_fail.setStatus("current")
_User_disconnect_Type = Unsigned32
_User_disconnect_Object = MibScalar
user_disconnect = _User_disconnect_Object(
    (1, 3, 6, 1, 4, 1, 54268, 1, 1, 1, 11),
    _User_disconnect_Type()
)
user_disconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user_disconnect.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETELASTIC-FLEXBNG-PPPOE",
    **{"UnsignedShort": UnsignedShort,
       "String": String,
       "HexList": HexList,
       "Ppp-auth-type": Ppp_auth_type,
       "Info-user-type": Info_user_type,
       "pppoeMib": pppoeMib,
       "connection-success": connection_success,
       "connection": connection,
       "discovery-timeout": discovery_timeout,
       "lcp-fail": lcp_fail,
       "lcp-fail-other": lcp_fail_other,
       "auth-fail": auth_fail,
       "auth-fail-other": auth_fail_other,
       "ipcp-fail": ipcp_fail,
       "ipcp-fail-other": ipcp_fail_other,
       "ipv4-assign-fail": ipv4_assign_fail,
       "user-disconnect": user_disconnect}
)
