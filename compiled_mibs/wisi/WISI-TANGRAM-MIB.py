# SNMP MIB module (WISI-TANGRAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\wisi\WISI-TANGRAM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:17 2025
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

(tangram,) = mibBuilder.importSymbols(
    "WISI-ROOT-MIB",
    "tangram")


# MODULE-IDENTITY

tangramMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 0)
)
if mibBuilder.loadTexts:
    tangramMIB.setRevisions(
        ("2016-09-08 00:00",
         "2014-04-29 00:00",
         "2012-12-06 09:00",
         "2012-10-31 00:00",
         "2011-12-13 00:00",
         "2011-04-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FloatingPoint(TextualConvention, OctetString):
    status = "current"
    displayHint = "63a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



# MIB Managed Objects in the order of their OIDs

_GtUnit_ObjectIdentity = ObjectIdentity
gtUnit = _GtUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1)
)
_GtGeneric_ObjectIdentity = ObjectIdentity
gtGeneric = _GtGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4)
)
_GtGenericNotifications_ObjectIdentity = ObjectIdentity
gtGenericNotifications = _GtGenericNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 0)
)
_GtGenericObjects_ObjectIdentity = ObjectIdentity
gtGenericObjects = _GtGenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 1)
)
_GtGenericObjectUsertrap_Type = Integer32
_GtGenericObjectUsertrap_Object = MibScalar
gtGenericObjectUsertrap = _GtGenericObjectUsertrap_Object(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 1, 1),
    _GtGenericObjectUsertrap_Type()
)
gtGenericObjectUsertrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gtGenericObjectUsertrap.setStatus("current")
_GtStandards_ObjectIdentity = ObjectIdentity
gtStandards = _GtStandards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4)
)
_GtIP_ObjectIdentity = ObjectIdentity
gtIP = _GtIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4, 1)
)
_GtRF_ObjectIdentity = ObjectIdentity
gtRF = _GtRF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4, 3)
)
_GtDVB_ObjectIdentity = ObjectIdentity
gtDVB = _GtDVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4, 4)
)
_GtTS_ObjectIdentity = ObjectIdentity
gtTS = _GtTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 5)
)
_GtProcessing_ObjectIdentity = ObjectIdentity
gtProcessing = _GtProcessing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 6)
)

# Managed Objects groups


# Notification objects

gtGenericNotifyUsertrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 0, 1)
)
if mibBuilder.loadTexts:
    gtGenericNotifyUsertrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WISI-TANGRAM-MIB",
    **{"FloatingPoint": FloatingPoint,
       "tangramMIB": tangramMIB,
       "gtUnit": gtUnit,
       "gtGeneric": gtGeneric,
       "gtGenericNotifications": gtGenericNotifications,
       "gtGenericNotifyUsertrap": gtGenericNotifyUsertrap,
       "gtGenericObjects": gtGenericObjects,
       "gtGenericObjectUsertrap": gtGenericObjectUsertrap,
       "gtStandards": gtStandards,
       "gtIP": gtIP,
       "gtRF": gtRF,
       "gtDVB": gtDVB,
       "gtTS": gtTS,
       "gtProcessing": gtProcessing}
)
