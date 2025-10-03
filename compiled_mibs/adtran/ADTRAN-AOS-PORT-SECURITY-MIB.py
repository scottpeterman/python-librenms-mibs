# SNMP MIB module (ADTRAN-AOS-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adtran\ADTRAN-AOS-PORT-SECURITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:14:23 2025
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

(adGenAOSSwitch,) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSSwitch")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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

adGenAOSPortSecurityID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSPortSecurity_ObjectIdentity = ObjectIdentity
adGenAOSPortSecurity = _AdGenAOSPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1)
)
_AdGenAOSPortSecurityTraps_ObjectIdentity = ObjectIdentity
adGenAOSPortSecurityTraps = _AdGenAOSPortSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1, 0)
)

# Managed Objects groups


# Notification objects

adGenAOSPortSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 1, 0, 0)
)
adGenAOSPortSecurityViolation.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    adGenAOSPortSecurityViolation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-PORT-SECURITY-MIB",
    **{"adGenAOSPortSecurity": adGenAOSPortSecurity,
       "adGenAOSPortSecurityTraps": adGenAOSPortSecurityTraps,
       "adGenAOSPortSecurityViolation": adGenAOSPortSecurityViolation,
       "adGenAOSPortSecurityID": adGenAOSPortSecurityID}
)
