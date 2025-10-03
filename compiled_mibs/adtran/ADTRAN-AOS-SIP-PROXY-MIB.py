# SNMP MIB module (ADTRAN-AOS-SIP-PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adtran\ADTRAN-AOS-SIP-PROXY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:14:26 2025
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

(adGenAOSConformance,
 adGenAOSVoice) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSVoice")

(adIdentityShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenAOSSipProxy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 5)
)
if mibBuilder.loadTexts:
    adGenAOSSipProxy.setRevisions(
        ("2013-05-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdProxyRolloverCauseTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transactionFailed", 1),
          ("pollFailed", 2),
          ("pollSucceeded", 3))
    )



# MIB Managed Objects in the order of their OIDs

_AdSipProxy_ObjectIdentity = ObjectIdentity
adSipProxy = _AdSipProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5)
)
_AdSipProxyTraps_ObjectIdentity = ObjectIdentity
adSipProxyTraps = _AdSipProxyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 0)
)
_AdProxyTimestamp_Type = TimeTicks
_AdProxyTimestamp_Object = MibScalar
adProxyTimestamp = _AdProxyTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 1),
    _AdProxyTimestamp_Type()
)
adProxyTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adProxyTimestamp.setStatus("current")
_AdProxyRolloverFromServerInetAddressType_Type = InetAddressType
_AdProxyRolloverFromServerInetAddressType_Object = MibScalar
adProxyRolloverFromServerInetAddressType = _AdProxyRolloverFromServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 2),
    _AdProxyRolloverFromServerInetAddressType_Type()
)
adProxyRolloverFromServerInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adProxyRolloverFromServerInetAddressType.setStatus("current")
_AdProxyRolloverFromServerInetAddress_Type = InetAddress
_AdProxyRolloverFromServerInetAddress_Object = MibScalar
adProxyRolloverFromServerInetAddress = _AdProxyRolloverFromServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 3),
    _AdProxyRolloverFromServerInetAddress_Type()
)
adProxyRolloverFromServerInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adProxyRolloverFromServerInetAddress.setStatus("current")
_AdProxyRolloverToServerInetAddressType_Type = InetAddressType
_AdProxyRolloverToServerInetAddressType_Object = MibScalar
adProxyRolloverToServerInetAddressType = _AdProxyRolloverToServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 4),
    _AdProxyRolloverToServerInetAddressType_Type()
)
adProxyRolloverToServerInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adProxyRolloverToServerInetAddressType.setStatus("current")
_AdProxyRolloverToServerInetAddress_Type = InetAddress
_AdProxyRolloverToServerInetAddress_Object = MibScalar
adProxyRolloverToServerInetAddress = _AdProxyRolloverToServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 5),
    _AdProxyRolloverToServerInetAddress_Type()
)
adProxyRolloverToServerInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adProxyRolloverToServerInetAddress.setStatus("current")
_AdProxyRolloverCause_Type = AdProxyRolloverCauseTC
_AdProxyRolloverCause_Object = MibScalar
adProxyRolloverCause = _AdProxyRolloverCause_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 6),
    _AdProxyRolloverCause_Type()
)
adProxyRolloverCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adProxyRolloverCause.setStatus("current")
_AdSipProxyConformance_ObjectIdentity = ObjectIdentity
adSipProxyConformance = _AdSipProxyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14)
)
_AdSipProxyGroups_ObjectIdentity = ObjectIdentity
adSipProxyGroups = _AdSipProxyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1)
)
_AdSipProxyCompliances_ObjectIdentity = ObjectIdentity
adSipProxyCompliances = _AdSipProxyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 2)
)

# Managed Objects groups

adSipProxyNotificationUtilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1, 2)
)
adSipProxyNotificationUtilityGroup.setObjects(
      *(("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyTimestamp"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddressType"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddress"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddressType"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddress"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverCause"))
)
if mibBuilder.loadTexts:
    adSipProxyNotificationUtilityGroup.setStatus("current")


# Notification objects

adSipProxyRollover = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 0, 1)
)
adSipProxyRollover.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyTimestamp"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddressType"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddress"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddressType"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddress"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverCause"))
)
if mibBuilder.loadTexts:
    adSipProxyRollover.setStatus(
        "current"
    )


# Notifications groups

adSipProxyNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1, 1)
)
adSipProxyNotificationGroup.setObjects(
    ("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyRollover")
)
if mibBuilder.loadTexts:
    adSipProxyNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adSipProxyFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 2, 1)
)
adSipProxyFullCompliance.setObjects(
      *(("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyNotificationUtilityGroup"),
        ("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyNotificationGroup"))
)
if mibBuilder.loadTexts:
    adSipProxyFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-SIP-PROXY-MIB",
    **{"AdProxyRolloverCauseTC": AdProxyRolloverCauseTC,
       "adSipProxy": adSipProxy,
       "adSipProxyTraps": adSipProxyTraps,
       "adSipProxyRollover": adSipProxyRollover,
       "adProxyTimestamp": adProxyTimestamp,
       "adProxyRolloverFromServerInetAddressType": adProxyRolloverFromServerInetAddressType,
       "adProxyRolloverFromServerInetAddress": adProxyRolloverFromServerInetAddress,
       "adProxyRolloverToServerInetAddressType": adProxyRolloverToServerInetAddressType,
       "adProxyRolloverToServerInetAddress": adProxyRolloverToServerInetAddress,
       "adProxyRolloverCause": adProxyRolloverCause,
       "adSipProxyConformance": adSipProxyConformance,
       "adSipProxyGroups": adSipProxyGroups,
       "adSipProxyNotificationGroup": adSipProxyNotificationGroup,
       "adSipProxyNotificationUtilityGroup": adSipProxyNotificationUtilityGroup,
       "adSipProxyCompliances": adSipProxyCompliances,
       "adSipProxyFullCompliance": adSipProxyFullCompliance,
       "adGenAOSSipProxy": adGenAOSSipProxy}
)
