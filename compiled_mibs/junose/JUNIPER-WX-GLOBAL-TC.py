# SNMP MIB module (JUNIPER-WX-GLOBAL-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\juniper\JUNIPER-WX-GLOBAL-TC
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:01 2025
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

(jnxWxModules,) = mibBuilder.importSymbols(
    "JUNIPER-WX-GLOBAL-REG",
    "jnxWxModules")

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

jnxWxGlobalTcModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxWxGlobalTcModule.setRevisions(
        ("2006-06-08 18:00",
         "2005-05-09 10:10",
         "2004-03-15 14:00",
         "2003-06-26 20:00",
         "2002-11-07 19:00",
         "2001-07-29 22:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TcAppName(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TcQosIdentifier(TextualConvention, OctetString):
    status = "current"
    displayHint = "24a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )



class TcChassisType(TextualConvention, Integer32):
    status = "current"
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("jnxWxOther", 1),
          ("jnxWx50", 2),
          ("jnxWx20", 3),
          ("jnxWx80", 4),
          ("jnxWx100", 5),
          ("jnxWxc500", 6),
          ("jnxWx15", 7),
          ("jnxWxc250", 8),
          ("jnxWx100V3", 9),
          ("jnxWx60", 10),
          ("jnxWxc590", 11),
          ("jnxIsm200Wxc", 12),
          ("jnxWxc1800", 13),
          ("jnxWxc2600", 14),
          ("jnxWxc3400", 15))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-WX-GLOBAL-TC",
    **{"TcAppName": TcAppName,
       "TcQosIdentifier": TcQosIdentifier,
       "TcChassisType": TcChassisType,
       "jnxWxGlobalTcModule": jnxWxGlobalTcModule}
)
