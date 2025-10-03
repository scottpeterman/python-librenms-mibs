# SNMP MIB module (DLINKSW-AAA-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-AAA-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:34 2025
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

dlinkSwAAACommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150)
)
if mibBuilder.loadTexts:
    dlinkSwAAACommonMIB.setRevisions(
        ("2013-01-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DAaaSessionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("console", 2),
          ("ssh", 3),
          ("http", 4))
    )



class DAaaPrivilegeLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class DAaaMethodListName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class DAaaMethodPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class DAaaMethodName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_DAaaCommonMIBNotifications_ObjectIdentity = ObjectIdentity
dAaaCommonMIBNotifications = _DAaaCommonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 0)
)
_DAaaMIBObjects_ObjectIdentity = ObjectIdentity
dAaaMIBObjects = _DAaaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1)
)
if mibBuilder.loadTexts:
    dAaaMIBObjects.setStatus("current")
_DAaaCommonObjects_ObjectIdentity = ObjectIdentity
dAaaCommonObjects = _DAaaCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 1)
)
if mibBuilder.loadTexts:
    dAaaCommonObjects.setStatus("current")


class _DAaaNewModelEnabled_Type(TruthValue):
    """Custom type dAaaNewModelEnabled based on TruthValue"""
    defaultValue = 2


_DAaaNewModelEnabled_Type.__name__ = "TruthValue"
_DAaaNewModelEnabled_Object = MibScalar
dAaaNewModelEnabled = _DAaaNewModelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 1, 1),
    _DAaaNewModelEnabled_Type()
)
dAaaNewModelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dAaaNewModelEnabled.setStatus("current")
_DAaaCommonMIBConformance_ObjectIdentity = ObjectIdentity
dAaaCommonMIBConformance = _DAaaCommonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 2)
)
_DAaaCommonMIBCompliances_ObjectIdentity = ObjectIdentity
dAaaCommonMIBCompliances = _DAaaCommonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 1)
)
_DAaaCommonMIBGroups_ObjectIdentity = ObjectIdentity
dAaaCommonMIBGroups = _DAaaCommonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 2)
)

# Managed Objects groups

daaaGlobalCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 2, 1)
)
daaaGlobalCtrlGroup.setObjects(
    ("DLINKSW-AAA-COMMON-MIB", "dAaaNewModelEnabled")
)
if mibBuilder.loadTexts:
    daaaGlobalCtrlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

daaaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 1, 1)
)
daaaMIBCompliance.setObjects(
    ("DLINKSW-AAA-COMMON-MIB", "daaaGlobalCtrlGroup")
)
if mibBuilder.loadTexts:
    daaaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-AAA-COMMON-MIB",
    **{"DAaaSessionType": DAaaSessionType,
       "DAaaPrivilegeLevel": DAaaPrivilegeLevel,
       "DAaaMethodListName": DAaaMethodListName,
       "DAaaMethodPriority": DAaaMethodPriority,
       "DAaaMethodName": DAaaMethodName,
       "dlinkSwAAACommonMIB": dlinkSwAAACommonMIB,
       "dAaaCommonMIBNotifications": dAaaCommonMIBNotifications,
       "dAaaMIBObjects": dAaaMIBObjects,
       "dAaaCommonObjects": dAaaCommonObjects,
       "dAaaNewModelEnabled": dAaaNewModelEnabled,
       "dAaaCommonMIBConformance": dAaaCommonMIBConformance,
       "dAaaCommonMIBCompliances": dAaaCommonMIBCompliances,
       "daaaMIBCompliance": daaaMIBCompliance,
       "dAaaCommonMIBGroups": dAaaCommonMIBGroups,
       "daaaGlobalCtrlGroup": daaaGlobalCtrlGroup}
)
