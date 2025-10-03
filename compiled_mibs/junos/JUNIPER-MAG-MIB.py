# SNMP MIB module (JUNIPER-MAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-MAG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:03:59 2025
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

(jnxMagMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMagMibRoot")

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

jnxMagMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1)
)
if mibBuilder.loadTexts:
    jnxMagMib.setRevisions(
        ("2010-02-20 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMagNotifications_ObjectIdentity = ObjectIdentity
jnxMagNotifications = _JnxMagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 0)
)
_JnxMagObjects_ObjectIdentity = ObjectIdentity
jnxMagObjects = _JnxMagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1)
)
_JnxMagSSOObjects_ObjectIdentity = ObjectIdentity
jnxMagSSOObjects = _JnxMagSSOObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1)
)
_JnxMagSSOAuthTokenAttempt_Type = Counter32
_JnxMagSSOAuthTokenAttempt_Object = MibScalar
jnxMagSSOAuthTokenAttempt = _JnxMagSSOAuthTokenAttempt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1, 1),
    _JnxMagSSOAuthTokenAttempt_Type()
)
jnxMagSSOAuthTokenAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMagSSOAuthTokenAttempt.setStatus("current")
_JnxMagSSOFailedAuthToken_Type = Counter32
_JnxMagSSOFailedAuthToken_Object = MibScalar
jnxMagSSOFailedAuthToken = _JnxMagSSOFailedAuthToken_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 1, 1, 2),
    _JnxMagSSOFailedAuthToken_Type()
)
jnxMagSSOFailedAuthToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMagSSOFailedAuthToken.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMagSSOValidationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 65, 1, 0, 1)
)
if mibBuilder.loadTexts:
    jnxMagSSOValidationError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MAG-MIB",
    **{"jnxMagMib": jnxMagMib,
       "jnxMagNotifications": jnxMagNotifications,
       "jnxMagSSOValidationError": jnxMagSSOValidationError,
       "jnxMagObjects": jnxMagObjects,
       "jnxMagSSOObjects": jnxMagSSOObjects,
       "jnxMagSSOAuthTokenAttempt": jnxMagSSOAuthTokenAttempt,
       "jnxMagSSOFailedAuthToken": jnxMagSSOFailedAuthToken}
)
