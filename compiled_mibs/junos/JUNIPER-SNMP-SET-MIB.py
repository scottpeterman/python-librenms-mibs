# SNMP MIB module (JUNIPER-SNMP-SET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-SNMP-SET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:45 2025
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

(jnxSnmpSetMibRoot,
 jnxSnmpSetTraps) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxSnmpSetMibRoot",
    "jnxSnmpSetTraps")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxSnmpSetMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 76, 1)
)
if mibBuilder.loadTexts:
    jnxSnmpSetMib.setRevisions(
        ("2013-11-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxSnmpSet_ObjectIdentity = ObjectIdentity
jnxSnmpSet = _JnxSnmpSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 76, 1, 1)
)
_JnxCommitSetFailureReason_Type = DisplayString
_JnxCommitSetFailureReason_Object = MibScalar
jnxCommitSetFailureReason = _JnxCommitSetFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 76, 1, 1, 1),
    _JnxCommitSetFailureReason_Type()
)
jnxCommitSetFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxCommitSetFailureReason.setStatus("current")
_JnxSnmpSetNotifications_ObjectIdentity = ObjectIdentity
jnxSnmpSetNotifications = _JnxSnmpSetNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 24, 1)
)

# Managed Objects groups


# Notification objects

jnxSnmpSetFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 24, 1, 1)
)
jnxSnmpSetFailure.setObjects(
    ("JUNIPER-SNMP-SET-MIB", "jnxCommitSetFailureReason")
)
if mibBuilder.loadTexts:
    jnxSnmpSetFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SNMP-SET-MIB",
    **{"jnxSnmpSetMib": jnxSnmpSetMib,
       "jnxSnmpSet": jnxSnmpSet,
       "jnxCommitSetFailureReason": jnxCommitSetFailureReason,
       "jnxSnmpSetNotifications": jnxSnmpSetNotifications,
       "jnxSnmpSetFailure": jnxSnmpSetFailure}
)
