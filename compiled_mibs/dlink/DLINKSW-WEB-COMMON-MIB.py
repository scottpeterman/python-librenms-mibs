# SNMP MIB module (DLINKSW-WEB-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-WEB-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:38:11 2025
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

dlinkSwWebCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 162)
)
if mibBuilder.loadTexts:
    dlinkSwWebCommonMIB.setRevisions(
        ("2013-10-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DWebCommonMIBNotifications_ObjectIdentity = ObjectIdentity
dWebCommonMIBNotifications = _DWebCommonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 0)
)
_DWebMIBObjects_ObjectIdentity = ObjectIdentity
dWebMIBObjects = _DWebMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 1)
)
_DHttpServerObjects_ObjectIdentity = ObjectIdentity
dHttpServerObjects = _DHttpServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1)
)


class _DHttpServerStatus_Type(TruthValue):
    """Custom type dHttpServerStatus based on TruthValue"""
    defaultValue = 1


_DHttpServerStatus_Type.__name__ = "TruthValue"
_DHttpServerStatus_Object = MibScalar
dHttpServerStatus = _DHttpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 1),
    _DHttpServerStatus_Type()
)
dHttpServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dHttpServerStatus.setStatus("current")


class _DHttpTcpPort_Type(Unsigned32):
    """Custom type dHttpTcpPort based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DHttpTcpPort_Type.__name__ = "Unsigned32"
_DHttpTcpPort_Object = MibScalar
dHttpTcpPort = _DHttpTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 2),
    _DHttpTcpPort_Type()
)
dHttpTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dHttpTcpPort.setStatus("current")


class _DHttpIdleTimeoutVal_Type(Unsigned32):
    """Custom type dHttpIdleTimeoutVal based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 36000),
    )


_DHttpIdleTimeoutVal_Type.__name__ = "Unsigned32"
_DHttpIdleTimeoutVal_Object = MibScalar
dHttpIdleTimeoutVal = _DHttpIdleTimeoutVal_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 3),
    _DHttpIdleTimeoutVal_Type()
)
dHttpIdleTimeoutVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dHttpIdleTimeoutVal.setStatus("current")
_DSslServerObjects_ObjectIdentity = ObjectIdentity
dSslServerObjects = _DSslServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2)
)


class _DSslServicePolicyName_Type(DisplayString):
    """Custom type dSslServicePolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DSslServicePolicyName_Type.__name__ = "DisplayString"
_DSslServicePolicyName_Object = MibScalar
dSslServicePolicyName = _DSslServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2, 1),
    _DSslServicePolicyName_Type()
)
dSslServicePolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSslServicePolicyName.setStatus("current")


class _DSslServerStatus_Type(TruthValue):
    """Custom type dSslServerStatus based on TruthValue"""
    defaultValue = 2


_DSslServerStatus_Type.__name__ = "TruthValue"
_DSslServerStatus_Object = MibScalar
dSslServerStatus = _DSslServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2, 2),
    _DSslServerStatus_Type()
)
dSslServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSslServerStatus.setStatus("current")
_DWebCommonMIBConformance_ObjectIdentity = ObjectIdentity
dWebCommonMIBConformance = _DWebCommonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 2)
)
_DWebCommonMIBCompliances_ObjectIdentity = ObjectIdentity
dWebCommonMIBCompliances = _DWebCommonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 1)
)
_DWebCommonGroups_ObjectIdentity = ObjectIdentity
dWebCommonGroups = _DWebCommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2)
)

# Managed Objects groups

dHttpServerGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2, 1)
)
dHttpServerGroups.setObjects(
      *(("DLINKSW-WEB-COMMON-MIB", "dHttpServerStatus"),
        ("DLINKSW-WEB-COMMON-MIB", "dHttpTcpPort"),
        ("DLINKSW-WEB-COMMON-MIB", "dHttpIdleTimeoutVal"))
)
if mibBuilder.loadTexts:
    dHttpServerGroups.setStatus("current")

dSslServerGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2, 2)
)
dSslServerGroups.setObjects(
      *(("DLINKSW-WEB-COMMON-MIB", "dSslServicePolicyName"),
        ("DLINKSW-WEB-COMMON-MIB", "dSslServerStatus"))
)
if mibBuilder.loadTexts:
    dSslServerGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dWebMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 1, 1)
)
dWebMIBCompliance.setObjects(
      *(("DLINKSW-WEB-COMMON-MIB", "dHttpServerGroups"),
        ("DLINKSW-WEB-COMMON-MIB", "dSslServerGroups"))
)
if mibBuilder.loadTexts:
    dWebMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-WEB-COMMON-MIB",
    **{"dlinkSwWebCommonMIB": dlinkSwWebCommonMIB,
       "dWebCommonMIBNotifications": dWebCommonMIBNotifications,
       "dWebMIBObjects": dWebMIBObjects,
       "dHttpServerObjects": dHttpServerObjects,
       "dHttpServerStatus": dHttpServerStatus,
       "dHttpTcpPort": dHttpTcpPort,
       "dHttpIdleTimeoutVal": dHttpIdleTimeoutVal,
       "dSslServerObjects": dSslServerObjects,
       "dSslServicePolicyName": dSslServicePolicyName,
       "dSslServerStatus": dSslServerStatus,
       "dWebCommonMIBConformance": dWebCommonMIBConformance,
       "dWebCommonMIBCompliances": dWebCommonMIBCompliances,
       "dWebMIBCompliance": dWebMIBCompliance,
       "dWebCommonGroups": dWebCommonGroups,
       "dHttpServerGroups": dHttpServerGroups,
       "dSslServerGroups": dSslServerGroups}
)
