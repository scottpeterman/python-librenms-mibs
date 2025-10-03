# SNMP MIB module (LINKSYS-TELNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-TELNET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:04 2025
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

(rnd,) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlTelnet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58)
)
if mibBuilder.loadTexts:
    rlTelnet.setRevisions(
        ("2008-11-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlTelnetMibVersion_Type = Integer32
_RlTelnetMibVersion_Object = MibScalar
rlTelnetMibVersion = _RlTelnetMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 1),
    _RlTelnetMibVersion_Type()
)
rlTelnetMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTelnetMibVersion.setStatus("current")


class _RlTelnetPassword_Type(DisplayString):
    """Custom type rlTelnetPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlTelnetPassword_Type.__name__ = "DisplayString"
_RlTelnetPassword_Object = MibScalar
rlTelnetPassword = _RlTelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 2),
    _RlTelnetPassword_Type()
)
rlTelnetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetPassword.setStatus("current")


class _RlTelnetTimeout_Type(Integer32):
    """Custom type rlTelnetTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlTelnetTimeout_Type.__name__ = "Integer32"
_RlTelnetTimeout_Object = MibScalar
rlTelnetTimeout = _RlTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 3),
    _RlTelnetTimeout_Type()
)
rlTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetTimeout.setStatus("current")
_RlTelnetUsersTable_Object = MibTable
rlTelnetUsersTable = _RlTelnetUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 4)
)
if mibBuilder.loadTexts:
    rlTelnetUsersTable.setStatus("current")
_RlTelnetUsersEntry_Object = MibTableRow
rlTelnetUsersEntry = _RlTelnetUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 4, 1)
)
rlTelnetUsersEntry.setIndexNames(
    (0, "LINKSYS-TELNET-MIB", "rlTelnetSessionId"),
)
if mibBuilder.loadTexts:
    rlTelnetUsersEntry.setStatus("current")
_RlTelnetSessionId_Type = Integer32
_RlTelnetSessionId_Object = MibTableColumn
rlTelnetSessionId = _RlTelnetSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 4, 1, 1),
    _RlTelnetSessionId_Type()
)
rlTelnetSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTelnetSessionId.setStatus("current")
_RlTelnetSessionClientAddressType_Type = InetAddressType
_RlTelnetSessionClientAddressType_Object = MibTableColumn
rlTelnetSessionClientAddressType = _RlTelnetSessionClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 4, 1, 2),
    _RlTelnetSessionClientAddressType_Type()
)
rlTelnetSessionClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTelnetSessionClientAddressType.setStatus("current")
_RlTelnetSessionClientAddress_Type = InetAddress
_RlTelnetSessionClientAddress_Object = MibTableColumn
rlTelnetSessionClientAddress = _RlTelnetSessionClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 4, 1, 3),
    _RlTelnetSessionClientAddress_Type()
)
rlTelnetSessionClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTelnetSessionClientAddress.setStatus("current")
_RlTelnetSessionLoginTime_Type = DisplayString
_RlTelnetSessionLoginTime_Object = MibTableColumn
rlTelnetSessionLoginTime = _RlTelnetSessionLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 4, 1, 4),
    _RlTelnetSessionLoginTime_Type()
)
rlTelnetSessionLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTelnetSessionLoginTime.setStatus("current")


class _RlTelnetSessionStatus_Type(Integer32):
    """Custom type rlTelnetSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnect", 2))
    )


_RlTelnetSessionStatus_Type.__name__ = "Integer32"
_RlTelnetSessionStatus_Object = MibTableColumn
rlTelnetSessionStatus = _RlTelnetSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 4, 1, 5),
    _RlTelnetSessionStatus_Type()
)
rlTelnetSessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetSessionStatus.setStatus("current")
_RlTelnetLoginBanner_Type = DisplayString
_RlTelnetLoginBanner_Object = MibScalar
rlTelnetLoginBanner = _RlTelnetLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 5),
    _RlTelnetLoginBanner_Type()
)
rlTelnetLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetLoginBanner.setStatus("current")
_RlTelnetSecondLoginBanner_Type = DisplayString
_RlTelnetSecondLoginBanner_Object = MibScalar
rlTelnetSecondLoginBanner = _RlTelnetSecondLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 6),
    _RlTelnetSecondLoginBanner_Type()
)
rlTelnetSecondLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetSecondLoginBanner.setStatus("current")
_RlTelnetEnable_Type = TruthValue
_RlTelnetEnable_Object = MibScalar
rlTelnetEnable = _RlTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 58, 7),
    _RlTelnetEnable_Type()
)
rlTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTelnetEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-TELNET-MIB",
    **{"rlTelnet": rlTelnet,
       "rlTelnetMibVersion": rlTelnetMibVersion,
       "rlTelnetPassword": rlTelnetPassword,
       "rlTelnetTimeout": rlTelnetTimeout,
       "rlTelnetUsersTable": rlTelnetUsersTable,
       "rlTelnetUsersEntry": rlTelnetUsersEntry,
       "rlTelnetSessionId": rlTelnetSessionId,
       "rlTelnetSessionClientAddressType": rlTelnetSessionClientAddressType,
       "rlTelnetSessionClientAddress": rlTelnetSessionClientAddress,
       "rlTelnetSessionLoginTime": rlTelnetSessionLoginTime,
       "rlTelnetSessionStatus": rlTelnetSessionStatus,
       "rlTelnetLoginBanner": rlTelnetLoginBanner,
       "rlTelnetSecondLoginBanner": rlTelnetSecondLoginBanner,
       "rlTelnetEnable": rlTelnetEnable}
)
