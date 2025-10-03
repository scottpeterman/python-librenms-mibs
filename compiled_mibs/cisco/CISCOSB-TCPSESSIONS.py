# SNMP MIB module (CISCOSB-TCPSESSIONS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-TCPSESSIONS
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:59 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

tcp = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    tcp.setRevisions(
        ("2011-05-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlTcpSessionTable_Object = MibTable
rlTcpSessionTable = _RlTcpSessionTable_Object(
    (1, 3, 6, 1, 2, 1, 6, 16)
)
if mibBuilder.loadTexts:
    rlTcpSessionTable.setStatus("current")
_RlTcpSessionEntry_Object = MibTableRow
rlTcpSessionEntry = _RlTcpSessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1)
)
rlTcpSessionEntry.setIndexNames(
    (0, "CISCOSB-TCPSESSIONS", "rlTcpSessionLocalAddrType"),
    (0, "CISCOSB-TCPSESSIONS", "rlTcpSessionLocalAddress"),
    (0, "CISCOSB-TCPSESSIONS", "rlTcpSessionLocalPort"),
    (0, "CISCOSB-TCPSESSIONS", "rlTcpSessionRemAddrType"),
    (0, "CISCOSB-TCPSESSIONS", "rlTcpSessionRemAddress"),
    (0, "CISCOSB-TCPSESSIONS", "rlTcpSessionRemPort"),
)
if mibBuilder.loadTexts:
    rlTcpSessionEntry.setStatus("current")
_RlTcpSessionLocalAddrType_Type = InetAddressType
_RlTcpSessionLocalAddrType_Object = MibTableColumn
rlTcpSessionLocalAddrType = _RlTcpSessionLocalAddrType_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 1),
    _RlTcpSessionLocalAddrType_Type()
)
rlTcpSessionLocalAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTcpSessionLocalAddrType.setStatus("current")
_RlTcpSessionLocalAddress_Type = InetAddress
_RlTcpSessionLocalAddress_Object = MibTableColumn
rlTcpSessionLocalAddress = _RlTcpSessionLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 2),
    _RlTcpSessionLocalAddress_Type()
)
rlTcpSessionLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTcpSessionLocalAddress.setStatus("current")


class _RlTcpSessionLocalPort_Type(Integer32):
    """Custom type rlTcpSessionLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlTcpSessionLocalPort_Type.__name__ = "Integer32"
_RlTcpSessionLocalPort_Object = MibTableColumn
rlTcpSessionLocalPort = _RlTcpSessionLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 3),
    _RlTcpSessionLocalPort_Type()
)
rlTcpSessionLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTcpSessionLocalPort.setStatus("current")
_RlTcpSessionRemAddrType_Type = InetAddressType
_RlTcpSessionRemAddrType_Object = MibTableColumn
rlTcpSessionRemAddrType = _RlTcpSessionRemAddrType_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 4),
    _RlTcpSessionRemAddrType_Type()
)
rlTcpSessionRemAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTcpSessionRemAddrType.setStatus("current")
_RlTcpSessionRemAddress_Type = InetAddress
_RlTcpSessionRemAddress_Object = MibTableColumn
rlTcpSessionRemAddress = _RlTcpSessionRemAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 5),
    _RlTcpSessionRemAddress_Type()
)
rlTcpSessionRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTcpSessionRemAddress.setStatus("current")


class _RlTcpSessionRemPort_Type(Integer32):
    """Custom type rlTcpSessionRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlTcpSessionRemPort_Type.__name__ = "Integer32"
_RlTcpSessionRemPort_Object = MibTableColumn
rlTcpSessionRemPort = _RlTcpSessionRemPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 6),
    _RlTcpSessionRemPort_Type()
)
rlTcpSessionRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlTcpSessionRemPort.setStatus("current")


class _RlTcpSessionState_Type(Integer32):
    """Custom type rlTcpSessionState based on Integer32"""
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
        *(("closed", 1),
          ("listen", 2),
          ("synSent", 3),
          ("synReceived", 4),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("closeWait", 8),
          ("lastAck", 9),
          ("closing", 10),
          ("timeWait", 11),
          ("deleteTCB", 12))
    )


_RlTcpSessionState_Type.__name__ = "Integer32"
_RlTcpSessionState_Object = MibTableColumn
rlTcpSessionState = _RlTcpSessionState_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 7),
    _RlTcpSessionState_Type()
)
rlTcpSessionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTcpSessionState.setStatus("current")


class _RlTcpSessionAppName_Type(DisplayString):
    """Custom type rlTcpSessionAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RlTcpSessionAppName_Type.__name__ = "DisplayString"
_RlTcpSessionAppName_Object = MibTableColumn
rlTcpSessionAppName = _RlTcpSessionAppName_Object(
    (1, 3, 6, 1, 2, 1, 6, 16, 1, 8),
    _RlTcpSessionAppName_Type()
)
rlTcpSessionAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTcpSessionAppName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-TCPSESSIONS",
    **{"tcp": tcp,
       "rlTcpSessionTable": rlTcpSessionTable,
       "rlTcpSessionEntry": rlTcpSessionEntry,
       "rlTcpSessionLocalAddrType": rlTcpSessionLocalAddrType,
       "rlTcpSessionLocalAddress": rlTcpSessionLocalAddress,
       "rlTcpSessionLocalPort": rlTcpSessionLocalPort,
       "rlTcpSessionRemAddrType": rlTcpSessionRemAddrType,
       "rlTcpSessionRemAddress": rlTcpSessionRemAddress,
       "rlTcpSessionRemPort": rlTcpSessionRemPort,
       "rlTcpSessionState": rlTcpSessionState,
       "rlTcpSessionAppName": rlTcpSessionAppName}
)
