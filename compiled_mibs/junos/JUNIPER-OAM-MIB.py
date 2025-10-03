# SNMP MIB module (JUNIPER-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-OAM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:25 2025
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
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(jnxOamMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxOamMibRoot")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81)
)
if mibBuilder.loadTexts:
    jnxOamMIB.setRevisions(
        ("2016-12-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxOamGreKeepAliveObjects_ObjectIdentity = ObjectIdentity
jnxOamGreKeepAliveObjects = _JnxOamGreKeepAliveObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1)
)
_JnxOamGreKeepAliveStatus_ObjectIdentity = ObjectIdentity
jnxOamGreKeepAliveStatus = _JnxOamGreKeepAliveStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 1)
)
_JnxOamGreKeepAliveStatusTable_Object = MibTable
jnxOamGreKeepAliveStatusTable = _JnxOamGreKeepAliveStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxOamGreKeepAliveStatusTable.setStatus("current")
_JnxOamGreKeepAliveStatusEntry_Object = MibTableRow
jnxOamGreKeepAliveStatusEntry = _JnxOamGreKeepAliveStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 1, 1, 1)
)
jnxOamGreKeepAliveStatusEntry.setIndexNames(
    (0, "JUNIPER-OAM-MIB", "jnxOamGreKeepAliveStatusIfIndex"),
)
if mibBuilder.loadTexts:
    jnxOamGreKeepAliveStatusEntry.setStatus("current")
_JnxOamGreKeepAliveStatusIfIndex_Type = InterfaceIndex
_JnxOamGreKeepAliveStatusIfIndex_Object = MibTableColumn
jnxOamGreKeepAliveStatusIfIndex = _JnxOamGreKeepAliveStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 1, 1, 1, 1),
    _JnxOamGreKeepAliveStatusIfIndex_Type()
)
jnxOamGreKeepAliveStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOamGreKeepAliveStatusIfIndex.setStatus("current")
_JnxOamGreKeepAliveStatusInterfaceName_Type = DisplayString
_JnxOamGreKeepAliveStatusInterfaceName_Object = MibTableColumn
jnxOamGreKeepAliveStatusInterfaceName = _JnxOamGreKeepAliveStatusInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 1, 1, 1, 2),
    _JnxOamGreKeepAliveStatusInterfaceName_Type()
)
jnxOamGreKeepAliveStatusInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxOamGreKeepAliveStatusInterfaceName.setStatus("current")
_JnxOamGreKeepAliveStatusSendCounter_Type = Counter32
_JnxOamGreKeepAliveStatusSendCounter_Object = MibTableColumn
jnxOamGreKeepAliveStatusSendCounter = _JnxOamGreKeepAliveStatusSendCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 1, 1, 1, 3),
    _JnxOamGreKeepAliveStatusSendCounter_Type()
)
jnxOamGreKeepAliveStatusSendCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOamGreKeepAliveStatusSendCounter.setStatus("current")
_JnxOamGreKeepAliveStatusReceiveCounter_Type = Counter32
_JnxOamGreKeepAliveStatusReceiveCounter_Object = MibTableColumn
jnxOamGreKeepAliveStatusReceiveCounter = _JnxOamGreKeepAliveStatusReceiveCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 1, 1, 1, 4),
    _JnxOamGreKeepAliveStatusReceiveCounter_Type()
)
jnxOamGreKeepAliveStatusReceiveCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOamGreKeepAliveStatusReceiveCounter.setStatus("current")


class _JnxOamGreKeepAliveStatusAdjacencyState_Type(Integer32):
    """Custom type jnxOamGreKeepAliveStatusAdjacencyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_JnxOamGreKeepAliveStatusAdjacencyState_Type.__name__ = "Integer32"
_JnxOamGreKeepAliveStatusAdjacencyState_Object = MibTableColumn
jnxOamGreKeepAliveStatusAdjacencyState = _JnxOamGreKeepAliveStatusAdjacencyState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 1, 1, 1, 5),
    _JnxOamGreKeepAliveStatusAdjacencyState_Type()
)
jnxOamGreKeepAliveStatusAdjacencyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOamGreKeepAliveStatusAdjacencyState.setStatus("current")
_JnxOamGreKeepAliveTraps_ObjectIdentity = ObjectIdentity
jnxOamGreKeepAliveTraps = _JnxOamGreKeepAliveTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 2)
)
_JnxOamGreKeepAliveTrapVars_ObjectIdentity = ObjectIdentity
jnxOamGreKeepAliveTrapVars = _JnxOamGreKeepAliveTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 3)
)
_JnxOamGreKeepAliveInterfaceName_Type = DisplayString
_JnxOamGreKeepAliveInterfaceName_Object = MibScalar
jnxOamGreKeepAliveInterfaceName = _JnxOamGreKeepAliveInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 3, 1),
    _JnxOamGreKeepAliveInterfaceName_Type()
)
jnxOamGreKeepAliveInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOamGreKeepAliveInterfaceName.setStatus("current")


class _JnxOamGreKeepAliveAdjacencyState_Type(Integer32):
    """Custom type jnxOamGreKeepAliveAdjacencyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_JnxOamGreKeepAliveAdjacencyState_Type.__name__ = "Integer32"
_JnxOamGreKeepAliveAdjacencyState_Object = MibScalar
jnxOamGreKeepAliveAdjacencyState = _JnxOamGreKeepAliveAdjacencyState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 3, 2),
    _JnxOamGreKeepAliveAdjacencyState_Type()
)
jnxOamGreKeepAliveAdjacencyState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxOamGreKeepAliveAdjacencyState.setStatus("current")

# Managed Objects groups


# Notification objects

jnxOamGreKeepAliveAdjacencyChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 83, 81, 1, 2, 1)
)
jnxOamGreKeepAliveAdjacencyChangeNotif.setObjects(
      *(("JUNIPER-OAM-MIB", "jnxOamGreKeepAliveInterfaceName"),
        ("JUNIPER-OAM-MIB", "jnxOamGreKeepAliveAdjacencyState"))
)
if mibBuilder.loadTexts:
    jnxOamGreKeepAliveAdjacencyChangeNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-OAM-MIB",
    **{"jnxOamMIB": jnxOamMIB,
       "jnxOamGreKeepAliveObjects": jnxOamGreKeepAliveObjects,
       "jnxOamGreKeepAliveStatus": jnxOamGreKeepAliveStatus,
       "jnxOamGreKeepAliveStatusTable": jnxOamGreKeepAliveStatusTable,
       "jnxOamGreKeepAliveStatusEntry": jnxOamGreKeepAliveStatusEntry,
       "jnxOamGreKeepAliveStatusIfIndex": jnxOamGreKeepAliveStatusIfIndex,
       "jnxOamGreKeepAliveStatusInterfaceName": jnxOamGreKeepAliveStatusInterfaceName,
       "jnxOamGreKeepAliveStatusSendCounter": jnxOamGreKeepAliveStatusSendCounter,
       "jnxOamGreKeepAliveStatusReceiveCounter": jnxOamGreKeepAliveStatusReceiveCounter,
       "jnxOamGreKeepAliveStatusAdjacencyState": jnxOamGreKeepAliveStatusAdjacencyState,
       "jnxOamGreKeepAliveTraps": jnxOamGreKeepAliveTraps,
       "jnxOamGreKeepAliveAdjacencyChangeNotif": jnxOamGreKeepAliveAdjacencyChangeNotif,
       "jnxOamGreKeepAliveTrapVars": jnxOamGreKeepAliveTrapVars,
       "jnxOamGreKeepAliveInterfaceName": jnxOamGreKeepAliveInterfaceName,
       "jnxOamGreKeepAliveAdjacencyState": jnxOamGreKeepAliveAdjacencyState}
)
