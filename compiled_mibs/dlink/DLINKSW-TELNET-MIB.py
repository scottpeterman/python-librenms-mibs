# SNMP MIB module (DLINKSW-TELNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-TELNET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:01 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwTelnetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 40)
)
if mibBuilder.loadTexts:
    dlinkSwTelnetMIB.setRevisions(
        ("2013-04-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DTelnetNotifications_ObjectIdentity = ObjectIdentity
dTelnetNotifications = _DTelnetNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 0)
)
_DTelnetObjects_ObjectIdentity = ObjectIdentity
dTelnetObjects = _DTelnetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1)
)


class _DTelnetServerEnabled_Type(TruthValue):
    """Custom type dTelnetServerEnabled based on TruthValue"""
    defaultValue = 1


_DTelnetServerEnabled_Type.__name__ = "TruthValue"
_DTelnetServerEnabled_Object = MibScalar
dTelnetServerEnabled = _DTelnetServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 1),
    _DTelnetServerEnabled_Type()
)
dTelnetServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTelnetServerEnabled.setStatus("current")


class _DTelnetServerTcpPort_Type(Unsigned32):
    """Custom type dTelnetServerTcpPort based on Unsigned32"""
    defaultValue = 23

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DTelnetServerTcpPort_Type.__name__ = "Unsigned32"
_DTelnetServerTcpPort_Object = MibScalar
dTelnetServerTcpPort = _DTelnetServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 2),
    _DTelnetServerTcpPort_Type()
)
dTelnetServerTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTelnetServerTcpPort.setStatus("current")


class _DTelnetSourceInterfaceIndex_Type(InterfaceIndexOrZero):
    """Custom type dTelnetSourceInterfaceIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_DTelnetSourceInterfaceIndex_Type.__name__ = "InterfaceIndexOrZero"
_DTelnetSourceInterfaceIndex_Object = MibScalar
dTelnetSourceInterfaceIndex = _DTelnetSourceInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 3),
    _DTelnetSourceInterfaceIndex_Type()
)
dTelnetSourceInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTelnetSourceInterfaceIndex.setStatus("current")
_DTelnetSessionTable_Object = MibTable
dTelnetSessionTable = _DTelnetSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 4)
)
if mibBuilder.loadTexts:
    dTelnetSessionTable.setStatus("current")
_DTelnetSessionEntry_Object = MibTableRow
dTelnetSessionEntry = _DTelnetSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 4, 1)
)
dTelnetSessionEntry.setIndexNames(
    (0, "DLINKSW-TELNET-MIB", "dTelnetSessionID"),
)
if mibBuilder.loadTexts:
    dTelnetSessionEntry.setStatus("current")


class _DTelnetSessionID_Type(Unsigned32):
    """Custom type dTelnetSessionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DTelnetSessionID_Type.__name__ = "Unsigned32"
_DTelnetSessionID_Object = MibTableColumn
dTelnetSessionID = _DTelnetSessionID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 4, 1, 1),
    _DTelnetSessionID_Type()
)
dTelnetSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dTelnetSessionID.setStatus("current")


class _DTelnetSessionUserName_Type(SnmpAdminString):
    """Custom type dTelnetSessionUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DTelnetSessionUserName_Type.__name__ = "SnmpAdminString"
_DTelnetSessionUserName_Object = MibTableColumn
dTelnetSessionUserName = _DTelnetSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 4, 1, 2),
    _DTelnetSessionUserName_Type()
)
dTelnetSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTelnetSessionUserName.setStatus("current")


class _DTelnetSessionUserPrivilegeLvl_Type(Unsigned32):
    """Custom type dTelnetSessionUserPrivilegeLvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DTelnetSessionUserPrivilegeLvl_Type.__name__ = "Unsigned32"
_DTelnetSessionUserPrivilegeLvl_Object = MibTableColumn
dTelnetSessionUserPrivilegeLvl = _DTelnetSessionUserPrivilegeLvl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 4, 1, 3),
    _DTelnetSessionUserPrivilegeLvl_Type()
)
dTelnetSessionUserPrivilegeLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTelnetSessionUserPrivilegeLvl.setStatus("current")
_DTelnetSessionLoginDuration_Type = Unsigned32
_DTelnetSessionLoginDuration_Object = MibTableColumn
dTelnetSessionLoginDuration = _DTelnetSessionLoginDuration_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 4, 1, 4),
    _DTelnetSessionLoginDuration_Type()
)
dTelnetSessionLoginDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTelnetSessionLoginDuration.setStatus("current")
if mibBuilder.loadTexts:
    dTelnetSessionLoginDuration.setUnits("seconds")
_DTelnetSessionHostAddrType_Type = InetAddressType
_DTelnetSessionHostAddrType_Object = MibTableColumn
dTelnetSessionHostAddrType = _DTelnetSessionHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 4, 1, 5),
    _DTelnetSessionHostAddrType_Type()
)
dTelnetSessionHostAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTelnetSessionHostAddrType.setStatus("current")
_DTelnetSessionHostAddr_Type = InetAddress
_DTelnetSessionHostAddr_Object = MibTableColumn
dTelnetSessionHostAddr = _DTelnetSessionHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 1, 4, 1, 6),
    _DTelnetSessionHostAddr_Type()
)
dTelnetSessionHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTelnetSessionHostAddr.setStatus("current")
_DTelnetConformance_ObjectIdentity = ObjectIdentity
dTelnetConformance = _DTelnetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 2)
)
_DTelnetCompliances_ObjectIdentity = ObjectIdentity
dTelnetCompliances = _DTelnetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 2, 1)
)
_DTelnetGroups_ObjectIdentity = ObjectIdentity
dTelnetGroups = _DTelnetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 2, 2)
)

# Managed Objects groups

dTelnetConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 2, 2, 1)
)
dTelnetConfigGroup.setObjects(
      *(("DLINKSW-TELNET-MIB", "dTelnetServerEnabled"),
        ("DLINKSW-TELNET-MIB", "dTelnetServerTcpPort"),
        ("DLINKSW-TELNET-MIB", "dTelnetSourceInterfaceIndex"))
)
if mibBuilder.loadTexts:
    dTelnetConfigGroup.setStatus("current")

dTelnetSessionInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 2, 2, 2)
)
dTelnetSessionInfoGroup.setObjects(
      *(("DLINKSW-TELNET-MIB", "dTelnetSessionUserName"),
        ("DLINKSW-TELNET-MIB", "dTelnetSessionUserPrivilegeLvl"),
        ("DLINKSW-TELNET-MIB", "dTelnetSessionLoginDuration"),
        ("DLINKSW-TELNET-MIB", "dTelnetSessionHostAddrType"),
        ("DLINKSW-TELNET-MIB", "dTelnetSessionHostAddr"))
)
if mibBuilder.loadTexts:
    dTelnetSessionInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dTelnetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 40, 2, 1, 1)
)
dTelnetCompliance.setObjects(
      *(("DLINKSW-TELNET-MIB", "dTelnetConfigGroup"),
        ("DLINKSW-TELNET-MIB", "dTelnetSessionInfoGroup"))
)
if mibBuilder.loadTexts:
    dTelnetCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-TELNET-MIB",
    **{"dlinkSwTelnetMIB": dlinkSwTelnetMIB,
       "dTelnetNotifications": dTelnetNotifications,
       "dTelnetObjects": dTelnetObjects,
       "dTelnetServerEnabled": dTelnetServerEnabled,
       "dTelnetServerTcpPort": dTelnetServerTcpPort,
       "dTelnetSourceInterfaceIndex": dTelnetSourceInterfaceIndex,
       "dTelnetSessionTable": dTelnetSessionTable,
       "dTelnetSessionEntry": dTelnetSessionEntry,
       "dTelnetSessionID": dTelnetSessionID,
       "dTelnetSessionUserName": dTelnetSessionUserName,
       "dTelnetSessionUserPrivilegeLvl": dTelnetSessionUserPrivilegeLvl,
       "dTelnetSessionLoginDuration": dTelnetSessionLoginDuration,
       "dTelnetSessionHostAddrType": dTelnetSessionHostAddrType,
       "dTelnetSessionHostAddr": dTelnetSessionHostAddr,
       "dTelnetConformance": dTelnetConformance,
       "dTelnetCompliances": dTelnetCompliances,
       "dTelnetCompliance": dTelnetCompliance,
       "dTelnetGroups": dTelnetGroups,
       "dTelnetConfigGroup": dTelnetConfigGroup,
       "dTelnetSessionInfoGroup": dTelnetSessionInfoGroup}
)
