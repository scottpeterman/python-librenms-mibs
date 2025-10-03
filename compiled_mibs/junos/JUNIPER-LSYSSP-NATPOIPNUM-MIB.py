# SNMP MIB module (JUNIPER-LSYSSP-NATPOIPNUM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-LSYSSP-NATPOIPNUM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:47 2025
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

(jnxLsysSpNATpoipnum,) = mibBuilder.importSymbols(
    "JUNIPER-LSYS-SECURITYPROFILE-MIB",
    "jnxLsysSpNATpoipnum")

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

jnxLsysSpNATpoipnumMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxLsysSpNATpoipnumObjects_ObjectIdentity = ObjectIdentity
jnxLsysSpNATpoipnumObjects = _JnxLsysSpNATpoipnumObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 1)
)
_JnxLsysSpNATpoipnumTable_Object = MibTable
jnxLsysSpNATpoipnumTable = _JnxLsysSpNATpoipnumTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumTable.setStatus("current")
_JnxLsysSpNATpoipnumEntry_Object = MibTableRow
jnxLsysSpNATpoipnumEntry = _JnxLsysSpNATpoipnumEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 1, 1, 1)
)
jnxLsysSpNATpoipnumEntry.setIndexNames(
    (1, "JUNIPER-LSYSSP-NATPOIPNUM-MIB", "jnxLsysSpNATpoipnumLsysName"),
)
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumEntry.setStatus("current")


class _JnxLsysSpNATpoipnumLsysName_Type(DisplayString):
    """Custom type jnxLsysSpNATpoipnumLsysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATpoipnumLsysName_Type.__name__ = "DisplayString"
_JnxLsysSpNATpoipnumLsysName_Object = MibTableColumn
jnxLsysSpNATpoipnumLsysName = _JnxLsysSpNATpoipnumLsysName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 1, 1, 1, 1),
    _JnxLsysSpNATpoipnumLsysName_Type()
)
jnxLsysSpNATpoipnumLsysName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumLsysName.setStatus("current")


class _JnxLsysSpNATpoipnumProfileName_Type(DisplayString):
    """Custom type jnxLsysSpNATpoipnumProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxLsysSpNATpoipnumProfileName_Type.__name__ = "DisplayString"
_JnxLsysSpNATpoipnumProfileName_Object = MibTableColumn
jnxLsysSpNATpoipnumProfileName = _JnxLsysSpNATpoipnumProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 1, 1, 1, 2),
    _JnxLsysSpNATpoipnumProfileName_Type()
)
jnxLsysSpNATpoipnumProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumProfileName.setStatus("current")
_JnxLsysSpNATpoipnumUsage_Type = Unsigned32
_JnxLsysSpNATpoipnumUsage_Object = MibTableColumn
jnxLsysSpNATpoipnumUsage = _JnxLsysSpNATpoipnumUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 1, 1, 1, 3),
    _JnxLsysSpNATpoipnumUsage_Type()
)
jnxLsysSpNATpoipnumUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumUsage.setStatus("current")
_JnxLsysSpNATpoipnumReserved_Type = Unsigned32
_JnxLsysSpNATpoipnumReserved_Object = MibTableColumn
jnxLsysSpNATpoipnumReserved = _JnxLsysSpNATpoipnumReserved_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 1, 1, 1, 4),
    _JnxLsysSpNATpoipnumReserved_Type()
)
jnxLsysSpNATpoipnumReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumReserved.setStatus("current")
_JnxLsysSpNATpoipnumMaximum_Type = Unsigned32
_JnxLsysSpNATpoipnumMaximum_Object = MibTableColumn
jnxLsysSpNATpoipnumMaximum = _JnxLsysSpNATpoipnumMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 1, 1, 1, 5),
    _JnxLsysSpNATpoipnumMaximum_Type()
)
jnxLsysSpNATpoipnumMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumMaximum.setStatus("current")
_JnxLsysSpNATpoipnumSummary_ObjectIdentity = ObjectIdentity
jnxLsysSpNATpoipnumSummary = _JnxLsysSpNATpoipnumSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 2)
)
_JnxLsysSpNATpoipnumUsedAmount_Type = Unsigned32
_JnxLsysSpNATpoipnumUsedAmount_Object = MibScalar
jnxLsysSpNATpoipnumUsedAmount = _JnxLsysSpNATpoipnumUsedAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 2, 1),
    _JnxLsysSpNATpoipnumUsedAmount_Type()
)
jnxLsysSpNATpoipnumUsedAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumUsedAmount.setStatus("current")
_JnxLsysSpNATpoipnumMaxQuota_Type = Unsigned32
_JnxLsysSpNATpoipnumMaxQuota_Object = MibScalar
jnxLsysSpNATpoipnumMaxQuota = _JnxLsysSpNATpoipnumMaxQuota_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 2, 2),
    _JnxLsysSpNATpoipnumMaxQuota_Type()
)
jnxLsysSpNATpoipnumMaxQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumMaxQuota.setStatus("current")
_JnxLsysSpNATpoipnumAvailableAmount_Type = Unsigned32
_JnxLsysSpNATpoipnumAvailableAmount_Object = MibScalar
jnxLsysSpNATpoipnumAvailableAmount = _JnxLsysSpNATpoipnumAvailableAmount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 2, 3),
    _JnxLsysSpNATpoipnumAvailableAmount_Type()
)
jnxLsysSpNATpoipnumAvailableAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumAvailableAmount.setStatus("current")
_JnxLsysSpNATpoipnumHeaviestUsage_Type = Unsigned32
_JnxLsysSpNATpoipnumHeaviestUsage_Object = MibScalar
jnxLsysSpNATpoipnumHeaviestUsage = _JnxLsysSpNATpoipnumHeaviestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 2, 4),
    _JnxLsysSpNATpoipnumHeaviestUsage_Type()
)
jnxLsysSpNATpoipnumHeaviestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumHeaviestUsage.setStatus("current")


class _JnxLsysSpNATpoipnumHeaviestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATpoipnumHeaviestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATpoipnumHeaviestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATpoipnumHeaviestUser_Object = MibScalar
jnxLsysSpNATpoipnumHeaviestUser = _JnxLsysSpNATpoipnumHeaviestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 2, 5),
    _JnxLsysSpNATpoipnumHeaviestUser_Type()
)
jnxLsysSpNATpoipnumHeaviestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumHeaviestUser.setStatus("current")
_JnxLsysSpNATpoipnumLightestUsage_Type = Unsigned32
_JnxLsysSpNATpoipnumLightestUsage_Object = MibScalar
jnxLsysSpNATpoipnumLightestUsage = _JnxLsysSpNATpoipnumLightestUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 2, 6),
    _JnxLsysSpNATpoipnumLightestUsage_Type()
)
jnxLsysSpNATpoipnumLightestUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumLightestUsage.setStatus("current")


class _JnxLsysSpNATpoipnumLightestUser_Type(DisplayString):
    """Custom type jnxLsysSpNATpoipnumLightestUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxLsysSpNATpoipnumLightestUser_Type.__name__ = "DisplayString"
_JnxLsysSpNATpoipnumLightestUser_Object = MibScalar
jnxLsysSpNATpoipnumLightestUser = _JnxLsysSpNATpoipnumLightestUser_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 16, 1, 2, 7),
    _JnxLsysSpNATpoipnumLightestUser_Type()
)
jnxLsysSpNATpoipnumLightestUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLsysSpNATpoipnumLightestUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-LSYSSP-NATPOIPNUM-MIB",
    **{"jnxLsysSpNATpoipnumMIB": jnxLsysSpNATpoipnumMIB,
       "jnxLsysSpNATpoipnumObjects": jnxLsysSpNATpoipnumObjects,
       "jnxLsysSpNATpoipnumTable": jnxLsysSpNATpoipnumTable,
       "jnxLsysSpNATpoipnumEntry": jnxLsysSpNATpoipnumEntry,
       "jnxLsysSpNATpoipnumLsysName": jnxLsysSpNATpoipnumLsysName,
       "jnxLsysSpNATpoipnumProfileName": jnxLsysSpNATpoipnumProfileName,
       "jnxLsysSpNATpoipnumUsage": jnxLsysSpNATpoipnumUsage,
       "jnxLsysSpNATpoipnumReserved": jnxLsysSpNATpoipnumReserved,
       "jnxLsysSpNATpoipnumMaximum": jnxLsysSpNATpoipnumMaximum,
       "jnxLsysSpNATpoipnumSummary": jnxLsysSpNATpoipnumSummary,
       "jnxLsysSpNATpoipnumUsedAmount": jnxLsysSpNATpoipnumUsedAmount,
       "jnxLsysSpNATpoipnumMaxQuota": jnxLsysSpNATpoipnumMaxQuota,
       "jnxLsysSpNATpoipnumAvailableAmount": jnxLsysSpNATpoipnumAvailableAmount,
       "jnxLsysSpNATpoipnumHeaviestUsage": jnxLsysSpNATpoipnumHeaviestUsage,
       "jnxLsysSpNATpoipnumHeaviestUser": jnxLsysSpNATpoipnumHeaviestUser,
       "jnxLsysSpNATpoipnumLightestUsage": jnxLsysSpNATpoipnumLightestUsage,
       "jnxLsysSpNATpoipnumLightestUser": jnxLsysSpNATpoipnumLightestUser}
)
